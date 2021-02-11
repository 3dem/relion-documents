Helical reconstruction
======================

Shaoda He, a PhD-student in the Scheres group, implemented a workflow for the processing of helical assemblies.
This involves additional tabs to the parameter-panels of the :jobtype:`Auto-picking`, :jobtype:`Particle extraction`, :jobtype:`2D classification`, :jobtype:`3D classification`, :jobtype:`3D auto-refine`, :jobtype:`Particle polishing` and :jobtype:`Mask create` job-types.
We do not have a separate tutorial for processing helical assemblies.
The general principles remain the same as for single-particle analysis, which is covered in this tutorial.
Therefore, users intending to use |RELION| for helical processing are still encouraged to do this tutorial first.
For a detailed description of the helical options, the user is referred to the corresponding pages on the `RELION wiki <http://www2.mrc-lmb.cam.ac.uk/relion/index.php/Helical_processing>`_, or to `Shaoda's paper <https://doi.org/10.1016/j.jsb.2017.02.003>`_:cite:`he_helical_2017`.
We are aware that a tutorial on helical processing is probably overdue, but due to time constraints we haven't got to doing that yet.
Sorry...


.. _sec_helix_inimodel2d:

Initial model generation for amyloids
-------------------------------------

The ``relion_helix_inimodel2d`` program is a new feature in |RELION|-3.1.
It allows generation of an initial 3D reference for helical reconstruction, in particular for amyloids.
It is run from the command line, and takes a selection of suitable 2D class averages as input.
It will try to align these class averages with respect to each other to form a continuously changing density that spans an entire cross-over.
At the heart of the iterative refinement process lies a `tomographic` 2D reconstruction with all 1D pixel columns from the cross-over.
Details of this program, together with a more elaborate documentation of its functionality remain to be published.
Possible usage is:

::

     relion_helix_inimodel2d --i Select/job056/class_averages.star \
       --crossover_distance 800  --angpix 1.15 --maxres 9 --search_shift 3 \
       --mask_diameter 250 --j 6 --iter 5 --o IniModel/run1

     relion_helix_inimodel2d --i IniModel/run1_it005.star \
       --iniref 1@IniModel/run1_it005_reconstructed.mrcs  --angpix 1.15 \
       --maxres 6 --search_angle 2 --step_angle 0.5 --mask_diameter 250 \
       --j 6 --iter 5  --o IniModel/run2


We like :textsc:`xmipp`-2.4 for live-updated display of the following images during the optimisation:

::

     xmipp_show -img rec.spi after_reproject.spi before_reproject.spi -poll &