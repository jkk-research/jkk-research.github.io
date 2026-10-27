# [jkk-research.github.io](https://jkk-research.github.io)
## Credits
A big thank you goes to the following people/groups:

- [MkDocs] for providing the software, to generate documentation.
- [squidfunk] for the [MkDocs Material Theme].
- [facelessuser] for the [PyMdown Extensions].

## Commands

``` r
$ python3 -m  pip install mkdocs mkdocs-material mkdocs-slides "mkdocs-material[imaging]" mkdocs-bibtex mike
$ mkdocs build
$ mkdocs serve

# Versioned docs deployment (mike)
$ mike deploy --update-aliases 1.0 latest
$ mike set-default latest
$ mike serve
```

### Wiki
The wiki (`wiki/`) is a separate site built with [Zensical](https://zensical.org) and published to
[jkk-research.github.io/wiki](https://jkk-research.github.io/wiki/) by `.github/workflows/deploy-wiki.yml`.
It is versioned with Zensical's fork of mike, using the same version as the main site.

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
