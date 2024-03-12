.. _sec_sta_bayesian_polishing:

Bayesian polishing
====================

|RELION| has also implemented the analogous to :ref:`Bayesian polishing <sec_bayesian_polishing>` in 2D for tomography.
This procedure refines the projections that map 3D space onto the images of the tilt series. Optionally, the beam-induced motion trajectories of the particles and deformations can also be estimated.
For a complete description of the arguments, check :ref:`program_tomo_align` program.

If you are running this job without following the tutorial, please, note the requirements for the reference map as described for :jobtype:`CTF refinement` job in subsection :ref:`sec_sta_ctfrefine_refmap`.


Running the job
---------------

The |optimisation_set| file we are using as input has updated the reference mask file field in the previous :jobtype:`CTF refinement` job, so we don't need to override any other input file.

On the :guitab:`I/O` tab of the :jobtype:`Bayesian polishing` job-type set:

:Input optimisation set:: ReconstructParticleTomo/job015/optimisation_set.star


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

On the :guitab:`Deformations` tab set:

:Estimate 2D?: No

    This dataset has shown better results when deformations have not been estimated.

On the :guitab:`Running` tab, set:

:Number of MPI procs:: 5
:Number of threads:: 112

Note that the per-particle motion estimation increases significantly the processing time. In our system it took around 2 hours.

Analysing the results
---------------------

In the output folder ``FrameAlignTomo/job017`` you will find new ``tomograms.star`` and ``particles.star`` files including the corrected tilt series alignment and particle positions and a |trajectory_set| file ``motion.star`` with particle trajectories.
Again, to assess the result, it is recommended to run a new :jobtype:`Reconstruct particle` job, with FSC estimation, using the new parameters. Compared to the previous FSC estimation, we should observe a clear improvement and a resolution around 3.5Å.


Tomo refinement cycle
----------------------

After running both tomo specific refinement steps, it is still recommended to run a new :jobtype:`3D auto-refine` job to take advantage of the improved tomograms and particles.
To that end, we need to construct a new set of pseudo-subtomos and reference maps as described in subsection :ref:`sec_sta_refine3d_subtomo`.
For the new :jobtype:`3D auto-refine` job, same parameter as in subsection :ref:`sec_sta_refine3d_refinebin1` apply except for:

On the :guitab:`Reference` tab, set:

:Initial low-pass filter (A): 3.5

On the :guitab:`Auto-sampling` tab set:

:Initial angular sampling:: 0.9 degrees


This new 3D refinement spent 1 day in our system (4 GPU cards) and it should report a resolution around 3.4Å, completing the first tomo refinement cycle.
If a new cycle of :jobtype:`CTF refinement`, :jobtype:`tomo frame alignment` and :jobtype:`3D auto-refine` is performed, the user should reach around 3.3Å and finally converge to 3.2Å in the third cycle.


.. |optimisation_set| replace:: :ref:`optimisation set <sec_sta_optimisation_set>`
.. |trajectory_set| replace:: :ref:`trajectory set <sec_sta_trajectory_set>`
