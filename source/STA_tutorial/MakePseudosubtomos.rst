.. _sec_sta_makepseudosubtomo:

Make pseudo-subtomograms
========================

Before processing with any of the regular |RELION| programs (those not specifically intended for tomography, e.g. `relion_refine`), we first need to construct the individual pseudo-subtomogram particles, equivalent to the particle extraction process in the SPA workflow.

Pseudo-subtomogram particle files are not only related to a |particle_set|. Indeed, they also rely on a |tomogram_set| (tilt series alignment, defocus estimation ...) and, in case the motion of particles has been refined, on a |trajectory_set|.
Therefore, everytime a :jobtype:`Tomo frame alignment` or :jobtype:`Tomo CTF refinement` job-types are run, a new set of updated pseudo-subtomos particles should be reconstructed to keep processing with regular |RELION| programs. This is not necessary in case of specific tomo |RELION| programs (prefix name ``relion_tomo_``) as they are directly fed with original tilt series stack files so referred pseudo-subtomo files are ignored.

In this tutorial, we will first construct the particles in lower resolution, in a binning scale factor 4, to start obtaining a de novo 3D model.


Running the job
---------------

Select the :guitab:`IO` tab from the :jobtype:`Make pseudo-subtomo` jobtype.
Note that input files can be passed using either an |optimisation_set| file solo and/or the |particle_set| and |tomogram_set| files to override the file within the |optimisation_set| file. Here, we will be using |optimisation_set| files where available.

:Input optimisation set:: ImportTomo/job002/optimisation_set.star
:Input particle set:: \
:Input tomogram set:: \
:Input trajectory set:: \

On the :guitab:`Reconstruct` tab, make sure the following is set to reconstruct particles with a binning factor of 4:

:Box size (pix):: 192
:Cropped box size (pix):: 96
:Binning factor:: 4

:Use cone weight?: No
:Cone angle:: \

On the :guitab:`Running` tab, set:

:Number of MPI procs:: 5
:Number of threads:: 24

Note that the MPI versions of the tomo |RELION| programs are parallelized in a tomogram base, that is, tomograms will be distributed among the number of processors.
Therefore, the ``Number of MPI processes`` will not improve the performance if it's greater than the number of tomograms.
Using the settings above, this job took less than 10 minutes on our system.

Your pseudo-subtomo particles and their related CTF and multiplicty patterns will be stored into MRC files in a new directory called ``PseudoSubtomo/job007/Subtomograms/`` separated by tomogram folder. You can check that, together with the updated ``particles.star`` file, a ``optimisation_set.star`` file is also created.







.. |tomogram_set| replace:: :ref:`tomogram set <sec_sta_tomogram_set>`
.. |particle_set| replace:: :ref:`particle set <sec_sta_particle_set>`
.. |trajectory_set| replace:: :ref:`trajectory set <sec_sta_trajectory_set>`
.. |optimisation_set| replace:: :ref:`optimisation set <sec_sta_optimisation_set>`
