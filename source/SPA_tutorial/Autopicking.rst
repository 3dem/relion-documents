Particle picking
================

Select a subset of the micrographs
----------------------------------

We will now use a template-free auto-picking procedure based on a Laplacian-of-Gaussian (LoG) filter to select an initial set of particles.
These particles will then be used in a :jobtype:`2D classification` job to generate 2D class averages.
The tutorial up until |RELION|-3.1 would suggest to use the resulting class averages as templates for a second, reference-based :jobtype:`Auto-picking` job.
Since |RELION|-4.0, there is also an integrated |Topaz| wrapper in the :jobtype:`Auto-picking` job, which will be used instead.
In addition, we will use a new automated 2D class average selection procedure to select particles that contribute to good classes without any user interaction.
The selected particles will then be used to train the neural network in |Topaz| to specifically pick particles for this data set.
Alternatively, one could run |Topaz| picking with their default neural network straight away.
In that case, one could skip the jobs of LoG-picking, 2D classification, automated 2D class selection and re-training of the |Topaz| network below, and proceed straight to the last :jobtype:`Auto-picking` job on this page.

One typically trains the |Topaz| neural network on a relatively small subset of the micrographs.
In order to select a subset of the micrographs, go to the :jobtype:`Subset selection` job, and on the :guitab:`I/O` tab leave everything empty, except:

:OR select from micrographs.star:: CtfFind/job003/micrographs\_ctf.star

Then, on the :guitab:`Subsets` tab, set:

:OR split into subsets?: Yes
:Randomise order before making subsets?: No
:Subset size:: 10
:OR number of subsets:: -1

Then press :runbutton:`Run!`, which will create star files with subsets of 10 micrographs in the output directory. We will only use the first one ``Select/job005/micrographs_split1.star``.

Note that if one would have preferred a more user-interactive way of selecting micrographs for training, one could have also selected certain micrographs in the GUI of the previous :jobtype:`Manual picking` job, to then save a file called ``micrographs_selected.star`` inside that output directory.


LoG-based auto-picking
----------------------

Now, proceed to the :jobtype:`Auto-picking` job, and on the :guitab:`I/O` tab set:

:Input micrographs for autopick:: Select/job005/micrographs\_split1.star

:Pixel size in micrographs (A): -1

     (The pixel size will be set automatically from the information in the input STAR file.)

:Use reference-based template-matching?: No

:OR\: use Laplacian-of-Gaussian?: Yes

:OR\: use Topaz?: No


On the :guitab:`Laplacian` tab, set:

:Min. diameter for loG filter (A): 150

:Max. diameter for loG filter (A): 180

     (This should correspond to the smallest and largest size of your particless projections in Ångstroms.)

:Are the particles white?: No

     (They are black.)

:Maximum resolution to consider: 20

     (Just leave the default value here.)

:Adjust default threshold: 0

     (Positive values, i.e. high thresholds, will pick fewer particles, negative values will pick fewer particles.
     Useful values are probably in the range [-1,1], but in many cases the default value of zero will do a decent job.
     The threshold is moved this many standard deviations away from the average.)

:Upper threshold: 5

     (Use this to discard picks with LoG values that are this many standard deviations above the average, e.g. to avoid high contrast contamination like ice and ethane droplets.
     Good values depend on the contrast of micrographs and may need to be interactively explored; for low contrast micrographs, values of ~ 1.5 may be reasonable, but this value is too low for the high-contrast micrographs in this tutorial.)


Ignore the :guitab:`Topaz`, :guitab:`References`, :guitab:`autopicking` and :guitab:`Helix` tabs, and run using a single MPI processor  on the :guitab:`Running tab`.
Perhaps an alias like ``LoG`` would be meaningful? Using a single processor, these calculations take about 15 seconds on our computer.

You can check the results by clicking the ``autopick.star`` option from the :button:`Display:` button.
One could manually add/delete particles in the pop-up window that appears at this stage.
In addition, one could choose to pick more or fewer particle by running a new job while adjusting the default threshold on the :guitab:`Laplacian` tab, and/or the parameters for the stddev and avg of the noise on the :guitab:`autopicking` tab.
However, at this stage we are merely after a more-or-less OK initial set of particles for the generation of templates for a second auto-picking job, so in many cases this is probably not necessary.


Particle extraction
-------------------

Once you have a coordinate file for every micrograph that you want to pick particles from, you can extract the corresponding particles and gather all required metadata through the :jobtype:`Particle extraction` job-type.
On the corresponding :guitab:`I/O` tab, set:

:micrograph STAR file:: CtfFind/job003/micrographs\_ctf.star

     (Use the `Browse` button to select this file.
     You could also chose the selected micrographs file from the ManualPick directory.
     It doesn't matter as there are only coordinate files for the three selected micrographs anyway.
     Warning that coordinates files are missing for the rest of the micrographs will appear in red in the bottom window of the GUI.)

:Input coordinates:: AutoPick/job006/autopick.star

     (Use the `Browse` button to select this file)

:OR re-extract refined particles?: No

     (This option allows you to use a ``_data.star`` file from a :jobtype:`2D cassification`, :jobtype:`3D classification` or :jobtype:`3D auto-refine` job for re-extraction of only those particles in the :textsc:`star` file.
     This may for example be useful if you had previously down-scaled your particles upon extraction, and after initial classifications you now want to perform refinements with the original-scaled particles.
     As of |RELION|-3.0, this functionality has been extended with an option to 're-center refined coordinates' on a user-specified X,Y,Z-coordinate in the 3D reference used for a :jobtype:`3D classification` or :jobtype:`3D auto-refine` job.
     This will adjust the X and Y origin coordinates of all particles, such that a reconstruction of the newly extracted particles will be centered on that X,Y,Z position.
     This is useful for focused refinements.)

:Write output in float16?: Yes

     (If set to Yes, this program will write output images in float16 MRC format. This will save a factor of two in disk space compared to the default of writing in float32. Note that RELION and CCPEM will read float16 images, but other programs may not (yet) do so.)


On the :guitab:`extract` tab you set the parameters for the actual particle extraction:

:Particle box size (pix):: 256

     (This should always be an even number!)

:Invert contrast?: Yes

     (This makes white instead of black particles.)

:Normalize particles?: Yes

     (We always normalize.)

:Diameter background circle (pix):: 200

     (Particles will be normalized to a mean value of zero and a standard-deviation of one for all pixels in the background area.The background area is defined as all pixels outside a circle with this given diameter in pixels (before rescaling).
     When specifying a negative value, a default value of 75\% of the Particle box size will be used.)

:Stddev for white dust removal:: -1

:Stddev for black dust removal:: -1

     (We only remove very white or black outlier pixels if we actually see them in the data.
     In such cases we would use stddev values of 5 or so.
     In this data set there are no outlier pixels, so we don't correct for them, and leave the default values at -1 (i.e. don't do anything).

:Rescale particles?: Yes

     (Down-scaling particles will speed up computations.
     Therefore, we often down-scale particles in the initial stages of processing, in order to speed up the initial classifications of suitable particles.
     Once our reconstructions get close to the Nyquist frequency, we then re-extract the particles without down-scaling.)

:Re-scaled sized (pixels)?: 64

:Use autopick FOM threshold?: No

     (This option allows to only extract those particles with the highest figure-of-merits from the autopicking procedure. We will use this later on to extract particles picked by |Topaz|.)

As we will later on also use the same job-type to extract all template-based auto-picked particles, it may be a good idea to give this job an alias like ``LoG``.
Ignore the :guitab:`Helix` tab, and run using a single MPI processor.

Your particles will be extracted into MRC stacks (which always have an ``.mrcs`` extension in |RELION|) in a new directory called ``Extract/job007/Movies/``.
It's always a good idea to quickly check that all has gone OK by visualising your extracted particles selecting ``out: particles.star`` from the :button:`Display:` button.
Right-mouse clicking in the display window may be used for example to select all particles (`Invert selection`) and calculating the average of all unaligned particles (`Show average of selection`).


2D class averaging to select good particles
-------------------------------------------

To calculate templates for the subsequent auto-picking of all micrographs, we will use the :jobtype:`2D classification` job-type.

On the :guitab:`I/O` tab, set:

:Input images STAR file: Extract/job007/particles.star 

:Continue from here: \ 

     (Note that any :jobtype:`2D classification`, :jobtype:`3D initial model`, :jobtype:`3D classification`, or :jobtype:`3D auto-refine` jobs may be continued in case it stalls, by providing the `_optimiser.star` file from the last completed iteration.)

On the :guitab:`CTF` tab set:

:Do CTF-correction?: Yes

     (We will perform full phase+amplitude correction inside the Bayesian framework)

:Ignore CTFs until first peak?: No

     (This option is occasionally useful, when amplitude correction gives spuriously strong low-resolution components, and all particles get classified together in very few, fuzzy classes.)


On the :guitab:`Optimisation` tab, set:

:Number of classes:: 50

     (For cryo-EM data we like to use on average at least approximately 100 particles per class.
     For negative stain one may use fewer, e.g. 20-50 particles per class.
     However, with this small number of particles, we have observed a better separation into different classes by relaxing these numbers.
     Possibly, always having a minimum of 50 classes is not a bad idea.)

:Regularisation parameter T:: 2

     (For the exact definition of T, please refer to :cite:`scheres_bayesian_2012`.
     For cryo-EM 2D classification we typically use values of T=2-3, and for 3D classification values of 3-4.
     For negative stain sometimes slightly lower values are better.
     In general, if your class averages appear very noisy, then lower T; if your class averages remain too-low resolution, then increase T.
     The main thing is to be aware of overfitting high-resolution noise.)

:Number of iterations:: 25

     (For the default EM-algorithm, one normally doesn't change the default of 25 iterations)

:Use gradient-driven algorithm?: No

     (This is a new option in |RELION|-4.0, which runs much faster than the standard EM-algorithm for large data set, and has been observed to yield better class average images in many cases.
     It is however slower for data sets with only a few thousand particles, which is the main reason we are not using it here.)

:Mask diameter (A):: 200

     (This mask will be applied to all 2D class averages.
     It will also be used to remove solvent noise and neighbouring particles in the corner of the particle images.
     On one hand, you want to keep the diameter small, as too much noisy solvent and neighbouring particles may interfere with alignment.
     On the other hand, you want to make sure the diameter is larger than the longest dimension of your particles, as you do not want to clip off any signal from the class averages.)

:Mask individual particles with zeros?: Yes

:Limit resolution E-step to (A):: -1

     (If a positive value is given, then no frequencies beyond this value will be included in the alignment.
     This can also be useful to prevent overfitting.
     Here we don't really need it, but it could have been set to 10-15A anyway.
     Difficult classifications, i.e. with very noisy data, often benefit from limiting the resolution.)

:Center class averages?: Yes

     (This is a new option in |RELION|-4.0. It will re-center all class average images every iteration based on their center of mass. 
     This is useful for their subsequent use in template-based auto-picking, but also for the automated 2D class average image selection in the next section.)

On the :guitab:`Sampling` tab we hardly ever change the defaults.
Six degrees angular sampling is enough for most projects, although some large icosahedral viruses or some filamentous structures may benefit from finer angular samplings.

Ignore the :guitab:`Helix` tab, and on the :guitab:`Compute` tab, set:

:Use parallel disc I/O?: Yes

     (This way, all MPI slaves will read their own particles from disc.
     Use this option if you have a fast (parallel?) file system.
     Note that non-parallel file systems may not be able to handle parallel access from multiple MPI nodes.
     In such cases one could set this option to No.
     In that case, only the master MPI node will read in the particles and send them through the network to the MPI slaves.)

:Number of pooled particles:: 30

     (Particles are processed in individual batches by MPI slaves.
     During each batch, a stack of particle images is only opened and closed once to improve disk access times.
     All particle images of a single batch are read into memory together.
     The size of these batches is at least one particle per thread used.
     The ``nr_pooled_particles`` parameter controls how many particles are read together for each thread.
     If it is set to 30 and one uses 8 threads, batches of 30x8=240 particles will be read together.
     This may improve performance on systems where disk access, and particularly metadata handling of disk access, is a problem.
     Typically, when using GPUs we use values of 10-30; when using only CPUs we use much smaller values, like 3.
     This option has a modest cost of increased RAM usage.)

:Pre-read all particles into RAM?: Yes

     (If set to Yes, all particle images will be read into computer memory, which will greatly speed up calculations on systems with slow disk access.
     *However, one should of course be careful with the amount of RAM available.*
     Because particles are read in double-precision, it will take ( N × box_size × box_size × 4 / (1024 × 1024 × 1024) ) Giga-bytes to read N particles into RAM.
     If parallel disc I/O is set to Yes, then all MPI slaves will read in all particles.
     If parallel disc I/O is set to No, then only the master reads all particles into RAM and sends those particles through the network to the MPI slaves during the refinement iterations.)

:Copy particles to scratch directory?: \

     (This is useful if you don't have enough RAM to pre-read all particles, but you do have a fast (SSD?) scratch disk on your computer.
     In that case, specify the name of the scratch disk where you can make a temporary directory, e.g. ``/ssd``)

:Combine iterations through disc?: No

     (This way all MPI nodes combine their data at the end of each iteration through the network.
     If the network is your main bottle-neck or somehow causing problems, you can set this option to No.
     In that case, all MPI nodes will write/read their data to disc.)

:Use GPU acceleration?: Yes

     (If you have a suitable GPU, this job will go much faster.)

:Which GPUs to use:: 0:1

     (This will depend on the available GPUs on your system! If you leave this empty, the program will try to figure out which GPUs to use, but you can explicitly tell it which GPU IDs , e.g. 0 or 1, to use.
     If you use multiple MPI-processors, you can run each MPI process on a specified GPU. Our machine has 2 GPUs, and we will use on MPI process on each GPU in this example.
     GPU IDs for different MPI processes are separated by colons, e.g. 0:1:0:1 will run MPI process 0 and 2 on GPU 0, and MPI process 1 and 3 will run on GPU 1. GPU IDs for different threads are separated by commas, so when using a single MPI process one could still use multiple GPUs, e.g. 0,1,2,3. Combinations of colons and commas are also possible.)


On the :guitab:`Running` tab, specify:

:Number of MPI procs: 3

     (Note that `when using the EM-algorithm`, :jobtype:`2D classification`, :jobtype:`3D classification`, :jobtype:`3D initial model` and :jobtype:`3D auto-refine` use one MPI process as a master, which does not do any calculations itself, but sends jobs to the other MPI processors.
     Therefore, we often run the EM-algorithm using a single worker MPI process on each of the available GPUs, so we specify 3 here to include the master and one workers on each of the two GPUs.)

:Number of threads: 8

     (Threads offer the advantage of more efficient RAM usage, whereas MPI parallelization may scale better than threads for iterations with many particles.
     Often, you may want to adjust the number of threads to make full use of all the CPU cores on your computer.
     The total number of requested CPUs, or cores, will be the product of the number of MPI processors and the number of threads.)

Because we will run more :jobtype:`2D classification` jobs, it may again be a good idea to use a meaningful alias, for example `LoG`.
You can look at the resulting class averages using the :button:`Display:` button to select `out: run_it025_optimiser.star` from.
On the pop-up window, you may want to choose to look at the class averages in a specific order, e.g. based on `rlnClassDistribution` (in reverse order, i.e. from high-to-low instead of the default low-to-high) or on `rlnAccuracyRotations`.


Selecting good 2D classes for Topaz training
--------------------------------------------

Selection of suitable class average images is done in the :jobtype:`Subset selection` job-type.
Up until |RELION|-3.1, this step was always done interactively by the user, who would select good class averages by clicking on them in the GUI.
As of |RELION|-4.0, there is also an automated procedure, based on a neural network that was trained on thousands of 2D class averages. 
This option will be used below. 

On the :guitab:`I/O` tab, remove the `micrographs.star` file entry from before, and set:

:Select classes from job:: Class2D/job008/run\_it025\_optimiser.star

On the :guitab:`Class options` tab, give:

:Automatically select 2D classes?: Yes

:Minimum threshold for auto-selection: 0.5

     (The score ranges from 0 for absolute rubbish class average images to 1 for gorgeous ones.)

:Python executable: python

     (This version of python should include torch and numpy. We have found that the one from topaz (which is also used for auto-picking) works well. At the LMB, it is here: /public/EM/anaconda3/envs/topaz/bin/python)

:Re-center the class averages?: No

     (This option allows automated centering of the 2D class averages, but we already did that during 2D class averaging.
     In particular when using class average images for auto-picking it is important that the are centered, as otherwise all your particle coordinates will become systematically off-centered.) 

:Regroup the particles?: No

     (This option is useful when there are very few (selected) particles on individual micrographs, in which case the estimation of noise power spectra and scale factors become unstable.
     By default, the latter are calculated independently per micrograph.
     This option allows to grouping particles from multiple micrographs together in these calcutaions. |RELION| will warn you (in classification or auto-refine runs) when your groups become too small.)

On the :guitab:`Subsets` tab, make sure you switch to ``No`` again the following option:

:OR\: split into subsets? No 

Ignore the other tabs, and run the job. You can visualise the results of the automated class selection by selecting ``rank_optimiser.star`` from the :button:`Display:` button, and sort the images on ``rlnClassScore``, in reverse order. Do you want to adjust the threshold for auto-selection?


Re-training the TOPAZ neural network
------------------------------------

In older versions of the |RELION| tutorial, one would now use the selected 2D class averages as templates for reference-based auto-picking. 
Instead, the new wrapper to |Topaz| will be used to first re-train the neural network in |Topaz| and then to pick the entire data set using the retrained network.

On the :guitab:`I/O` tab of the :jobtype:`Auto-picking` job-type, set:

:Input micrographs for autopick:: Select/job005/micrographs\_split1.star

:Pixel size in micrographs (A): -1

:Use reference-based template-matching?: No

:OR\: use Laplacian-of-Gaussian?: No

:OR\: use Topaz?: Yes

On the :guitab:`Topaz` tab, set:

:Topaz executable: /where/ever/it/is/topaz

     (The location of the Topaz executable. 
     You can control the default of this field by setting environment variable ``RELION_TOPAZ_EXECUTABLE``.
     If you need to activate conda environment, please make a wrapper shell script to do so and specify it. 
     At LMB, we use the following script as topaz executable:

     ``#!/bin/bash``
     
     ``source /public/EM/anaconda3/bin/activate topaz``
     
     ``topaz $@``

     )

:Perform topaz training?: Yes

:Input picked coordinates for training: \ 

     (This option can be used to train on manually selected particles from a :jobtype:`Manual picking` job.
     We will use the automatically selected particles from the previous step instead.)

:OR train on a set of particles?: Yes

:Particles STAR file for training: Select/job009/particles.star

:Perform topaz picking?: No

:Particle diameter (A): 180

:Nr of particles per micrograph: 300

:Additional topaz arguments: \ 

On the :guitab:`autopicking` tab, you can ignore everything except the below:

:Use GPU acceleration?: Yes

     (Topaz picking and training require one GPU)

:Which GPUs to use:: 0

Ignore the other tabs, and run using a single MPI processor  on the :guitab:`Running tab`.
On our computer, with a Titan V GPU, this step took 10 minutes.
Perhaps a good time for a quick cup of coffee?


Pick all micrographs with the re-trained TOPAZ neural network
-------------------------------------------------------------

On the :guitab:`I/O` tab of a new :jobtype:`Auto-picking` job, set:

:Input micrographs for autopick:: CtfFind/job003/micrographs\_ctf.star

:Pixel size in micrographs (A): -1

:Use reference-based template-matching?: No

:OR\: use Laplacian-of-Gaussian?: No

:OR\: use Topaz?: Yes

On the :guitab:`Topaz` tab, set:

:Topaz executable: /where/ever/it/is/topaz

:Perform topaz training?: No

:Perform topaz picking?: Yes

:Trained topaz model: AutoPick/job010/model_epoch10.sav

     (If you leave this field empty, then the default pre-trained (general) neural network of |Topaz| will be used.)

:Particle diameter (A): 180

:Nr of particles per micrograph: 300

:Additional topaz arguments: \ 

On the :guitab:`autopicking` tab, you can ignore everything except the below:

:Use GPU acceleration?: Yes

     (Topaz picking and training require one GPU)

:Which GPUs to use:: 0

Ignore the other tabs, and as this has been parallelised, you could for example run using four MPI processors from the :guitab:`Running tab`.
On our computer, this step takes approximately 1 minute.

The number of particles from default |Topaz| picking will be relatively high, because no threshold to its figure-of-merit will be applied. 
The figure-of-merits for all picks are stored in the ``rlnAutopickFigureOfMerit`` column in the output `STAR` files.
A minimum threshold of -3 is probably reasonable in many cases.
One can visualise the figure of merits by colouring the picks in the micrographs. 
For that, change the colouring parameters in the :jobtype:`Manual picking` job-type.

On the following on the :guitab:`Colors` tab, set:

:Blue<>red color particles?: Yes

:MetaDataLabel for color:: rlnAutopickFigureOfMerit

:STAR file with color label:: \

:Blue value:: 5

:Red value:: -3

and save the settings use the option `Save job settings` from the top left `Jobs` menu.

Then, select ``autopick.star`` from the :button:`Display:` button of the ``Autopick/job010`` job to launch the GUI. 
From the ``File`` menu at the top left of its main window, one can use ``Set FOM threshold`` to display only picks with a FOM above the threshold
A similar option is also available in the per-micrograph viewer, using the right-mouse button pop-up menu.
Picks with a high threshold will be blue; picks with a low threshold will be red.


Particle extraction
-------------------

Finally, one needs to re-extract the final set of picked coordinates by again using the :jobtype:`Particle extraction` job-type.

On the corresponding :guitab:`I/O` tab, set:

:micrograph STAR file:: CtfFind/job003/micrographs\_ctf.star

:Input coordinates:: AutoPick/job011/autopick.star

:OR re-extract refined particles?: No

Leave all the other options as they were before, except for the :guitab:`extract` tab, where one sets:

:Use autopick FOM threshold?: Yes

:Minimum autopick FOM: -3

:Write output in float16?: Yes

Running this job will generate the initial particle set for further processing. Using four MPI processors, this job takes a few seconds.


