# Resimpy
![](https://img.shields.io/badge/Resimpy-executable-519dd9.svg)
![](https://img.shields.io/badge/last_released-Jan._2022-green.svg)
![](https://img.shields.io/github/stars/cribbslab/resimpy?logo=GitHub&color=blue)
![](https://img.shields.io/pypi/v/resimpyx?logo=PyPI)
[![Documentation Status](https://readthedocs.org/projects/resimpy/badge/?version=latest)](https://resimpy.readthedocs.io/en/latest/?badge=latest)
[![Downloads](https://pepy.tech/badge/mclumi)](https://pepy.tech/project/mclumi)

###### tags: `ResimPy` `read simulation` `PCR amplification` `scRNA-seq` `bulkRNA-seq`


## Overview
```angular2html
 ____           _                         _____           _ _    _ _
|  _ \ ___  ___(_)_ __ ___  _ __  _   _  |_   _|__   ___ | | | _(_) |_
| |_) / _ \/ __| | '_ ` _ \| '_ \| | | |   | |/ _ \ / _ \| | |/ / | __|
|  _ <  __/\__ \ | | | | | | |_) | |_| |   | | (_) | (_) | |   <| | |_
|_| \_\___||___/_|_| |_| |_| .__/ \__, |   |_|\___/ \___/|_|_|\_\_|\__|
                           |_|    |___/
```
The **RE**ad **SIM**ulation **PY**thon program (ResimPy) provides an scalable interface for users via Python to simulate massive reads of varying sequencing technologies, in order to avoid the time-consuming nature of experimental trials. Simulated reads can have the UMI- barcode- primer-, or spacer-featured composition. ResimPy has been made avilable through the command-line interface (CLI) and Python-inline visits.

## Documentation
The Resimpy documentation is shown either along this README file below or https://resimpy.readthedocs.io/en/latest/index.html.

## Installation
There are two ways provided for installing the ResimPy package. It is in principle that ResimPy can be installed on an environment with the Python version of >3.6 but <3.10. We highly recommend installing the package  with Python 3.9.1. Other versions of Python above 3.9.1 will possibly cause conflicts between dependencies, such as NumPy will need a Cython compiler. 

1. Released via PyPI

    * step 1: create a conda environment, e.g., resimpy

        ```angular2html
        conda create --name resimpy python=3.9.1
        
        conda activate resimpy
        ```

    * step 2: sourced from https://pypi.org/project/resimpyx.
        ```angular2html
        pip install resimpyx==0.0.2
        ```

2. Released via an up-to-date GitHub package

    * step 1: create a conda environment

        ```angular2html
        conda create --name resimpy python=3.9.1
        
        conda activate resimpy
        ```

    * step 2: sourced from GitHub
        ```angular2html
        mkdir project
        
        cd project/
        
        git clone https://github.com/cribbslab/resimpy
        
        cd resimpy
        
        python setup.py install
        ```
        
You are supposed to be all set after going through either one step above. Now you can move on to testing the package and we post a few example commands below for you to reproduce the simulation results used in our paper https://www.biorxiv.org/content/10.1101/2023.04.06.535911v1. To do so, a single command with parameters is used. The vignette in **Overview** helps you understand what each parameter represents. You can also refer to https://resimpy.readthedocs.io/en/latest/tutorial/index.html for parameter illustration. Please note that anything you are meant to do should be done within the conda environment resimpy as created above.

## Usage and simulation result reproducibility
To reproduce the results used in https://www.biorxiv.org/content/10.1101/2023.04.06.535911v1, please follow the instruction below.

***Situation 1***. test the impact of differnt PCR error rates on quantification accuracy using ResimPy by varying the `pcr_errs` parameter while keeping other parameters by default. `pcr_errs` is a list of values while only one value is set as exclusive to `pcr_err`. When `pcr_errs` is used, you can mute `pcr_err` or not. The program will turn off the parameter `pcr_err` anyways. This will be set the same in other situations below. When a list of values are set, they must be separated by `;`, such as `-pcr_errs 1e-3;1e-2;0.1`.
```angular2html
resimpy_general -r pcr_errs -rs umi+seq -perm_num 3 -umiup 1 -umiul 10 -umi_num 50 -seq_len 20 -pcr_num 8 -pcr_err 0.0001 -seq_err 0.0001 -ampl_rate 0.85 -sim_thres 3 -spl_rate 1 -pcr_errs 1e-3;1e-2;0.1 -out_dir ./
```

***Situation 2***. test the impact of differnt PCR amplification rates on quantification accuracy using ResimPy by varying the ampl_rates parameter while keeping other parameters by default.
```angular2html
resimpy_general -r ampl_rates -rs umi+seq -perm_num 3 -umiup 1 -umiul 10 -umi_num 50 -seq_len 20 -pcr_num 8 -pcr_err 0.0001 -seq_err 0.0001 -ampl_rate 0.85 -sim_thres 3 -spl_rate 1 -ampl_rates 0.1;0.2;0.3;0.4;0.5;0.6;0.7;0.8;0.9;1.0 -out_dir ./
```

***Situation 3***. test the impact of differnt PCR cycles on quantification accuracy using ResimPy by varying the pcr_nums parameter while keeping other parameters by default.
```angular2html
# pcr_nums
resimpy_general -r pcr_nums -rs umi+seq -perm_num 3 -umiup 1 -umiul 10 -umi_num 50 -seq_len 20 -pcr_num 8 -pcr_err 0.0001 -seq_err 0.0001 -ampl_rate 0.85 -sim_thres 3 -spl_rate 1 -pcr_nums 6;7;8;9;10;11;12;13;14 -out_dir ./
```

***Situation 4***. test the impact of UMIs of different lengths on quantification accuracy using ResimPy by varying the umi_lens parameter while keeping other parameters by default.
```shell
# umi_lens
resimpy_general -r umi_lens -rs umi+seq -perm_num 3 -umiup 1 -umiul 10 -umi_num 50 -seq_len 20 -pcr_num 8 -pcr_err 0.0001 -seq_err 0.0001 -ampl_rate 0.85 -sim_thres 3 -spl_rate 1 -umi_lens 6;7;8;9;10;11;12 -out_dir ./
```

In fact, users are allowed to test more situations (e.g., sequencing error) beyond what is shown above by simply varying one parameter while keeping the rest of the parameters by default.


## Output
After running each of the commands above, the simulated reads represented by FastQ will be saved to your specified folder within which you can see a few folders like permutation_x. The number of the permutation folders is equal to the permutation number (--permutation_num) specified. A library of UMIs is saved to `umi.txt` by order and all genomic sequences are saved to `seq.txt` by order. If you set `-pcr_errs 1e-3;1e-2;0.1`, there are 3 FastQ files pcr_err_0.fastq.gz;pcr_err_1.fastq.gz;pcr_err_2.fastq.gz, where 0;1;2 correspond to 1e-3;1e-2;0.1.

## Parameter illustration
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

## Citation
Please cite our work if you use ResimPy in your research.
```javascript=
@article{homotrimerumibs,
    author = {Jianfeng Sun and Martin Philpott and Danson Loi and Shuang Li and Pablo Monteagudo-Mesas and Gabriela Hoffman and Jonathan Robson and Neelam Mehta and Vicki Gamble and Tom Brown, Jr and Tom Brown Sr and Stefan Canzar and Udo Oppermann and Adam P Cribbs},
	title = {Correcting PCR amplification errors in unique molecular identifiers to generate absolute numbers of sequencing molecules},
	year = {2023},
	doi = {10.1101/2023.04.06.535911},
	URL = {https://www.biorxiv.org/content/early/2023/04/06/2023.04.06.535911},
	journal = {bioRxiv}
}
```

## Contact
Developer: Jianfeng Sun, Cribbslab

Homepage: https://www.ndorms.ox.ac.uk/team/adam-cribbs  