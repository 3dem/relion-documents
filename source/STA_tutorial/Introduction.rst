Introduction
============

This tutorial will walk you through the tomography and sub-tomogram averaging pipeline of |RELION|-5.0 . 
This semi-automated pipeline is designed to carry out all of the steps in a typical subtomogram averaging project from your raw tilt series movies to your final subtomogram average. 
We will use a test data set composed of 5 tomograms of immature HIV-1 dMACANC VLPs, which is available at `EMPIAR-10164 <https://www.ebi.ac.uk/empiar/EMPIAR-10164/>`_.

Requirements
------------

   1. Your raw tilt series data as individual movies, or as individual motion-corrected images, but not as combined tilt series stacks. 
   2. The mdoc files containing the metadata for each tilt series.

Getting Organised
-----------------
We recommend creating a single directory per project. We’ll call this the project directory. 

To start processing, make your own project directory and download the raw data (frames and mdoc files) corresponding to the five tomograms (``TS_01``, ``TS_03``, ``TS_43``, ``TS_45``, ``TS_54``) from the EMPIAR link above. 
A RELION project directory containing precalculated results of all the processing steps of this dataset can be downloaded from:

.. image::  https://zenodo.org/badge/DOI/10.5281/zenodo.11068319.svg
   :target: https://doi.org/10.5281/zenodo.11068319

We will start by launching the |RELION| GUI.
**It is important to always launch the RELION graphical user-interface (GUI) from the project directory**. 
To prevent errors with this, the GUI will ask for confirmation the first time you launch it in a new directory.
Make sure you are inside the project directory, and launch the GUI by typing:

::

    relion --tomo&

and answer ``Yes`` when prompted to set up a new |RELION| project here.
