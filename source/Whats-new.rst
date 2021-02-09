What's new in release 3.1?
==========================

Aberration corrections and optics groups
----------------------------------------

One of the major new features in |RELION|-3.1 is a correction for higher-order aberrations in the data, i.e. besides the beamtilt correction already present in |RELION|-3.0, the current version can also estimate and correct for trefoil and tetrafoil, as well as deviations from the nominal spherical aberration (Cs).
The corresponding paper can be found on bioRxiv :cite:`Zivanov_estimation_2019`.
The signal to estimate these aberrations is calculated by averaging over particles from multiple micrographs.
To allow for multiple subsets of a data set having different Zernike coefficients, |RELION|-3.1 implements the new concept of *optics groups*.
Optics groups are defined in a separate table called ``data_optics`` at the top of a STAR file, which will also contain a table called ``data_movies``, ``data_micrographs`` or ``data_particles``, depending on what type of images it refers to.
The second table is similar to the content of STAR files in previous releases, but contains a new column called ``rlnOpticsGroup``, which is also present in the ``data_optics`` table.
Common CTF-parameters, like ``rlnVoltage`` and ``_`rlnSphericalAberration``, but also the new ``rlnOddZernike`` and ``rlnEvenZernike``, can be stored once for each optics group in the ``data_optics`` table, without the need to store them for each particle/micrograph in the second table.

The same program that handles higher-order aberrations can also be used to refine differences in (anisotropic) magnification between the reference and (groups of) the particles.
Besides correcting for anisotropic magnification in the data, this is also useful when combining data from different scopes.
As of release 3.1, the program that does 2D/3D classification and 3D refinement (``relion_refine``) can combine particles with different box sizes and pixel sizes in a single refinement, and the magnification refinement can be used to correct small errors in the (calibrated) pixel sizes.
The box and pixel size of the input reference (or the first optics group in 2D classification) will be used for the reconstructions/class averages.
You may want to check they are on the desired scale before running classifications or refinements!

Upon reading STAR files that were generated in older releases of |RELION|, |RELION|-3.1 will attempt to convert these automatically into the |RELION|-3.1-style STAR files.
Therefore, moving a project from an older release to |RELION|-3.1 should be easy.

.. caution: Compatibility
    However, please note that |RELION|-3.1-style STAR files cannot be read by older releases.
    Therefore, it will be more difficult to go back from a |RELION|-3.1 project to an older release.


The External job-type
---------------------

|RELION|-3.1 allows execution of third-party software within the |RELION| pipeline through the new :jobtype:`External` job-type.
See :ref:`this section <sec_external_jobtype>` for details on how to use this.


*Schedules* for on-the-fly processing
-------------------------------------

The python script ``relion_it.py`` in |RELION|-3.0 has been replaced by a new framework of *Schedules*, which implement decision-based scheduling and execution of |RELION| jobs.
This comes with its own GUI interface.
See :ref:`Schedules <sec_schedules>` for details on how to use this.


General tweaks
--------------

Several tweaks have been made to enhance user experience:

-   The pipeliner no longer looks for output files to see whether a job has finished.
    Instead, upon successful exit, all programs that are launched from within the |RELION| pipeline will write out a file called ``RELION_EXIT_SUCCESS`` in the job directory.
    This avoids problems with subsequent execution of scheduled jobs with slow disc I/O.
-   Likewise, when encountering an error, all programs will write out a file called ``RELION_EXIT_FAILURE``.
    The GUI will recognise these jobs and use a red font in the :joblist:`Finished jobs` list.
    Note that incorrectly labeled jobs can be changed using the 'Mask as finished' or 'Mark as failed' options from the :button:`Job actions` pull-down menu.
-   There is an '`Abort running'` option on the :button:`Job actions` pull-down menu, which will trigger the currently selected job to abort.
    This works because all jobs that are executed from within the |RELION| pipeline will be on the lookout for a file called ``RELION_JOB_ABORT_NOW`` in their output directory.
    When this file is detected, the job will exit prematurely and write out a ``RELION_EXIT_ABORTED`` file in the job directory.
    Thereby, users no longer need to kill undesired processes through the queuing or operating system.
    The GUI will display aborted jobs with a strike-through red font in the :joblist:`Finished jobs` list.
-   When a job execution has given an error, in previous releases the user would need to fix the error through the input parameters, and then launch a new job.
    They would then typically delete the old job. |RELION|-3.1 allows to directly overwrite the old job.
    This is accessible on Linux systems through ``ALT+o`` or through the ``Overwrite continue`` option from the 'File menu'.
    Note that the ``run.out`` and ``run.err`` files will be deleted upon a job overwrite.


Tweaks to helical processing
----------------------------

Several new functionalities were implemented for helical processing:

- The ``relion_helix_inimodel2d`` program can be used to generate initial 3D reference maps for helices, in particular for amyloids, from 2D classes that span an entire cross-over (see :ref:`this section <sec_helix_inimodel2d>`).
- The translational offsets along the direction of the helical axis can now be restricted to a single rise in 2D-classification.
- The 3D refinement and 3D classification now can use a prior on the first Euler angle, (``rlnAngleRotPrior``), which was implemented by Kent Thurber from the Tycko lab at the NIH.