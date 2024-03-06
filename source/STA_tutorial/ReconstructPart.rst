.. _sec_sta_reconstructpart:

Reconstruct particle
====================

**[TODO: update]**

The usual method to obtain a 3D reference map from a set of particles has been by averaging their extracted pseudo-subtomograms in a given orientation.
However, it is also possible to obtain that reference map directly by averaging the 2D projections for each particle from the tilt series.
Here, although in the :jobtype:`Tomo reconstruct particle` jobtype we offer both options, we strongly recommend the reconstruction from 2D tilt series projections.
This saves an interpolation step and prevent from artifacts related to pseudo-subtomogram construction.
It also creates both halfmaps along with the reference map and saves computational time.

The main differences the user will find are:

- averaging from 2D tilt series uses :ref:`program_tomo_reconstruct_particle` program so that an input :ref:`optimisation set <sec_sta_optimisation_set>` file is accepted. On the other hand, from 3D pseudo-subtomos option uses the regular `relion_reconstruct` program and requires to provide the input particle set filename explicitly.
- It's also possible to estimate the FSC curve in the same job if averaging from 2D tilt series is selected. To do this, an FSC solvent mask should be provided in the :guitab:`Average` tab.

Following the tutorial, we will reconstruct the 3D reference map after the initial 3D refinement with a smaller binning factor to keep refining for a higher resolution.

Running the job
---------------

Select the :guitab:`IO` tab from the :jobtype:`Tomo reconstruct particle` jobtype.
Note that we are using a particle set file after recentering the reference map so we could pass the tomogram information directly setting the |tomogram_set| file or the  |optimisation_set| file from any previous step. Then, |particle_set| file should also be specifically provided.

:Input optimisation set:: Refine3D/job009/optimisation_set.star
:Input particle set:: Refine3D/job009/run_data_z2.75.star
:Input tomogram set:: \
:Input trajectory set:: \

On the :guitab:`Average` tab, make sure the following is set to reconstruct particles with a binning factor of 2:

:Average from 2D tilt series?: Yes
:Box size (pix):: 256
:Cropped box size (pix):: 128
:Binning factor:: 2
:Wiener SNR constant:: 0
:FSC Solvent mask:: \

   (If provided, the post-processing output files will be found in ``ReconstructParticleTomo/jobXXX/PostProcess/`` folder.)

:Symmetry:: C6


On the :guitab:`Running` tab, set:

:Number of MPI procs:: 5
:Number of threads:: 24

Note that reconstructing from 2D tilt series :ref:`program_tomo_reconstruct_particle` program has 3 thread arguments.
The number of threads provided here sets both ``--j`` and ``--j_out`` arguments so, to avoid exceeding the available memory resources, the ``--mem`` argument should also be set using around 80-90% to keep a safety margin.
In our system, we ran 1 MPI process per cluster node (64Gb) so we added:

:Additional arguments:: \--mem 50

Using the settings above, this job took less than 5 minutes on our system.


Analysing the results
---------------------

You could look at the output map ``ReconstructParticleTomo/job013/merged.mrc`` with a 3D viewer like UCSF :textsc:`chimera`.



.. |tomogram_set| replace:: :ref:`tomogram set <sec_sta_tomogram_set>`
.. |particle_set| replace:: :ref:`particle set <sec_sta_particle_set>`
.. |optimisation_set| replace:: :ref:`optimisation set <sec_sta_optimisation_set>`
