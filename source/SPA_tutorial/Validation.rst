Local-resolution estimation
===========================

The estimated resolution from the post-processing program is a global estimate.
However, a single number cannot describe the variations in resolution that are often observed in reconstructions of macromolecular complexes.
Alp Kucukelbir and Hemant Tagare wrote a nifty program to estimate the variation in resolution throughout the map :cite:`kucukelbir_quantifying_2014`. |RELION| implements a wrapper to this program through the :jobtype:`Local resolution` job-type.
Alternatively, one can choose to run a post-processing-like procedure with a soft spherical mask that is moved around the entire map.
In the example below, we use the latter.


Running the job
---------------

 On the :guitab:`I/O` tab set:

:One of the two unfiltered half-maps:: Refine3D/job029/run\_half1\_class001\_unfil.mrc

:User-provided solvent mask:: MaskCreate/job020/mask.mrc

:Calibrated pixel size:: 1.244

     (Sometimes you find out when you start building a model that what you thought was the correct pixel size, in fact was off by several percent.
     Inside |RELION|, everything up until this point was still consistent (provided you aren't at resolutions beyond 2 Angstrom). so you do not need to re-refine your map and/or re-classify your data. All you need to do is provide the correct pixel size here for your correct map and final resolution estimation.)


On the :guitab:`ResMap` tab set:

:Use ResMap?: No


On the :guitab:`Relion` tab set:

:Use Relion?: Yes

:User-provided B-factor:: -30

     (This value will be used to also calculate a locally-filtered and sharpened map.
     Probably you want to use a value close to the one determined automatically during the :jobtype:`Post-processing` job.)

:MTF of the detector (STAR file):: mtf_k2_200kV.star

     (The same as for the :jobtype:`Post-processing` job.)


Analysing the results
---------------------

Running with 8 MPI processes, this job took approximately 7 minutes.
The output is a file called ``LocalRes/job031/relion_locres.mrc`` that may be used in UCSF :textsc:`chimera` to color the `Postprocess/job030/postprocess.mrc` map according to local resolution.
This is done using ``[Tools]-[Volume data]-[Surface color]``, and then select ``by volume data value`` and browse to the ``resmap`` file.

Unique to the |RELION| option is the additional output of a locally-filtered (and sharpened map), which may be useful to describe the overall variations in map quality in a single map.
This map is saved as ``LocalRes/job031/relion_locres_filtered.mrc`` and can be visualised directly in UCSF :textsc:`chimera` (and optionally also coloured by local resolution as before).


Checking the handedness
=======================

Careful inspection of the map may indicate that the handedness is incorrect, e.g. because the α-helices turn the wrong way around.
Remember that it is impossible to determine absolute handedness from a data set without tilting the microscopy stage.
The SGD algorithm in the :jobtype:`3D initial model` jobtype therefore has a 50 % chance of being in the opposite hand.
In our precalculated results, this was not the case.
One may flip the handedness of the postprocessed map from the command line as follows:

::

    relion_image_handler --i PostProcess/job030/postprocess.mrc  \
      --o PostProcess/job030/postprocess_invert.mrc --invert_hand


The same command could also be run on any of the other maps.
If one realises earlier on in the image processing procedure that the hand is wrong, one could of course also switch to the other hand earlier on.
For |RELION| itself it doesn't matter, as both hands cannot be distinguished, but it may be more convenient to flip the hand as soon as you notice it.

Once in the correct hand, you might want to load the map into UCSF :textsc:`chimera` and superimpose it with an atomic model for β-galactosidase.
You could try fetching one straight from the PDB using PDB-ID 5a1a.
