.. _sec_sta_bayesian_polishing:

Tomo refinement 2: Bayesian polishing
=======================================

|RELION| has also implemented the analogous to :ref:`Bayesian polishing <sec_bayesian_polishing>` for tomography.
This procedure refines the projections that map 3D space onto the images of the tilt series. Optionally, the beam-induced motion trajectories of the particles and deformations can also be estimated.
For a complete description of the arguments, check the :ref:`program_tomo_align` program.

If you are running this job without following the tutorial, please note the requirements for the reference map and FSC data as described in :ref:`sec_sta_ctfrefine_refmap`.


Running the job
---------------

Select the :jobtype:`Bayesian polishing` job-type and set on the :guitab:`I/O` tab:

:Input optimisation set:: CtfRefine/job038/optimisation_set.star

:OR\: use direct entries?: No

:One of the 2 reference half-maps:: Reconstruct/job039/half1.mrc

:Reference mask:: mask_align.mrc

:Input postprocess STAR: PostProcess/job040/postprocess.star


On the :guitab:`Polish` tab, set:

:Box size for estimation (pix): 512

:Max position error (pix): 5

:Align by shift only?: No

:Alignment model: \

    (Does not apply)


On the :guitab:`Motion` tab, set:

:Fit per-particle motion?: Yes

:Sigma for velocity (Å/dose): 0.2

:Sigma for divergence (Å): 5000

:Use Gaussian decay: No

On the :guitab:`Running` tab, set:

:Number of MPI procs:: 5
:Number of threads:: 6

Note that the per-particle motion estimation increases the processing time significantly. 
On our system it took around 2 hours.

Analysing the results
---------------------

In the output folder ``Polish/job041`` you will find new ``tomograms.star`` and ``particles.star`` files including the corrected tilt series alignment and particle positions and a |trajectory_set| file ``motion.star`` with particle trajectories.
Again, to assess the result, run new :jobtype:`Reconstruct particle` and :jobtype:`Post-processing` jobs using the new parameters. 
Compared to the previous FSC estimation, we observe a clear improvement and a resolution of 3.6Å.


.. |optimisation_set| replace:: :ref:`optimisation set <sec_sta_optimisation_set>`
.. |trajectory_set| replace:: :ref:`trajectory set <sec_sta_trajectory_set>`
