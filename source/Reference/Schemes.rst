.. _sec_schemes:

Automation: *Schemes*
=======================

*Schemes* were introduced to |RELION|-3.1, where they were called *Schedules* but to prevent confusion with scheduled jobs in the main GUI, they were renamed to *Schemes* in |RELION|-4.0 and their functionality was further improved. *Schemes* aim to provide a generalised methodology for automatic submission of |RELION| jobs. This is useful for creating standardised workflows, for example to be used in on-the-fly processing. The ``relion_it.py`` script that was introduced in |RELION|-3.1 has been re-written to work with the *Schemes*.

The *Schemes* framework is built around the following key concepts: a directed graph that represents the logic of a series of subsequent |RELION| job-types is encoded in *Nodes* and *Edges*. *Nodes* can be either a |RELION| job or a so-called *Operator*; *Edges* form the connections between *Nodes*.
In addition, *Schemes* have their own *Variables*.

All information for each *Scheme* is stored in its own subdirectory of the ``Schemes/`` directory in a |RELION| project, e.g. ``Schemes/prep``.
Within each *Scheme*'s directory, the ``scheme.star`` file contains information about all the  *Variables*, *Edges*, *Operators* and *Jobs*.


Variables
---------

Three different types of *Variables* exist: *floatVariables* are numbers; *booleanVariables* are either True or False; and *stringVariables* are text.
Each Variable has a *VariableName*; a so-called *VariableResetValue*, at which the value is initialised; and a *VariableValue*, which may change during execution of the *Scheme* through the actions of Operators, as outlined below.

One special *stringVariable* is called ``email``.
When this is set, upon completion or upon encountering an error, the *Scheme* will send an email (through the Linux ``mail`` command) to the value of the `email` *stringVariable*.


Jobs
----

Jobs are the first type of *Node*.
They can be of any of the jobtypes defined in the |RELION| pipeliner, i.e. :jobtype:`Import`, :jobtype:`Motion correction`, etc, including the new :jobtype:`External`.
Any *Variable* defined in the *Scheme* can be set as a parameter in a Job, by using two dollar signs on the GUI or in the `job.star` file.
For example, one could define a *floatVariable* ``voltage`` and use ``$$voltage`` on the corresponding input line of an :jobtype:`Import` job.
Upon execution of the job inside the *Scheme*, the ``$$voltage`` will be replaced with the current value of the ``voltage`` *floatVariable*.

Jobs within a *Scheme* each have a `JobName` and a `JobNameOriginal`.
The latter is defined upon creation of the job (see next section); the former depends on the execution status of the *Scheme*, and will be set to the executed |RELION| job's name, e.g. ``CtfFind/job004``.
In addition, each job has a `JobMod` and a `jobHasStarted` status.
There are two types of `JobMode`:


``new``
    regardless of `jobHasStarted`, a new job will be created, with its own new `JobName`, every time the *Schemer* passes through this Node.

``continue``
    if `jobHasStarted` is False, a new job, with its own new `JobName`, will be created.
    If `jobHasStarted` is True, the job will be executed as a continue job inside the existing `JobName` directory.

When a *Scheme* executes a Job, it always sets `jobHasStarted` to True.
When a *Scheme* is reset, the `jobHasStarted` status for all jobs is set to False.


Operators
---------

*Operators* are the second type of *Node*.
Each operator within a *Scheme* has a unique name and a type.
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

``bool=set``
    `output` = *booleanVariable* `input1`
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

``string=set``
    `output` = *stringVariable* `input1`
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
    terminates the execution of the *Scheme* after the number of hours have passed since its start as stored in *floatVariable* `input1`.
``exit``
    terminates the execution of the *Scheme*.


Edges
-----

Two types of *Edges* exist.
The first type is a normal *Edge*, which connects an `inputNode` to an `ouputNode`, thereby defining their consecutive execution.

The second type is called a *Fork*.
A Fork has one `inputNode`, an `outputNode`, an `outputNodeIfTrue`, and an associated *booleanVariable*.
Whether one or the other output Node is executed depends on the current value of the booleanVariable that is associated with the Fork.
The fork with lead from the `inputNode`, an `outputNode` if the *booleanVariable* is *False*.
The fork will lead from the `inputNode`, an `outputNodeIfTrue` if the *booleanVariable* is *True*.
Thereby, Forks are the main instrument of making decisions in *Schemes*.


Create a Scheme
-----------------

The combination of the *Variables*, *Nodes* and *Edges* allows one to create complicated sequences of jobs.
It is probably a good idea to draw out a logical flow-chart of your sequence before creating a *Scheme*. Then, use your favourite text editor to manually edit the files ``Schemes/SCHEMENAME/scheme.star`` and all the files ``Schemes/SCHEMENAME/JOBNAMES/job.star`` for all the jobs in that *Scheme*. Following the ``prep`` and ``proc`` examples in the ``scripts`` directory of your |relion| installation is probably the easiest way to get started.

In the ``Schemes/SCHEMENAME/scheme.star`` file, first add all the different variables and operators that you will need.  

Note that any variable names that contain a `JobNameOriginal` of any of the *Jobs* inside any *Scheme* that is present in the *ProjectDirectory*, will be replaced by the current `JobName` upon execution of an operator.
For example, a *stringVariable* with the value ``Schemes/prep/ctffind/micrographs_ctf.star`` will be replaced to something like ``CtfFind/job003/micrographs_ctf.star`` upon execution of the job that uses it, assuming that the current `JobName` of that job is ``CtfFind/job003/`` in the ``Schemes/prep/scheme.star`` file.

Then, add your jobs. You can use the normal |relion| GUI to fill in all parameters of each job that you need and then use the ``Save job.star`` options from the ``Jobs`` menu to save the ``job.star`` file in the corresponding ``Schemes/SCHEMENAME/JOBNAMES/`` directory. 
Jobs use the same mechanism as described for the *Variables* above. 
So, if an :jobtype:`Auto-picking` job depends on its micrographs STAR file input on a :jobtype:`CTF estimation` job called `ctffind`, and this :jobtype:`CTF estimation` job is part of a *Scheme* called ``prep``, then the micrographs STAR file input for the :jobtype:`Auto-picking` job should be set to ``Schemes/prep/ctffind/micrographs_ctf.star``, and this will be converted to ``CtfFind/job003/micrographs_ctf.star`` upon execution of the job. 
In addition, a corresponding edge will be added to the ``default_pipeliner.star`` upon execution of the *Scheme*. 
Also note that parameters in ``job.star`` files may be updated with the current values of *Variables* from the *Scheme* by using the ``$$`` prefix, followed by the name of the corresponding *Variable*, as also mentioned above.

In addition, the `JobMode` needs to be chosen from options: ``new`` or ``continue``.
Typically, in on-the-fly-processing procedures that iterate over ever more movies, jobs like :jobtype:`Import`, :jobtype:`Motion correction`, :jobtype:`CTF estimation`, :jobtype:`Auto-picking` and :jobtype:`Particle extraction` are set as ``continue``, whereas most other jobs are set as ``new``.

Finally, once all the *Variables*, *Operators* and *Jobs* are in place, one should define all the *Edges* between them.

The *Scheme* will be initialised (and reset) to the left-hand *Node* of the first defined *Edge*.
If the *Scheme* is not an infinite loop, it is recommended to add the ``exit`` *Operator* as the last *Node*.

Once a *Scheme* has been created, it may be useful for more than one |RELION| project.
Therefore, you may want to store it in a tar-ball:

::

    tar -zcvf preprocess_scheme.tar.gz Schemes/preprocess


That tar-ball can then be extracted in any new |RELION| project directory:

::

    tar -zxvf preprocess_scheme.tar.gz




.. _sec_execute_schemes:

Executing a *Scheme*
^^^^^^^^^^^^^^^^^^^^^^

Once you have created the Scheme/name/ (sub)directories (with "name" being the name of your scheme), you can launch a separate GUI using:


::

    relion_schemegui.py name


You can start, stop, change parameters, and restart the scheme from there. You can also look into this python script to see the actual calls it makes to relion_schemer, which is the command line program that executes the scheme. While it runs, you can then follow the generation of new jobs in the normal relion GUI.


