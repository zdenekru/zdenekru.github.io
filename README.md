# zdenekru.github.io

Personal blog of Zdeněk R.: R&D for electronics, embedded, IoT, industrial automation and PLCs.

**Live site:** <https://zdenekru.github.io>

Built with [Jekyll](https://jekyllrb.com/) and the [Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) theme (installed as a gem, set up from the Chirpy starter), deployed to GitHub Pages via GitHub Actions.

## What's here

| Path | Contents |
| --- | --- |
| `_posts/` | Blog posts (project logs, homelab, tech notes) |
| `_tabs/` | Top-level pages: About, CV, Projects, Stack, Collaborators, … |
| `assets/img/` | Images and videos, one folder per project |
| `_config.yml` | Site configuration |
| `_data/`, `_plugins/` | Theme data and the last-modified hook |
| `tools/` | Local helper scripts |

Posts use a two-level category scheme, `[type, series]`, for example `[projects, zdenduino]` or `[tech-notes, linux]`. Tags are lowercase and hyphenated.

## Run locally

Requires Ruby and Bundler.

```bash
bundle install
bundle exec jekyll serve      # http://127.0.0.1:4000
```

Add `--drafts` to preview posts in `_drafts/`.

## Deployment

Every push to `main` triggers [`.github/workflows/pages-deploy.yml`](.github/workflows/pages-deploy.yml). It builds the site, checks internal links with `htmlproofer` and publishes to GitHub Pages. Changes to `README.md` and `LICENSE` alone don't trigger a deploy.

## License

- **Code, configuration and scripts:** [MIT](LICENSE)
- **Posts, pages, images and videos** (`_posts/`, `_tabs/`, `assets/img/`): [CC BY 4.0](LICENSE-CONTENT). You're free to reuse them, including commercially, as long as you credit the author and link back.

## Credits

Theme: [jekyll-theme-chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) by Cotes Chung, MIT License.
