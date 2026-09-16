# FullDive release notes

Public, user-facing release notes for products actively developed by FullDive.

The initial catalog covers Roomcord, Autoworker Hub, and Hermes Hub. Roomcord combines changes from its client and API into one product timeline.

## Release cycle

- Publish tagged product releases as dated release notes.
- Publish a weekly note when a product ships continuously without a meaningful public version.
- Skip empty weeks.
- Describe user-visible behavior. Exclude internal implementation, private links, customer data, and security-sensitive detail.

## Add a release

Copy `_templates/release.md` to `_releases/<product>/<YYYY-MM-DD>-<slug>.md`, complete the front matter, then run:

```bash
python3 scripts/validate.py
```

Merges to `main` publish the site through GitHub Pages.

## Automation permissions

Source repositories are private, so their default `GITHUB_TOKEN` cannot write here. Automated submissions should use a GitHub App installed only on the source repositories and this repository, with:

- source repositories: Metadata read and Contents read;
- this repository: Metadata read, Contents write, and Pull requests write.

The app should open a pull request. Human review remains the publication boundary.

