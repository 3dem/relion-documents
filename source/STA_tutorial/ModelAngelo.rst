.. _sec_sta_modelangelo


Model building with ModelAngelo
===============================

Building an atomic model using ``ModelAngelo`` :cite:`jamali_automated_2023` is done in the same way as in the :ref:`SPA tutorial<sec_spa_modelangelo>`.
First, download the protein sequence as a FASTA file from `this link <https://www.rcsb.org/structure/5L93>`_ (``Download Files`` -> ``FASTA Sequence``).

Running the job
---------------

Select the :jobtype:`ModelAngelo building` job type and, on the :guitab:`I/O` tab, set:

:B-factor sharpened map:: PostProcess/job079/postprocess_masked.mrc

:FASTA sequence for proteins:: rcsb_pdb_5L93.fasta

After inputing the path to the ``ModelAngelo`` executable and the GPUs to use and making sure that ``Perform HMMer search?`` is set to ``No`` on the :guitab:`Hmmer` tab, we run the job.

Analysing the results
---------------------

On our machine with 2 GPUs, this job took 3 minutes to run.
The output is a coordinate file called ``ModelAngelo/job080/job080.cif`` that may be used in UCSF :textsc:`chimera` together with the ``Postprocess/job079/postprocess.mrc`` map.
Note that although ``ModelAngelo`` did a very good job on this relatively easy test case, you should always check its results carefully in a program like ``coot`` :cite:`emsley_coot_2010` . You will also need to perform a stereochemical refinement of the coordinates. For this, we like ``servalcat`` :cite:`yamashita_servalcat_2021`.

