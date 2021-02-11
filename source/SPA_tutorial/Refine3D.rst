High-resolution 3D refinement
=============================

Once a subset of sufficient homogeneity has been selected, one may use the :jobtype:`3D auto-refine` procedure in |RELION| to refine this subset to high resolution in a fully automated manner.
This procedure employs the so-called **gold-standard** way to calculate Fourier Shell Correlation (FSC) from independently refined half-reconstructions in order to estimate resolution, so that self-enhancing overfitting may be avoided :cite:`scheres_prevention_2012`.
Combined with a procedure to estimate the accuracy of the angular assignments :cite:`scheres_relion:_2012`, it automatically determines when a refinement has converged.
Thereby, this procedure requires very little user input, i.e. it remains objective, and has been observed to yield excellent maps for many  data sets.
Another advantage is that one typically only needs to run it once, as there are hardly any parameters to optimize.

However, before we start our high-resolution refinement, we should first re-extract our current set of selected particles with less down-scaling, so that we can potentially go to higher resolution.
To do this, go to the :jobtype:`Particle extraction` jobtype on the GUI, and on the :guitab:`I/O` tab give:


:micrograph STAR file:: CtfFind/job003/micrographs\_ctf.star

     (This should still be there.)

:Coordinate-file suffix:: \

     (Leave this empty now.)

:OR re-extract refined particles?: Yes

:Refined particles STAR file:: Select/class3d\_first\_exhaustive/particles.star

     (Now, we will use only the refined subset of selected particles.)

:Reset the refiend offsets to zero?: No

     (This would discard the translational offsets from the previous classification runs.)

:OR\: re-center refined coordinates?: Yes

     (This will re-center all the particles according to the aligned offsets from the :jobtype:`3D classification` job above.)

:Recenter on - X, Y, Z (pix): 0 0 0

     (We want to keep the centre of the molecule in the middle of the box.)

:Manually set pixel size?: No

     (This is only necessary when the input micrograph :textsc:`star` file does NOT contain CTF information.)


And on the :guitab:`extract` tab, we keep everything as it was, except:

:Particle box size (pix): 360

     (we will use a larger box, so that de-localised CTF signals can be better modeled.
     This is important for the CTF refinement later on.)

:Rescale particles?: Yes

     (to prevent working with very large images, let's down-sample to a pixel size of 360\*0.885/256=1.244 Å.
     This will limit our maximum achievable resolution to 2.5 Å, which is probably enough for such a small data set.)

:Re-scaled size (pixels):: 256


We used the alias `best3dclass_bigbox` for this job.

In addition, we will need to rescale the best map obtained thus far to the 256-pixel box size.
This is done from the command-line:

::

    relion_image_handler --i Class3D/first_exhaustive/run_it025_class001.mrc \
     --angpix 3.54 --rescale_angpix 1.244 --new_box 256 \
     --o Class3D/first_exhaustive/run_it025_class001_box256.mrc


Running the auto-refine job
---------------------------


On the :guitab:`I/O` tab of the :jobtype:`3D auto-refine` job-type set:

:Input images STAR file:: Extract/best3dclass\_bigbox/particles.star

:Reference map:: Class3D/first\_exhaustive/run\_it025\_class001\_box256.mrc

     (Note this one is again not directly available through the :button:`Browse` button.)

:Reference mask (optional):: \

     (leave this empty for now)


On the :guitab:`Reference` tab, set:

:Ref. map is on absolute greyscale?: No

     (because of the different normalisation of down-scaled images, the rescaled map is no longer on the correct absolute grey scale.
     Setting this option to ``No`` is therefore important, and will correct the greyscale in the first iteration of the refinement.)

:Initial low-pass filter (A): 50

     (We typically start auto-refinements from low-pass filtered maps to prevent bias towards high-frequency components in the map, and to maintain the `gold-standard` of completely independent refinements at resolutions higher than the initial one.)

:Symmetry: D2

     (We now aim for high-resolution refinement, so imposing symmetry will effectively quadruple the number of particles.)


Parameters on the :guitab:`CTF`, :guitab:`Optimisation` and :guitab:`Auto-sampling` tabs remain the same as they were in the :jobtype:`3D classification` job.
Note that the orientational sampling rates on the :guitab:`Sampling` tab will only be used in the first few iterations, from there on the algorithm will automatically increase the angular sampling rates until convergence.
Therefore, for all refinements with less than octahedral or icosahedral symmetry, we typically use the default angular sampling of 7.5 degrees, and local searches from a sampling of 1.8 degrees.
Only for higher symmetry refinements, we use 3.7 degrees sampling and perform local searches from 0.9 degrees.

As the MPI nodes are divided between one master (who does nothing else than bossing the others around) and two sets of slaves who do all the work on the two half-sets, it is most efficient to use an odd number of MPI processors, and the minimum number of MPI processes for :jobtype:`3D auto-refine` jobs is 3.
Memory requirements may increase significantly at the final iteration, as all frequencies until Nyquist will be taken into account, so for larger sized boxes than the ones in this test data set you may want to run with as many threads as you have cores on your cluster nodes.
Perhaps an alias like ``first3dref`` would be meaningful?


Analysing the results
---------------------

Also the output files are largely the same as for the :jobtype:`3D classification` job.
However, at every iteration the program writes out two ``run_it0??_half?_model.star`` and two ``run_it0??_half?_class001.mrc`` files: one for each independently refined half of the data.
Only upon convergence a single `run_model.star` and ``run_class001.mrc`` file will be written out (without ``_it0??`` in their names).
Because in the last iteration the two independent half-reconstructions are joined together, the resolution will typically improve significantly in the last iteration.
Because the program will use all data out to Nyquist frequency, this iteration also requires more memory and CPU.

Note that the automated increase in angular sampling is an important aspect of the auto-refine procedure.
It is based on signal-to-noise considerations that are explained in :cite:`scheres_relion:_2012`, to estimate the accuracy of the angular and translational assignments.
The program will not use finer angular and translational sampling rates than it deems necessary (because it would not improve the results).
The estimated accuracies and employed sampling rates, together with current resolution estimates are all stored in the `_optimiser.star` and ``_model.star`` files, but may also be extracted from the stdout file.
For example, try:

::

    grep Auto Refine3D/first3dref/run.out