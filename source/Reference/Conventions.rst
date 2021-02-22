Conventions
===========

Image formats
-------------

|RELION| reads the following image file formats:

* **MRC images** (with extension ``.mrc``)
* **MRC stacks** (with extension ``.mrcs``)
* **SPIDER images** (with extension ``.spi``)
* **SPIDER stacks** (with extension ``.spi``)
* **TIFF images or movies** (with extensions ``.tif`` and ``.tiff``)
* **EER movies** (with extension ``.eer``)

For compatibility with other EM programs (e.g.
UCSF MotionCor2, IMOD), TIFF images are flipped along the slow axis when being read into memory or written to a file.
This happens regardless of the ``TIFFTAG_ORIENTATION`` value in the header.

|RELION| writes individual images and image stacks in `the MRC format <https://www.ccpem.ac.uk/mrc_format/mrc2014.php>`_ .
Because there is no distinction between 3D maps or stacks of 2D images in MRC format, 3D maps are indicated with a ``.mrc`` extension, and stacks with a ``.mrcs`` extension.
Individual images in stacks are indicated by an integer number (ranging from 1 to the number of images in the stack) followed by an "@" sign and the filename of the stack.
Thereby, the first three images in a stack called my_images.mrcs are called:

::

    1@my_images.mrcs
    2@my_images.mrcs
    3@my_images.mrcs

RELION supports the following MRC modes.

0:
    signed 8-bit integer

1:
    signed 16-bit integer

2:
    32-bit floating point

6:
    unsigned 16-bit integer

101:
    packed 4-bit integer (IMOD extension)

STAR format
-----------

|RELION| uses the *STAR* (Self-defining Text Archiving and Retrieval) format (Hall, Allen and Brown, 1991) for the storage of label-value pairs for all kinds of input and output metadata.
The STAR format is an alternative to XML, but it is more readable and occupies less space.
The STAR format has been adopted by the crystallographic community in the form of `CIF (Crystallographic Information Framework) <https://www.iucr.org/resources/cif>`_, and Bernard Heymann's `BSOFT package <https://lsbr.niams.nih.gov/bsoft/>`_ was the first to use STAR in the field of 3D-EM.

|RELION|'s implementation of the STAR format has the following rules (partially copied from BSOFT's manual):

*   The file name must end in a ".star" extension.
*   Each file must have one or more data blocks.
    The start of a data block is defined by the keyword ``data_`` followed by an optional string for identification (e.g., "data_images").
*   Multiple values associated with one or more labels in a data block can be arranged in a table using the keyword ``loop_`` followed by the list of labels and columns of values.
    The values are delimited by whitespace (i.e., blanks, tabs, end-of-lines and carriage returns).
    The loop must be followed by an empty line to indicate its end.
*   Label names always starts with an underscore ("_").
    Each label may only be used once within each data block.
*   Data items or values can be numeric or strings of characters.
    A string is interpreted as a single item when it doesn't contain spaces
*   Comments are strings which can occur in three places:
    * File comments: All text before the first ``data_`` keyword
    * Data block comments: Strings on their own lines starting with "#" or with ";" as the first character in the line.
    * Item comments: Strings on the same line as and following tag-value items, also indicated by a leading "#".
*   String values that contain spaces can be quoted by ``"``.
    An empty string becomes ``""``.

**Metadata label definitions**

|RELION| has its own set of defined metadata labels.
The following command will print a list of the definitions of all of them:

::

    relion_refine --print_metadata_labels


Optics Groups
-------------

|RELION| 3.1 introduced optics groups.
See :cite:`Zivanov_estimation_2020` for an introduction.

Movies, micrographs or particles are in the ``movies``, ``micrographs`` and ``particles`` tables, respectively, and refer to an optics group entry in the ``optics`` table via the ``rlnOpticsGroup`` column.
``rlnOpticsGroupName`` strings are used when merging two STAR files.
Optics groups with different names are considered different and ``rlnOpticsGroup`` IDs will be re-numbered.

|RELION| 3.1+ automatically upgrades old-style STAR files from |RELION| 3.0 and earlier.
You can also manually convert them by ``relion_convert_star``.
Downgrading to the |RELION| 3.0 format is not officially supported but you might find `this ccpem mailing list post <https://www.jiscmail.ac.uk/cgi-bin/webadmin?A2=ind1910&L=CCPEM&P=R321009>`_ useful.


Orientations
------------

Orientations (``rlnAngleRot``, ``rlnAngleTilt``, ``rlnAnglePsi``) in a STAR file rotate the reference into observations (i.e.
particle image), while translations (``rlnOriginXAngstrom`` and ``rlnOriginYAngstrom``) shifts observations into the reference projection.
For developers, a good starting point for code reading is ``ObservationModel::predictObservation()`` in the `src/jaz/obs_model.cpp <https://github.com/3dem/relion/blob/ver3.1/src/jaz/obs_model.cpp>`_.

In compliance with the `Heymann, Chagoyen and Belnap (2005) standard <https://pubmed.ncbi.nlm.nih.gov/16043364/>`_ |RELION| uses a right-handed coordinate system with orthogonal axes X, Y and Z, where right-handed rotations are called positive, and Euler angles are defined as:

*   The first rotation is called ``rlnAngleRot`` and is around the Z-axis.
*   The second rotation is called ``rlnAngleTilt`` and is around the new Y-axis.
*   The third rotation is called ``rlnAnglePsi`` and is around the new Z axis

As such, |RELION| uses the same Euler angles as XMIPP, SPIDER and FREALIGN.

The center of rotation of a 2D image of dimensions xdim x ydim is defined by ``((int)xdim/2, (int)(ydim/2))`` (with the first pixel in the upper left being (0,0).
Note that for both xdim=ydim=65 and for xdim=ydim=64, the center will be at (32,32).
This is the same convention as used in SPIDER and XMIPP.
Origin offsets reported for individual images translate the image to its center and are applied BEFORE rotations.

Particle translations used to be in pixels (``rlnOriginX`` and ``rlnOriginY``) but this changed to Angstroms (``rlnOriginXAngstrom`` and ``rlnOriginYAngstrom``) in |RELION| 3.1.

The unit of particle coordinates in a micrograph (``rlnCoordinateX`` and ``rlnCoordinateY``) is pixel in the aligned and summed micrograph (possibly binned from super-resolution movies).
The origin is the first element in the 2D array of an MRC file.
The origin is displayed at the upper-left corner in |RELION| (other programs might display in other ways).


Contrast Transfer Function
--------------------------

CTF parameters are defined as in |CTFFIND4.1|, also see :cite:`mindell_ctffind_2003`.


**Higher order aberrations**

``rlnOddZernike`` contains coefficients for asymmetric (antisymmetric) Zernike polynomials :math:`Z_1^{-1}, Z_1^1 , Z_3^{-3}, Z_3{-1}, Z_3^1, Z_3^3, \cdots` in this order.
``rlnEvenZernike`` contains coefficients for symmetric Zernike polynomials :math:`Z_0^0, Z_2^{-2}, Z_2^0, Z_2^2, Z_4^{-4}, Z_4^{-2}, Z_4^0, Z_4^2, Z_4^4 \cdots` in this order.
Thus, the 7-th item in the ``rlnEvenZernike``, Z\ :sub:`4`\ \ :sup:`0`\ , is related to an error in the spherical aberration coefficient.

Look at the `table in Wikipedia <https://en.wikipedia.org/wiki/Zernike_polynomials#Zernike_polynomials>`_ but ignore square root terms, as the coefficients are not normalised in |RELION|.
For example, :math:`Z_3^{-1} = (3 r^3 - 2r) \sin \theta = 3 (k_x^2 + k_y^2) k_y - 2 k_y`, where :math:`k_x` and :math:`k_y` are wave-numbers in the reciprocal space (1 / Å).


**Anisotropic magnification corrections**

Transformation by anisotropic magnification brings the reference into observations (i.e.particle images) in real space.
Note that stretching in real space is shrinking in reciprocal space and vice versa.

``rlnMagMatrix_00`` to ``rlnMagMatrix_11`` represent the matrix ``M`` in the section 2.4 of :cite:`Zivanov_estimation_2020`.
The values become larger when the observed particle in the real space *looks larger* than the reference projection at the nominal pixel size.
This also means that the true pixel size is *actually smaller* than the nominal pixel size.


Symmetry
--------

Symmetry libraries have been copied from XMIPP.
As such, with the exception of tetrahedral symmetry, they comply with :cite:`heymann_convention_2005`:

.. list-table::
   :header-rows: 1
   :widths: 20 10 30 40

   * - Group
     - Notation
     - Origin
     - Orientation
   * - Asymmetric
     - C1
     - User-defined
     - User-defined
   * - Cyclic
     - C<n>
     - On symm axis, Z user-defined
     - Symm axis on Z
   * - Dihedral
     - D<n>
     - Intersection of symm axes
     - principle symm axis on Z, 2-fold on X
   * - Tetrahedral
     - T
     - Intersection of symm axes
     - 3-fold axis on Z (deviating from Heymann et al!)
   * - Octahedral
     - O
     - Intersection of symm axes
     - 4-fold axes on X, Y, Z
   * - Icosahedral
     - I<n>
     - Intersection of symm axes
     - \*\*

\*\* Multiple settings of the icosahedral symmetry group have been implemented:

I1:
    No-crowther 222 setting (=standard in Heymann et al): 2-fold axes on X,Y,Z.
    With the positive Z pointing at the viewer, the front-most 5-fold vertices are in YZ plane, and the front-most 3-fold axes are in the XZ plane.
I2:
    Crowther 222 setting: 2-fold axes on X,Y,Z.
    With the positive Z pointing at the viewer, the front-most 5-fold vertices are in XZ plane, and the front-most 3-fold axes are in the YZ plane.
I3:
    52-setting (as in SPIDER?): 5-fold axis on Z and 2-fold on Y.
    With the positive Z pointing at the viewer and without taken into account the 5-fold vertex in Z, there is one of the front-most 5-fold vertices in -XZ plane
I4:
    Alternative 52 setting: with the positive Z pointing at the viewer and without taken into account the 5-fold vertices in Z, there is one of the front-most 5-fold vertices in +XZ plane.

In case of doubt, a list of all employed symmetry operators may be printed to screen using the command (for example for the D7 group):

::

    relion_refine --sym D7 --print_symmetry_ops