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
import os
import sys
sys.path.insert(0, os.path.abspath('./_ext'))

# -- Project information -----------------------------------------------------

project = 'RELION'
copyright = 'RELION developer team, licensed under GPLv3'
author = 'Sjors Scheres, Takanori Nakane'

rst_prolog = """
.. role:: textsc
   :class: smallcaps

.. role:: schemevar
.. role:: button
.. role:: runbutton
.. role:: joblist
.. role:: jobtype
.. role:: guitab
.. |RELION| replace:: :textsc:`relion`
.. |MotionCor2| replace:: :textsc:`motioncor`\ 2
.. |CTFFIND4.1| replace:: :textsc:`ctffind` 4.1
.. |Topaz| replace:: :textsc:`topaz`
"""

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinxcontrib.bibtex", "custom_field_list"
]

bibtex_bibfiles = ["refs.bib"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Needed for ReadTheDocs
html_static_path = []

html_sidebars = {
   '**': [
      'about.html',
      'navigation.html',
      'relations.html',
      'searchbox.html',
      'donate.html',
    ]
}

html_theme_options = {
   'logo': 'relion-logo.png',
   'github_user': '3dem',
   'github_repo': 'relion',
   'github_button': True,
   'github_type': 'star',
   'extra_nav_links': {'Source repository of this documentation': 'https://github.com/3dem/relion-documents'},
   'sidebar_collapse': True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for LaTeX output ------------------------------------------------

latex_documents = [("index", "relion.tex", "RELION", "RELION developers", "manual", "toctree_only")]

latex_elements = {
   'preamble': r'''
      %% Some tricks for Unicode characters
      \sphinxDUC{212B}{\AA}
      \sphinxDUC{2260}{$\neq$}
      \sphinxDUC{03B1}{$\alpha$}
      \sphinxDUC{03B2}{$\beta$}
      \sphinxDUC{03BB}{$\lambda$}

      %% Custom colors: Change together with the CSS file _static/custom.css.
      \definecolor{guiBackground}{RGB}{230,230,240}
      \definecolor{guiBackground2}{RGB}{180,180,190}
      \definecolor{entryYellow}{RGB}{255,255,230}
      \definecolor{buttonColor}{RGB}{200,80,110}
      \definecolor{runButtonColor}{RGB}{160, 30, 60}

      %% First paragram in field-list definitions (enabled by custom_field_list.py)
      \newcommand{\docutilsrolefieldlistfirstparagraph}[1] {\colorbox{entryYellow}{\small#1}}

      %% Custom roles
      \newcommand{\docutilsrolebutton}[1] {\colorbox{buttonColor}{\small#1}}
      \newcommand{\docutilsrolerunbutton}[1] {\colorbox{runButtonColor}{\small#1}}
      \newcommand{\docutilsrolejoblist}[1] {\colorbox{guiBackground}{\fbox{\small#1}}}
      \newcommand{\docutilsrolejobtype}[1] {\fbox{\small#1}}
      \newcommand{\docutilsroleguitab}[1] {\colorbox{guiBackground2}{\small#1}}
   '''
}
