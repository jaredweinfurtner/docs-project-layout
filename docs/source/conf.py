# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'docs-project-layout'
author = 'Jared Weinfurtner'
copyright = '... enter this in conf.py'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.drawio',
    'sphinx_rtd_theme',
    'myst_parser',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# fix for the following error:
# master file /home/jared/Projects/TOP90/energy-eot/docs/source/contents.rst not found
# Makefile:20: recipe for target 'html' failed
# make: *** [html] Error 2
master_doc = 'index'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for draw.io plugin ----------------------------------------------
# @see https://pypi.org/project/sphinxcontrib-drawio/

drawio_default_transparency = True
drawio_headless = True
drawio_no_sandbox = True
drawio_binary_path = "/usr/bin/drawio"

# -- Options for latexpdf ----------------------------------------------------
# By default, Sphinx documentation outputs a PDF that's formatted for duplex printing, so there are alternating blank
# pages in the generated pdf.  The following options disables this:

latex_elements = {
    'extraclassoptions': 'openany,oneside'
}
