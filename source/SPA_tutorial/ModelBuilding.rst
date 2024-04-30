.. _sec_spa_modelangelo:

ModelAngelo: atomic modelling
=============================

As of release 5.0, |RELION| comes with a machine-learning approach for automated atomic model building called ``ModelAngelo`` :cite:`jamali_automated_2024`. ModelAngelo is a graph neural network that combines information from the cryo-EM map with sequence information of the proteins that are present in the map to build an atomic model.

Because we know that the sample in this data set is beta-galactosidase from *E.coli*, we can provide the protein sequence as a ``FASTA`` file. You can download it from ``uniprot`` through `this link <https://www.uniprot.org/uniprotkb/P00722/entry>`_. Save it as ``betagal.fasta`` in the project directory.

Running the job
---------------

Using the :jobtype:`ModelAngelo building` job type, we set on the :guitab:`I/O` tab:

:B-factor sharpened map:: PostProcess/job030/postprocess\_masked.mrc

:FASTA sequence for proteins:: betagal.fasta

:FASTA sequence for DNA:: \

     (There is no DNA in this complex.)
			
:FASTA sequence for RNA:: \

     (There is no RNA in this complex.)

:Which GPUs to use:: 0,1,2,3

     
On the :guitab:`Hmmer` tab make sure you this is set:

:Perform HMMer search?: No



Analysing the results
---------------------

Running with 4 GPUs (relatively old 1080s), this job took approximately 18 minutes.
The output is a coordinate file called ``ModelAngelo/job032/job032.cif`` that may be used in UCSF :textsc:`chimera` together wit the ``Postprocess/job030/postprocess.mrc`` map.
Note that although ``ModelAngelo`` did a very good job on this relatively easy test case, you should always check its results carefully in a program like ``coot`` :cite:`emsley_coot_2010` . You will also need to perform a stereochemical refinement of the coordinates. For this, we like ``servalcat`` :cite:`yamashita_servalcat_2021`.


Discovering unknown proteins
----------------------------

One does not always know the identity of all proteins that are present in a cryo-EM reconstruction. One can also run ``ModelAngelo`` without providing a ``FASTA`` file with the known protein sequence. It will still try to model protein chains in the map, but will perform less well without the knowledge of the sequence. But, one can then perform a Hidden Markov Model search using the full probabilities for all 20 amino acids for every residue, for example against a FASTA file that contains the entire genome for that organism. In that way, one can identify unknown proteins in the map.

Download the *E.coli* genome (K-12 substrain) from `this link to NCBI <https://www.ncbi.nlm.nih.gov/nuccore/NC_000913.3>`_. Use the ``Send to`` dropdown menu on the top right to select ``Coding Sequences``, select the ``FASTA protein`` format, and click ``Create File``. Save the resulting file as ``Ecoli.fasta`` in your project directory.


Using the same :jobtype:`ModelAngelo building` job type, this time we set on the :guitab:`I/O` tab:

:B-factor sharpened map:: PostProcess/job030/postprocess\_masked.mrc

:FASTA sequence for proteins:: \

:FASTA sequence for DNA:: \

     (There is no DNA in this complex.)
			
:FASTA sequence for RNA:: \

     (There is no RNA in this complex.)

:Which GPUs to use:: 0,1,2,3

     
On the :guitab:`Hmmer` tab, we now set:

:Perform HMMer search?: Yes

:Library with sequences for HMMer search:: Ecoli.fasta
					 
:Alphabet for HMMer search:: amino

And we leave the rest of the HMMSearch parameters at their defaults.


Which one is my protein?
------------------------

Running with 4 GPUs (again our relatively old 1080s), this job took approximately 12 minutes: running without the sequence is faster than running with the sequence. However, without knowledge of the sequence, ModelAngelo has trouble building a single chain, as you can see by visualising ``ModelAngelo/job033/job033.cif`` in UCSF :textsc:`chimera`.
The subsequent HMM search easily identifies beta-galactosidase, as you can see in ``ModelAngelo/job033/best_hits.csv``. Cool, huh?



