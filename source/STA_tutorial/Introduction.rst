Introduction
============

.. warning::
    This tutorial has not yet been updated for the new subtomogram averaging pipeline in |RELION|-5.0. Please be patient while we work on this.

This tutorial will walk you through the tomography and sub-tomogram averaging pipeline of |RELION|-5.0 . 
This *semi-*automated pipeline is designed to carry out all of the steps in a typical subtomogram averaging project from your raw data to your final structure. 
We will use a test data set composed of 5 tomograms of immature HIV-1 dMACANC VLPs, available at `EMPIAR-10164 <https://www.ebi.ac.uk/empiar/EMPIAR-10164/>`_.

Requirements
------------

   1. Your raw data as individual tilt images, not as tilt series stacks. These images may either be pre-motion corrected or movies, depending on user preference.
   2. The mdoc files containing the metadata for each tilt series of raw data.

Getting Organised
-----------------
We recommend to create a single directory per project, i.e. per structure you want to determine. We’ll call this the project directory. 
**It is important to always launch the RELION graphical user-interface (GUI) from the project directory**. 
You can download and unpack the raw data to start processing using the command below:

::

    wget ftp://ftp.mrc-lmb.cam.ac.uk/pub/scheres/relion50_sta_tutorial.tar.gz
    tar -zxf relion50_sta_tutorial.tar.gz

We will start by launching the |RELION| GUI.
This GUI always needs to be launched from the project directory.
To prevent errors with this, the GUI will ask for confirmation the first time you launch it in a new directory.
Make sure you are inside the project directory, and launch the GUI by typing:

::

    relion --tomo&

and answer ``Yes`` when prompted to set up a new |RELION| project here.