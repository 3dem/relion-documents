.. _sec_sta_refine3d_ini:

Initial 3D refinement
======================

Once we have an initial reference map, one may use the :jobtype:`3D auto-refine` procedure in |RELION| to refine the dataset to high resolution in a fully automated manner.
This procedure employs the so-called **gold-standard** way to calculate Fourier Shell Correlation (FSC) from independently refined half-reconstructions in order to estimate resolution, so that self-enhancing overfitting may be avoided :cite:`scheres_prevention_2012`.
Combined with a procedure to estimate the accuracy of the angular assignments :cite:`scheres_relion:_2012`, it automatically determines when a refinement has converged.
Thereby, this procedure requires very little user input, i.e. it remains objective, and has been observed to yield excellent maps for many  data sets.
Another advantage is that one typically only needs to run it once, as there are hardly any parameters to optimize.

However, as the pseudo-subtomogram files require more memory resources compared to SPA, we suggest to run this procedure in several steps, from high binning factors to 1, to improve the processing time.
Since the initial model was processed using pseudo-subtomograms with binning factor 4, we will start the 3D refinement using those same particles.

Running the auto-refine job
---------------------------

On the :guitab:`I/O` tab of the :jobtype:`3D auto-refine` job-type set:

:Input optimisation set:: PseudoSubtomo/job007/optimisation_set.star

    (If an optimisation set file is provided, the input images STAR, reference map and solvent mask filenames are set based on its content, if not overrode below.)

:Input images STAR file:: \

    (Note this is blank as it is extracted from the optimisation set file.)

:Reference map:: InitialModel/job008/initial_model.mrc

:Reference mask (optional):: \

     (We're not using a mask at this moment so leave this empty for now. The optimisation set file shouldn't contain a reference mask either as it's been created after importing tomograms and coordinates.)


On the :guitab:`Reference` tab, set:

:Ref. map is on absolute greyscale?: Yes

:Initial low-pass filter (A): 50

     (We typically start auto-refinements from low-pass filtered maps to prevent bias towards high-frequency components in the map, and to maintain the `gold-standard` of completely independent refinements at resolutions higher than the initial one.)

:Symmetry: C6

On the :guitab:`CTF` tab set:

:Do CTF correction?: Yes

:Ignore CTFs until first peak?: No

On the :guitab:`Optimisation` tab set:

:Mask diameter (A):: 230

and keep the defaults for the remaining options.

On the :guitab:`Auto-sampling` tab, one can usually keep the defaults.
Note that the orientational sampling rates on the :guitab:`Sampling` tab will only be used in the first few iterations, from there on the algorithm will automatically increase the angular sampling rates until convergence.
Therefore, for all refinements with less than octahedral or icosahedral symmetry, we typically use the default angular sampling of 7.5 degrees, and local searches from a sampling of 1.8 degrees.
Only for higher symmetry refinements, we use 3.7 degrees sampling and perform local searches from 0.9 degrees.
The only thing we will change here is to set:


:Use finer angular sampling faster?: Yes

     (This will be more aggresive in proceeding with iterations of finer angular sampling faster.
     This will therefore speed up the calculations.
     You might want to check that you're not loosing resolution for this in the later stages of your own processing, but during the initial stages it often does not matter much.)

Ignore the :guitab:`Helix` tab, and on the :guitab:`Compute` tab set:

:Use parallel disc I/O?: Yes

:Number of pooled particles:: 16

:Skip padding?: No

:Skip gridding?: Yes

:Pre-read all particles into RAM?: No


:Copy particles to scratch directory: \

:Combine iterations through disc?: No

:Use GPU acceleration?: Yes

:Which GPUs to use: \

    (Set the id sequence of the GPU cards separated by colon (``0:1:2``) or leave it blank to automatically use all configured cards)

On the :guitab:`Running` tab, set:

:Number of MPI procs: 5

:Number of threads: 8

As the MPI nodes are divided between one master (who does nothing else than bossing the others around) and two sets of slaves who do all the work on the two half-sets, it is most efficient to use an odd number of MPI processors, and the minimum number of MPI processes for :jobtype:`3D auto-refine` jobs is 3.
Memory requirements may increase significantly at the final iteration, as all frequencies until Nyquist will be taken into account, so for larger sized boxes than the ones in this test data set you may want to run with as many threads as you have cores on your cluster nodes.

On our computer with 4 GPUs, we used 5 MPIs and 8 threads, and this calculation took approximately 1 hour.


Analysing the results
---------------------

At every iteration the program writes out two ``run_it0??_half?_model.star`` and two ``run_it0??_half?_class001.mrc`` files: one for each independently refined half of the data.
Only upon convergence a single ``run_model.star`` and ``run_class001.mrc`` file will be written out (without ``_it0??`` in their names).
Because in the last iteration the two independent half-reconstructions are joined together, the resolution will typically improve significantly in the last iteration.
Because the program will use all data out to Nyquist frequency, this iteration also requires more memory and CPU.

Note that the automated increase in angular sampling is an important aspect of the auto-refine procedure.
It is based on signal-to-noise considerations that are explained in :cite:`scheres_relion:_2012`, to estimate the accuracy of the angular and translational assignments.
The program will not use finer angular and translational sampling rates than it deems necessary (because it would not improve the results).
The estimated accuracies and employed sampling rates, together with current resolution estimates are all stored in the ``_optimiser.star`` and ``_model.star`` files, but may also be extracted from the stdout file. For more information, check the SPA tutorial :ref:`high-resolution 3D refinement <sec_refine3d>` step.

If you provided an :ref:`optimisation set <sec_sta_optimisation_set>` file as input then the program also writes out another optimisation set ``run_optimisation_set.star`` file, updated with ``run_data.star``, ``run_half<1/2>_class001_unfil.mrc`` files and the solvent mask file if provided as input.
This ``run_optimisation_set.star`` file  shouldn't be confused with the ``_optimiser.star`` files used regularly by `relion_refine`.


This job will have likely achieved Nyquist frequency so, to go to higher resolution, we will need a new set of pseudo-subtomo particles and reference map at a smaller binning factor, 2 or directly 1.
Before this, since the refined map we obtained in this initial 3D refinement covers HIV capsid and matrix, we need to make sure the mask we will be using in the next refinement is aligned and focused on the capsid only.
We suggest to recenter the reference as masks provided in ``masks/`` folder are already centered.
You could look at the output refined map (``Refine3D/job009/run_class001.mrc``) and mask (``masks/mask_align_bin4.mrc``) with a 3D viewer like IMOD :textsc:`3dmod` to estimate the Z offset between both maps, in pixels. In our case, it is 2.75 pixels but this could be different as it depends on the initial *de novo* model. Thus, recentering the particles can be done from the command-line:

::

    relion_star_handler --i Refine3D/job009/run_data.star \
    --o Refine3D/job009/run_data_z2.75.star --center --center_Z 2.75


To assess the capsid within the reference map is aligned with the mask, we could reconstruct it using the :jobtype:`Tomo reconstruct particle` job-type, described in the next step :ref:`reconstruct particle <sec_sta_reconstructpart>`.