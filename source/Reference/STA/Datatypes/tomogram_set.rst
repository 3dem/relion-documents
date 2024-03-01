.. _sec_sta_tomogram_set:

Tomogram set
============

The tomogram set describes all the tomograms (i.e. tilt series) defined in a project, and is usually named ``tomograms.star``.
It contains a single table, named ``global``, which defines the properties pertaining to each tomogram.
Each row corresponds to one tomogram, and it lists the following properties:

- The **tomogram name** (``rlnTomoName``): a unique identifier used to refer to this tomogram within the entire project (i.e. within the tomogram set, the particle set and the trajectory set)
- The **tilt series file name** (``rlnTomoTiltSeriesStarFile``): the path to the star file corresponding to each tomogram/image stack
- The **tomogram size** (``rlnTomoSize<X/Y/Z>``): the extent of the tomogram region in 3D space
- The **handedness** (``rlnTomoHand``): this value is either +1 or -1, and it describes whether the focus increases or decreases as a function of depth (projected Z coordinate). It cannot be known a priori and has to be determined experimentally. It is typically identical across the entire data set.
- The **pixel size of the raw micrographs**, given in Å (``rlnMicrographOriginalPixelSize``)
- The **pixel size of the tilt series**, given in Å (``rlnTomoTiltSeriesPixelSize``), corresponding to the dimensions given by ``rlnTomoSize<X/Y/Z>``, after the binning applied in the :jobtype:`Motion correction` job
- The **tomogram binning** (``rlnTomoTomogramBinning``): the binning applied to the tilt series in ``rlnTomoTiltSeriesStarFile`` to reconstruct the tomogram in ``rlnTomoReconstructedTomogram``
- The **reconstructed tomogram file** (``rlnTomoReconstructedTomogram``): the path to the reconstructed tomogram mrc file, at the binning in ``rlnTomoTomogramBinning``
- The **Etomo file** (``rlnEtomoDirectiveFile``)
- The **optics group name** (``rlnOpticsGroupName``)
- The **voltage**, given in kV (``rlnVoltage``)
- The **spherical aberration**, given in mm^-1 (``rlnSphericalAberration``)
- The **amplitude contrast** (``rlnAmplitudeContrast``)

The star file for each tomogram, that ``rlnTomoTiltSeriesStarFile`` points to, contains a single table with the same name as the tomogram. In it, each row corresponds to one tilt image and includes the following properties, among others:

- The **tilt image rotation angles and shifts** (``rlnTomo<X/Y>Tilt``, ``rlnTomoZRot`` and ``rlnTomo<X/Y>ShiftAngst``)
- The **astigmatic defocus** (``rlnDefocus<U/V>`` and ``rlnDefocusAngle``)
- The **intensity scale factor** related to effective ice thickness at each tilt angle (``rlnCtfScalefactor``)
- The **cumulative radiation dose** (``rlnMicrographPreExposure``)
- The **frame count** (``rlnTomoTiltMovieFrameCount``)


.. _IMOD: https://bio3d.colorado.edu/imod
