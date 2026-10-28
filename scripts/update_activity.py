"""Render the contribution counts GitHub already exposes on the public profile."""

from datetime import date
from html import escape
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
PROFILE = "sk-asd"
PALETTE = ["#293132", "#194e36", "#24784c", "#39a767", "#85d99e"]


class Calendar(HTMLParser):
    def __init__(self):
        super().__init__()
        self.days = {}
        self.heading = False
        self.heading_text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "td" and "data-date" in attrs and "data-level" in attrs:
            self.days[date.fromisoformat(attrs["data-date"])] = int(attrs["data-level"])
        if tag == "h2" and attrs.get("id") == "js-contribution-activity-description":
            self.heading = True

    def handle_endtag(self, tag):
        if tag == "h2":
            self.heading = False

    def handle_data(self, data):
        if self.heading:
            self.heading_text.append(data)


def render(calendar: Calendar) -> str:
    if len(calendar.days) < 300:
        raise ValueError("GitHub did not return a complete contribution calendar")
    heading = " ".join(calendar.heading_text).strip()
    match = re.search(r"([\d,]+)\s+contributions?", heading)
    if not match:
        raise ValueError("GitHub contribution count was not found")
    total = int(match[1].replace(",", ""))
    start = min(calendar.days)
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="232" viewBox="0 0 1040 232" role="img" aria-labelledby="title desc">',
        f'<title id="title">{total:,} GitHub contributions in the past year</title>',
        '<desc id="desc">Public activity and anonymized private contribution counts, as shown by GitHub.</desc>',
        '<rect width="1040" height="232" rx="8" fill="#171b1c"/>',
        '<g font-family="Arial, sans-serif">',
        '<text x="28" y="36" font-size="15" fill="#b9c0b9" letter-spacing="2">ACTIVITY</text>',
        f'<text x="1006" y="36" text-anchor="end" font-size="17" fill="#f1eddf">{total:,} contributions / past year</text>',
    ]
    previous_month = None
    for day, level in sorted(calendar.days.items()):
        delta = (day - start).days
        week, weekday = delta // 7, delta % 7
        x, y = 82 + week * 17, 78 + weekday * 17
        if previous_month != day.month and weekday == 0:
            parts.append(f'<text x="{x}" y="65" font-size="11" fill="#b9c0b9">{day:%b}</text>')
            previous_month = day.month
        parts.append(f'<rect x="{x}" y="{y}" width="13" height="13" rx="2" fill="{PALETTE[min(max(level, 0), 4)]}"><title>{day.isoformat()}: activity level {level}</title></rect>')
    for label, row in [("Mon", 1), ("Wed", 3), ("Fri", 5)]:
        parts.append(f'<text x="28" y="{88 + row * 17}" font-size="11" fill="#b9c0b9">{label}</text>')
    updated = date.today().isoformat()
    parts.append(f'<text x="28" y="218" font-size="11" fill="#b9c0b9">Includes anonymized private activity. Updated {escape(updated)}.</text>')
    parts.append('</g></svg>')
    return "\n".join(parts) + "\n"


def main():
    request = Request(f"https://github.com/users/{PROFILE}/contributions", headers={"User-Agent": "profile-activity-renderer"})
    with urlopen(request, timeout=30) as response:
        html = response.read().decode("utf-8")
    calendar = Calendar()
    calendar.feed(html)
    svg = render(calendar)
    path = ROOT / "assets" / "activity.svg"
    path.parent.mkdir(exist_ok=True)
    path.write_text(svg, encoding="utf-8")
    print("Updated activity.svg from public GitHub contribution data")


if __name__ == "__main__":
    main()
