.. _sec_schedules:

Automation: *Schedules*
=======================

*Schedules* were introduced to |RELION|-3.1 and further improved in |RELION|-4.0. *Schedules* aim to provide a generalised methodology for automatic submission of |RELION| jobs. This is useful for creating standardised workflows, for example to be used in on-the-fly processing. The ``relion_it.py`` script that was nitroduced in |RELION|-3.1 has been re-written to work with the *Schedules*.

The *Schedules* framework is built around the following key concepts: a directed graph that represents the logic of a series of subsequent |RELION| job-types is encoded in *Nodes* and *Edges*. *Nodes* can be either a |RELION| job or a so-called *Operator*; *Edges* form the connections between *Nodes*.
In addition, *Schedules* have their own *Variables*.

All information for each *Schedule* is stored in its own subdirectory of the ``Schedules/`` directory in a |RELION| project, e.g. ``Schedules/prep``.
Within each *Schedule*'s directory, the ``schedule.star`` file contains information about all the  *Variables*, *Edges*, *Operators* and *Jobs*.


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
For example, one could define a *floatVariable* ``voltage`` and use ``$$voltage`` on the corresponding input line of an :jobtype:`Import` job.
Upon execution of the job inside the *Schedule*, the ``$$voltage`` will be replaced with the current value of the ``voltage`` *floatVariable*.

Jobs within a *Schedule* each have a `JobName` and a `JobNameOriginal`.
The latter is defined upon creation of the job (see next section); the former depends on the execution status of the *Schedule*, and will be set to the executed |RELION| job's name, e.g. ``CtfFind/job004``.
In addition, each job has a `JobMod` and a `jobHasStarted` status.
There are two types of `JobMode`:


``new``
    regardless of `jobHasStarted`, a new job will be created, with its own new `JobName`, every time the *Scheduler* passes through this Node.

``continue``
    if `jobHasStarted` is False, a new job, with its own new `JobName`, will be created.
    If `jobHasStarted` is True, the job will be executed as a continue job inside the existing `JobName` directory.

When a *Schedule* executes a Job, it always sets `jobHasStarted` to True.
When a *Schedule* is reset, the `jobHasStarted` status for all jobs is set to False.


Operators
---------

*Operators* are the second type of *Node*.
Each operator within a *Schedule* has a unique name and a type.
Operators can also have an output Variable: `output`, on which they act, and up to two input Variables: `input1` and `input2`.
Most, but not all operators change the value of their `output` Variable.

The following types of operators act on an `output` that is a *floatVariable*:

``float=set``
    `output` = *floatVariable* `input1`
``float=plus``
    `output` = *floatVariable* `input1` + *floatVariable* `input2`
``float=minus``
     `output` = *floatVariable* `input1` - *floatVariable* `input2`
``float=mult``
    `output` = *floatVariable* `input1` × *floatVariable* `input2`
``float=divide``
    `output` = *floatVariable* `input1` / *floatVariable* `input2`
``float=round``
    `output` = ROUND(*floatVariable* `input1`)
``float=count_images``
    sets `output` to the number of images in the STAR file with the filename in *stringVariable* `input1`. *stringVariable* `input2` can be `particles`, `micrographs` or `movies`, depending on what type of images need to be counted.
``float=count_words``
    sets `output` to the number of words in *stringVariable* `input1`, where individual words need to be separated with a `,` (comma) sign.
``float=read_star``
    sets `output` to the value of a double or integer that is read from a STAR file. *stringVariable* `input1` defines which variable to read as: *starfilename,tablename,metadatalabel*.
    If *tablename* is a table instead of a list, then *floatVariable* `input2` defines the line number, with the default of zero being the first line.
``float=star_table_max``
    sets `output` to the maximum value of a column in a starfile table, where *stringVariable* `input1` specifies the column as *starfilename,tablename,metadatalabel*.
``float=star_table_min``
    sets `output` to the minimum value of a column in a starfile table, where *stringVariable* `input1` specifies the column as *starfilename,tablename,metadatalabel*.
``float=star_table_avg``
    sets `output` to the average value of a column in a starfile table, where *stringVariable* `input1` specifies the column as *starfilename,tablename,metadatalabel*.
``float=star_table_sort_idx``
    a sorting will be performed on the values of a column in a starfile table, where *stringVariable* `input1` specifies the column as *starfilename,tablename,metadatalabel*. *stringVariable* `input2` specifies the index in the ordered array: the lowest number is 1, the second lowest is 2, the highest is -1 and the one-but-highest is -2.
    Then, `output` is set to the corresponding index in the original table.


The following types of operators act on an `output` that is a *booleanVariable*:

``bool=and``
    `output` = *booleanVariable* `input1` AND *booleanVariable* `input2`
``bool=or``
    `output` = *booleanVariable* `input1` OR *booleanVariable* `input2`
``bool=not``
    `output` = NOT *booleanVariable* `input1`
``bool=gt``
    `output` = *floatVariable* `input1` > *floatVariable* `input2`
``bool=lt``
    `output` = *floatVariable* `input1` < *floatVariable* `input2`
``bool=ge``
    `output` = *floatVariable* `input1` >= *floatVariable* `input2`
``bool=le``
    `output` = *floatVariable* `input1` <= *floatVariable* `input2`
``bool=eq``
    `output` = *floatVariable* `input1` == *floatVariable* `input2`
``bool=file_exists``
    `output` = True if a file with the filename stored in *stringVariable* `input1` exists on the file system; False otherwise
``bool=read_star``
    reads `output` from a boolean that is stored inside a STAR file. *stringVariable* `input1` defines which variable to read as: *starfilename,tablename,metadatalabel*.
    If *tablename* is a table instead of a list, then *floatVariable* `input2` defines the line number, with the default of zero being the first line.


The following types of operators act on an `output` that is a *stringVariable*:

``string=join``
    `output` = concatenate *stringVariable* `input1` and *stringVariable* `input2`
``string=before_first``
    sets `output` to the substring of *stringVariable* `input1` that occurs before the first instance of substring *stringVariable* `input2`.
``string=after_first``
    sets `output` to the substring of *stringVariable* `input1` that occurs after the first instance of substring *stringVariable* `input2`.
``string=before_last``
    sets `output` to the substring of *stringVariable* `input1` that occurs before the last instance of substring *stringVariable* `input2`.
``string=after_last``
    sets `output` to the substring of *stringVariable* `input1` that occurs after the last instance of substring *stringVariable* `input2`.
``string=read_star``
    reads `output` from a string that is stored inside a STAR file. *stringVariable* `input1` defines which variable to read as: *starfilename,tablename,metadatalabel*.
    If *tablename* is a table instead of a list, then *floatVariable* `input2` defines the line number, with the default of zero being the first line.
``string=glob``
    `output` = GLOB(*stringVariable* `input1`), where input1 contains a Linux wildcard and GLOB is the Linux function that returns all the files that exist for that wildcard.
    Each existing file will be separated by a comma in the `output` string.
``string=nth_word``
    `output` = the Nth substring in *stringVariable* `input1`, where N=*floatVariable* `input2`, and substrings are separated by commas.
    Counting starts at one, and negative values for *input2* mean counting from the end, e.g. *input2=-2* means the second-last word.


The following types of operators do not act on any variable:

``touch_file``
    performs ``touch input1`` on the file system
``copy_file``
    performs ``cp input1 input2`` on the file system. *stringVariable* `input1` may contain a linux wildcard.
    If *stringVariable* `input2` contains a directory structure that does not exist yet, it will be created.
``move_file``
    performs ``mv input1 input2`` on the file system. *stringVariable* `input1` may contain a linux wildcard.
    If *stringVariable* `input2` contains a directory structure that does not exist yet, it will be created.
``delete_file``
    performs ``rm -f input1`` on the file system. *stringVariable* `input1` may contain a linux wildcard.
``email``
    sends an email, provided a *stringVariable* with the name `email` exists and the Linux command `mail` is functional.
    The content of the email has the current value of *stringVariable* `input1`, and optionally also *stringVariable* `input2`.
``wait``
    waits *floatVariable* `input1` seconds since the last time this operator was executed.
    The first time it is executed, this operator only starts the counter and does not wait.
    Optionally, if `output` is defined as a *floatVariable*, then the elapsed number of seconds since last time is stored in `output`.
``exit_maxtime`` 
    terminates the execution of the *Schedule* after the number of hours have passed since its start as stored in *floatVariable* `input1`.
``exit``
    terminates the execution of the *Schedule*.


Edges
-----

Two types of *Edges* exist.
The first type is a normal *Edge*, which connects an `inputNode` to an `ouputNode`, thereby defining their consecutive execution.

The second type is called a *Fork*.
A Fork has one `inputNode`, an `outputNode`, an `outputNodeIfTrue`, and an associated *booleanVariable*.
Whether one or the other output Node is executed depends on the current value of the booleanVariable that is associated with the Fork.
The fork with lead from the `inputNode`, an `outputNode` if the *booleanVariable* is *False*.
The fork will lead from the `inputNode`, an `outputNodeIfTrue` if the *booleanVariable* is *True*.
Thereby, Forks are the main instrument of making decisions in *Schedules*.


Create a Schedule
-----------------

The combination of the *Variables*, *Nodes* and *Edges* allows one to create complicated sequences of jobs.
It is probably a good idea to draw out a logical flow-chart of your sequence before creating a *Schedule* as outlined below.

The creation of a *Schedule* is most easily done through the GUI, using the following command:

::

    relion --schedule preprocess &


Note that the ``--schedule`` argument launches the GUI in a modifed mode, where slider bars and Yes/No pull-down menus are replaced by plain input text fields for more convenient placement of *Variables* with a ``$$`` prefix.

*Variables* can be added or deleted using the corresponding :button:`Set` and :button:`Del` buttons, respectively.
The left-hand input field defines the `VariableName`, the right-hand input field defines its `VariableValue` and `VariableResetValue`.
Any variable names that contain a `JobNameOriginal` of any of the *Jobs* inside the same *Schedule*, will be replaced by the current `JobName` upon execution of an operator.
For example, a *stringVariable* with the value ``Schedules/prep/ctffind/micrographs_ctf.star`` will be replaced to something like ``CtfFind/job003/micrographs_ctf.star`` upon execution of the job that uses it.

Similarly, *Operators* can be added or deleted using the corresponding :button:`Add` and :button:`Del` buttons, respectively.
The upper-left pull-down menu contains all possible *OperatorTypes*.
The upper-right pull-down menu (next to the ``->`` sign) will define the `output` variable, and the menu contains a list of all defined *Variables*.
The lower two pull-down menus (with labels ``i1:`` and ``i2:``) define `Input1` and `Input2` variables.
Adding *Operators* with types for the input or output variables that are incompatible with the `OperatorType` will result in a pop-up error message.
You can provide your own (sensible) names for the *Operators* through the ``name:`` entry.

*Jobs* can be added by first clicking on the job-type menu on the left-hand side of the top half of the GUI; then filling in the parameters on all tabs.
Note that parameters may be updated with the current values of *Variables* from the *Schedule* by using the ``$$`` prefix, followed by the name of the corresponding *Variable*, as also mentioned above.
The dependence of one *Job* on another *Job* inside any *Schedule* is deduced from the names of their input nodes. 
This uses the same mechanism as described for the *Variables above. 
So, if an :jobtype:`Auto-picking` job in depends on its micrographs STAR file input on a :jobtype:`CTF estimation` job called `ctffind`, and this :jobtype:`CTF estimation` job is part of a *Schedule* called ``prep``, then the micrographs STAR file input for the :jobtype:`Auto-picking` job should be set to ``Schedules/prep/ctffind/micrographs_ctf.star``, and this will be converted to ``CtfFind/job003/micrographs_ctf.star`` upon execution of the job.
When using the :button:`Browse` button to select the input files from the same `Schedules` subdirectory, this will be handled automatically.
This way, the *Schedule* will be able to define the correct dependencies between the newly created jobs upon its execution.
Once all tabs on the top part of the GUI have been filled in, one needs to provide a `JobNameOriginal` in the input field with the label ``Name:``.
In addition, the `JobMode` needs to be chosen from the pull-down menu: ``new``, ``continue``.
Typically, in on-the-fly-processing procedures that iterate over ever more movies, jobs like :jobtype:`Import`, :jobtype:`Motion correction`, :jobtype:`CTF estimation`, :jobtype:`Auto-picking` and :jobtype:`Particle extraction` are set as ``continue``, whereas most other jobs are set as ``new``.
Then, the job can be added to the *Schedule* by clicking the :runbutton:`Add job` button.

Finally, once all the *Variables*, *Operators* and *Jobs* are in place, one may add or delete the *Edges* using the corresponding :button:`Add` and :button:`Del` buttons, respectively.
All defined *Operators* and *Jobs* will be available from the pull-down menus below these buttons.
Normal *Edges* go from the left-hand pull-down to the right-hand pull-down menu, with the ``->`` sign in between them. *Forks* are defined by also selecting a *booleanVariable* from the pull-down menu with the ``if:`` label.
If the *booleanVariable* is False, it will point to the *Node* defined by the upper-right pull-down menu (with the ``->`` label).
If the *booleanVariable* is True, it will point to the *Node* defined by the lower-right pull-down menu (with the `:` label).
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


.. note::
    You may find it easier to generate *Schedules* completely by hand using your favourite text editor to edit the files ``Schedules/NAME/schedule.star`` and all the files ``Schedules/NAME/JOBNAMES/job.star`` for all the jobs in that Schedule. As of |RELION|-4.0 that should be a lot easier than before. You could look at the ``proc`` *Schedule* from the ``relion_it.py` setup for inspiration. One can generate ``job.star`` files for any job type by filling in the normal |RELION| GUI and clicking *Save job settings* from the *Jobs* menu on the top left of the GUI. Those files are hidden, i.e. their filename starts with a '.', but you can visualise them using ``ls -a`` in the *ProjectDirectory*.


Executing a *Schedule*
^^^^^^^^^^^^^^^^^^^^^^

Once a *Schedule* has been created using the `--schedule` argument to the GUI, it is no longer necessary to provide that argument.
One can instead launch the GUI normally (and have slider bars for numbers and Yes/No pull-down menues for booleans):

::

    relion &


The *Schedule* can then be accessed through the 'Scheduling' menu at the top of the GUI, where all defined *Schedules* are available through the 'Schedules' sub-menu.
The same GUI can be toggled back into the normal 'pipeline' mode from the same menu (or by pressing ALT+'p' on Linux).
If one wants to start a *Schedule* from scratch, one would typically press the :button:`Reset` button first, and then press the :runbutton:`Run!` button.
This will lock the *Schedule* directory from further writing by the GUI and to reflect this, the lower part of the GUI will be de-activated.
Once the *Schedule* finishes, the lock (in effect a hidden directory with the name ``.relion_lock_schedule_NAME``) will be removed and the bottom part of the GUI will be re-activated.
One can safely toggle between the pipeliner and the scheduler mode during execution of any *Schedule*, and multiple (different) *Schedules* can run simultaneously.

When a *Schedule* for whatever reason dies in error, the lock will not be automatically removed.
If this happens, use the :runbutton:`Unlock` button to remove the lock manually.
Be careful not to remove the lock on a running *Schedule* though, as this itself will cause it to die with an error.

If one would like to stop a running *Schedule* for whatever reason, one can press the :runbutton:`Abort` button.
This will send an abort signal (i.e. it will create files called ``RELION_JOB_ABORT_NOW`` in the job directory of the currently running job, and in the directory of the *Schedule* itself), which will cause the *Schedule* to stop, and the lock to be removed.
If one were to press the :runbutton:`Run!` button again, the same *Schedule* would continue the same execution as before, from the point where it was aborted.
Most likely though, one has aborted because one would like to change something in the *Schedule* execution.
For example, one could change parameters of a specific *Job*.
To do so, select that *Job* by clicking on it in the list of *Jobs* in the lower part of the GUI.
Then, edit the corresponding parameters on the relevant tabs of that *Job* on the top part of the GUI.
Then, one may want to set `jobHasStarted` status to False, in order to make these options effective for all data processed in the *Schedule* thus far.
For example, after running a *Schedule* for automated pre-processing for a while, one might want to change the threshold for picking particles in a :jobtype:`Auto-picking` job.
One would then reset the `jobHasStarted` status of the :jobtype:`Auto-picking` job to False, while one would leave the `jobHasStarted` status of other jobs like :jobtype:`Motion correction` and :jobtype:`CTF estimation` to True.
Thereby, upon a re-start of the *Schedule*, only new movies would be subjected to :jobtype:`Motion correction` and :jobtype:`CTF estimation` inside the same output directories as generated previously, but a new :jobtype:`Auto-picking` directory would be created, in which all movies acquired thus far would be processed.


