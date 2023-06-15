.. mclumi documentation master file, created by
   sphinx-quickstart on Fri Oct 22 01:46:02 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Tutorials
=========
In the tutorials, we will go through a few number of using Resimpy. The use of a combination of parameters is of paramount importance to quality control of simulated reads. In Resimpy, five parameters are primarily considered to vary over PCR cycles so as to simulate reads in different scenarios. They are ``seq_errs``, ``pcr_errs``, ``pcr_nums``, ``ampl_rates``, and ``umi_lens`` to be included in all the three modules, ``resimpy_general``, ``resimpy_umi_sc``, and ``resimpy_umi_transloc``.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   umi_exclusive_or_umi_seq
   umi_transloc
   scRNAseq

