# Resimpy
![](https://img.shields.io/badge/Resimpy-executable-519dd9.svg)
![](https://img.shields.io/badge/last_released-Jan._2022-green.svg)
![](https://img.shields.io/github/stars/cribbslab/resimpy?logo=GitHub&color=blue)
![](https://img.shields.io/pypi/v/resimpyx?logo=PyPI)
[![Documentation Status](https://readthedocs.org/projects/resimpy/badge/?version=latest)](https://resimpy.readthedocs.io/en/latest/?badge=latest)
[![Downloads](https://pepy.tech/badge/mclumi)](https://pepy.tech/project/mclumi)

###### tags: `Resimpy` `read simulation` `PCR amplification` `scRNA-seq` `bulkRNA-seq`


## Overview
```angular2html
 ____           _                         _____           _ _    _ _
|  _ \ ___  ___(_)_ __ ___  _ __  _   _  |_   _|__   ___ | | | _(_) |_
| |_) / _ \/ __| | '_ ` _ \| '_ \| | | |   | |/ _ \ / _ \| | |/ / | __|
|  _ <  __/\__ \ | | | | | | |_) | |_| |   | | (_) | (_) | |   <| | |_
|_| \_\___||___/_|_| |_| |_| .__/ \__, |   |_|\___/ \___/|_|_|\_\_|\__|
                           |_|    |___/
```
The **RE**ad **SIM**ulation **PY**thon program (Resimpy) provides an scalable interface for users through Python to massively simulate and generate reads of varying sequencing technologies, in order to avoid timeconsuming experimental trials and other error-prone approaches. Simulated reads can have the UMI- barcode- primer-, or spacer-featured composition. Resimpy has been made avilable through the command-line interface (CLI) and Python-inline visits. 

## Citation
Please cite our work if you use Resimpy in your research.

## Result reproducibility
To reproduce the results used in xxx, please follow the instruction below.
```angular2html
resimpy_general ...
resimpy_umi_sc ...
resimpy_umi_transloc ...
```

## Documentation
The Resimpy documentation showing its usage in different situations are available at https://resimpy.readthedocs.io/en/latest/index.html.

## Installation
Released via https://pypi.org/project/resimpyx/
```angular2html
pip install --upgrade resimpyx
```

## Overview
```angular2html
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
```

## Usage
### resimpy_general
#### Example 1: sequencing errors
```shell
resimpy_general \
-r seq_errs \
-rs umi+seq \
-perm_num 3 \
-umiup 1 \
-umiul 10 \
-umi_num 50 \
-seq_len 20 \
-pcr_num 8 \
-pcr_err 0.0001 \
-seq_err 0.0001 \
-ampl_rate 0.85 \
-sim_thres 3 \
-spl_rate 1 \
-seq_errs 1e-3;1e-2;0.1 \
-out_dir ./
```

```
# resimpy_general pcr_errs
resimpy_general -r pcr_errs -rs umi+seq -perm_num 3 -umiup 1 -umiul 10 -umi_num 50 -seq_len 20 -pcr_num 8 -pcr_err 0.0001 -seq_err 0.0001 -ampl_rate 0.85 -sim_thres 3 -spl_rate 1 -pcr_errs 1e-3;1e-2;0.1 -out_dir ./

# resimpy_general ampl_rates 
resimpy_general -r ampl_rates -rs umi+seq -perm_num 3 -umiup 1 -umiul 10 -umi_num 50 -seq_len 20 -pcr_num 8 -pcr_err 0.0001 -seq_err 0.0001 -ampl_rate 0.85 -sim_thres 3 -spl_rate 1 -ampl_rates 0.1;0.2;0.3;0.4;0.5;0.6;0.7;0.8;0.9;1.0 -out_dir ./

# resimpy_general pcr_nums
resimpy_general -r pcr_nums -rs umi+seq -perm_num 3 -umiup 1 -umiul 10 -umi_num 50 -seq_len 20 -pcr_num 8 -pcr_err 0.0001 -seq_err 0.0001 -ampl_rate 0.85 -sim_thres 3 -spl_rate 1 -pcr_nums 6;7;8;9;10;11;12;13;14 -out_dir ./

# resimpy_general umi_lens
resimpy_general -r umi_lens -rs umi+seq -perm_num 3 -umiup 1 -umiul 10 -umi_num 50 -seq_len 20 -pcr_num 8 -pcr_err 0.0001 -seq_err 0.0001 -ampl_rate 0.85 -sim_thres 3 -spl_rate 1 -umi_lens 6;7;8;9;10;11;12 -out_dir ./
```

## Contact

Homepage: https://www.ndorms.ox.ac.uk/team/adam-cribbs  

<style>
  code {
    white-space : pre-wrap !important;
    word-break: break-word;
  }
</style>