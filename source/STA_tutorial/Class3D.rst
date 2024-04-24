.. _sec_sta_class3d:

3D classification
====================

After removing the duplicate particles from the particle set, we will now perform 3D classification in order to filter out bad particles that will prevent us from obtaining a high-resolution structure in the subsequent refinement steps at binning factor 1.

As the particles were initially picked at random on the spherical annotations, while the HIV capsids are not strictly spherical, it is likely that some of the particles we have refined up to this point either do not correspond to actual hexamers at all (in the case when the spherical annotation and the capsid do not coincide in the tomogram) or were sampled from regions where the data itself does not contain high-resolution information or has artifacts. 

Therefore, assuming we have obtained a good low-resolution reference map, we will now classify the particles based on how well they align with the reference and discard those that align poorly, which will show as blurry, or completely incorrect, 3D classes.

Running the 3D classification job
----------------------------------

Select the :jobtype:`3D classification` job-type, and on the :guitab:`I/O` tab, set the appropriate files:

:Input optimisation set:: ""

:OR\: use direct entries?: Yes

      (Since we ran the :jobtype:`Subset selection` job to remove the duplicate particles in the previous step, we will now use its output particles file as the particle set instead of the previously used optimisation set. The tomogram set will be the same as the one in the previous optimisation set file.)

:Input particle set:: Select/job016/particles.star

:Input tomogram set:: Denoise/job008/tomograms.star

:Reference map:: Refine3D/job015/run_class001.mrc

On the :guitab:`Reference` tab, ensure that the following two fields are set as follows:

:Initial low-pass filter (A):: 60

      (We low-pass filter the reference map at a low enough resolution in order not to bias the refined classes towards high-resolution features.)

:Symmetry:: C1

      (At this point, the aim is to find the bad particles in the particle set rather than to obtain the best reconstruction, so we perform the classification without enforcing the symmetry, since the bad particles are not necessarily symmetric. The good (and symmetric) particles will end up assigned to a class that hopefully results in a symmetric map.)

Leave the fields on the :guitab:`CTF` tab with their default values, then in the :guitab:`Optimisation` tab leave the default values for all fields except:

:Number of classes:: 9

      (There is no right number of classes, and in your own run of the pipeline it may be useful to experiment with different numbers to ensure that the largest number of good particles is selected. Note that the computational cost of 3D classification scales linearly with the number of classes, both in terms of CPU time and memory.)

:Mask diameter (A):: 230

On the :guitab:`Sampling` tab, change the fields:

:Perform image alignment?: Yes

:Angular sampling interval:: 1.8 degrees

:Perform local angular searches?: Yes

      (As the purpose of this classification step for this particular dataset is to see which particles align well with the reference structure we have so far, rather than to discover heterogeneity in the data, we only perform local alignment of the individual particles.)

:Prior width on tilt angle (deg): 10

Ignore the :guitab:`Helix` tab and set the fields on the :guitab:`Compute` and :guitab:`Running` tabs to the same values as in the :jobtype:`3D auto-refine` jobs in the :ref:`sec_sta_refine3d_ini` section:

:Number of pooled particles:: 30

:Use GPU acceleration?: Yes

:Number of MPI procs:: 5

:Number of threads:: 6

On our computer with 2 GPUs, this job took around 2 hours for 25 iterations and 21659 particles.


Analysing the results of the 3D classification
------------------------------------------------

For an overview of the the resulting classes in the final iteration, use the :button:`Display:` button on the :jobtype:`3D classification` job that has just completed and select ``out:run_it025_optimiser.star``, which will open a Relion Display GUI. This allows you to see central slices through all classes side-by-side. Before pressing the :button:`Display!` button on the Relion Display GUI, it is useful to set a few fields as follows.

The ``Min`` and ``Max`` fields set the intensity range of the displayed images, and setting them to non-zero values allows you to see all class images in the same intensity range. This is useful to see which classes have low intensity (i.e. little mass inside the volume), which otherwise would be difficult to assess on a normalised scale for each image. The specific values to set depend on the resulting intensities after each run; in our data for this particular :jobtype:`3D classification` run, the following values were useful:

:Min: -0.01

:Max: 0.04

Another useful field to tick is 

:Sort images on:: rlnClassDistribution

as well as the ``Display label?`` field. Finally, press the :button:`Display!` button and the class images will be shown in the order of the fraction of the total number of particles assigned to each class, with the fraction shown as the label of each image.
Right-clicking on individual images and selecting ``Show metadata this class`` will open a new window with more information about the class, such as the number of particles in it.

It is also possible to see 2D slices through each class map by going back to the main Relion GUI and clicking on :button:`Display:` and ``out:run_it025_class00X.mrc`` for any class index ``X``. This will open the Relion Display GUI and pressing :button:`Display!` will open a new window with the individual slices through the map.
Alternatively, the individual map files are located in ``Class3D/job017/run_it025_class001.mrc`` and can be opened with a 3D volume viewer such as UCSF :textsc:`chimera`.


Discarding the bad particles 
----------------------------------

Next, we want to only keep in our dataset the particles belonging to the best classes obtained in the 3D classification and discard the rest. To do this, go to the :jobtype:`Subset selection` job-type and in the :guitab:`I/O` tab input the ``_optimiser.star`` file from the previous :jobtype:`3D auto-refine` job into the appropriate field:

:Select classes from job::  Class3D/job017/run_it025_optimiser.star

Leave all the other fields in all tabs set to their default values (set the ``remove duplicates?`` field in the :guitab:`Duplicates` tab to ``No`` if it was set otherwise from the previous job) and press the :runbutton:`Run!` button. This will open the Relion Display GUI, and after setting the fields to the same values as explained above, press the :button:`Display!` button, which will open the window showing all classes side-by-side.

Select the good classes by clicking on the individual class images -- the selected classes will have a red border, then right-click on one of the selected images and select ``Save selected classes``. 
The output of the job in the main Relion GUI will show a message indicating that the ``particles.star`` file has been saved and the number of selected particles it contains. 
You can now safely close the Relion Display GUI windows, and the new particles file containing only the particles in the selected classes is ``Select/job018/particles.star``.

In our workspace, the resulting ``particles.star`` file now contains 9442 particles.


Visualising the remaining particles
------------------------------------

To visualise the particles we have left as 3D annotations on the tomograms, we can launch the Napari picker with ``picking mode: particles`` (also see :ref:`sec_sta_particlepicking`), with the additional particles file given as the optional input.

First, make sure that the Relion GUI is running locally, as the Napari plugin is slow over the network. Then, select the :jobtype:`Pick tomograms` job type and set the following fields on the :guitab:`I/O` tab:

:Input tomograms.star::  Denoise/job008/tomograms.star

:Picking mode:: particles

:Particle spacing(A):: ""

   (Since we selected the ``particles`` picking mode above, this field will be ignored.)

:Input particles.star (optional)::  Select/job018/particles.star

   (The particle set file that we want to visualise.)

Running the job will generate the particle annotation files ``Picks/job019/annotations/TS_XX_particles.star`` from the input ``particles.star`` file and start the Napari plugin, where you can visualise the particle annotations and manipulate them as explained in the :ref:`sec_sta_particlepicking` section. After clicking the ``save particles`` button and closing the Napari window, new ``particles.star`` and ``optimisation_set.star`` files will be created, which can be used in subsequent steps.

----------------------------------

The procedure to perform 3D classification using pseudo-subtomograms is the same as in the single particle analysis pipeline, so you may find it useful to also read the description in the :ref:`SPA tutorial<sec_class3d>`.
