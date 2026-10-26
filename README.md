![Profile header](./banner.svg)

### Sıraç

I build scraping, automation and data collection systems.

Most of my work is around websites that do not behave like clean APIs: authenticated portals, changing tables, mobile/web request differences, session handling, rate limits and data that has to stay fresh.

<p>
  <img src="https://img.shields.io/badge/Python-automation-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Node.js-data%20workers-339933?style=flat-square&logo=node.js&logoColor=white" />
  <img src="https://img.shields.io/badge/Playwright-browser%20automation-2EAD33?style=flat-square" />
  <img src="https://img.shields.io/badge/Elasticsearch-search%20data-005571?style=flat-square&logo=elasticsearch&logoColor=white" />
</p>

I run two products of my own:

- [OranAnalizcim](https://orananalizcim.com/tr/) - football odds and historical odds analysis
- [dizifilmyorum](https://dizifilmyorum.com) - TV and film tracking/review platform

## Work

- authenticated scraping and browser automation
- direct API extraction when browser automation is too slow or expensive
- reversing request signatures, device fingerprints and TLS/JA3 checks to reach protected endpoints
- proxy-aware request flows, cookies, sessions, retries and pacing
- odds/data normalization, snapshotting and change tracking
- Linux deploys and production workers

## Public demos

- [signed-endpoint-scraper](https://github.com/sk-asd/signed-endpoint-scraper) - breaks a signed + fingerprint-gated endpoint: reads the seed off the page, rebuilds the signature, refreshes and backs off on a 403
- [tls-fingerprint-scraper](https://github.com/sk-asd/tls-fingerprint-scraper) - getting past TLS/JA3 anti-bot fingerprinting with curl_cffi
- [har-endpoint-finder](https://github.com/sk-asd/har-endpoint-finder) - pulls the data endpoints (xhr/json/graphql) out of a HAR, past the html, css and trackers
- [async-crawler](https://github.com/sk-asd/async-crawler) - asyncio bfs crawler: bounded workers, per-host pacing, retry with backoff, dedup
- [crawlee-shop-scraper](https://github.com/sk-asd/crawlee-shop-scraper) - small Crawlee/TypeScript crawler: enqueue product links, extract name/price/sku
- [portal-data-extractor](https://github.com/sk-asd/portal-data-extractor) - authenticated portal scraping with session reuse, paging, retries and CSV/JSON export
- [scraper-reliability-kit](https://github.com/sk-asd/scraper-reliability-kit) - retry, cooldown, health scoring and 403/429 handling against a fake local target
- [odds-data-pipeline-demo](https://github.com/sk-asd/odds-data-pipeline-demo) - mock odds feed normalization, snapshots and change tracking

Most of my real scraping work cannot be public because it contains private endpoints, customer logic, session details or source-specific request handling. These repos are cleaned demos that show the workflow without exposing targets.
