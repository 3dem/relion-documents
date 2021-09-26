Introduction
============

This tutorial provides an introduction for the subtomogram analysis workflow in |RELION|-4.0: preprocessing; importing tomograms; importing coordinates; pseudo-subtomograms construction; particle reconstruction; 3D classification; high-resolution 3D refinement; frame alignment refinement; CTF refinement and higher-order aberration correction; and final map sharpening and local-resolution estimation.
Carefully going through this tutorial should take less than a day (if you have a suitable GPU or if you follow our precalculated results).
After that, you should be able to run |RELION| on your own data.

This tutorial uses a test data set composed by 5 tomograms of immature HIV-1 dMACANC VLPs available at `EMPIAR-10164 <https://www.ebi.ac.uk/pdbe/emdb/empiar/entry/10164/>`_.
The data to start processing (Tilt series, tomograms alignment, CTF estimation, particle coordinates, masks ...) may be downloaded and unpacked using the command below.

::

    wget ftp://ftp.mrc-lmb.cam.ac.uk/pub/scheres/relion40_sta_tutorial_data.tar
    tar -xf relion40_sta_tutorial_data.tar

.. The data to start processing (Tilt series, tomograms alignment, CTF estimation, particle coordinates, masks ...) and our precalculated results may be downloaded and unpacked using the commands below.

.. ::

..    wget ftp://ftp.mrc-lmb.cam.ac.uk/pub/scheres/relion40_sta_tutorial_data.tar
    wget ftp://ftp.mrc-lmb.cam.ac.uk/pub/scheres/relion40_sta_tutorial_precalculated_results.tar.gz
    tar -xf relion40_sta_tutorial_data.tar
    tar -zxf relion40_sta_tutorial_precalculated_results.tar.gz

If you have any questions about |RELION|, first read this entire document, check the `FAQ <http://www2.mrc-lmb.cam.ac.uk/relion/index.php/FAQs>`_ on the |RELION| Wiki and the archives of the `CCPEM <https://www.jiscmail.ac.uk/ccpem>`_ mailing list.
If that doesn't help, subscribe to the CCPEM email list and use the email address above for asking your question.

.. caution::
    Please, please, please, do not send us direct emails, as we can no longer respond to all of those.
