.. _sec_schedules:

On-the-fly processing: *Schedules*
==================================

*Schedules* are a new feature introduced to |RELION|-3.1. *Schedules* aim to provide a generalised replacement for the ``relion_it.py`` script for on-the-fly processing introduced to |RELION|-3.0.
Although all the functionality to write python scripts is maintained in |RELION|-3.1, we no longer maintain and distribute the script itself for every |RELION| release.
The reason for this is that for each new release some input/output options on the GUI will have changed, requiring a rewrite of (parts of) the python script.
Instead, the *Schedules* framework in |RELION|-3.1 aims to formalise the decision process that was encoded in the python code of the ``relion_it.py`` script.
The *Schedules* framework is built around the following key concepts: a directed graph that represents the logic of a series of subsequent |RELION| job-types is encoded in *Nodes* and *Edges*. *Nodes* can be either a |RELION| job or a so-called *Operator*; *Edges* form the connections between *Nodes*.
In addition, *Schedules* have their own *Variables*.

All information for each *Schedule* is stored in its own subdirectory of the ``Schedules/`` directory in a |RELION| project, e.g. ``Schedules/preprocess``.
Within each *Schedule*'s directory, the ``schedule.star`` file contains information about all the  *Variables*, *Edges*, *Operators* and *Jobs*.
In addition, within the *Schedule*'s directory, a ``schedule_pipeline.star`` file contains information which jobs provide input for other jobs, and each job has a unique subdirectory (named according to its ``JobNameOriginal``, see below) that contains a ``job.star`` file with the parameters for that job.


Variables
---------

Three different types of *Variables* exist: *floatVariables* are numbers; *booleanVariables* are either True or False; and *stringVariables* are text.
Each Variable has a *VariableName*; a so-called *VariableResetValue*, at which the value is initialised; and a *VariableValue*, which may change during execution of the *Schedule* through the actions of Operators, as outlined below.

One special *stringVariable* is called ``email``.
When this is set, upon completion or upon encountering an error, the *Schedule* will send an email (through the Linux ``mail`` command) to the value of the `email` *stringVariable*.


Jobs
----

Jobs are the first type of *Node*.
They can be of any of the jobtypes defined in the |RELION| pipeliner, i.e. :jobtype:`Import`, :jobtype:`Motion correction`, etc, including the new :jobtype:`External`.
Any *Variable* defined in the *Schedule* can be set as a parameter in a Job, by using two dollar signs on the GUI or in the `job.star` file.
For example, one could define a *floatVariable* ``voltage`` and use ``$$voltage`` on the correspondig input line of an :jobtype:`Import` job.
Upon execution of the job inside the *Schedule*, the ``$$voltage`` will be replaced with the current value of the ``voltage`` *floatVariable*.

Jobs within a *Schedule* each have a :schedulevar:`JobName` and a :schedulevar:`JobNameOriginal`.
The latter is defined upon creation of the job (see next section); the former depends on the execution status of the *Schedule*, and will be set to the executed |RELION| job's name, e.g. ``CtfFind/job004``.
In addition, each job has a ``JobMode`` and a :schedulevar:`jobHasStarted` status.
There are three types of ``JobMode``:


``new``
    regardless of :schedulevar:`jobHasStarted`, a new job will be created, with its own new :schedulevar:`JobName`, every time the *Scheduler* passes through this Node.

``continue``
    if :schedulevar:`jobHasStarted` is False, a new job, with its own new :schedulevar:`JobName`, will be created.
    If :schedulevar:`jobHasStarted` is True, the job will be executed as a continue job inside the existing :schedulevar:`JobName` directory.

``overwrite``
    if :schedulevar:`jobHasStarted` is False, a new job, with its own new *JobName*, will be created.
    If :schedulevar:`jobHasStarted` is True, a new job execution will overwrite what was already present inside the existing *JobName* directory.

When a *Schedule* executes a Job, it always sets :schedulevar:`jobHasStarted` to True.
When a *Schedule* is reset, the :schedulevar:`jobHasStarted` status for all jobs is set to False.


Operators
---------

*Operators* are the second type of *Node*.
Each operator within a *Schedule* has a unique name and a type.
Operators can also have an output Variable: :schedulevar:`output`, on which they act, and up to two input Variables: :schedulevar:`input1` and :schedulevar:`input2`.
Most, but not all operators change the value of their :schedulevar:`outputVariable`.

The following types of operators exist to act on a *floatVariable*:

``float=set``
    :schedulevar:`output` = *floatVariable* :schedulevar:`input1`
``float=plus``
    :schedulevar:`output` = *floatVariable* :schedulevar:`input1` + *floatVariable* :schedulevar:`input2`
``float=minus``
     :schedulevar:`output` = *floatVariable* :schedulevar:`input1` - *floatVariable* :schedulevar:`input2`
``float=mult``
    :schedulevar:`output` = *floatVariable* :schedulevar:`input1` × *floatVariable* :schedulevar:`input2`
``float=divide``
    :schedulevar:`output` = *floatVariable* :schedulevar:`input1` / *floatVariable* :schedulevar:`input2`
``float=round``
    :schedulevar:`output` = ROUND(*floatVariable* :schedulevar:`input1`)
``float=count_images``
    sets :schedulevar:`output` to the number of images in the STAR file called *stringVariable* :schedulevar:`input1`. *stringVariable* :schedulevar:`input2` can be `particles`, `micrographs` or `movies`.
``float=count_words``
    sets :schedulevar:`output` to the number of words in *stringVariable* :schedulevar:`input1`, where individual words need to be separated with a `,` (comma) sign.
``float=read_star``
    reads :schedulevar:`output` from a double or integer that is stored inside a STAR file. *stringVariable* :schedulevar:`input1` defines which variable to read as: *starfilename,tablename,metadatalabel*.
    If *tablename* is a table instead of a list, then *floatVariable* :schedulevar:`input2` defines the line number, with the default of zero being the first line.
``float=star_table_max``
    sets :schedulevar:`output` to the maximum value of a column in a starfile table, where *stringVariable* :schedulevar:`input1` specifies the column as *starfilename,tablename,metadatalabel*.
``float=star_table_min``
    sets :schedulevar:`output` to the minimum value of a column in a starfile table, where *stringVariable* :schedulevar:`input1` specifies the column as *starfilename,tablename,metadatalabel*.
``float=star_table_avg``
    sets :schedulevar:`output` to the average value of a column in a starfile table, where *stringVariable* :schedulevar:`input1` specifies the column as *starfilename,tablename,metadatalabel*.
``float=star_table_sort_idx``
    a sorting will be performed on the values of a column in a starfile table, where *stringVariable* :schedulevar:`input1` specifies the column as *starfilename,tablename,metadatalabel*. *stringVariable* :schedulevar:`input2` specifies the index in the ordered array: the lowest number is 1, the second lowest is 2, the highest is -1 and the one-but-highest is -2.
    Then, :schedulevar:`output` is set to the corresponding index in the original table.

The following types of operators exist to act on a *booleanVariable*:

``bool=and``
    :schedulevar:`output` = *booleanVariable* :schedulevar:`input1` AND *booleanVariable* :schedulevar:`input2`
``bool=or``
    :schedulevar:`output` = *booleanVariable* :schedulevar:`input1` OR *booleanVariable* :schedulevar:`input2`
``bool=not``
    :schedulevar:`output` = NOT *booleanVariable* :schedulevar:`input1`
``bool=gt``
    :schedulevar:`output` = *floatVariable* :schedulevar:`input1` > *floatVariable* :schedulevar:`input2`
``bool=lt``
    :schedulevar:`output` = *floatVariable* :schedulevar:`input1` < *floatVariable* :schedulevar:`input2`
``bool=ge``
    :schedulevar:`output` = *floatVariable* :schedulevar:`input1` >= *floatVariable* :schedulevar:`input2`
``bool=le``
    :schedulevar:`output` = *floatVariable* :schedulevar:`input1` <= *floatVariable* :schedulevar:`input2`
``bool=eq``
    :schedulevar:`output` = *floatVariable* :schedulevar:`input1` == *floatVariable* :schedulevar:`input2`
``bool=file_exists``
    :schedulevar:`output` = True if *stringVariable* :schedulevar:`input1` exists on the file system; False otherwise
``bool=read_star``
    reads :schedulevar:`output` from a boolean that is stored inside a STAR file. *stringVariable* :schedulevar:`input1` defines which variable to read as: *starfilename,tablename,metadatalabel*.
    If *tablename* is a table instead of a list, then *floatVariable* :schedulevar:`input2` defines the line number, with the default of zero being the first line.


The following types of operators exist to act on a *stringVariable*:

``string=join``
    :schedulevar:`output` = concatenate *stringVariable* :schedulevar:`input1` and *stringVariable* :schedulevar:`input2`
``string=before_first``
    sets :schedulevar:`output` to the substring of *stringVariable* :schedulevar:`input1` that occurs before the first instance of substring *stringVariable* :schedulevar:`input2`.
``string=after_first``
    sets :schedulevar:`output` to the substring of *stringVariable* :schedulevar:`input1` that occurs after the first instance of substring *stringVariable* :schedulevar:`input2`.
``string=before_last``
    sets :schedulevar:`output` to the substring of *stringVariable* :schedulevar:`input1` that occurs before the last instance of substring *stringVariable* :schedulevar:`input2`.
``string=after_last``
    sets :schedulevar:`output` to the substring of *stringVariable* :schedulevar:`input1` that occurs after the last instance of substring *stringVariable* :schedulevar:`input2`.
``string=read_star``
    reads :schedulevar:`output` from a string that is stored inside a STAR file. *stringVariable* :schedulevar:`input1` defines which variable to read as: *starfilename,tablename,metadatalabel*.
    If *tablename* is a table instead of a list, then *floatVariable* :schedulevar:`input2` defines the line number, with the default of zero being the first line.
``string=glob``
    :schedulevar:`output` = GLOB(*stringVariable* :schedulevar:`input1`), where input1 contains a Linux wildcard and GLOB is the Linux function that returns all the files that exist for that wildcard.
    Each existing file will be separated by a comma in the :schedulevar:`output` string.
``string=nth_word``
    :schedulevar:`output` = the Nth substring in *stringVariable* :schedulevar:`input1`, where N=*floatVariable* :schedulevar:`input2`, and substrings are separated by commas.
    Counting starts at one, and negative values for *input2* mean counting from the end, e.g. *input2=-2* means the second-last word.


The following types of operators do not act on any variable:

``touch_file``
    performs ``touch input1`` on the file system**
``copy_file``
    performs ``cp input1 input2`` on the file system. *stringVariable* :schedulevar:`input1` may contain a linux wildcard.
    If *stringVariable* :schedulevar:`input2` contains a directory structure that does not exist yet, it will be created.
``move_file``
    performs ``mv input1 input2`` on the file system. *stringVariable* :schedulevar:`input1` may contain a linux wildcard.
    If *stringVariable* :schedulevar:`input2` contains a directory structure that does not exist yet, it will be created.**
``delete_file``
    performs ``rm -f input1`` on the file system. *stringVariable* :schedulevar:`input1` may contain a linux wildcard.
``email``
    sends an email, provided a *stringVariable* with the name `email` exists and the Linux command `mail` is functional.
    The content of the email has the current value of *stringVariable* :schedulevar:`input1`, and optionally also *stringVariable* :schedulevar:`input2`.
``wait``
    waits *floatVariable* :schedulevar:`input1` seconds since the last time this operator was executed.
    The first time it is executed, this operator only starts the counter and does not wait.
    Optionally, if :schedulevar:`output` is defined as a *floatVariable*, then the elapsed number of seconds since last time is stored in :schedulevar:`output`.
``exit``
    terminates the execution of the *Schedule*, and sends a confirmation email if the `email` *stringVariable* is defined.


Edges
-----

Two types of Edges exist.
The first type is a normal *Edge*, which connects an :schedulevar:`inputNode` to an :schedulevar:`ouputNode`, thereby defining their consecutive execution.
The second type is called a *Fork*.
A Fork has one :schedulevar:`inputNode` and two :schedulevar:`outputNodes`.
Whether one or the other output Node is executed depends on the current value of the booleanVariable that is associated with the Fork.
Thereby, Forks are the main instrument of making decisions in *Schedules*.


Creating a new Schedule
-----------------------

The combination of the *Variables*, *Nodes* and *Edges* allows one to create complicated sequences of jobs.
It is probably a good idea to draw out a logical flow-chart of your sequence before creating a *Schedule* as outlined below.

The creation of a *Schedule* is most easily done through the GUI, using the following command:

::

    relion --schedule preprocess &


Note that the ``--schedule`` argument launches the GUI in a modifed mode, where slider bars and Yes/No pull-down menus are replaced by plain input text fields for more convenient placement of *Variables* with a ``$$`` prefix.

*Variables* can be added or deleted using the corresponding :button:`Set` and :button:`Del` buttons, respectively.
The left-hand input field defines the :schedulevar:`VariableName`, the right-hand input field defines its :schedulevar:`VariableValue` and :schedulevar:`VariableResetValue`.
Any variable names that contain a :schedulevar:`JobNameOriginal` of any of the *Jobs* inside the same *Schedule*, will be replaced by the current :schedulevar:`JobName` upon execution of an operator.

Similarly, *Operators* can be added or deleted using the corresponding :button:`Add` and :button:`Del` buttons, respectively.
The upper-left pull-down menu contains all possible *OperatorTypes*.
The upper-right pull-down menu (next to the ``->`` sign) will define the :schedulevar:`output` variable, and the menu contains a list of all defined *Variables*.
The lower two pull-down menus (with labels ``i1:`` and ``i2:``) define :schedulevar:`Input1` and :schedulevar:`Input2` variables.
Adding *Operators* with types for the input or output variables that are incompatible with the :schedulevar:`OperatorType` will result in a pop-up error message.

*Jobs* can be added by first clicking on the job-type menu on the left-hand side of the top half of the GUI; then filling in the parameters on all tabs.
Note that parameters may be updated with the current values of *Variables* from the *Schedule* by using the ``$$`` prefix, followed by the name of the corresponding *Variable*, as also mentioned above.
If one *Job* depends on another *Job* inside the same *Schedule*, it is important to use the :button:`Browse` button for its input parameters on the :guitab:`I/O` tab of the job, and to select the input files from the same `Schedules` subdirectory.
This is because, much like with *Variables*, all parameters of *Jobs* that contain a :schedulevar:`JobNameOriginal` of any of the *Jobs* inside the same *Schedule*, will be replaced by the current *JobName* upon execution of that *Job*.
This way, the *Schedule* will be able to define the correct dependencies between the newly created jobs upon its execution.
Once all tabs on the top part of the GUI have been filled in, one needs to provide a :schedulevar:`JobNameOriginal` in the input field with the label ``Name:``.
In addition, the :schedulevar:`JobMode` needs to be chosen from the pull-down menu: ``new``, ``continue`` or ``overwrite``.
Then, the job can be added to the *Schedule* by clicking the :runbutton:`Add job` button.

Finally, once all the *Variables*, *Operators* and *Jobs* are in place, one may add or delete the *Edges* using the corresponding :button:`Add` and :button:`Del` buttons, respectively.
All defined *Operators* and *Jobs* will be available from the pull-down menus below these buttons.
Normal *Edges* go from the left-hand pull-down to the right-hand pull-down menu, with the ``->`` sign in between them. *Forks* are defined by also selecting a *booleanVariable* from the pull-down menu with the ``if:`` label.
When the *booleanVariable* is True, it will point to the *Node* defined by the lower-right pull-down menu (with the `:` label).
When the *booleanVariable* is False, it will point to the *Node* defined by the upper-right pull-down menu (with the ``->`` label).
The *Schedule* will be initialised (and reset) to the left-hand *Node* of the first defined *Edge*.
If the *Schedule* is not an infinite loop, it is recommended to add the ``exit`` *Operator* as the last *Node*.

To check the logic of the defined *Schedule* one can use the :button:`Set`, :button:`Prev`, :button:`Next` and :button:`Reset` buttons at the bottom of the GUI to set the *CurrentNodeName* to any of the defined *Nodes*; to go to the previous *Node*; to go to the next *Node*; or to reset all *Variables* and set *CurrentNodeName* to the left-hand side *Node* of the first *Edge*.

Also, using the 'Scheduling' menu on the top of the GUI, one can make a copy of any *Schedule* using the 'Copy Schedule' option.
This may be useful to make a back-up of a schedule during the different stages of its creation.
Once a *Schedule* has been created, it may be useful for more than one |RELION| project.
Therefore, you may want to store it in a tar-ball:

::

    tar -zcvf preprocess_schedule.tar.gz Schedules/preprocess


That tar-ball can then be extracted in any new |RELION| project directory:

::

    tar -zxvf preprocess_schedule.tar.gz


Executing a *Schedule*
^^^^^^^^^^^^^^^^^^^^^^

Once a *Schedule* has been created using the `--schedule` argument to the GUI, it is no longer necessary to provide that argument.
One can instead launch the GUI normally (and have slider bars for numbers and Yes/No pull-down menues for booleans):

::

    relion &


The *Schedule* can then be accessed through the 'Scheduling' menu at the top of the GUI, where all defined *Schedules* are available through the 'Schedules' sub-menu.
The same GUI can be toggled back into the normal 'pipeline' mode from the same menu (or by pressing ALT+'p').
If one wants to start a *Schedule* from scratch, one would typically press the :button:`Reset` button first, and then press the :runbutton:`Run!` button.
This will lock the *Schedule* directory from further writing by the GUI and to reflect this, the lower part of the GUI will be de-activated.
Once the *Schedule* finishes, the lock (in effect a hidden directory with the name ``.relion_lock_schedule_NAME``) will be removed and the bottom part of the GUI will be re-activated.
One can safely toggle between the pipeliner and the scheduler mode during execution of any *Schedule*, and multiple (different) *Schedules* can run simultaneously.

When a *Schedule* for whatever reason dies, the lock will not be automatically removed.
If this happens, use the :runbutton:`Unlock` button to remove the lock manually.
Be careful not to remove the lock on a running *Schedule* though, as this itself will cause it to die with an error.

If one would like to stop a running *Schedule* for whatever reason, one can press the :runbutton:`Abort` button.
This will send an abort signal (i.e. it will create files called ``RELION_JOB_ABORT_NOW`` in the job directory of the currently running job, and in the directory of the *Schedule* itself), which will cause the *Schedule* to stop, and the lock to be removed.
If one were to press the :runbutton:`Run!` button again, the same *Schedule* would continue the same execution as before, from the point where it was aborted.
Most likely though, one has aborted because one would like to change something in the *Schedule* execution.
For example, one could change parameters of a specific *Job*.
To do so, select that *Job* by clicking on it in the list of *Jobs* in the lower part of the GUI.
Then, edit the corresponding parameters on the relevant tabs of that *Job* on the top part of the GUI.
Then, one may want to set :schedulevar:`jobHasStarted` status to False, in order to make these options effective for all data processed in the *Schedule* thus far.
For example, after running a *Schedule* for automated pre-processing for a while, one might want to change the threshold for picking particles in a :jobtype:`auto-picking` job.
One would then reset the :schedulevar:`jobHasStarted` status of the :jobtype:`auto-picking` job to False, while one would leave the :schedulevar:`jobHasStarted` status of other jobs like :jobtype:`Motion correction` and :jobtype:`CTF estimation` to True.
Thereby, upon a re-start of the *Schedule*, only new movies would be subjected to :jobtype:`Motion correction` and :jobtype:`CTF estimation` inside the same output directories as generated previously, but a new :jobtype:`auto-picking` directory would be created, in which all movies acquired thus far would be processed.
Examples like these were very hard to do with the ``relion_it.py`` script in |RELION|-3.0.