.. _sec_class3d:

Unsupervised 3D classification
==============================

All data sets are heterogeneous! The question is how much you are willing to tolerate. |RELION|'s 3D multi-reference refinement procedure provides a powerful unsupervised 3D classification approach.


Running the job
---------------

Unsupervised 3D classifcation may be run from the :jobtype:`3D classification` job-type.
On the :guitab:`I/O` tab set:

:Input images STAR file:: Select/class2d\_template/particles.star

:Reference map:: InitialModel/symC1/run\_it150\_class001\_symD2.mrc

     (Note that this map does not appear in the :button:`Browse` button as it is not part of the pipeline.
     You can either type it's name into the entry field, or first import the map using the :jobtype:`Import` jobtype.
     Also note that, because we wil be running in symmetry C1, we could have also chosen to use the non-symmetric ``InitialModel/job015/run_it150_class001.mrc``.
     However, already being in the right symmetry setting is more convenient later on.)

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

:Has reference been CTF-corrected?: Yes

     (As this model was made using CTF-correction in the SGD.)

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


On the :guitab:`Sampling` tab one usually does not need to change anything (only for large and highly symmetric particles, like icosahedral viruses, does one typically use a 3.7 degree angular sampling at this point).
Ignore the :guitab:`Helix` tab, and fill in the :guitab:`Compute` tab like you did for the previous :jobtype:`2D-classification`.
Again, on the :guitab:`Running` tab, one may specify the ``Number of MPI processors`` and ``threads`` to use.
As explained for the :jobtype:`2D classification` job-type, 3D classification takes more memory than 2D classification, so often more threads are used.
However, in this case the images are rather small and RAM-shortage may not be such a big issue.
Perhaps you could use an alias like ``first_exhaustive``, to indicate this is our first 3D classification and it uses exhaustive angular searches? On our computer with 4 GPUs, 5 MPIs and 6 threads, this calculation took approximately 10 minutes.

When analysing the resulting class reconstructions, it is extremely useful to also look at them in slices, not only as a thresholded map in for example UCSF :textsc:`chimera`.
In the slices view you will get a much better impression of unresolved heterogeneity, which will show up as fuzzy or streaked regions in the slices.
Slices also give a good impression of the flatness of the solvent region.
Use the :button:`Display:` button and select any of the reconstructions from the last iteration to open a slices-view in |RELION|.

When looking at your rendered maps in 3D, e.g. using UCSF :textsc:`chimera`, it is often a good idea to fit them all into the best one, as maps may rotate slightly during refinement.
In :textsc:`chimera`, we use the ``[Tools]-[Volume Data]-[Fit in Map]`` tool for that.
For looking at multiple maps alongside each other, we also like the ``[Tools]-[Structure Comparison]-[Tile Structures]`` tool, combined with the ``independent`` center-of-rotation method on the ``Viewing`` window.

As was the case for the 2D classification, one can again use the :jobtype:`Subset selection` to select a subset of the particles assigned to one or more classes.
On the :guitab:`I/O` tab select the ``_model.star`` file from the last iteration.
The resulting display window will show central slices through the 4 refined models.
Select the best classes, and save the corresponding particles using the right-mouse pop-up menu.
Use an alias like ``class3d_first_exhaustive``.


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

    relion_star_printtable Class3D/first_exhaustive/run_it025_model.star
      data_model_class_1 rlnResolution rlnSsnrMap

It will print the two columns with the resolution (``rlnResolution``) and the spectral signal-to-noise ratio (``rlnSsnrMap``) from table ``data_model_class_1`` to the screen.
You could redirect this to a file for subsequent plotting in your favourite program.
Alternatively, if `gnuplot` is installed on your system, you may type:

::

    relion_star_plottable Class3D/first_exhaustive/run_it025_model.star
      data_model_class_1 rlnResolution rlnSsnrMap

To check whether your run had converged, (as mentioned above) you could also monitor:

::

    grep _rlnChangesOptimalClasses Class3D/first_exhaustive/run_it???_optimiser.star

As you may appreciate by now: the :textsc:`star` files are a very convenient way of handling many different types of input and output data.
Linux shell commands like ``grep`` and `awk`, possibly combined into scripts like ``relion_star_printtable``, provide you with a flexible and powerful way to analyze your results.
