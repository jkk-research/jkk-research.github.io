# [jkk-research.github.io](https://jkk-research.github.io)
## Credits
A big thank you goes to the following people/groups:

- [Zensical](https://zensical.org) for providing the software, to generate the site.
- [squidfunk] for the [MkDocs Material Theme] it grew out of.
- [facelessuser] for the [PyMdown Extensions].

## Commands
The site is built with [Zensical](https://zensical.org) from `zensical.toml` and published to
[jkk-research.github.io](https://jkk-research.github.io/) by `.github/workflows/deploy.yml`.
It is versioned with Zensical's fork of mike. The Publications list is generated from `refs.bib`
by `bibliography.py`.

``` r
$ python3 -m pip install -r requirements.txt
$ zensical serve
$ zensical build

# Versioned deployment (mike)
$ mike deploy --update-aliases 2026-autumn latest
$ mike set-default latest
```

### Wiki
The wiki (`wiki/`) is a separate Zensical site, published to
[jkk-research.github.io/wiki](https://jkk-research.github.io/wiki/) by `.github/workflows/deploy-wiki.yml`.
It uses the same version as the main site.

``` r
$ cd wiki
$ python3 -m pip install -r requirements.txt
$ zensical serve
$ zensical build

# Versioned wiki deployment (mike, under wiki/ on the gh-pages branch)
$ mike deploy --deploy-prefix wiki --update-aliases 2026-autumn latest
$ mike set-default --deploy-prefix wiki latest
```

## License
This template is served under the MIT license.  
Read the [LICENSE] file for more info.
