# Cogito Engineering

This repository powers `https://engineering.cogito-ai.org`, the publishing home
for engineering writing at Cogito AI.

## Stack

- Markdown-first authoring
- Cogito Publish (`pyssg`) for static generation
- GitHub Pages for hosting
- Cloudflare DNS for the custom domain

## Local development

```bash
uv sync
uv run cogito-publish --site . serve
```

The local preview runs at `http://127.0.0.1:8000` by default.

## Create a new post

```bash
uv run cogito-publish --site . new post --title "My New Post" --tag engineering
```

Posts are created in `content/posts/`.

## Build for production

```bash
uv run cogito-publish --site . build
```

The output is written to `dist/`.

## Deployment

GitHub Actions builds the site on every push to `main` and deploys `dist/` to
GitHub Pages.

To finish the custom-domain setup:

1. In GitHub Pages settings, set the custom domain to `engineering.cogito-ai.org`.
2. In Cloudflare DNS, create a `CNAME` record for `engineering` that points to
   your GitHub Pages hostname, usually `<org-or-user>.github.io`.
3. Enable HTTPS in GitHub Pages after DNS is active.

## Branding assets

- GitHub organization: `https://github.com/cogitoForge-AI`
- Local horizontal logo: `layouts/theme/assets/brand/logo-horizontal.png`
- Local icon: `layouts/theme/assets/brand/icon.png`
