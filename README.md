# Inventory ERP website

Static marketing site (Home, Features, About, Contact). No build step needed to serve it.

- Edit copy in `tools/build.py`, then run `python3 tools/build.py` to regenerate the HTML pages.
- Styles: `assets/style.css`. Behaviour and the demo form: `assets/site.js`.
- Form submissions are emailed to `arun.idevs@gmail.com` through FormSubmit. The first submission after deploy sends an activation email to that address; click the link in it once.
- Deployed with GitHub Pages from the `main` branch root.
