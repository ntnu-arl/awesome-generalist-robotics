# Maintaining the repository

[Collection](../README.md) · [Contributing](../CONTRIBUTING.md)

## GitHub setup

- **Name:** `awesome-generalist-robotics`
- **Description:** A curated collection of research on generalist robot policies, cross-embodiment learning, and unified embodied autonomy.
- **Topics:** `robotics`, `robot-learning`, `cross-embodiment`, `embodied-ai`, `autonomy`, `awesome-list`.

Follow the [publishing guide](../PUBLISHING.md) to upload the package and enable GitHub Pages.

## Updates

Edit [data/catalog.json](../data/catalog.json), preserve existing IDs, and update the curation date. Then run:

```bash
python3 scripts/build.py
python3 scripts/build.py --check
```

Commit the catalogue and generated README, [compact index](by-year.md), and `index.html`. Python 3.11+ is sufficient; no packages are needed. The checks cover catalogue consistency and local links, not external URL availability or scientific claims.
