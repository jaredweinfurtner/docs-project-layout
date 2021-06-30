# docs-project-layout

## Overview

For open-source projects, we tend to include everything in one mono-repository to reduce the complexity for adopters.  This creates a challenge to organize both documentation for users of the repository and technical documentation.  This project addresses the latter.  

For technical documentation, we often distribute it via the web (think readthedocs.org), pdf (whitepaper), or even to internal organization confluence pages.  Instead of having duplicate and often out-of-sync documentation for each distribution method, we use [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) &  [Sphinx](https://www.sphinx-doc.org/en/master/) to enable documentation as code - automating documentation generation from a single codebase.  

## Getting Started

You will probably want to separate your project code (for example, in `/src`) from your technical documentation code (in `/docs`).  To get started with technical documentation, please head over to [*/docs*](./docs).

## Technical Documentation

For reading the technical documentation you have options:
- To view as a PDF, please go to the [latest release assets](https://github.com/jaredweinfurtner/docs-project-layout/releases)
- To view as HTML, please go to [jaredweinfurtner.github.io/docs-project-layout](https://jaredweinfurtner.github.io/docs-project-layout)

## CI / Deployment

The technical documentation is generated via [GitHub Actions](https://github.com/features/actions) and served via [GitHub Pages](https://pages.github.com/)

Here is the GitHub actions yml file located in `.github/workflows/docs.yml`:

```
# This is a basic workflow to help you get started with Actions
 
name: Documentation
 
# Controls when the workflow will run
on:
  # Triggers the workflow on push or pull request events but only for the main branch
  push:
    branches: [ main ]
 
# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
      with:
        persist-credentials: false # otherwise, the token used is the GITHUB_TOKEN, instead of your personal token
        fetch-depth: 0 # otherwise, you will failed to push refs to dest repo
    - name: Generate Documentation
      run: |
        docker run --rm -v `pwd`/docs:/docs jaredweinfurtner/sphinx-drawio-docker make html
        cp -r docs/build/html/* ./docs
        touch docs/.nojekyll
    - name: Commit files
      run: |
        git add --all
        git config --local user.email "docs-project-layout[bot]@noreply.github.com"
        git config --local user.name "docs-project-layout[bot]"
        git commit -m "[bot] docs generation" -a
    - name: Push changes
      uses: ad-m/github-push-action@v0.6.0
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        branch: docs
        force: true
```

## License

**docs-project-layout** is open-sourced under the Unlicense license. See the
[LICENSE](LICENSE) file for details.

