Generating sequencing reads for detecting PCR artificial translocation
======================================================================

tags: ``Resimpy``
                 

Introduction
------------

``resimpy_umi_transloc`` is a module designed for simulating sequencing
reads consisting of two UMIs per each for detecting PCR artificial
translocation. To achieve this purpose, a case-study CLI should look
like below:

.. code:: shell

   resimpy_umi \
   -r seq_errs \
   -rs umi \
   -tr 0.02 \
   -perm_num 3 \
   -umiup 1 \
   -umiul 10 \
   -umi_num 50 \
   -pcr_num 8 \
   -pcr_err 0.0001 \
   -seq_err 0.0001 \
   -ampl_rate 0.85 \
   -sim_thres 3 \
   -spl_rate 1 \
   -seq_errs 1e-3;1e-2;0.1 \
   -out_dir ./

Parameters are illustrated below.

+--------+-------------+-----------------------------------------------+
| Par    | Full name   | Function                                      |
| ameter |             |                                               |
| a      |             |                                               |
| cronym |             |                                               |
+========+=============+===============================================+
| r      | recipe      | to specify a module to work on your           |
|        |             | requirement                                   |
+--------+-------------+-----------------------------------------------+
| rs     | read        | e.g., umi+seq or umi                          |
|        | structure   |                                               |
+--------+-------------+-----------------------------------------------+
| -tr    | tr          | artificial PCR translocation rate e.g., 0.02  |
|        | anslocation |                                               |
|        | rate        |                                               |
+--------+-------------+-----------------------------------------------+
| pe     | permutation | in silico test numbers                        |
| rm_num | number      |                                               |
+--------+-------------+-----------------------------------------------+
| umiup  | UMI unit    | 1 for monomer blocks, 2 for dimer blocks, 3   |
|        | pattern     | for trimer blocks                             |
+--------+-------------+-----------------------------------------------+
| umiul  | UMI unit    | the fixed length of a monomer UMI             |
|        | len fixed   |                                               |
+--------+-------------+-----------------------------------------------+
| u      | UMI number  | the fixed number of molecules/UMIs to be      |
| mi_num | fixed       | initiated in the initial read pool            |
+--------+-------------+-----------------------------------------------+
| sim    | similarity  | how many nucleotites are different at least   |
| _thres | threshold   | between each pair of two randomly generated   |
|        | fixed       | UMIs                                          |
+--------+-------------+-----------------------------------------------+
| p      | PCR         | a fixed PCR number                            |
| cr_num | n           |                                               |
|        | umber/cycle |                                               |
+--------+-------------+-----------------------------------------------+
| p      | PCR error   | a fixed DNA polymerase error rate during PCR  |
| cr_err |             |                                               |
+--------+-------------+-----------------------------------------------+
| s      | sequencing  | a fixed sequencing error rate                 |
| eq_err | error       |                                               |
+--------+-------------+-----------------------------------------------+
| amp    | am          | PCR amplification rate                        |
| l_rate | plification |                                               |
|        | rate        |                                               |
+--------+-------------+-----------------------------------------------+
| sp     | subsampling | subsampling rate used for sequencing          |
| l_rate | rate        |                                               |
+--------+-------------+-----------------------------------------------+
| se     | sequencing  | sequencing error rate partitioned by          |
| q_errs | errors      | semicolon, e.g., 1e-3;1e-2;0.1                |
+--------+-------------+-----------------------------------------------+
| pc     | PCR errors  | DNA polymerase error rate partitioned by      |
| r_errs |             | semicolon, e.g., 1e-3;1e-2;0.1                |
+--------+-------------+-----------------------------------------------+
| pc     | PCR numbers | PCR numbers partitioned by semicolon, e.g.,   |
| r_nums |             | 8;9;10;11;12                                  |
+--------+-------------+-----------------------------------------------+
| um     | UMI lengths | UMI lengths partitioned by semicolon, e.g.,   |
| i_lens |             | 8;9;10;11;12                                  |
+--------+-------------+-----------------------------------------------+
| ampl   | am          | amplification rates partitioned by semicolon, |
| _rates | plification | e.g., 0.1;0.2;0.3;0.4;0.5;0.6;0.7;0.8;0.9;1.0 |
|        | rates       |                                               |
+--------+-------------+-----------------------------------------------+
| o      | output      | a directory where you want to output results  |
| ut_dir | directory   |                                               |
+--------+-------------+-----------------------------------------------+

In each permutation test, reads will be generated based on one varying
parameter such as ``seq_errs`` and all of the fixed parameters such as
``pcr_num`` except for the varying one. In this context, ``seq_err``
will not be applied because ``seq_errs`` is claimed, such that reads can
be examined under this varying one. This is actually a one-factor
experiment control. Similarly, for ``pcr_errs``, ``pcr_nums``,
``umi_lens``, and ``ampl_rates``, the CLIs should look like below:

Reads changing with PCR errors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   resimpy_general -r pcr_errs -rs umi+seq -tr 0.02 -perm_num 3 -umiup 1 -umiul 10 -umi_num 50 -seq_len 20 -pcr_num 8 -pcr_err 0.0001 -seq_err 0.0001 -ampl_rate 0.85 -sim_thres 3 -spl_rate 1 -pcr_errs 1e-3;1e-2;0.1 -out_dir ./

Reads changing with amplification rates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   resimpy_general -r ampl_rates -rs umi+seq -tr 0.02 -perm_num 3 -umiup 1 -umiul 10 -umi_num 50 -seq_len 20 -pcr_num 8 -pcr_err 0.0001 -seq_err 0.0001 -ampl_rate 0.85 -sim_thres 3 -spl_rate 1 -ampl_rates 0.1;0.2;0.3;0.4;0.5;0.6;0.7;0.8;0.9;1.0 -out_dir ./

Reads changing with PCR numbers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   resimpy_general -r pcr_nums -rs umi+seq -tr 0.02 -perm_num 3 -umiup 1 -umiul 10 -umi_num 50 -seq_len 20 -pcr_num 8 -pcr_err 0.0001 -seq_err 0.0001 -ampl_rate 0.85 -sim_thres 3 -spl_rate 1 -pcr_nums 6;7;8;9;10;11;12;13;14 -out_dir ./

Reads changing with UMI lengths
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   resimpy_general -r umi_lens -rs umi+seq -tr 0.02 -perm_num 3 -umiup 1 -umiul 10 -umi_num 50 -seq_len 20 -pcr_num 8 -pcr_err 0.0001 -seq_err 0.0001 -ampl_rate 0.85 -sim_thres 3 -spl_rate 1 -umi_lens 6;7;8;9;10;11;12 -out_dir ./
