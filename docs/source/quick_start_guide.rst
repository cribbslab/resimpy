Quick start guide
=================

tags: ``Resimpy``
                 

Overview
--------

We set up a quick start guide to walk you through examples to use
Resimpy. Resimpy can be applied to generating a myriad of sequencing
data over a predefined number of PCR cycles and of course, along with a
number of other parameters. It is currently equipped with 3 modules,
that is, ``resimpy_general``, ``resimpy_umi_sc``, and
``resimpy_transloc`` to support the generation of scRNA-seq reads,
UMI-exclusive reads, and other loosely-structured RNA-seq reads. Given
the error assignment approaches inherent to the nucleotide synthesis
process, almost all methods are inevitably confronted with several
challenges such as time-comsuming processes and high-momery
requirements, so is Resimpy. However, we speeded up Resimpy in a quite
notable manner owing to several optimization strategies. For instance,
we used Pandas vectorization and an optimized nucleotide position
retrieving strategy. We tested and run Resimpy with an initial sequence
number 50 in seconds below 14 PCR cycles, and in minutes below 18-20
cycles.

Documentation
-------------

The API documentation of Mclumi is available at Readthedocs
https://resimpy.readthedocs.io/en/latest/index.html.

System Requirement
------------------

Cross platforms.

Installation
------------

-  PyPI https://pypi.org/project/resimpyx/

::

   pip install --upgrade resimpyx

Usage
-----

Command-Line Interface (CLI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Overview

.. code:: angular2html

   usage: resimpy_general [-h] --recipe recipe --read_structure read_structure
                          --permutation_num permutation_num
                          [--umi_unit_pattern umi_unit_pattern]
                          [--umi_unit_len_fixed umi_unit_len_fixed]
                          [--umi_num_fixed umi_num_fixed]
                          [--seq_length seq_length]
                          [--sim_thres_fixed sim_thres_fixed]
                          [--pcr_num_fixed pcr_num_fixed]
                          [--ampl_rate_fixed ampl_rate_fixed]
                          [--seq_sub_spl_rate seq_sub_spl_rate]
                          [--pcr_err_fixed pcr_err_fixed]
                          [--seq_err_fixed seq_err_fixed]
                          [--ampl_set_rates ampl_set_rates]
                          [--umi_unit_set_lens umi_unit_set_lens]
                          [--pcr_set_nums pcr_set_nums]
                          [--pcr_set_errs pcr_set_errs]
                          [--seq_set_errs seq_set_errs]
                          [--out_directory out_directory]

   Welcome to the resimpy_general module

   optional arguments:
     -h, --help            show this help message and exit
     --recipe recipe, -r recipe
                           which condition among seq_errs, ampl_rates, pcr_errs,
                           pcr_nums, and umi_lens is used
     --read_structure read_structure, -rs read_structure
                           read structure consisting of a UMI block (umi) and a
                           sequence block (seq), e.g., umi or umi+seq
     --permutation_num permutation_num, -perm_num permutation_num
                           permutation test number
     --umi_unit_pattern umi_unit_pattern, -umiup umi_unit_pattern
                           unit UMI pattern. This is to specify if UMIs consist
                           of monomer, dimer, trimer, or other blocks
     --umi_unit_len_fixed umi_unit_len_fixed, -umiul umi_unit_len_fixed
                           unit UMI length fixed. This is to specify the length
                           of a monomer UMI. The final UMI length =
                           umi_unit_pattern * umi_unit_len_fixed
     --umi_num_fixed umi_num_fixed, -umi_num umi_num_fixed
                           UMI number
     --seq_length seq_length, -seq_len seq_length
                           genomic sequence length
     --sim_thres_fixed sim_thres_fixed, -sim_thres sim_thres_fixed
                           edit distance-measured similarities between UMIs
     --pcr_num_fixed pcr_num_fixed, -pcr_num pcr_num_fixed
                           Number of PCR cycles fixed
     --ampl_rate_fixed ampl_rate_fixed, -ampl_rate ampl_rate_fixed
                           PCR amplification rate fixed
     --seq_sub_spl_rate seq_sub_spl_rate, -spl_rate seq_sub_spl_rate
                           Subsampling rate for sequencing
     --pcr_err_fixed pcr_err_fixed, -pcr_err pcr_err_fixed
                           PCR error fixed
     --seq_err_fixed seq_err_fixed, -seq_err seq_err_fixed
                           Sequencing error fixed
     --ampl_set_rates ampl_set_rates, -ampl_rates ampl_set_rates
                           a semicolon-partitioned string of a set of
                           amplification rates
     --umi_unit_set_lens umi_unit_set_lens, -umi_lens umi_unit_set_lens
                           a semicolon-partitioned string of a set of unit UMI
                           lens
     --pcr_set_nums pcr_set_nums, -pcr_nums pcr_set_nums
                           a semicolon-partitioned string of a set of PCR numbers
     --pcr_set_errs pcr_set_errs, -pcr_errs pcr_set_errs
                           a semicolon-partitioned string of a set of PCR errors
     --seq_set_errs seq_set_errs, -seq_errs seq_set_errs
                           a semicolon-partitioned string of a set of sequencing
                           errors
     --out_directory out_directory, -out_dir out_directory
                           output directory

Contact
-------

Homepage: https://www.ndorms.ox.ac.uk/team/adam-cribbs
