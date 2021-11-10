.. _sec_sta_ctfrefine:

Tomo CTF refinement
===================

In this step we will show how to apply the refinement of the different parameters related to the CTF estimation. That is, tilt series projections defocus and astigmatism, scale and the asymmetrical and symmetrical aberrations.
For a full description of the arguments, check :ref:`program_tomo_refine_ctf` program.


.. _sec_sta_ctfrefine_refmap:

Reference map at bin 1 and FSC data
-----------------------------------

Before running any of the tomo refinement jobs (this :jobtype:`Tomo CTF refinement` or  :jobtype:`Tomo frame alignment` jobs), the user should run a :jobtype:`Tomo reconstruct particle` to estimate the reference map to feed these type of jobs.
The main reason is that projection and reconstruction algorithms fully match and we will prevent suboptimal results because artifacts related to pseudo-subtomogram construction in the average map from the :jobtype:`3D auto-refine` job.

On the other hand, a post-processed FSC data for the reference half-maps is optionally required to estimate the SNR. In case it is not provided, these programs internally calculate it without phase randomization so SNR would be slightly optimistic. Since the FSC data estimation is also integrated in the :jobtype:`Tomo reconstruct particle`
job, we recommend to estimate it before running tomo refinement jobs.

Note that, independently of the binning factor level you were processing in the previous :jobtype:`3D auto-refine` job, :jobtype:`Tomo CTF refinement` and :jobtype:`Tomo frame alignment` protocols both process data in the original pixel size (binning 1).
Therefore, the reference map should always be reconstructed at this binning level as well as proper reference and FSC masks should be used.


Running the job
---------------

As described in previous jobs, we're using the :jobtype:`Tomo reconstruct particle` output |optimisation_set| file as input.
At this point, that optimisation set file should include the initial |tomogram_set| we imported, the ``run_data.star`` file from the :jobtype:`3D auto-refine` job as |particle_set|, ``ReconstructParticleTomo/jobXXX/half<12>.mrc``  files as half maps and ``ReconstructParticleTomo/jobXXX/PostProcess/postprocess.star`` file as FSC data.
Note the reference mask file used in previous :jobtype:`3D auto-refine` job should also be included in the optimisation set file. Otherwise, or in case that reference mask is designed for a binning factor other than 1, a reference mask should be specifically provided.

On the :guitab:`I/O` tab of the :jobtype:`Tomo CTF refinement` job-type set:

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

If you check the output folder ``CtfRefineTomo/job013`` you will find new ``tomograms.star`` and ``particles.star`` files with the refined CTF, scale and Zernike aberrations. To assess the result, it is recommended to run a new :jobtype:`Tomo reconstruct particle` job, with FSC estimation, using the new parameters. Note this reference map will also be used as input for the next :jobtype:`Tomo frame alignment` run. Compared to the previous FSC estimation, we should observe a slight improvement in the middle and high frequency ranges.


.. |optimisation_set| replace:: :ref:`optimisation set <sec_sta_optimisation_set>`
.. |particle_set| replace:: :ref:`particle set <sec_sta_particle_set>`
.. |tomogram_set| replace:: :ref:`tomogram set <sec_sta_tomogram_set>`