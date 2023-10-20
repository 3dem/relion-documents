.. _sec_class3d:

Unsupervised 3D classification
==============================

All data sets are heterogeneous! The question is how much you are willing to tolerate. |RELION|'s 3D multi-reference refinement procedure provides a powerful unsupervised 3D classification approach.


Running the job
---------------

Unsupervised 3D classifcation may be run from the :jobtype:`3D classification` job-type.
On the :guitab:`I/O` tab set:

:Input images STAR file:: Select/job014/particles.star

:Reference map:: InitialModel/job015/initial_model.mrc

:Reference mask (optional):: \

     (Leave this empty.
     This is the place where we for example provided large/small-subunit masks for our focussed ribosome refinements.
     If left empty, a spherical mask with the particle diameter given on the :guitab:`Optimisation` tab will be used.
     This introduces the least bias into the classification.)


On the :guitab:`Reference` tab set:

:Ref. map is on absolute greyscale:: Yes

     (Given that this map was reconstructed from this data set, it is already on the correct greyscale.
     Any map that is not reconstructed from the same data in |RELION| should probably be considered as not being on the correct greyscale.)

:Initial low-pass filter (A):: 50

     (One should NOT use high-resolution starting models as they may introduce bias into the refinement process.
     As also explained in :cite:`scheres_classification_2010`, one should filter the initial map as much as one can.
     For ribosome we often use 70 Å, for smaller particles we typically use values of 40-60 Å.)

:Symmetry:: C1

     (Although we know that this sample has D2 symmetry, **it is often a good idea to perform an initial classification without any symmetry**, so bad particles, which are not symmetric, can get separated from proper ones, and the symmetry can be verified in the reconstructed maps.)


On the :guitab:`CTF` tab set:

:Do CTF correction?: Yes

:Ignore CTFs until first peak?: No

     (Only use this option if you also did so in the :jobtype:`2D classification` job that you used to create the references.)


On the :guitab:`Optimisation` tab set:

:Number of classes:: 4

     (Using more classes will divide the data set into more subsets, potentially describing more variability.
     The computational costs scales linearly with the number of classes, both in terms of CPU time and required computer memory.)

:Regularisation parameter T:: 4

     For the exact definition of T, please refer to :cite:`scheres_bayesian_2012`.
     For cryo-EM 2D classification we typically use values of T=1-2, and for 3D classification values of 2-4.
     For negative stain sometimes slightly lower values are better.
     In general, if your class averages appear noisy, then lower T; if your class averages remain too low resolution, then increase T.
     The main thing is to be aware of overfitting high-resolution noise.

:Number of iterations:: 25

     (We typically do not change this.)

:Use fast subsets (for large data sets)?:: No

     (This option will significantly speed up calculations for data sets of hundreds of thousands pf particles.
     However, sometimes performance is affected too.
     For small data sets like this one, we do not recommend using this option.)

:Mask diameter (A):: 200

     (Just use the same value as we did before in the :jobtype:`2D classification` job-type.)

:Mask individual particles with zeros?: Yes

:Limit resolution E-step to (A):: -1

     (If a positive value is given, then no frequencies beyond this value will be included in the alignment.
     This can also be useful to prevent overfitting.
     Here we don't really need it, but it could have been set to 10-15A anyway.)

:Use Blush regularisation?: Yes

     (This is new as of |RELION|-5.0. It switches from the default smoothness prior in Fourier space to a new prior in the form of a denoising convolutional neural network that was trained on many EMDB half-maps. It is particularly powerful when the signal-to-noise ratios in the images is low, e.g. because of small complexes, and standard 3D classification, 3D auto-refinement (see next section of this tutorial), or multi-body refinement suffers from overfitting. This tutorial data set has relatively high signal-to-noise ratios, so using Blush regularisation is probably not necessary. We used it here anyway to make you aware of the option. To run this option, the |RELION|-5 conda environment should be installed and you need CUDA-enabled GPUs to run ``pytorch`` on. If you cannot run this, don't worry and just set the option to ``No``.)


On the :guitab:`Sampling` tab one usually does not need to change anything (only for large and highly symmetric particles, like icosahedral viruses, does one typically use a 3.7 degree angular sampling at this point).
Ignore the :guitab:`Helix` tab, and on the :guitab:`Compute` tab set:


:Use parallel disc I/O?: Yes

:Number of pooled particles:: 30

:Skip padding?: No

:Skip gridding?: Yes

:Pre-read all particles into RAM?: Yes

     (Again, this is only possible here because the data set is small. For your own data, you would like write the particles to a scratch disk instead, see below.)

:Copy particles to scratch directory: \ 

:Combine iterations through disc?: No

:Use GPU acceleration?: Yes

:Which GPUs to use: 0:1:2:3

On the :guitab:`Running` tab, set:

:Number of MPI procs: 5

:Number of threads: 6

3D classification takes more memory than 2D classification, so often more threads are used.
However, in this case the images are rather small and RAM-shortage may not be such a big issue.
On our computer with 4 GPUs, we used 5 MPIs and 6 threads, and this calculation took approximately 6 minutes without Blush. Switching Blush on changed this to xx minutes. The relatively difference will be much smaller for larger data sets that spend more time during their E-step. 

When analysing the resulting class reconstructions, it is useful to also look at them in 2D slices, not only as a thresholded map in for example UCSF :textsc:`chimera`.
In the slices view you will get a much better impression of unresolved heterogeneity, which will show up as fuzzy or streaked regions in the slices.
Slices also give a good impression of the flatness of the solvent region.
Use the :button:`Display:` button and select any of the reconstructions from the last iteration to open a slices-view in |RELION|; you can also see a central slice through all classes simultaneously by selecting the ``run_it025_optimiser.star`` option from the :button:`Display:` button. We then often reverse sort them on ``rlnClassDistribution``.

When looking at your rendered maps in 3D, e.g. using UCSF :textsc:`chimera`, it is often a good idea to fit them all into the best one, as maps may rotate slightly during refinement.
In :textsc:`chimera`, we use the ``[Tools]-[Volume Data]-[Fit in Map]`` tool for that.
For looking at multiple maps alongside each other, we also like the ``[Tools]-[Structure Comparison]-[Tile Structures]`` tool, combined with the ``independent`` center-of-rotation method on the ``Viewing`` window.

Selecting good particles for further processing
-----------------------------------------------

After the :jobtype:`3D classification` job has finished, we can launch another :jobtype:`Subset selection` job.

On the :guitab:`I/O` tab, set:

:Select classes from job:: Class3D/job016/run\_it25\_optimiser.star

Because automated class selection has not been implemented for 3D classification, on the :guitab:`Class options` tab, we now need to set:

:Automatically select 2D classes?: No

We selected a single good class, discarding particles from 3 suboptimal classes. We retained over 4400 particles. This well-behaved tutorial data set is relatively homogeneous...

Note that this procedure of :jobtype:`3D classification` and :jobtype:`Subset selection` may be repeated several times.


Analysing the results in more detail
------------------------------------

.. note::
    Again, if you are in a hurry to get through this tutorial, you can skip this sub-section.
     It contains more detailed information for the interested reader.

The output files are basically the same as for the 2D classification run (we're actually using the same code for 2D and 3D refinements).
The only difference is that the map for each class is saved as a separate MRC map, e.g. `run_it025_class00?.mrc`, as opposed to the single MRC stack with 2D class averages that was output before.

As before, smaller classes will be low-pass filtered more strongly than large classes, and the spectral signal-to-noise ratios are stored in the ``data_model_class_N`` tables (with :math:`N=1,\dots,K`) of the ``_model.star`` files.
Perhaps now is a good time to introduce two handy scripts that are useful to extract any type of data from :textsc:`star` files.
Try typing:

::

    relion_star_printtable Class3D/job016/run_it025_model.star
      data_model_class_1 rlnResolution rlnSsnrMap

It will print the two columns with the resolution (``rlnResolution``) and the spectral signal-to-noise ratio (``rlnSsnrMap``) from table ``data_model_class_1`` to the screen.
You could redirect this to a file for subsequent plotting in your favourite program.
Alternatively, if `gnuplot` is installed on your system, you may type:

::

    relion_star_plottable Class3D/job016/run_it025_model.star
      data_model_class_1 rlnResolution rlnSsnrMap

To check whether your run had converged, (as mentioned above) you could also monitor:

::

    grep _rlnChangesOptimalClasses Class3D/job016/run_it???_optimiser.star

As you may appreciate by now: the :textsc:`star` files are a very convenient way of handling many different types of input and output data.
Linux shell commands like ``grep`` and ``awk``, possibly combined into scripts like ``relion_star_printtable``, provide you with a flexible and powerful way to analyze your results.
