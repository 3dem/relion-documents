.. _sec_sta_refine3d_ini:

Initial 3D refinement
======================

Once we have an initial reference map, one may use the :jobtype:`3D auto-refine` procedure in |RELION| to refine the dataset to high resolution in a fully automated manner.
This procedure employs the so-called **gold-standard** way to calculate Fourier Shell Correlation (FSC) from independently refined half-reconstructions in order to estimate resolution, so that self-enhancing overfitting may be avoided :cite:`scheres_prevention_2012`.
Combined with a procedure to estimate the accuracy of the angular assignments :cite:`scheres_relion:_2012`, it automatically determines when a refinement has converged.
Thereby, this procedure requires very little user input, i.e. it remains objective, and has been observed to yield excellent maps for many  data sets.
Another advantage is that one typically only needs to run it once, as there are hardly any parameters to optimize.

However, as the pseudo-subtomogram files require more memory resources compared to SPA, we suggest to run this procedure in several steps, from high binning factors to 1, to improve processing time.
Since the initial reference map was processed using pseudo-subtomograms at binning factor 6, we will start the 3D refinement using those same particles.

Running the auto-refine job
---------------------------

On the :guitab:`I/O` tab of the :jobtype:`3D auto-refine` job-type set:

:Input optimisation set:: Extract/job009/optimisation_set.star

    (If an optimisation set file is provided, the input particles and tomograms STAR files are set based on its content.)

:OR use direct entries?: No

    (Since we provide an optimisation set file in the field above, we will not be providing a particle set, tomogram set or trajectory set.)

:Input particle set:: ""

    (Note this is blank as it is extracted from the optimisation set file.)

:Input tomogram set:: ""

    (This is also blank as it is given in the optimisation set file.)

:Input trajectory set:: ""

    (This is blank as we have not run a :jobtype:`Bayesian polishing` job yet.)

:Reference map:: Reconstruct/job010/merged.mrc

:Reference mask (optional):: ""

     (We're not using a mask at this point, so leave this empty for now.)


On the :guitab:`Reference` tab, set:

:Ref. map is on absolute greyscale?: Yes

:Resize reference if needed?: Yes

:Initial low-pass filter (A): 60

     (We typically start auto-refinements from low-pass filtered maps to prevent bias towards high-frequency components in the map, and to maintain the `gold-standard` of completely independent refinements at resolutions higher than the initial one.)

:Symmetry: C6

On the :guitab:`CTF` tab set:

:Do CTF correction?: Yes

:Ignore CTFs until first peak?: No

On the :guitab:`Optimisation` tab set:

:Mask diameter (A):: 500 

and keep the defaults for the remaining options.

Note that the box size at bin 6 is 96 x 8.1Å = 777.6Å, so setting a large mask diameter of 500Å (remember the HIV capsid hexamers are 75Å apart) in the first :jobtype:`3D auto-refine` job at bin 6 allows us to use more information in the low-resolution images to obtain a first round of particle alignments and a map that will then be further refined with a smaller mask of diameter 230Å and a smaller binning factor (i.e. higher resolution).

On the :guitab:`Auto-sampling` tab, one can usually keep the defaults.
Note that the orientational sampling rates on the :guitab:`Auto-sampling` tab will only be used in the first few iterations, from there on the algorithm will automatically increase the angular sampling rates until convergence.
Therefore, for all refinements with less than octahedral or icosahedral symmetry, we typically use the default angular sampling of 7.5 degrees, and local searches from a sampling of 1.8 degrees.
Only for higher symmetry refinements we use 3.7 degrees sampling and perform local searches from 0.9 degrees.

The last two fields on the :guitab:`Auto-sampling` tab are set as follows:

:Use finer angular sampling faster?: No 

     (If set to yes, the refinement is more aggresive in proceeding with iterations of finer angular sampling.
     This will speed up the calculations at the potential cost of suboptimal convergence.
     Therefore, if using this option, you might want to check that you are not obtaining suboptimal alignments in the early refine jobs and not losing resolution in the later stages of your own processing.)

:Prior width on tilt angle (deg): 10

     (This field has the same purpose as in the :jobtype:`3D initial reference` job: enforcing priors on the tilt angle of the particles. Since we know from the sphere picking procedure that the particles are normal to the surface of the spheres, we can use this knowledge to speed-up convergence.)

Ignore the :guitab:`Helix` tab, and on the :guitab:`Compute` tab set:

:Use parallel disc I/O?: Yes

:Number of pooled particles:: 30

:Skip padding?: No

:Pre-read all particles into RAM?: No

:Copy particles to scratch directory: ""


:Combine iterations through disc?: No

:Use GPU acceleration?: Yes

:Which GPUs to use: \

    (Set the id sequence of the GPU cards separated by colon (``0:1:2``) or leave blank to automatically use all configured cards)

On the :guitab:`Running` tab, set:

:Number of MPI procs: 5

:Number of threads: 6

As the MPI nodes are divided between one leader (who does nothing else than bossing the others around) and two sets of followers who do all the work on the two half-sets, it is most efficient to use an odd number of MPI processors, and the minimum number of MPI processes for :jobtype:`3D auto-refine` jobs is 3.
Memory requirements may increase significantly at the final iteration, as all frequencies until Nyquist will be taken into account, so for larger sized boxes than the ones in this test data set you may want to run with as many threads as you have cores on your cluster nodes.

Before pressing the :runbutton:`Run!` button, we give this job the alias ``bin6`` so we can refer to it easily later.

On our computer with 4 GPUs, this calculation took approximately 5 hours.


Analysing the results
---------------------

At every iteration the program writes out two ``run_it0??_half?_model.star`` and two ``run_it0??_half?_class001.mrc`` files: one for each independently refined half of the data.
Only upon convergence a single ``run_model.star`` and ``run_class001.mrc`` file will be written out (without ``_it0??`` in their names).
Because the two independent half-reconstructions are joined together in the last iteration, the resolution will typically improve significantly.
This iteration also requires more memory and CPU, as the program will use all the data up to Nyquist frequency.

Note that the automated increase in angular sampling is an important aspect of the auto-refine procedure.
It is based on signal-to-noise considerations that are explained in :cite:`scheres_relion:_2012`, to estimate the accuracy of the angular and translational assignments.
The program will not use finer angular and translational sampling rates than it deems necessary (because it would not improve the results).
The estimated accuracies and employed sampling rates, together with current resolution estimates, are stored in the ``_optimiser.star`` and ``_model.star`` files, but may also be extracted from the stdout file. For more information, check the SPA tutorial :ref:`high-resolution 3D refinement <sec_refine3d>` step.

The program also writes an optimisation set ``run_optimisation_set.star`` file, updated with ``run_data.star`` (i.e. the particles file) and the tomograms and trajectories files (given as input to the :jobtype:`3D auto-refine` job).
This ``run_optimisation_set.star`` file  should not be confused with the ``_optimiser.star`` files used regularly by `relion_refine`.


This job will have likely reached Nyquist frequency so, to go to higher resolution, we will need a new set of pseudo-subtomo particles and reference map at a smaller binning factor, 2 or directly 1.

**[TODO: Move the paragraph below to the High-resolution 3D refinement page and adapt for bin2 and bin1]**
Before this, since the refined map we obtained in this initial 3D refinement covers the HIV capsid and matrix, we need to make sure the mask we will be using in the next refinement is aligned and focused on the capsid only.
We suggest to recenter the reference as masks provided in ``masks/`` folder are already centered.
You could look at the output refined map (``Refine3D/job009/run_class001.mrc``) and mask (``masks/mask_align_bin4.mrc``) with a 3D viewer like IMOD :textsc:`3dmod` to estimate the Z offset between both maps, in pixels. In our case, it is 2.75 pixels but this could be different as it depends on the initial *de novo* model. Thus, recentering the particles can be done from the command-line:

::

    relion_star_handler --i Refine3D/job009/run_data.star \
    --o Refine3D/job009/run_data_z2.75.star --center --center_Z 2.75


To assess the capsid within the reference map is aligned with the mask, we could reconstruct it using the :jobtype:`Tomo reconstruct particle` job-type, described in the next step :ref:`reconstruct particle <sec_sta_reconstructpart>`.
