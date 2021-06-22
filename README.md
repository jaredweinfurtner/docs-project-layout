# docs-project-layout

## Overview

For open-source projects, we tend to include everything in one mono-repository to reduce the complexity for adopters.  This creates a challenge to organize both documentation for users of the repository and technical documentation.  This project addresses the latter.  

For technical documentation, we often distribute it via the web (think readthedocs.org), pdf (whitepaper), or even to internal organization confluence pages.  Instead of having duplicate and often out-of-sync documentation for each distribution method, we use [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) &  [Sphinx](https://www.sphinx-doc.org/en/master/) to enable documentation as code - automating documentation generation from a single codebase.  

## Getting Started

You will probably want to separate your project code (for example, in `/src`) from your technical documentation code (in `/docs`).  To get started with technical documentation, please head over to [*/docs*](./docs).

## Technical Documentation

You can add the generated pdf of the technical documentation as [release assets](https://github.com/jaredweinfurtner/docs-project-layout/releases), or deploy the static html to [Read the Docs](https://github.com/jaredweinfurtner/docs-project-layout/releases), [GitHub Pages](https://pages.github.com/), or any service that will host static html.

## License

**docs-project-layout** is open-sourced under the Unlicense license. See the
[LICENSE](LICENSE) file for details.

