.. _sec_sta_preprocessing:

Preprocessing
=============

At this moment, |RELION| requires tomograms to be preprocessed externally.
It is user responsability to perform the initial steps of movie frames alignment, tilt series alignment and particle picking.

In summary, the required information to start processing in |RELION| is:

- **Tilt series alignment**: It should be done using IMOD_ package. Standard IMOD pipeline is typically accepted but note that not all IMOD options are supported.
- **Initial CTF parameters**: They can be estimated by either `CTFFind <https://grigoriefflab.umassmed.edu/ctffind4>`_ or `CtfPlotter <https://bio3d.colorado.edu/imod/doc/man/ctfplotter.html>`_.
- **Order list**: Chronological order of the tilt series acquisition.
- **Fractional electron dose**: electron dose per tilt image.

For a full description (See :ref:`program_tomo_import_tomograms`).


Getting organised
-----------------

We recommend to create a single directory per project, i.e. per structure you want to determine.
We'll call this the project directory. **It is important to always launch the RELION graphical user-interface (GUI) from the project directory.** Inside the project directory you should make a separate directory to store all your IMOD_ reconstructed tomograms folder.
We like to call this directory ``tomograms/``. Inside, we should find the different tomograms in folders like ``TS_1`` or ``TS_01``.
If for some reason you do not want to place your movies inside the |RELION| project directory, then inside the project directory you can also make a symbolic link to the directory where your reconstructed tomograms are stored.

|RELION| uses the original tilt series stack prior to tilt axis alignment and imports the alignment data from Imod. The tomogram folder should contain: a stack file, with extension ``.st``, ``.mrc`` or ``mrcs``; a ``newst.com`` and ``tilt.com`` script files, where the transformation and tilt angles filenames are obtained from, together with tomogram dimensions, offsets and excluded views.

When you unpacked the tutorial test data, the (``Tomograms/``) directory was created.
It should contain 37 tomogram folders and an ``order_list.csv`` file.

We will start by launching the |RELION| GUI.
As said before, this GUI always needs to be launched from the project directory.
To prevent errors with this, the GUI will ask for confirmation the first time you launch it in a new directory.
Make sure you are inside the project directory, and launch the GUI by typing:

::

    relion --tomo&

and answer ``Yes`` when prompted to set up a new |RELION| project here.





.. |tomogram_set| replace:: :ref:`tomogram set <sec_sta_tomogram_set>`
.. _IMOD: https://bio3d.colorado.edu/imod