# Contributing

Suggest a reference or correction through an issue or pull request. Include the exact title, primary source URL, year and a brief explanation of relevance. Check for an existing preprint or conference version first.

## Add or edit an entry

Edit [data/catalog.json](data/catalog.json). Keep existing IDs stable and follow a neighboring entry's format.

| Required field | Content |
| :--- | :--- |
| `id` | Unused `r` or `n` followed by three digits. |
| `title`, `url` | Exact title and primary HTTPS source. |
| `summary` | Original, neutral description, at most 45 words. |
| `year` | First arXiv year, otherwise publication year; `null` for undated projects. |
| `year_basis` | `first-preprint`, `record-year`, `maintainer-provided`, or `undated-project`. |
| `resource_type` | `paper`, `survey`, `system`, `perspective`, `dataset`, `benchmark`, `infrastructure`, `method`, or `project`. |
| `record_check` | Check date and [verification status](docs/curation.md). |

Add `authors` as the complete ordered list from the primary record, with `first_author` matching its first name. Record the source URL and check date in `authors_check`. All listed authors are searchable on the website.

Optional fields include `related_url`, `publication_note`, `first_submitted` and editorial `caution` notes. Caution notes are not displayed in the reading lists.

Summarize the contribution without promotional language. Distinguish shared weights from shared methods, and simulation from hardware results. Follow the [curation policy](docs/curation.md).

Update the catalogue's `updated` date, then run:

```bash
python3 scripts/build.py
python3 scripts/build.py --check
```

Include the catalogue and generated `README.md`, `docs/by-year.md` and `index.html` in your pull request. Use Python 3.11+; no packages are needed.

Contributions use [CC BY 4.0](LICENSE.md) for text, data and artwork, and [MIT](scripts/LICENSE) for scripts. Linked works retain their own licenses. Keep discussion respectful and source-based.
