.. _sec_sta_makepseudosubtomo:

Extract (pseudo-)subtomograms
=============================

Now that we have 3D particle coordinates, we can extract the relevant cropped areas of the tilt series images for each individual particle and save them as CTF-premultiplied extracted 2D image stacks (or as 3D volumes, where Fourier slices of the 2D images are combined in 3D) on the disk for further processing using the `relion_refine` program. As these are not really boxed out of a 3D tomogram, we call these particles pseudo-subtomograms. 

Pseudo-subtomogram particles are described by a **[TODO: edit these data types!!]** |particle_set| star file, as well as a |tomogram_set| star file. In addition, if :jobtype:`Tomo frame alignment` has been performed, the pseudo-subtomograms are also described by a |trajectory_set| star file. For convenience, a single |optimisation_set| star file provides links to the corresponding three star files. After a :jobtype:`Tomo frame alignment` and/or :jobtype:`Tomo CTF refinement` job, a new set of updated pseudo-subtomos particles should be extracted, prior to can be extractedcalculated should be reconstructed to keep processing with further refinement or classification by `relion_refine`.

We will start by extracting pseudo-subtomograms in relatively large boxes with a large (binned) pixel size to speed up the initial calculations to obtain a *de novo* initial model. Select the :jobtype:`Extract subtomos` jobtype, and on the :guitab:`IO` tab set:


:Input optimisation set:: ""
    (We don't have an |optimisation_set| star file yet, so we will use individual starfiles below. **TODO: let Picking jobtype write out optimisation_set**)
:OR: use direct entries? Yes			
:Input particle set:: Picks/job007/particles.star
:Input tomogram set:: Tomograms/job008/tomograms.star
:Input trajectory set:: ""

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
