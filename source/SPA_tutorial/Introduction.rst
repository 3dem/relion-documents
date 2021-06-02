Introduction
============

This tutorial provides an introduction to the use of |RELION|-4.0 for cryo-EM structure determination.
This tutorial covers the entire single-particle analysis workflow in |RELION|-4.0: beam-induced motion-correction, CTF estimation; automated particle picking; particle extraction; 2D class averaging; automated 2D class selection; SGD-based initial model generation; 3D classification; high-resolution 3D refinement; CTF refinement and higher-order aberration correction; the processing of movies from direct-electron detectors; and final map sharpening and local-resolution estimation.
Carefully going through this tutorial should take less than a day (if you have a suitable GPU or if you follow our precalculated results).
After that, you should be able to run |RELION| on your own data.

This tutorial uses a test data set on beta-galactosidase that was kindly given to us by Takayuki Kato from the Namba group at Osaka university, Japan.
It was collected on a JEOL CRYO ARM 200 microscope.
The data and our precalculated results may be downloaded and unpacked using the commands below.
The full data set is also available at EMPIAR-10204.

::

    wget ftp://ftp.mrc-lmb.cam.ac.uk/pub/scheres/relion30_tutorial_data.tar
    wget ftp://ftp.mrc-lmb.cam.ac.uk/pub/scheres/relion40_tutorial_precalculated_results.tar.gz
    tar -xf relion30_tutorial_data.tar
    tar -zxf relion40_tutorial_precalculated_results.tar.gz


If you have any questions about |RELION|, first read this entire document, check the `FAQ <http://www2.mrc-lmb.cam.ac.uk/relion/index.php/FAQs>`_ on the |RELION| Wiki and the archives of the `CCPEM <https://www.jiscmail.ac.uk/ccpem>`_ mailing list.
If that doesn't help, subscribe to the CCPEM email list and use the email address above for asking your question.

.. caution::
    Please, please, please, do not send us direct emails, as we can no longer respond to all of those.
