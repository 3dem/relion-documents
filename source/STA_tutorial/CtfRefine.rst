.. _sec_sta_ctfrefine:

Tomo refinement 1: CTF refinement
======================================

In this step we will show how to apply the refinement of the different parameters related to the CTF estimation such as tilt series projection defocus and contrast scale.
For a full description of the arguments, check the :ref:`program_tomo_refine_ctf` program.

If you are running this job without following the tutorial, please note the requirements for the reference map and FSC data as described in :ref:`sec_sta_ctfrefine_refmap`.

Running the job
---------------

Since we ran both :jobtype:`Reconstruct particle` and :jobtype:`Post-processing` after the bin 1 refinement step at the end of the :ref:`sec_sta_refine3d` section, we already have the required reference halfmaps (``Reconstruct/job025/half<12>.mrc``) and post-processing FSC data (``PostProcess/job026/postprocess.star``).

In addition, we can use the |optimisation_set| file from a previous job or, in this case, the explicit |particle_set| from the duplicate removal step and the separate |tomogram_set| (which would otherwise be included in the optimisation set).

Lastly, the reference mask file used in the previous :jobtype:`3D auto-refine` at binning factor 1 is also required by the tomo refinement jobs, which in our case is ``mask_align.mrc``.

Select the :jobtype:`CTF refinement` job-type and set on the :guitab:`I/O` tab:

:Input optimisation set:: ""

:OR\: use direct entries?: Yes

      (Because the previous job run was :jobtype:`Subset selection` to remove duplicate particles, we will use the resulting particles file as the input particle set.
      Otherwise, we could have used the optimisation set file directly from the previous :jobtype:`3D auto-refine` job.)

:Input particle set:: Select/job024/particles.star

:Input tomogram set:: Denoise/job008/tomograms.star

:Input trajectory set: ""

	(This is empty in the first tomo refinement cycle, unless :jobtype:`Bayesian polishing` is run first, in which case we would include the generated ``motion.star`` file, unless it already is included in the optimisation set file.)

:One of the 2 reference half-maps:: Reconstruct/job025/half1.mrc

:Reference mask:: mask_align.mrc

:Input postprocess STAR:: PostProcess/job026/postprocess.star

On the :guitab:`Defocus` tab, set:

:Box size for estimation (pix): 512

:Refine defocus?: Yes

:Defocus search range (Å): 3000

:Do defocus regularisation?: Yes

:Defocus regularsation lambda: 0.1

:Refine constrast scale?: Yes

:Refine scale per frame?: Yes

:Refine scale per tomogram?: No


On the :guitab:`Running` tab, set:

:Number of MPI procs:: 5
:Number of threads:: 12

With these parameters, the job should take around 10 minutes to run.

Analysing the results
---------------------

The output folder ``CtfRefine/job027`` contains a new ``tomograms.star`` file with the refined parameters. 
To assess the result, run new :jobtype:`Reconstruct particle` and :jobtype:`Post-processing` jobs using the generated ``CtfRefine/job027/optimisation_set.star`` file.
In our workspace, we see a slight improvement in the resolution to 3.87Å.

These reference map and postprocess files will also be used as inputs for the next :jobtype:`Bayesian polishing` run. 


.. |optimisation_set| replace:: :ref:`optimisation set <sec_sta_optimisation_set>`
.. |particle_set| replace:: :ref:`particle set <sec_sta_particle_set>`
.. |tomogram_set| replace:: :ref:`tomogram set <sec_sta_tomogram_set>`
