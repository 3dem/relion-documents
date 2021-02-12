On-the-fly processing
=====================

As of |RELION|-4.0, on-the-fly processing is based on the :ref:`Schedules <sec_schedules>` functionality. This has been implemented together with a small `Tkinter` GUI that was written by Colin Palmer from CCPEM for the ``relion_it.py`` python script that was distributed with |RELION|-3.0 and 3.1. The new program still carries the same name, and can be launched from your Project directory from the command line:

::

     relion_it.py &

This will launch the GUI, which contains several sections that need to be filled in by the user. 

Computation details
-------------------

This section specifies what calculations will be performed.

:Do MotionCorr & CTF?: v

     (If selected, a *Schedule* called ``Schedules/prep`` will be lanuched that will loop over all movies (as defined in the section `Movie details` to run :jobtype:`Import`, :jobtype:`Motion correction` and :jobtype:`CTF estimation`. 
     By default this will be done for a maximum of 50 movies at a time.)

:micrographs_ctf.star:: Schedules/prep/ctffind/micrographs\_ctf.star

     (This option is only used if `Do MotionCorr & CTF?` is not selected. In that case, the user can provide the output STAR file from a previous :jobtype:`CTF estimation` job to perform the rest of the processing on.

:Do Autopick & Class2D?: v

     (If selected, a second *Schedule* called ``Schedules/proc`` will be lanuched that will automatically pick particles, as specified on the `Particle details` and `Picking details` sections, and then perform :jobtype:`2D classification` and automated class selection through the :jobtype:`Subset selection` job. 
     This is repeated on a loop, while the number of particles extracted is still increasing.)

:Do Refine3D?: v

     (If selected, the iteration of the second *Schedule* will also comprise a :jobtype:`3D auto-refine` job.) 

:3D reference:: None

     (If set to `None`, or anything else that does not exist as a file, then an :jobtype:`3D initial model` job will be launched before the auto-refine job.
     Note that in the case of symmetry, as defined in the `Particle details` section, the initial model calculation is still performed in C1, but this calculation is followed by an alignment of the symmetry axes and the application of the symmetry to the model.)

:GPUs (comma-separated):: 0,1

     (This option is used to specify the IDs of the GPU devices you want to run on. 
     Since the motion correction and CTF estimation are CPU-only, this option is only used by the second *Schedule*.)

Experimental details
--------------------

This section specifies information about where the movies are and how they were recorded.

:Pattern for movies:: Movies/\*.tiff

     (This specifies where the movies are.
     If you have recorded movies in the ``.eer`` format, it is recommended that you convert them to ``.tiff`` format during the copying process from the microscope computer to your processing computer.)

:Gain reference (optional):: Movies/gain.mrc

     (Only use this option if your movies have not been gain-corrected yet, otherwise leave empty.)

:Super-resolution?: \ 

     (Click this if your movies are in super-resolution.
     Note that we do not recommend recording movies in super-resolution, and that they will be binned during the :jobtype:`Motion correction` job.)

:Voltage (kV):: 300

:Cs (mm):: 2.7

:Phase plate?: v

     (Click this if you have collected your images with a phase plate.
     In that case, the :jobtype:`CTF estimation` job will also estimate the phase shift.)

:(Super-res) pixel size (A):: v 

     (Provide the pixel size in the movies. 
     If they are in super-resolution, then provide the (smaller) super-resolution pixel size.)

:Exposure rate (e-/A2/frame):: 1.2

     (This is the accumulated dose in a single movie frame.)


Particle details
----------------

:Symmetry:: C1

:Longest diameter (A):: 180

     (The longest diameter will be used to automatically determine the box size below, as well as for LoG and |TOPAZ| picking.)

:Shortest diameter (A):: 150

     (This will only be used for LoG picking. 
     This value should be smaller or equal than the longest diameter above, and is useful to pick elongated particles.) 

:Mask diameter (A):: 198.0

     (This is used for :jobtype:`Auto-picking` jobs, as well as :jobtype:`2D classification`, :jobtype:`3D initial model` and :jobtype:`3D auto-refine`

:Box size (px):: 246

     (The box size in the original micrograph.)

:Down-sample to (px): 64

     (To speed up all calculations in the ``proc`` *Schedule*, all particles will be downsampled to this box size.)

:Calculate for me:: v

     (This will generate automated suggestions for the mask diameter, the box size and the down-sampled box size. 
     We often use these.)


Picking details
---------------

:Retrain topaz network?: v

     (If this is selected, then the ``proc`` *Schedule* will first use the below specified number of particles for an initial :jobtype:`2D classification` and automated class selection in  :jobtype:`Subset selection`.
     The selected particles are then used to re-train the neural network in |TOPAZ| for this data set.
     Once the re-training is finished, the entire data set will be picked using |TOPAZ|.

:Nr particles for Log picking:: 10000

     (The number of particles used for LoG picking.)

:LoG picking threshold:: 0

     (The threshold to LoG pick particles.  

:LoG class2d score:: 0.5

     (The threshold to automatically select 2D class averages from the LoG picked particles.
     A value of 0 means rubbish classes; a value of 1 means gorgeous classes.)

:Topaz model:: Schedules/proc/train_topaz/model_epoch10.sav

     (If one does not retrain the |TOPAZ| network, then this option can be used to provide a pre-trained network.
     If this option is left empty, then the default general network inside |TOPAZ| is used.)

:Nr particles per micrograph:: 300

     (The expected number of particles per micrograph, which is used both for |TOPAZ| training and picking.)

:Topaz picking threshold:: 0

     (The |TOPAZ| threshold to select particle. Using negative values, e.g. -3, will pick more particles.)

:Topaz class2d score:: 0.5

     (The threshold to automatically select 2D class averages from the LoG picked particles.
     A value of 0 means rubbish classes; a value of 1 means gorgeous classes.)

Finally, the GUI has two action buttons: 

The :runbutton:`Save options` button will save the currently selected options to a file called ``relion_it_options.py``. This (together with any other options files) can be read in when launching the GUI a next time from the command line: 

::

     relion_it.py relion_it_options.py [extra_options2.py ....] &

The :runbutton:`Save &run` button will also save the options, and it will actually launch the *Schedules* and open the normal |RELION| GUI, from which the progress can be monitored, as explained on the :ref:`Schedules <sec_execute_schedules>` reference page.


Intervening 
-----------

Once the *Schedules* are running and you start seeing some results, you may find that you want to change some of the parameters. To stop a *Schedule*, you will need to press its :runbutton:`Abort` button on the *Schedule* part of the GUI, which is accessible from the top ``Schedules->Schedules`` menu. This will also abort any running |RELION| job, which may take a few seconds to happen.

The *Schedules* GUI itself is capable of setting the current state of any of the two *Schedules* to any point (using the :button:`Prev`, :button:`Next` and :button:`Set` buttons. Specific options can also be modified and saved for each job using the top part of the GUI and the :button:`Save` button. By changing the ``has_started`` to ``has_not_started``, any job in the *Schedule* can be forced to re-run from the beginning. The entire *Schedule* can be reset to its original state through the :button:`Reset` button. Note however that the ``relion_it.py`` script will remain unaware of any changes made to the *Schedule* throught the |RELION| GUI, so this script should not be executed again after making to the *Schedules* in this manner.

It is perhaps easier to re-start both or one of the *Schedules* from scratch. To do so, one could execute from the command line:

::

     rm -rf Schedules/prep #and/or Schedules/proc
     relion_it.py relion_it_options.py

and then change the necessary parameters on the ``relion_it.py`` GUI, and re-launch (only!) the necessary *Schedule* through the options on its `Computation details` section. This will launch new jobs inside the |RELION| pipeline. You could manually delete the jobs you don't need anymore from the :button:`Job actions` button on the main |RELION| GUI.

Control more options
--------------------

Not all options of all |RELION| jobs, or all of the parameters of the *Schedules* themselves can be controlled from the ``relion_it.py`` GUI. You can still control all of these through manually editing the ``relion_it_options.py`` file. 
For this, use double underscores to separate ``SCHEDULENAME__JOBNAME__JOBOPTION`` for any option. 
Some options are already in the default file and would need to be edited. Other options can be added to the file.

E.g. to change the number of 2D classes (``nr_classes``) in the ``class2d_logbatch`` job of the the ``proc`` Schedule, you can add the following line to the  ``relion_it_options.py`` file: 

::

     'proc__class2d_logbatch__nr_classes', '200', 

Likewise, use ``SCHEDULENAME__VARIABLENAME`` for variables in the *Schedules* themselves, e.g. to set de ``do_at_most`` variable, which determines the maximum number of micrographs that are processed in one cycle of the ``prep`` *Schedule*, edit this line:

::

     'prep__do_at_most', '100', 


Upon reading the options file, the ``relion_it.py`` script will set the corresponding values of all joboptions and schedule-variable values that are given in the input options file in the Schedule STAR files. Either the ``relion_it.py`` GUI or the |RELION| *Scheduler* GUI can then be used to execute the necessary *Schedule*.

