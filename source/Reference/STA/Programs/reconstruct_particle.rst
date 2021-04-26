.. _program_tomo_reconstruct_particle:

relion_tomo_reconstruct_particle
================================

This program constructs high-resolution 3D reference maps from a given :ref:`optimisation set <sec_sta_optimisation_set>`.
It is similar to ``relion_reconstruct``, except that it does not require pre-extracted particle images.
Instead, it extracts square windows of arbitrary size (``--b`` argument) directly from the tilt series and it uses those for the reconstruction (using Fourier inversion).
It considers the defoci of the individual particles, as well as particle motion and higher-order aberrations.

The output consists of a pair of maps (one for each half set) as well as a merged map.
In addition, the numerator (data term) and denominator (weight term) (see Eq. 3 in the `|RELION| paper <https://www.sciencedirect.com/science/article/pii/S1047847712002481>`_) of all 3 maps are also written out to facilitate further processing.

Relevant program arguments:
---------------------------

- ``--i`` and/or ``--p``, ``--t`` and ``--mot``: input optimisation-set and/or its components (see :ref:`optimisation set <sec_sta_optimisation_set>`).
- ``--b``: box size of the reconstruction. Note that this is independent of the box size used to refine the particle. This allows the user to construct a 3D map of arbitrary size to gain an overview of the structure surrounding the particle. A sufficiently large box size also allows more of the high-frequency signal to be captured that has been delocalised by the CTF.
- ``--crop``: cropped box size. If set, the program will output an additional set of maps that have been cropped to this size. This is useful if a map is desired that is smaller than the box size required to retrieve the CTF-delocalised signal.
- ``--bin``: downsampling (binning) factor. Note that this does not alter the box size. The reconstructed region instead becomes larger.
- ``--SNR``: apply a `Wiener filter <https://en.wikipedia.org/wiki/Wiener_filter>`_ with this signal-to-noise ratio. If omitted, the reconstruction will use a heuristic to prevent divisions by excessively small numbers. Please note that using a low (even though realistic) SNR might wash out the higher frequencies, which could make the map unsuitable to be used for further refinement.
- ``--sym``: name of the symmetry class (e.g. C6 for six-fold point symmetry).
- ``--mem``: (approximate) maximum amount of memory to be used for the reconstruction (see below).
- ``--j``: number of threads used for the non-reconstruction parts of the program (e.g. symmetry application or gridding correction). This should be set to the number of CPU cores available.
- ``--j_out``: number of threads that compute partial reconstructions in parallel. This is faster, but it requires additional memory for each thread. When used together with the ``--mem`` argument, this number will be reduced to (approximately) maintain the imposed memory limitation.
- ``--j_in``: number of threads to be used for each partial reconstruction. This is a slower way to parallelise the procedure, but it does not require additional memory. Unless memory is limited, the ``--j_out`` option should be preferred. The product of ``--j_out`` and ``--j_in`` should not exceed the number of CPU cores available.
- ``--o``: name of the output directory (that will be created).

Program output:
---------------

After running the program, the output directory (``--o`` argument) will contain the following items:

- **<half1/half2/merged>.mrc**: the reconstructed cropped maps.
- **<half1/half2/merged>_full.mrc**: the reconstructed full-size maps, in case the full size (``--b`` argument) differs from the cropped size (``--crop`` argument).
- **data_<half1/half2/merged>.mrc**: the reconstructed data term at full size.
- **weight_<half1/half2/merged>.mrc**: the reconstructed weight term at full size.
- **note.txt**: a text file containing the command issued to run the program.