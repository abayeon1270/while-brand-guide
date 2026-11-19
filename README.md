# ’while — Brand Guidelines

Source files for the current ’while Online Brand Guidelines website, including the latest spread-layout brand guidelines PDF.

The website design, copy, logos, fonts, images, and interactions are preserved. The PDF download uses the newly supplied spread version, with a versioned link to prevent an older cached file from being downloaded. The package uses the original logo and custom apostrophe, Chubbo and National Park fonts, and the brand colors #FF9A3E / #3D3535 / #FDFFEE.

## Save to GitHub

1. Extract this ZIP file.
2. Create a **Private** repository on GitHub.
3. Upload the files and folders **inside** `while-brand-guidelines` to the repository root.

This package has no automatic public deployment configuration. GitHub Pages does not need to be enabled to store the files. Hosting account settings and Git history are excluded.

## Run Locally

With Python 3 installed, run this command from the repository folder:

```sh
python3 -m http.server 8000 --directory dist
```

Open `http://localhost:8000` in your browser. The website uses static HTML, CSS, and JavaScript; no package installation is required.

## File Structure

| Path | Purpose |
| --- | --- |
| `dist/` | Complete website, ready to serve |
| `dist/assets/` | Logos, fonts, images, and the current PDF |
| `dist/assets/while-brand-guidelines.pdf` | Supplied spread-layout brand guidelines PDF |
| `dist/app.js` | Website interactions |
| `dist/data.js` | Application examples and prompt data |
| `dist/styles.css` | Responsive styles |
| `build.py` | Generates seven pages and the search index |
| `validate.py` | Checks internal links, images, anchors, and asset integrity |
| `asset-manifest.json` | SHA-256 hashes for assets |

## Edit and Validate

To update page content, edit `build.py` and run it. Edit CSS and JavaScript directly in `dist/`.

```sh
python3 build.py
python3 validate.py
node --check dist/app.js
node --check dist/data.js
```

When replacing the PDF, keep its existing asset path and update its download link and description in `build.py`, as well as its SHA-256 hash in `asset-manifest.json`. Rebuild the pages afterward.

Brand and collaboration examples are supplied project materials. This package does not grant an open-source redistribution license.
