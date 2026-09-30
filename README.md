# Shomen Sports website

Static, self-contained site for [Shōmen Sports](https://www.shomen-sports.com/), a Portuguese karate brand. Since Phase 3 the whole site is **one file**, `index.html` (markup, CSS, JS, fonts and grain texture embedded); only the photos live in `assets/img/`. To ship a new version, swap `index.html` at the repo root. No build step, no external requests at runtime. It replaces the previous Squarespace site and drops the online store: since Phase 4 the whole site is one continuous page, products open inline under their tiles, without prices, and the only purchase path is contact by email or Instagram. Maintenance notes, tokens and rules live in [CLAUDE.md](CLAUDE.md); each finished phase is frozen under `archive/`.

## Preview locally

Any static file server works. With Python installed:

```bash
python -m http.server 8000
```

Then open <http://localhost:8000/>.

## Deploy (GitHub Pages)

The site is served straight from the `main` branch root; there is nothing to build.

1. Push to `https://github.com/apcanario/shomen-sports`.
2. In the repository, go to **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**, branch `main`, folder `/ (root)`. Save.
4. Under **Custom domain**, enter `shomen-sports.com` and save. The `CNAME` file in the repo already contains this value, so it will survive future pushes. Tick **Enforce HTTPS** once the certificate has been issued.

### DNS (not done yet)

DNS for `shomen-sports.com` still points at Squarespace. Do not change it until the new site has been reviewed at the `*.github.io` address. When ready, at the DNS provider:

- Replace the apex `A` records with GitHub Pages' IPs: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` (and, optionally, `AAAA` records `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`).
- Point `www` with a `CNAME` record to `apcanario.github.io`.
- Remove the old Squarespace `A`/`CNAME` records.

GitHub's current list of IPs is at <https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site>.

## Repository layout

See the file map in [CLAUDE.md](CLAUDE.md). Raw data from the old site is in `docs/scrape/` (JSON) and `docs/squarespace-tokens.md` (colours and fonts).
