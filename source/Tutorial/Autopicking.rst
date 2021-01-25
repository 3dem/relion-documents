Autopicking
===========

LoG-based auto-picking
----------------------

We will now use a template-free auto-picking procedure based on a Laplacian-of-Gaussian (LoG) filter to select an initial set of particles.
These particles will then be used in a :jobtype:`2D classification` job to generate templates for a second :jobtype:`Auto-picking` job.
Because we do not need many particles in the first round, we will only perform LoG-based auto-picking on the first 3 micrographs.
Note that in general, one would probably perform LoG-based picking on all available micrographs to get as good templates as possible.
However, here we only use a few micrographs to speed up the calculations in this tutorial.

First, in order to select a few micrographs, go to the :jobtype:`Subset selection` job, and on the :guitab:`I/O` tab leave everything empty, except:

:OR select from picked coords:: ManualPick/job004/coords\_suffix\_manualpick.star

     (which was generated when we saved a few manually picked coordinates.
     We are not going to use the coordinates here, we are only using that job to make a subset selecton of the micrographs.)

We used an alias `5mics` for this job.
When you press :runbutton:`Run!`, the same pop-up window of the :jobtype:`Manual picking` job will appear again, i.e. the one with all the :button:`pick` and :button:`CTF` buttons.
Use the 'File' menu to 'Invert selection'; click on the check box in front of the first five micrographs to select those; and then use the 'File' menu again to 'Save selection'.
This will result in a file called ``ManualPick/job004/micrographs_selected.star``, which we will use for the :jobtype:`Auto-picking` job below.

Then, proceed to the :jobtype:`Auto-picking` job, and on the :guitab:`I/O` tab set:

:Input micrographs for autopick:: Select/job005/micrographs\_selected.star

:Pixel size in micrographs (A): -1

     (The pixel size will be set automatically from the information in the input STAR file.)

:2D references:: \

     (Leave this empty for template-free LoG-based auto-picking.)

:OR\: provide a 3D reference?: No

:OR\: use Laplacian-of-Gaussian?: Yes


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


Ignore the :guitab:`References` tab, and on the :guitab:`autopicking` tab, the first four options will be ignored.
Set the rest as follows:

:Write FOM maps?: No

     (This will be used in the template-based picking below.)

:Read FOM maps?: No

     (This will be used in the template-based picking below.)

:Shrink factor:: 0

     (By setting shrink to 0, the autopicking program will downscale the micrographs to the resolution of the lowpass filter on the references.
     This will go much faster and require less memory, which is convenient for doing this tutorial quickly.
     Values between 0 and 1 will be the resulting fraction of the micrograph size.
     Note that this will lead to somewhat less accurate picking than using shrink=1, i.e. no downscaling.
     A more detailed description of this new parameter is given in the next subsection.)

:Use GPU acceleration?: No

     (LoG-based picking has not been GPU-accelerated as the calculations are very quick anyway.)


Ignore the :guitab:`Helix` tab, and run using a single MPI processor  on the :guitab:`Running tab`.
Perhaps an alias like `LoG` would be meaningful? Using a single processor, these calculations take about 15 seconds on our computer.

You can check the results by clicking the `coords_suffix_autopick` option from the :button:`Display:` button.
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

:Coordinate-file suffix:: AutoPick/job006/coords\_suffix\_autopick.star

     (Use the `Browse` button to select this file)

:OR re-extract refined particles?: No

     (This option allows you to use a ``_data.star`` file from a :jobtype:`2D cassification`, :jobtype:`3D classification` or :jobtype:`3D auto-refine` job for re-extraction of only those particles in the :textsc:`star` file.
     This may for example be useful if you had previously down-scaled your particles upon extraction, and after initial classifications you now want to perform refinements with the original-scaled particles.
     As of |RELION|-3.0, this functionality has been extended with an option to 're-center refined coordinates' on a user-specified X,Y,Z-coordinate in the 3D reference used for a :jobtype:`3D classification` or :jobtype:`3D auto-refine` job.
     This will adjust the X and Y origin coordinates of all particles, such that a reconstruction of the newly extracted particles will be centered on that X,Y,Z position.
     This is useful for focused refinements.)

:Manually set pixel size?: No

     (This is only necessary when the input micrograph :textsc:`star` file does NOT contain CTF information.)


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

As we will later on also use the same job-type to extract all template-based auto-picked particles, it may be a good idea to give this job an alias like `LoG`.
Ignore the :guitab:`Helix` tab, and run using a single MPI processor.

Your particles will be extracted into MRC stacks (which always have an `.mrcs` extension in |RELION|) in a new directory called `Extract/job007/Movies/`.
It's always a good idea to quickly check that all has gone OK by visualising your extracted particles selecting `out: particles.star` from the :button:`Display:` button.
Right-mouse clicking in the display window may be used for example to select all particles (`Invert selection`) and calculating the average of all unaligned particles (`Show average of selection`).


Making templates for auto-picking
---------------------------------

To calculate templates for the subsequent auto-picking of all micrographs, we will use the :jobtype:`2D classification` job-type.
On the :guitab:`I/O` tab, select the `Extract/job007/particles.star` file (using the :button:`Browse` button), and on the :guitab:`CTF` tab set:

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

     (We hardly ever change this)

:Use fast subsets for large data sets?: No

     (If set to Yes, the first 5 iterations will be done with random subsets of only K\*100 particles, with K being the number of classes; the next 5 with K\*300 particles, the next 5 with 30\% of the data set; and the final ones with all data.
     This was inspired by a cisTEM implementation by Tim Grant, Niko Grigorieff et al.
     This option may be useful to make classification of very large data sets.
     With hundreds of thousands of particles it is much faster.
     For a small data set like this one, it is not needed.)

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


On the :guitab:`Sampling` tab we hardly ever change the defaults.
Six degrees angular sampling is enough for most projects, although some large icosahedral viruses may benefit from finer angular samplings.
In that case, one could first run 25 iterations with a sampling of 6 degrees, and then continue that same run (using the :button:`Continue!` button) for an additional five iteration (by setting `Number of iterations: 30` on the :guitab:`Optimisation` tab) with a sampling of say 2 degrees.
For this data set, this is NOT necessary at all.
It is useful to note that the same :button:`Continue!` button may also be used to resume a job that has somehow failed before, in which case one would not change any of the parameters.
For continuation of :jobtype:`2D classification`, :jobtype:`3D initial model`, :jobtype:`3D classification`, or :jobtype:`3D auto-refine` jobs one always needs to specify the `_optimiser.star` file from the iteration from which one continues on the :guitab:`I/O` tab.

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
     In that case, specify the name of the scratch disk where you can make a temporary directory, e.g. /ssd)

:Combine iterations through disc?: No

     (This way all MPI nodes combine their data at the end of each iteration through the network.
     If the network is your main bottle-neck or somehow causing problems, you can set this option to No.
     In that case, all MPI nodes will write/read their data to disc.)

:Use GPU acceleration?: Yes

     (If you have a suitable GPU, this job will go much faster.)

:Which GPUs to use:: 0:1:2:3

     (This will depend on the available GPUs on your system! If you leave this empty, the program will try to figure out which GPUs to use, but you can explicitly tell it which GPU IDs , e.g. 0 or 1, to use.
     If you use multiple MPI-processors, you can run each MPI process on a specified GPU.
     GPU IDs for different MPI processes are separated by colons, e.g. 0:1:0:1 will run MPI process 0 and 2 on GPU 0, and MPI process 1 and 3 will run on GPU 1.)


On the :guitab:`Running` tab, specify the 'Number of MPI processors' and the 'Number of threads' to use.
The total number of requested CPUs, or cores, will be the product of the two values.
Note that :jobtype:`2D classification`, :jobtype:`3D classification`, :jobtype:`3D initial model` and :jobtype:`3D auto-refine` use one MPI process as a master, which does not do any calculations itself, but sends jobs to the other MPI processors.
Therefore, if one specifies 4 GPUs above, running with five MPI processes would be a good idea.
Threads offer the advantage of more efficient RAM usage, whereas MPI parallelization scales better than threads.
Often, for :jobtype:`3D classification` and :jobtype:`3D auto-refine` jobs you will probably want to use many threads in order to share the available RAM on each (multi-core) computing node. 2D classification is less memory-intensive, so you may not need so many threads.
However, the points where communication between MPI processors (the bottle-neck in scalability there) becomes limiting in comparison with running more threads, is different on many different clusters, so you may need to play with these parameters to get optimal performance for your setup.
We pre-read all particles into RAM, used parallel disc I/O, 4 GPUs and 5 MPI process with 6 threads each, and our job finished in approximately three minutes.

Because we will run more :jobtype:`2D classification` jobs, it may again be a good idea to use a meaningful alias, for example `LoG`.
You can look at the resulting class averages using the :button:`Display:` button to select `out: run_it025_model.star` from.
On the pop-up window, you may want to choose to look at the class averages in a specific order, e.g. based on `rlnClassDistribution` (in reverse order, i.e. from high-to-low instead of the default low-to-high) or on `rlnAccuracyRotations`.


Selecting templates for auto-picking
------------------------------------

Selection of suitable class average images is done in the :jobtype:`Subset selection` job-type.
On the :guitab:`I/O` tab, remove the picked coords entry from before, and select the `Class2D/LoG/run_it025_model.star` file using the :button:`Browse` button on the line with `Select classes from model.star:`.

On the :guitab:`Class options` tab, give:

:Re-center the class averages?: Yes

     (This option allows automated centering of the 2D class averages.
     The images are centered based on their center-of-mass, and the calculations for this require that the particles are WHITE (not black).
     Re-centering is often necessary, as class averages may become non-centered in the 2D classification run.
     In particular when using class average images for auto-picking it is important that the are centered, as otherwise all your particle coordinates will become systematically off-centered.) 

:Regroup the particles?: No

     (This option is useful when there are very few (selected) particles on individual micrographs, in which case the estimation of noise power spectra and scale factors become unstable.
     By default, the latter are calculated independently per micrograph.
     This option allows to grouping particles from multiple micrographs together in these calcutaions. |RELION| will warn you (in classification or auto-refine runs) when your groups become too small.)


Ignore the other tabs, and use an alias like `templates4autopick`.
You may again want to order the class averages based on their `rlnClassDistribution`.
Select a few class averages that represent different views of your particle.
Don't repeat very similar views, and don't include bad class averages.
We selected four templates from our run.
Selection is done by left-clicking on the class averages.
You can save your selection of class averages from the right-click pop-up menu using the `Save selected classes` option.


Auto-picking
------------

We will now use the selected 2D class averages as templates in a reference-based run of the :jobtype:`Auto-picking` job-type.
However, before we will run the auto-picking on all micrographs, we will need to optimise four of its main parameters on the :guitab:`autopicking` tab: the `Picking threshold`, the `Minimum inter-particle distance`, the `Maximum stddev noise`, and the `Minimum avg noise`.
This will be done on only a few micrographs in order to save time.
We will use the same five micrographs we selected for the LoG-based auto-picking before.

Then, on the :guitab:`I/O` tab of the :jobtype:`Auto-picking` job-type, set:

:Input micrographs for autopick:: Select/5mics/micrographs.star

:Pixel size in micrographs (A): -1

     (The pixel size will be set automatically from the information in the input STAR file.)

:2D references:: Select/templates4autopick/class\_averages.star

:OR\: provide a 3D reference?: No

:OR\: use Laplacian-of-Gaussian?: No


Ignore the :guitab:`Laplacian`, and on the :guitab:`References` tab, set:

:Lowpass filter references (A):: 20

     (It is very important to use a low-pass filter that is significantly LOWER than the final resolution you aim to obtain from the data, to keep ``Einstein-from-noise`` artifacts at bay)

:Highpass filter (A):: -1

     (If you give a positive value, e.g. 200, then the micrograph will be high-pass filtered prior to autopicking.
     This can help in case of strong grey-scale gradients across the micrograph.)

:Pixel size in references (A):: 3.54

     (If a negative value is given, the references are assumed to be on the same scale as the input micrographs.
     If this is not the case, e.g. because you rescaled particles that were used to create the references upon their extraction, then provide a positive value with the correct pixel size in the references here.
     As we downscaled the particles by a factor of 4 (i.e. from 256 to 64) in the :jobtype:`Particle extraction` job, **the pixel size in the references is now 4 × 0.885 = 3.54 Å**)

:Mask diameter (A): -1

    (When a negative value is given, the diameter of the mask will be determined automatically from the input reference images to be the same as the one used in the :jobtype:`2D classification` job.)

:Angular sampling (deg):: 5

     (This value seems to work fine in almost all cases.)

:References have inverted contrast?: Yes

     (Because we have black particles in the micrographs, and the references we will use are white.)

:Are References CTF corrected?: Yes

     (Because we performed 2D class averaging with the CTF correction.)

:Ignore CTFs until first peak:: No

     (Only use this option if you also did so in the :jobtype:`2D classification` job that you used to create the references.)

On the :guitab:`autopicking` tab, set:

:Picking threshold:: 0.8

     (This is the threshold in the FOM maps for the peak-search algorithms.
     Particles with FOMs below this value will not be picked.)

:Minimum inter-particle distance (A):: 200

     (This is the maximum allowed distance between two neighbouring particles.
     An iterative clustering algorithm will remove particles that are nearer than this distance to each other.
     Useful values for this parameter are often in the range of 50-60\% of the particle diameter.)

:Maximum stddev noise:: -1

     (This is useful to prevent picking in carbon areas, or areas with big contamination features.
     Peaks in areas where the background standard deviation in the normalized micrographs is higher than this value will be ignored.
     Useful values are probably in the range 1.0 to 1.2.
     Set to -1 to switch off the feature to eliminate peaks due to high background standard deviations.)

:Minimum avg noise:: -999

     (This is useful to prevent picking in carbon areas, or areas with big contamination features.
     Peaks in areas where the background standard deviation in the normalized micrographs is higher than this value will be ignored.
     Useful values are probably in the range -0.5 to 0.
     Set to -999 to switch off the feature to eliminate peaks due to low average background densities.)

:Write FOM maps?: Yes

     (See the explanation below.)

:Read FOM maps?: No

     (See the explanation below.)

:Shrink factor:: 0

     (By setting shrink to 0, the autopicking program will downscale the micrographs to the resolution of the lowpass filter on the references.
     This will go much faster and require less memory, which is convenient for doing this tutorial quickly.
     Values between 0 and 1 will be the resulting fraction of the micrograph size.
     Note that this will lead to somewhat less accurate picking than using shrink=1, i.e. no downscaling.
     A more detailed description of this new parameter is given in the next subsection.)

:Use GPU acceleration?: Yes

     (Only if you have a suitable GPU!)

:Which GPUs to use:: 0

     (If you leave this empty, the program will try to figure out which GPUs to use, but you can explicitly tell it which GPU IDs , e.g. 0 or 1, to use.
     If you use multiple MPI-processors (not for this case!), you can run each MPI process on a specified GPU.
     GPU IDs for different MPI processes are separated by colons, e.g. 0:1:0:1 will run MPI process 0 and 2 on GPU 0, and MPI process 1 and 3 will run on GPU 1.)


Ignore the :guitab:`Helix` tab, and run using a single MPI processor  on the :guitab:`Running tab`.
Perhaps an alias like `optimise_params` would be meaningful? When using GPU-acceleration, the job completes in half a minute.

The expensive part of this calculation is to calculate a probability-based figure-of-merit (related to the cross-correlation coefficient between each rotated reference and all positions in the micrographs.
This calculation is followed by a much faster peak-detection algorithm that uses the threshold and minimum distance parameters mentioned above.
Because these parameters need to be optimised, the program will write out so-called FOM maps as specified on the :guitab:`References` tab.
These are two large (micrograph-sized) files per reference.
To avoid running into hard disc I/O problems, the autopicking program can only be run sequentially (hence the single MPI processor above) when writing out FOM maps.

Once the FOM maps have been written to disc they can be used to optimise the picking parameters much faster.
First, examine the auto-picked particles with the current settings using the `coords_suffix_autopick` option from the :button:`Display:` button of the job you just ran.
Note that the display window will take its parameters (like size and sigma-contrast) from the last :jobtype:`Manual picking` job you executed.
You can actually change those parameters in the :jobtype:`Manual picking` job-type, and save the settings use the option `Save job settings` from the top left `Jobs` menu.
Do this, after you've set on the following on the :guitab:`Colors` tab:


:Blue<>red color particles?: Yes

:MetaDataLabel for color:: rlnAutopickFigureOfMerit

:STAR file with color label:: \

:Blue value:: 1

:Red value:: 0

Executing the job on the :guitab:`Running` tab will produce a similar GUI with :button:`pick` and :button:`CTF` buttons as before.
Open both micrographs from the display window, and decide whether you would like to pick more or less particles (i.e. decrease or increase the threshold) and whether they could be closer together or not (fot setting the minimum inter-particle distance).
Note that each particle is colored from red (very low FOM) to blue (very high FOM).
You can leave the display windows for both micrographs open, while you proceed with the next step.

Select the ``AutoPick/optimise_params`` job from the :joblist:`Finished jobs`, and change the parameters on the :guitab:`autopicking` tab.
Also, change:

:Write FOM maps?: No

:Read FOM maps?: Yes

When executing by clicking the :button:`Continue!` button, this will re-read the previously written FOM maps from disc instead of re-doing all FOM calculations.
The subsequent calculation of the new coordinates will then be done in a few seconds.
Afterwards, you can right-click in the micrograph display windows and select ``Reload coordinates`` from the pop-up menu to read in the new set of coordinates.
This way you can quickly optimise the two parameters.

Have a play around with all three parameters to see how they change the picking results.
Once you know the parameters you want to use for auto-picking of all micrographs, you click the :jobtype:`Auto-picking` option in the job-type browser on the top left of the GUI to select a job with a :runbutton:`Run!` button.
On the :guitab:`I/O` tab, you replace the input micrographs :textsc:`star` file with the 2 selected micrographs with the one from the original :jobtype:`CTF estimation` job (``CtfFind/job003/micrographs_ctf.star``).
Leave everything as it was on the :guitab:`References` tab, and on the :guitab:`autopicking` tab set:

:Picking threshold:: 0.0

:Minimum inter-particle distance (A):: 100

     (Good values are often around 50-70\% of the particle diameter.)

:Maximum stddev noise:: -1

:Minimum avg noise:: -999

:Write FOM maps?: No

:Read FOM maps?: No


This time, the job may be run in parallel (as no FOM maps will be written out).
On the :guitab:`Running` tab, specify the number of cores to run auto-picking on.
The maximum useful number of MPI processors is the number of micrographs in the input :textsc:`star` file.
Using only a single MPI process and a single GPU, our calculation still finisged in about one minute.
We used as alias `template`.

Note that there is an important difference in how the :button:`Continue!` button works depending on whether you read/write FOM maps or not.
When you either write or read the FOM maps and you click :button:`Continue!`, the program will re-pick all input micrographs (typically only a few).
However, when you do not read, nor write FOM maps, i.e. in the second job where you'll autopick all micrographs, upon clicking the :button:`Continue!` button, only those micrographs that were not autopicked yet will be done.
This is useful in the iterative running of scheduled jobs, e.g. for on-the-fly data processing during your microscopy session.
Also see section :ref:`sec_schedules` for more details.
If you want to-repick all micrographs with a new set of parameters (instead of doing only unfinished micrographs), then click the :jobtype:`Auto-picking` entry on the jobtype-browser on the left to get a :runbutton:`Run!` button instead, which will then make a new output directory.

You can again check the results by clicking the ``coords_suffix_autopick`` option from the :button:`Display:` button.
Some people like to manually go over all micrographs to remove false positives.
For example, carbon edges or high-contrast artifacts on the micrographs are often mistaken for particles.
You can do this for each micrograph using the pop-up window from the :button:`Display:` button.
Remove particles using the middle-mouse button; you can hold it down to remove many false positives in larger areas.
Remember to save the new coordinates using the right-mouse click pop-up menu!

Once you're happy with the overall results, in order to save disc space you may want to delete the FOM-maps that were written out in the first step.
You can use the `Gentle clean` option from the :button:`Job actions` button to do that conveniently.

Once you are happy with your entire set of coordinates, you will need to re-run a :jobtype:`Particle extraction` job, keeping everything as before, and change the `Input coordinates` for the newly generated, autopick ones.
This will generate your initial single-particle data set that will be used for further refinements below.
Perhaps an alias like `template` would be meaning ful?


The shrink parameter
^^^^^^^^^^^^^^^^^^^^

To enable faster processing, |RELION| implements a filtering option of the micrographs through the command-line argument ``--shrink``.
The simplest way to use it is to simply use ``--shrink 0``.
But it can be used with much more control.
If this is desired, it works in the following way:


The default value for ``--shrink`` is 1.0, which has no effect and does not filter the micrographs at all.
This is identical behaviour to versions prior to the |RELION|-2.0 autopicker.

-   ``--shrink`` val = 0  results in a micrograph lowpassed to `--lowpass`, the same as that of the reference templates.
    This is recommended use for single-particle analysis (but not for helical picking).
-   ``--shrink`` 0 < val <= 1 results in a size = val :math:`\cdot` micrograph_size, i.e. val is a scaling factor applied to the micrographs original size.
-   ``--shrink`` val > 1 results in a size = val - (val :math:`\mod` 2), i.e. the smallest even integer value lower than val.
    This is then a way to give the micrographs a specific (even) integer size.

If the new size is smaller than ``--lowpass``, this results in a **non-fatal** warning, since this limits resolution beyond the requested (or default) resolution.
Because the |RELION| autopicker does many FFTs, the size of micrographs is now also automatically adjusted to avoid major pitfalls of FFT computation.
A note of this and how it can be overridden is displayed in the initial output of each autopicking the user performs.