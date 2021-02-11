.. _sec_wrappingup:

Wrapping up
===========


Making a flowchart
------------------

Do you wonder how you got to your final reconstruction? Select the last job you performed from the :joblist:`Finished jobs` list and try the ``Make flowchart`` option from the :button:`Job actions` button.
You'll need :math:`\LaTeX` and the ``TikZ`` package on your system in order for this to work.
On the first page will be an overview flowchart without the exact job names, which may be useful for publication purposes (perhaps after editing it in your favourite vector-based design program).
After the overview flowchart, the first detailed flowchart shows you the path how you got to this end.
Note that flowcharts longer than 10 steps will be cut into pieces.
There may be branches in your work flow.
Therefore, following the flowchart of your last job, there will also be flowcharts for each branch.
You can click on the links to get to the corresponding position in the PDF file.


Cleaning up your directories
----------------------------

In order to save disk space, |RELION| has an option to clean up job directories.
There are two modes of cleaning: 'gentle' cleaning will only delete intermediate files from the job directory being cleaned; 'harsh' cleaning also deletes files that may be necessary to launch a new job that needs input from the job being cleaned.
For example, harsh cleaning will remove averaged micrographs from a :jobtype:`MotionCorr` job, or extracted particles stacks from a :jobtype:`Particle extraction` job, while gentle cleaning will remove all files from itermediate iterations of :jobtype:`2D classification`, :jobtype:`3D classification` or :jobtype:`3D auto-refine` jobs.
You can clean individual jobs from the :button:`Job actions` button; or you can clean all jobs from the 'Jobs' pull-down menu at the top of the GUI.
We used the 'Gently clean all jobs' option from that menu before making a tarball of the project directory that we distributed as our precalculated results.
You might want to gently clean your project directory before you put your data in long-term storage.


Asking questions and citing us
------------------------------

That's it! Hopefully you enjoyed this tutorial and found it useful.
If you have any questions about |RELION|, please first check the FAQ on the |RELION| Wiki and the CCPEM mailing list.
If that doesn't help, use the CCPEM list for asking your question.

.. attention:
    Please, please, please, do not send a direct email to Sjors, as he can no longer respond to all of those.

If |RELION| turns out to be useful in your research, please do cite `our papers <http://www2.mrc-lmb.cam.ac.uk/groups/scheres/publications.html>`_ and tell your colleagues about it.


Further reading
---------------

The theory behind the refinement procedure in |RELION| is described in detail in:

- S.H.W. Scheres (2012) "|RELION|: Implementation of a Bayesian approach to cryo-EM structure determination" **J. Struc. Biol.**, 180, 519-530.
-  S.H.W. Scheres (2012) "A Bayesian view on cryo-EM structure determination" **J. Mol. Biol.**, 415, 406-418.

A comprehensive overview of how to use |RELION| for all types of classifications is described in:

- S.H.W. Scheres (2016) "Processing of structurally heterogeneous cryo-EM data in |RELION|" **Meth. Enzym.**, 579, 125-157.

This tutorial does not cover multi-body refinement, which is useful to describe continuous motions in relatively large complexes.
You can find a manuscript with specific instructions on how to perform multi-body refinement on the `RELION Wiki <ftp://ftp.mrc-lmb.cam.ac.uk/pub/scheres/multibody_protocol.pdf>`_