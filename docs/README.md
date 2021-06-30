## Usage

Generating documentation from the codebase should be as simple as possible for contributors. For Sphinx documentation, I have nicely packaged up a [Dockerfile](https://github.com/jaredweinfurtner/sphinx-drawio-docker) with Sphinx, python, drawio support, and all the necessary libraries pre-installed so it only requires one command inside the */docs* folder to generate all documentation.

### To generate the documentation, simply run the following in the `/docs` folder:

```shell
docker run --rm -v `pwd`:/docs jaredweinfurtner/sphinx-drawio-docker make html latexpdf
```

### To embed draw.io files, simply add to your documentation markup:

reStructuredText:
~~~
.. drawio-figure:: my-awesome-model.drawio
~~~

Markdown:
~~~
```{drawio-figure} my-awesome-model.drawio
```
~~~



### Structure

```
build
│
├───html
│   ├─  ...
│   └─  index.html
│      
└───latex
    ├─  ...
    └─  docs-project-layout.pdf

source
│   ├─ index.rst    
│   └─ conf.py
│
├───section
│   ├─  overview.rst
│   └─  my-drawing.drawio
│   
└───section
    ├─  overview.rst
    └─  my-drawing.drawio
```

### `/build/**`

Contains generated documentation and should be ignored via .gitignore

### `/build/html/**`

Contains static html that can be deployed as any other static html site - for example to: [Read the Docs](https://readthedocs.org/), [GitHub Pages](https://pages.github.com/), etc

### `/build/latex/**`

Contains mainly cached files for quicker follow-up generation of the pdf, but your `*.pdf` should be buried in here somewhere.  

### `/source/index.rst`

This is your landing page and should contain the tree structure of your documentation.  I highly recommend separating each section & subsection into its own folder so that you can include any diagrams alongside the .rst file.

### `/source/conf.py`

This is the only thing you need to copy & configure into your own project. Simply set the properties listed at the top for your particular project:

```shell
# -- Project information -----------------------------------------------------

project = 'docs-project-layout'
author = 'Jared Weinfurtner'
copyright = '© 1984-2021 Jared Weinfurtner'

# The full version, including alpha/beta/rc tags
release = '0.0.1'
```
