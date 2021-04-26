Reference-free 2D class averaging
=================================

We almost always use reference-free 2D class averaging to throw away bad particles.
Because bad particles do not average well together, they often go to relatively small classes that yield ugly 2D class averages.
Throwing those away then becomes an efficient way of cleaning up your data.


Running the job
---------------

Most options will remain the same as explained when we were generating templates for the auto-picking in the previous section, but on the :guitab:`I/O` tab of the :jobtype:`2D classification` job-type, set:

:Input images STAR file:: Extract/job012/particles.star

and on the :guitab:`Optimisation` tab, we used:

:Number of classes:: 100

     (because we now have more particles, we can allow more classes than before.)

:Regularisation parameter T:: 2

     (For the exact definition of T, please refer to :cite:`scheres_bayesian_2012`.
     For cryo-EM 2D classification we typically use values of T=2-3, and for 3D classification values of 3-4.
     For negative stain sometimes slightly lower values are better.
     In general, if your class averages appear very noisy, then lower T; if your class averages remain too-low resolution, then increase T.
     The main thing is to be aware of overfitting high-resolution noise.)

:Number of iterations:: 100

     (We will now use a new gradient-driven algorithm that is new in |RELION|-4.0. 
     It uses batches (of hundreds or thousands) of particles per iteration, but therefore needs to perform more iterations. 
     A 100 iterations has been observed to be a good number in many cases)

:Use gradient-driven algorithm?: Yes

     (This is a new option in |RELION|-4.0, which runs much faster than the standard EM-algorithm for large data set, and has been observed to yield better class average images in many cases.)

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

The gradient-driven algorithm doesn't scale well with MPI parallelisation. Using 1 GPUs, and a single MPI process with 12 threads, this job took 13 minutes on our computer.


Selecting good particles for further processing
-----------------------------------------------

After the :jobtype:`2D classification` job has finished, we can launch another :jobtype:`Subset selection` job (``Select/job014``).

On the :guitab:`I/O` tab, set:

:Select classes from job:: Class2D/job013/run\_it100\_optimiser.star

On the :guitab:`Class options` tab, set:

:Automatically select 2D classes?: Yes

:Minimum threshold for auto-selection: 0.35

     (Let's be slightly less restrictive in the selection of particles at this stage, as we don't want to leave any minority views behind.)

We got just over 4200 particles from 35 selected classes.

Note that this procedure of :jobtype:`2D classification` and :jobtype:`Subset selection` may be repeated several times.


Analysing the Class2D results in more detail
--------------------------------------------

.. note::
    If you are in a hurry to get through this tutorial, you can skip this sub-section.
    It contains more detailed information for the interested reader.

For every iteration of 2D or 3D classification |RELION| performs, it writes out a set of files.
For the last iteration of our 2D class averaging calculation these are:


-   ``Class2D/job013/run_it100_classes.mrcs`` is the MRC stack with the resulting class averages.
    These are the images that will be displayed in the |RELION| GUI when you select the `_optimiser.star` file from the :button:`Display:` button on the main GUI.
    Note that |RELION| performs full CTF correction (if selected on the GUI), so your class averages are probably white on a black background.
    If the data is good, often they are very much like projections of a low-pass filtered atomic model.
    The quality of your 2D class averages are a very good indication of how good your 3D map will become.
    We like to see internal structure within projections of protein domains, and the solvent area around you particles should ideally be flat.
    Radially extending streaks in the solvent region are a typical sign of overfitting.
    If this happens, you could try to limit the resolution in the E-step of the 2D classification algorithm.

-   ``Class2D/job013/run_it100_model.star`` contains the model parameters that are refined besides the actual class averages (i.e. the distribution of the images over the classes, the spherical average of the signal-to-noise ratios in the reconstructed structures, the noise spectra of all groups, etc.
    Have a look at this file using the ``less`` command.
    In particular, check the distribution of particles over each class in the table ``data_model_classes``.
    If you compare this with the class averages themselves, you will see that particles with few classes are low-resolution, while classes with many particles are high-resolution.
    This is an important feature of the Bayesian approach, as averaging over fewer particles will naturally lead to lower signal-to-noise ratios in the average.
    The estimated spectral signal-to-noise ratios for each class are stored in the ``data_model_class_N`` tables, where ``N`` is the number of each class.
    Likewise, the estimated noise spectra for each group are stored in the tables called ``data_model_group_N``.
    The table ``data_model_groups`` stores a refined intensity scale-factor for each group: groups with values higher than one have a stronger signal than the average, relatively low-signal groups have values lower than one.
    These values are often correlated with the defocus, but also depend on accumulated contamination and ice thickness.

-   ``Class2D/job013/run_it100_data.star`` contains all metadata related to the individual particles.
    Besides the information in the input ``particles.star`` file, there is now additional information about the optimal orientations, the optimal class assignment, the contribution to the log-likelihood, etc.
    Note that this file can be used again as input for a new refinement, as the :textsc:`star` file format remains the same.

-   ``Class2D/job013/run_it100_optimiser.star`` contains some general information about the refinement process that is necessary for restarting an unfinished run.
    For example, if you think the process did not converge yet after 25 iterations (you could compare the class averages from iterations 24 and 25 to assess that), you could select this job in the :joblist:`Finished jobs` panel, and on the :guitab:`I/O` tab select this file for ``Continue from here``, and then set ``Number of iterations: 40`` on the :guitab:`Optimisation` tab.
    The job will then restart at iteration 26 and run until iteration 40.
    You might also choose to use a finer angular or translational sampling rate on the :guitab:`Sampling` tab.
    Another useful feature of the optimiser.star files is that it's first line contains a comment with the exact command line argument that was given to this run.
    As of release-4.0, |RELION| also uses the optimiser.star files as input nodes for different types of subsequent jobs. 
    For example, it replaces the model.star input nodes for :jobtype:`Subset selection` jobs.

- ``Class2D/job013/run_it100_sampling.star`` contains information about the employed sampling rates.
    This file is also necessary for restarting.


Making groups
-------------

.. note::
    If you are in a hurry to get through this tutorial, you can skip this sub-section.
    It contains more detailed information for the interested reader.

|RELION| groups particles together to do two things: estimate their average noise power spectrum and estimate a single-number intensity scale factor that describes differences in overall signal-to-noise ratios between different parts of the data, e.g. due to ice thickness, defocus or contamination.

The default behaviour is to treat all particles from each micrograph as a separate group.
This behaviour is fine if you have many particles per micrograph, but when you are using a high magnification, your sample is very diluted, or your final selection contains only a few particles per micrograph, then the estimation of the intensity scale factor (and the noise spectra) may become unstable.
We generally recommend to have at least 10-20 particles in each group, but do note that initial numbers of particles per group may become much smaller after 2D and 3D classification.

In cases with few particles per micrograph we recommend to group particles from multiple micrographs together.
For this purpose, the GUI implements a convenient functionality in the :jobtype:`Subset selection` job-type: when selecting a ``_optimiser.star`` file on the :guitab:`I/O` tab, one can use ``Regroup particles? Yes`` and ``Approximate nr of groups: 5`` on the :guitab:`Class options` tab to re-group all particles into 5 groups. (The actual number may vary somewhat from the input value, hence the `Approximate` on the input field.) This way, complicated grouping procedures in previous releases of |RELION| may be avoided.
As the micrographs in this tutorial do contain sufficient particles, we will not use this procedure now.

Please note that the groups in |RELION| are very different from defocus groups that are sometimes used in other programs. |RELION| will always use per-particle (anisotropic) CTF correction, irrespective of the groups used.
