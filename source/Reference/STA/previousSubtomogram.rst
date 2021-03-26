.. _sec_sta_relion1.4:

Relion 1.4 Subtomogram averaging
================================

For sub-tomogram averaging, which was implemented with help from Tanmay Bharat, a former postdoc in the Lowe group at MRC-LMB, the same holds as for helical processing.
Many general concepts remain the same as for single-particle analysis, and users intending to perform sub-tomogram averaging in |RELION| are encouraged to go through this tutorial first.
For a detailed description of the sub-tomogram averaging procedures, the user is referred to the corresponding pages on the `:textsc:`relion <http://www2.mrc-lmb.cam.ac.uk/relion/index.php/Sub-tomogram_averaging>`_ Wiki`, or to `Tanmay's paper <http://dx.doi.org/10.1016/j.str.2015.06.026>`_:cite:`bharat_advances_2015`.
Please note that we are still actively working on making the sub-tomogram averaging pipeline more convenient to use and better.
This work is done in close collaboration with the group of John Briggs, also at MRC-LMB.
Meanwhile, please be advised that the sub-tomogram averaging pipeline is considerably less stream-lined than the single-particle one, and users should be prepared to do some scripting outside the |RELION| pipeline for many cases.
