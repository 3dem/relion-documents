Using RELION
============


The GUI
-------


A pipeline approach
^^^^^^^^^^^^^^^^^^^

The GUI serves a central role in it's pipelined approach, details of which have been published in the `2016 Proceedings of the CCP-EM Spring Symposium <https://doi.org/10.1107/S2059798316019276>`_ :cite:`fernandez-leiro_pipeline_2017`.
We recommend to create a single directory per project, i.e. per structure you want to determine.
We call this the project directory.
It is important to always launch the relion graphical user-interface (GUI), by typing the command ``relion``, from the project directory.

The GUI keeps track of all jobs and how output from one job is used as input for another, thereby forming a workflow or pipeline.
Each type of job has its own output directory, e.g. ``Class2D/``, and inside these job-type directories, new jobs get consecutive numbers, e.g. ``Class2D/job010``.
Inside these individual job directories, output names are fixed, e.g. ``Class2D/job010/run``.
To provide a mechanism to have more meaningful names for jobs, a system of job `aliases` is used, which are implemented as symbolic links to the individual job directories on the filesystem.
All info about the pipeline is stored in a file called ``default_pipeline.star``, but in normal circumstances the user does not need to look into this file.
In case this file gets corrupted, one can copy back a backup of this file from the last executed job directory.


The upper half: jobtype-browser and parameter-panel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On the left of the upper half of the GUI is the jobtype-browser: a vertical list of jobtypes, e.g. :jobtype:`2D classification`.
On the right is a panel with multiple tabs, where parameters to the different types of jobs may be input.
On the top left of the GUI are three different menu's, providing a range of functionalities.
The :runbutton:`Scheme` and :runbutton:`Run!` buttons can be used to scheme jobs for future execution, or to execute them now.
The former is particularly useful in preparing fully automated ``pipelines`` that can be run iteratively, for example in real-time as data is being collected.
See :ref:`Schemes <sec_schemes>` for more details.
By clicking in the jobtype-browser on the left-hand side of the GUI, a new job (with a :runbutton:`Run!` button) will be loaded in the parameter-panel on the right.


The lower half: job-lists and stdout/stderr windows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The lower half of the GUI contains lists of jobs that are still running (:joblist:`Running jobs`), have already finished (:joblist:`Finished jobs`), or are schemed for later execution (:joblist:`Schemed jobs`).
By clicking jobs in these lists, the parameters of that job will be loaded in the parameter-panel, and the :runbutton:`Run!` button will change color and turn into :button:`continue now!`.
Upon clicking the latter, no new output job-directory will be made, but the job will be continued according to the parameters given in the parameter-panel. :jobtype:`2D classification`, :jobtype:`3D classifications` and :jobtype:`3D auto-refine` jobs will need a `_optimiser.star` file to continue from, and will have filenames with the iteration from which they were continued, e.g. `run_ct23`.
Other types of jobs may continue from the point until they were executed before, e.g. :jobtype:`Motion correction`, :jobtype:`CTF estimation`, :jobtype:`Auto-picking` and :jobtype:`Particle Extraction` will continue by running only on those micrographs that weren't done before.
The :joblist:`Input to this job` and :joblist:`Output from this job` lists link jobs together and can be used to browse backwards or forwards in the project history.

At the bottom of the lower half of the GUI, the standard output (stdout) and standard error (stderr) of the selected (finished or running) job will show in black and red text, respectively.
The stderr should ideally be empty, any text here is usually worth inspection.
These text displays get updated every time you click on a job in the job-lists.
Double-clicking on the stdout or stderr displays will open a pop-up window with the entire text for more convenient scrolling.


The Display button
^^^^^^^^^^^^^^^^^^

The :button:`Display:` button below the run and scheme buttons serves to visualise the most important input and output files for each job.
When a job from the job-lists in the lower half of the GUI is selected, clicking this button will pop-up a menu with all the input and output of this job that can be displayed (for example, particles, micrographs, coordinates, PDF files, etc).
A more general functionality to display any (e.g. intermediate) file can be accessed through the `Display` option of the `File` menu on the top left of the GUI.


The Job actions button
^^^^^^^^^^^^^^^^^^^^^^

The :button:`Job actions` button opens up a little menu with options for the selected (running, finished or schemed) job.
Here, you can access a file called `note.txt` (that is saved in every individual job directory and which may be used to store user comments); you can change the alias of the job; you can mark a job as finished (in case it somehow got stuck); you can make a flowchart of the history of that job (provided \LaTeX\  and the `TikZ` package are installed on your system, also see :ref:`this section <sec_wrappingup>`); or you can delete or clean a job to save disk space (see below).


Clean-up to save disk space
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Deletion of jobs moves the entire job directory from the project directory into a directory called ``Trash/``.
You can empty the Trash folder from 'File' menu on the top left of the GUI to really free up the space.
Until you do so, you can still `undelete` jobs using the corresponding option from the `Jobs` menu on the top left.

To save disk space, you can also `clean` jobs, which will move intermediate files to the Trash folder, e.g. the files written out for all intermediate iterations of refine jobs.
There are two cleaning options: ``gentle clean`` will leave all files intact that could be used as input into another job, while ``harsh clean`` may also remove those.
Evidently, ``harsh`` cleaning can free up more space, in particular directories with particle stacks or micrographs may become large, e.g. from :jobtype:`Motion correction`, :jobtype:`Particle extraction`, :jobtype:`Movie refinement` and :jobtype:`Particle polishing` job types.
One can also clean all directories in the project with a single click using the corresponding options from the `Jobs` menu on the top left of the GUI.
You can protect specific directories from ``harsh`` cleaning by placing a file called ``NO_HARSH_CLEAN`` inside them, e.g. you may want to protect your final set of polished particles from deletion by executing:

::

    touch Polish/job098/NO_HARSH_CLEAN


Optimise computations for your setup
------------------------------------


GPU-acceleration
^^^^^^^^^^^^^^^^

Dari Kimanius and Bjoern Forsberg from the group of Erik Lindahl (Stockholm) have ported the most computationally expensive parts of |RELION| for the use of GPUs.
Because they used the :textsc:`cuda`-libraries from :textsc:`nvidia` to do this, GPU-acceleration in |RELION| only works with :textsc:`nvidia` cards.
These need to be of `compute capability <https://en.wikipedia.org/wiki/CUDA#Version_features_and_specifications>`_ 3.5 or higher.
Both single and double precision cards will work, so one is not restricted to the expensive double-precision cards, but can use the cheaper gaming cards as well.
Details of their implementation can be found in their `eLife paper <https://elifesciences.org/articles/18722>`_:cite:`kimanius_accelerated_2016`.

Two different relion programs have been GPU-accelerated: `relion_autopick` (for :jobtype:`Auto-picking`) and `relion_refine` (for :jobtype:`2D classification`, :jobtype:`3D classification` and :jobtype:`3D auto-refine` jobs).
Both the sequential and the MPI-versions of these programs have been accelerated. 


Disk access
^^^^^^^^^^^

With the much improved speed of image processing provided by the GPU-acceleration, access to the hard disk increasingly becomes a bottle neck.
Several options are available on the |RELION| GUI to optimise disk access for your data set and computer setup.
For :jobtype:`2D classification`, :jobtype:`3D initial model`, :jobtype:`3D classification` and :jobtype:`3D auto-refine` one can choose to `use parallel  disc I/O`.
When set to `Yes`, all MPI processes will read particles simultaneously from the hard disk.
Otherwise, only the master will read images and send them through the network to the slaves.
Parallel file systems like gluster of fhgfs are good at parallel disc I/O.
NFS may break with many slaves reading in parallel.

One can also set the `number of pooled particles`.  Particles are processed in individual batches by MPI slaves.
During each batch, a stack of particle images is only opened and closed once to improve disk access times.
All particle images of a single batch are read into memory together.
The size of these batches is at least one particle per thread used.
This parameter controls how many particles are read together in a batch by each thread.
If it is set to 3 and one uses 8 threads, batches of 3x8=24 particles will be read together.
This may improve performance on systems where disk access, and particularly metadata handling of disk access, is a problem.
It has a modest cost of increased RAM usage.

If one has a relatively small data set (and/or a computer with a lot of RAM), then one can `pre-read all particles into RAM` at the beginning of a calculation.
This will greatly speed up calculations on systems with relatively slow disk access.  However, one should of course be careful with the amount of RAM available.
Because particles are read in float-precision, it will take :math:`\frac{N \times boxsize \times boxsize \times 4}{1024 \times 1024 \times 1024}` gigabytes to read N particles into RAM.
For 100,000 particles with a 200-pixel boxsize that becomes 15GB, or 60 GB for the same number of particles in a 400-pixel boxsize.

If the data set is too large to pre-read into RAM, but each computing node has a local, fast disk (e.g. a solid-state drive) mounted with the same name, then one can let each MPI slave copy all particles onto the local disk prior to starting the calculations.
This is done using the ``Copy particles to scratch directory``.
If multiple slaves will be executed on the same node, only the first slave will copy the particles.
If the local disk is too small to hold the entire data set, those particles that no loner fit on the scratch disk will be read from their original position.
A sub-directory called ``relion_volatile`` will be created inside the specified directory name.
For example, if one specifies ``/ssd``, then a directory called ``/ssd/relion_volatile`` will be created.
If the ``/ssd/relion_volatile`` directory already exists, it will be wiped before copying the particles.
Then, the program will copy all input particles into a single large stack inside this directory.
If the job finishes correctly, the ``/ssd/relion_volatile`` directory will be deleted again.
If the job crashes before finishing, you may want to remove it yourself.
The program will create the ``/ssd/relion_volatile`` directory with writing permissions for everyone.
Thereby, one can choose to use ``/ssd``, i.e. without a username, as a scratch directory.
That way, provided always only a single job is executed by a single user on each computing node, the local disks do not run the risk of filling up with junk when jobs crash and users forget to clean the scratch disk themselves.

Finally, there is an option to ``combine iterations through disc``.
If set to ``Yes``, at the end of every iteration all MPI slaves will write out a large file with their accumulated results.
The MPI master will read in all these files, combine them all, and write out a new file with the combined results.
All MPI salves will then read in the combined results.
This reduces heavy load on the network, but increases load on the disc I/O.
This will affect the time it takes between the progress-bar in the expectation step reaching its end (the mouse gets to the cheese) and the start of the ensuing maximisation step.
It will depend on your system setup which is most efficient.
This option was originally implemented to circumvent bugs on the network cards on our old cluster at LMB.
Nowadays, we prefer not to use this option, as it tends to be very slow when refinements reached high resolutions.


Interaction with other programs
-------------------------------

Although, in principle, |RELION| can use particles that have been extracted by a different program, this is NOT the recommended procedure.
Many programs change the particles themselves, e.g. through phase flipping, band-pass or Wiener filtering, masking etc.
All these are sub-optimal for subsequent use in |RELION|.
Moreover, gathering all the required metadata into a correctly formatted |RELION|-type :textsc:`star` file may be prone to errors.
Because re-extracting your particles in |RELION| is straightforward and very fast, the procedure outlined below is often a much easier (and better) route into |RELION|.

Also, several implementations of wrappers around |RELION| have now been reported (e.g. in :textsc:`eman2`, :textsc:`scipion` and :textsc:`appion`).
Although we try to be helpful when others write these wrappers, we have absolutely no control over them and do not know whether their final product uses |RELION| in the best way.
Therefore, in case of any doubt regarding results obtained with these wrappers, we would recommend following the procedures outlined in this tutorial.
The recommended way of executing external programs from within the |RELION| pipeline itself is outlined in the next section.


.. _sec_external_jobtype:

The External job-type
---------------------


User interaction through the GUI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


The :jobtype:`External` job-type on the |RELION|-3.1 GUI provides a way to execute any third-party program from within the |RELION| pipeline.
The interaction with the user is as follows:

On the :guitab:`Input` tab set:

:External executable:: myscript.py

     (This is the filename of an executable script, which will call the external program.)

:Input movies:: \

:Input micrographs:: \

:Input particles:: \

:Input coordinates:: \

:Input 3D reference:: \

:Input 3D mask:: \


The user provides at least one of the input entries to tell |RELION| from which other jobs the input nodes come from, and what type of input this is.
This will therefore allow to maintain an intact directional graph inside the pipeliner.
On the :guitab:`Params` tab, the user can then provide up to ten (optional) free parameters that will be passed onto the executable script.
Finally, the :guitab:`Running` tab allows multi-threaded execution, queue submission, and any other arguments to be passed through the `Additional arguments` entry.

The GUI will then create and execute the following command, either locally or through a queueing system:

::

    myscript.py --o External/jobXXX/ --in_YYY ZZZ --LABELN VALUEN --j J


where

-   ``XXX`` is the current jobnumber in the pipeline.
-   ``YYY`` is the type of the input node: `movies`, `mics`, `parts`,  `coords`, `3dref`, or `mask`,
-   ``ZZZ`` is the name of the corresponding input node.
    Note that more than one input node may be given, each with its own ``--in_YYY`` argument.
-   ``LABELN`` is the label of a free parameter, as defined on the :guitab:`Params` tab of the GUI.
    Note that up to ten different labels may be used.
-   ``VALUEN`` is the corresponding value of the free parameter.
    This is optional: not every label needs a value.
-    ``J`` is the number of threads defined on the running tab.

.. _sec_externaljob_script:

Functionality of the executable script
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is the responsibility of the executable script (`myscript.py`) to handle the command line parsing of the generated command.
In addition, there are a few rules the script needs to adhere to:


-   All output needs to be written out in the output directory, as specified by the ``--o External/jobXXX/`` option.
    In addition, for jobs that emulate |RELION| job-types like :jobtype:`Motion correction` or :jobtype:`Auto-picking`, the output should be organised in the same directory structure as the corresponding |RELION| job-type would make.
-   When completed, the script should create an empty file called ``RELION_JOB_EXIT_SUCCESS`` in the output directory.
    This will tell the pipeliner that the task has finished successfully.
    Aborted or failed runs may optionally be communicated by creating files called ``RELION_JOB_EXIT_ABORTED`` and ``RELION_JOB_EXIT_FAILURE``.
-   The job should output file called ``RELION_OUTPUT_NODES.star``, which should have a table called `data_output_nodes`.
    This table should have two columns with the names and types of all the output nodes of the job, using the ``_rlnPipeLineNodeName`` and ``_rlnPipeLineNodeType`` metadata labels.
    See the ``data_pipeline_nodes`` table in the ``default_pipeline.star`` file of any |RELION| project directory for examples.
    Output nodes defined here will lead to the creation of edges between jobs in the directional graph of the pipeliner; and output nodes will be available for convenient displaying by the user using the :button:`Display:` button on the GUI.
-   The following may not be necessary or relevant, but the GUI has a :button:`Job` actions button, which allows users to abort running jobs.
    This button will create a file called ``RELION_JOB_ABORT_NOW`` in the output directory.
    If this functionality is to be used, the script should abort the job when this file is present, create the ``RELION_JOB_EXIT_ABORTED`` file, remove the ``RELION_JOB_ABORT_NOW`` file, and then exit.


Example: a particle-picker
^^^^^^^^^^^^^^^^^^^^^^^^^^

If your external program is a particle picker, e.g.
Topaz :cite:`Bepler_positive_2019`, then you would give on the :guitab:`Input` tab:

:External executable:: run\_topaz.py

:Input micrographs:: CtfFind/job005/micrographs\_ctf.star

     (This file would be visible through the :button:`Browse` button next to the input entry, which would only show star files of micrographs that exist in the current project.)


On the :guitab:`Params` tab, one would provide any necessary arguments to be picked up by the script, for example:

:Param1 label, value:: threshold      0.1

:Param2 label, value:: denoise_first


Upon pressing the :runbutton:`Run!` button, this would execute the following command:

::

    run_topaz.py --o External/job006/ \
      --in_mics CtfFind/job005/micrographs_ctf.star \
      --threshold 0.1 --denoise_first --j 1


The executable `run_topaz.py` is then responsible for correctly passing the command line arguments to `topaz`, and to make sure the rules in the previous section are adhered to.
For picking jobs, the directory structure of the input movies (or micrographs) should be maintained inside the output directory, and each micrograph would have a STAR file with the picked coordinates that has the same rootname as the original micrograph, but with a ``_PICKNAME.star`` suffix.
The ``PICKNAME`` is a free string.
One could use the name of the particle-picking program, for example ``topaz``.
Therefore, if a movie was originally imported as ``Movies/mic001.tif``, its corresponding STAR file with the picked coordinate would be placed in ``External/job006/Movies/mic001_topaz.star``.  In addition, in the output directory, the script should create a text file called ``coords_suffix_PICKNAME.star`` (i.e. ``coords_suffix_topaz.star``).
This file should contain at least one line of text, which is the name of the input micrographs STAR file given on the  :guitab:`Input` tab, i.e. ``CtfFind/job005/micrographs_ctf.star``.
The output node (the ``coords_suffix_topaz.star`` file) should also be listed in the ``RELION_OUTPUT_NODES.star`` file.
This file would therefore look like this:

::

    data_output_nodes
    loop_
    _rlnPipeLineNodeName #1
    _rlnPipeLineNodeType #2
    External/job006/coords_suffix_topaz.star            2
