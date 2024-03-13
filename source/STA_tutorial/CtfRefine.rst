.. _sec_sta_ctfrefine:

Tomo refinement 1: CTF refinement
======================================

In this step we will show how to apply the refinement of the different parameters related to the CTF estimation. That is, tilt series projections defocus and astigmatism, scale and the asymmetrical and symmetrical aberrations.
For a full description of the arguments, check :ref:`program_tomo_refine_ctf` program.



Running the job
---------------

Since we ran both :jobtype:`Reconstruct particle` and :jobtype:`Post-processing` after the bin 1 refinement step at the end of the :ref:`sec_sta_refine3d` section, we already have the required reference halfmaps (``Reconstruct/job036/half<12>.mrc``) and post-processing FSC data (``PostProcess/job037/postprocess.star``).

In addition, we can use the |optimisation_set| file from a previous job or, in this case, the explicit |particle_set| from the duplicate removal step and the separate |tomogram_set| (which would otherwise be included in the optimisation set).

Lastly, the reference mask file used in the previous :jobtype:`3D auto-refine` at binning factor 1 is also required by the tomo refinement jobs, which in our case is ``mask_align.mrc``.

On the :guitab:`I/O` tab of the :jobtype:`CTF refinement` job-type set:

:Input optimisation set:: ReconstructParticleTomo/job012/optimisation_set.star

:Reference mask (optional):: masks/mask_align.mrc

    (If optimisation set does not include it)

On the :guitab:`Defocus` tab, set:

:Box size for estimation (pix): 512

:Refine defocus?: Yes

:Defocus search range (Å): 3000

:Do defocus regularisation?: Yes

:Defocus regularsation lambda: 0.1

:Refine constrast scale?: Yes

:Refine scale per frame?: Yes

:Refine scale per tomogram?: No


On the :guitab:`Aberrations` tab set:

:Refine odd aberrations?: Yes
:Order of odd aberrations: 3

:Refine even aberrations?: Yes
:Order of even aberrations: 4


On the :guitab:`Running` tab, set:

:Number of MPI procs:: 5
:Number of threads:: 112

With these running parameters, the process should take around 10 minutes to finish.

Analysing the results
---------------------

If you check the output folder ``CtfRefineTomo/job013`` you will find new ``tomograms.star`` and ``particles.star`` files with the refined CTF, scale and Zernike aberrations. To assess the result, it is recommended to run a new :jobtype:`Reconstruct particle` job, with FSC estimation, using the new parameters. Note this reference map will also be used as input for the next :jobtype:`Bayesian polishing` run. Compared to the previous FSC estimation, we should observe a slight improvement in the middle and high frequency ranges.


.. |optimisation_set| replace:: :ref:`optimisation set <sec_sta_optimisation_set>`
.. |particle_set| replace:: :ref:`particle set <sec_sta_particle_set>`
.. |tomogram_set| replace:: :ref:`tomogram set <sec_sta_tomogram_set>`
