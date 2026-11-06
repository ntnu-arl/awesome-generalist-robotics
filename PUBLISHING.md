# Publish on GitHub Pages

Expected address: **https://ntnu-arl.github.io/awesome-generalist-robotics/**

The website is ready to serve: `index.html`, `assets/`, `data/` and `.nojekyll` are included. No hosting build, dependency installation, API key or custom domain is needed. The complete repository also includes the catalogue, contribution guides and maintenance scripts.

## 1. Create the repository

On GitHub, choose **New repository**:

- Owner: **ntnu-arl**
- Name: **awesome-generalist-robotics**
- Visibility: **Public**
- Description: **A curated collection of research on generalist robot policies, cross-embodiment learning, and unified embodied autonomy.**

Leave the options to add a README, license and .gitignore unchecked; this package supplies them. Create the empty repository.

## 2. Push the package

Extract the ZIP into a new folder outside another Git repository. Open a terminal in that folder, where `README.md` and `index.html` are directly visible, and run:

```bash
git init -b main
git add .
git commit -m "Publish Awesome Generalist Robotics"
git remote add origin https://github.com/ntnu-arl/awesome-generalist-robotics.git
git push -u origin main
```

Authenticate with your GitHub account when prompted. These commands assume an empty remote repository and an account permitted to push to the organization. Alternatively, use GitHub Desktop to add the extracted folder and publish it to the same organization and repository name.

Push the extracted contents, including `.github/`, `.nojekyll`, `.gitattributes` and `.gitignore`. Do not upload the ZIP itself or place the contents inside an extra enclosing folder. The repository root must contain `index.html`.

## 3. Enable Pages

In the repository, open **Settings → Pages → Build and deployment**:

1. Source: **Deploy from a branch**.
2. Branch: **main**.
3. Folder: **/(root)**.
4. Click **Save**.

Wait for the Pages deployment to finish, then use **Visit site** on that settings page. GitHub may take several minutes to publish. The included `.nojekyll` tells Pages to serve the prepared static files directly.

If Pages settings are unavailable, ask an organization administrator to check your repository permissions and the organization's Pages policy.

## 4. Check the result

- Open the expected address above.
- Check the header, search and year filter; selecting 2020 should show eight references in this initial release.
- Open a paper and the GitHub link.
- Check **Actions**: the catalogue validation and Pages deployment should pass.
- In the repository's **About** settings, set the Website field to the published address. Suggested topics: `robotics`, `robot-learning`, `cross-embodiment`, `embodied-ai`, `autonomy`, `awesome-list`.

## Later updates

Edit `data/catalog.json`, preserve existing IDs, update its `updated` date, and run with Python 3.11 or newer:

```bash
python3 scripts/build.py
python3 scripts/build.py --check
```

Commit and push the catalogue and generated `README.md`, `docs/by-year.md` and `index.html`. Pages republishes after each push to `main`. Edit appearance in `assets/site.css`, behavior in `assets/site.js`, and page structure in `scripts/site_builder.py`; regenerate after changing the structure. Do not edit generated files directly.

Official guidance: [Configure a GitHub Pages publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).
