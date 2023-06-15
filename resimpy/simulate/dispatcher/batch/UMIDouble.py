__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "MIT"
__lab__ = "cribbslab"

import argparse
from resimpy.simulate.dispatcher.single.UMIDouble import umiDouble as simugeneral


class umiDouble(object):

    def __init__(self,
                 mode,
                 transloc_rate=0.02,
                 permutation_num=10,
                 umi_unit_pattern=1,
                 umi_unit_len_fixed=10,
                 umi_num_fixed=50,
                 pcr_num_fixed=10,
                 pcr_err_fixed=1e-3,
                 seq_err_fixed=1e-3,
                 ampl_rate_fixed=0.85,
                 sim_thres_fixed=3,
                 seq_sub_spl_rate=1,
                 ampl_rates=None,
                 umi_unit_lens=None,
                 pcr_nums=None,
                 pcr_errs=None,
                 seq_errs=None,
                 sv_fp='./',
                 ):
        if mode == 'internal':
            self.permutation_num = permutation_num
            self.transloc_rate = transloc_rate
            self.umi_unit_len_fixed = umi_unit_len_fixed
            self.umi_num_fixed = umi_num_fixed
            self.umi_unit_pattern = umi_unit_pattern
            self.pcr_num_fixed = pcr_num_fixed
            self.pcr_err_fixed = pcr_err_fixed
            self.seq_err_fixed = seq_err_fixed
            self.ampl_rate_fixed = ampl_rate_fixed
            self.sim_thres_fixed = sim_thres_fixed
            self.seq_sub_spl_rate = seq_sub_spl_rate
            self.ampl_rates = ampl_rates
            self.umi_unit_lens = umi_unit_lens
            self.pcr_nums = pcr_nums
            self.pcr_errs = pcr_errs
            self.seq_errs = seq_errs
            self.sv_fp = sv_fp
            print('run resimpy internally.')
        else:
            self.parser = argparse.ArgumentParser(
                description='Welcome to the resimpy_umi_transloc module'
            )
            self.parser.add_argument(
                "--recipe", "-r",
                metavar='recipe',
                dest='r',
                required=True,
                type=str,
                help='which condition among seq_errs, ampl_rates, pcr_errs, pcr_nums, and umi_lens is used',
            )
            self.parser.add_argument(
                "--transloc_rate", "-tr",
                metavar='transloc_rate',
                dest='tr',
                default=0.02,
                type=float,
                help='translocation rate',
            )
            self.parser.add_argument(
                "--read_structure", "-rs",
                metavar='read_structure',
                dest='rs',
                required=True,
                type=str,
                help='read structure consisting of a UMI block (umi) and a sequence block (seq), e.g., umi or umi+seq',
            )
            self.parser.add_argument(
                "--permutation_num", "-perm_num",
                metavar='permutation_num',
                dest='perm_num',
                required=True,
                type=int,
                help='permutation test number',
            )
            self.parser.add_argument(
                "--umi_unit_pattern", "-umiup",
                metavar='umi_unit_pattern',
                dest='umiup',
                default=1,
                type=int,
                help='unit UMI pattern. This is to specify if UMIs consist of monomer, dimer, trimer, or other blocks',
            )
            self.parser.add_argument(
                "--umi_unit_len_fixed", "-umiul",
                metavar='umi_unit_len_fixed',
                dest='umiul',
                default=10,
                type=int,
                help='unit UMI length fixed. This is to specify the length of a monomer UMI. The final UMI length = umi_unit_pattern * umi_unit_len_fixed',
            )
            self.parser.add_argument(
                "--umi_num_fixed", "-umi_num",
                metavar='umi_num_fixed',
                dest='umi_num',
                default=50,
                type=int,
                help='UMI number',
            )
            self.parser.add_argument(
                "--sim_thres_fixed", "-sim_thres",
                metavar='sim_thres_fixed',
                dest='sim_thres',
                default=3,
                type=int,
                help='edit distance-measured similarities between UMIs',
            )
            self.parser.add_argument(
                "--pcr_num_fixed", "-pcr_num",
                metavar='pcr_num_fixed',
                dest='pcr_num',
                default=8,
                type=int,
                help='Number of PCR cycles fixed',
            )
            self.parser.add_argument(
                "--ampl_rate_fixed", "-ampl_rate",
                metavar='ampl_rate_fixed',
                dest='ampl_rate',
                default=0.85,
                type=float,
                help='PCR amplification rate fixed',
            )
            self.parser.add_argument(
                "--seq_sub_spl_rate", "-spl_rate",
                metavar='seq_sub_spl_rate',
                dest='spl_rate',
                default=1.0,
                type=float,
                help='Subsampling rate for sequencing',
            )
            self.parser.add_argument(
                "--pcr_err_fixed", "-pcr_err",
                metavar='pcr_err_fixed',
                dest='pcr_err',
                default=0.001,
                type=float,
                help='PCR error fixed',
            )
            self.parser.add_argument(
                "--seq_err_fixed", "-seq_err",
                metavar='seq_err_fixed',
                dest='seq_err',
                default=0.001,
                type=float,
                help='Sequencing error fixed',
            )
            self.parser.add_argument(
                "--ampl_set_rates", "-ampl_rates",
                metavar='ampl_set_rates',
                dest='ampl_rates',
                default='0.1;0.2;0.3;0.4;0.5;0.6;0.7;0.8;0.9;1.0',
                type=str,
                help='a semicolon-partitioned string of a set of amplification rates',
            )
            self.parser.add_argument(
                "--umi_unit_set_lens", "-umi_lens",
                metavar='umi_unit_set_lens',
                dest='umi_lens',
                default='6;7;8;9;10;11;12',
                type=str,
                help='a semicolon-partitioned string of a set of unit UMI lens',
            )
            self.parser.add_argument(
                "--pcr_set_nums", "-pcr_nums",
                metavar='pcr_set_nums',
                dest='pcr_nums',
                default='6;7;8;9;10;11;12;13;14',
                type=str,
                help='a semicolon-partitioned string of a set of PCR numbers',
            )
            self.parser.add_argument(
                "--pcr_set_errs", "-pcr_errs",
                metavar='pcr_set_errs',
                dest='pcr_errs',
                default='1e-4;1e-3;1e-2;0.1',
                type=str,
                help='a semicolon-partitioned string of a set of PCR errors',
            )
            self.parser.add_argument(
                "--seq_set_errs", "-seq_errs",
                metavar='seq_set_errs',
                dest='seq_errs',
                default='1e-3;1e-2;0.1',
                type=str,
                help='a semicolon-partitioned string of a set of sequencing errors',
            )
            self.parser.add_argument(
                "--out_directory", "-out_dir",
                metavar='out_directory',
                dest='out_dir',
                default='./',
                type=str,
                help='output directory',
            )
            args = self.parser.parse_args()
            self.recipe = args.r
            self.transloc_rate = args.tr
            self.read_structure = args.rs
            self.permutation_num = args.perm_num
            self.umi_unit_pattern = args.umiup
            self.umi_unit_len_fixed = args.umiul
            self.umi_num_fixed = args.umi_num
            self.pcr_num_fixed = args.pcr_num
            self.pcr_err_fixed = args.pcr_err
            self.seq_err_fixed = args.seq_err
            self.ampl_rate_fixed = args.ampl_rate
            self.sim_thres_fixed = args.sim_thres
            self.seq_sub_spl_rate = args.spl_rate
            self.ampl_rates = args.ampl_rates
            self.umi_unit_lens = args.umi_lens
            self.pcr_nums = args.pcr_nums
            self.pcr_errs = args.pcr_errs
            self.seq_errs = args.seq_errs
            self.sv_fp = args.out_dir

        self.seq_errs = [float(i) for i in self.seq_errs.split(';')]
        self.pcr_errs = [float(i) for i in self.pcr_errs.split(';')]
        self.pcr_nums = [int(i) for i in self.pcr_nums.split(';')]
        self.umi_unit_lens = [int(i) for i in self.umi_unit_lens.split(';')]
        self.ampl_rates = [float(i) for i in self.ampl_rates.split(';')]
        self.read_structure = [str(i) for i in self.read_structure.split('+')]
        print(self.seq_errs)
        print(self.pcr_errs)
        print(self.pcr_nums)
        print(self.umi_unit_lens)
        print(self.ampl_rates)

    def pcrNums(self, ):
        for pn in range(self.permutation_num):
            simu_params = {
                'init_seq_setting': {
                    'seq_num': self.umi_num_fixed,
                    'umi_unit_pattern': self.umi_unit_pattern,
                    'umi_unit_len': self.umi_unit_len_fixed,
                    # 'seq_len': self.seq_len,
                    'is_seed': True,
                    'working_dir': self.sv_fp + '/permute_' + str(pn) + '/',
                    'is_sv_umi_lib': True,
                    'umi_lib_fpn': self.sv_fp + '/permute_' + str(pn) + '/umi.txt',
                    # 'is_sv_seq_lib': True if 'seq' in self.read_structure else False,
                    # 'seq_lib_fpn': self.sv_fp + '/permute_' + str(pn) + '/seq.txt',
                    'condis': self.read_structure,
                    'sim_thres': self.sim_thres_fixed,
                    'permutation': pn,
                },
                'transloc_rate': self.transloc_rate,
                'ampl_rate': self.ampl_rate_fixed,
                'pcr_nums': self.pcr_nums,
                'err_num_met': 'nbinomial',
                'pcr_error': self.pcr_err_fixed,
                'seq_error': self.seq_err_fixed,
                'seq_sub_spl_rate': self.seq_sub_spl_rate,
                'use_seed': False,
                'seed': None,
                'write': {
                    'fastq_fp': self.sv_fp + '/permute_' + str(pn) + '/',
                    'fastq_fn': '',
                }
            }
            p = simugeneral(simu_params)
            print(p.ondemandPCRNums())
        return

    def pcrErrs(self, ):
        for pn in range(self.permutation_num):
            simu_params = {
                'init_seq_setting': {
                    'seq_num': self.umi_num_fixed,
                    'umi_unit_pattern': self.umi_unit_pattern,
                    'umi_unit_len': self.umi_unit_len_fixed,
                    # 'seq_len': self.seq_len,
                    'is_seed': True,
                    # ### /*** block. general ***/
                    # 'working_dir': to('data/simu/monomer/general/1/pcr_err/permute_') + str(pn) + '/',
                    # 'is_sv_umi_lib': True,
                    # 'umi_lib_fpn': to('data/simu/monomer/general/1/pcr_err/permute_') + str(pn) + '/umi.txt',

                    # # ### /*** block. dimer ***/
                    # 'working_dir': to('data/simu/dimer/pcr_err/permute_') + str(pn) + '/',
                    # 'is_sv_umi_lib': True,
                    # 'umi_lib_fpn': to('data/simu/dimer/pcr_err/permute_') + str(pn) + '/umi.txt',

                    # ### /*** block. trimer ***/
                    'working_dir': self.sv_fp + '/permute_' + str(pn) + '/',
                    'is_sv_umi_lib': True,
                    'umi_lib_fpn': self.sv_fp + '/permute_' + str(pn) + '/umi.txt',

                    # 'is_sv_seq_lib': True if 'seq' in self.read_structure else False,
                    # 'seq_lib_fpn': self.sv_fp + '/permute_' + str(pn) + '/seq.txt',
                    'condis': self.read_structure,
                    'sim_thres': self.sim_thres_fixed,
                    'permutation': pn,
                },
                'transloc_rate': self.transloc_rate,
                'ampl_rate': self.ampl_rate_fixed,
                'pcr_num': self.pcr_num_fixed,
                'err_num_met': 'nbinomial',
                'pcr_errors': self.pcr_errs,
                'seq_error': self.seq_err_fixed,
                'seq_sub_spl_rate': self.seq_sub_spl_rate,
                'use_seed': False,
                'seed': None,
                'write': {
                    'fastq_fp': self.sv_fp + '/permute_' + str(pn) + '/',
                    'fastq_fn': '',
                }
            }
            p = simugeneral(simu_params)
            print(p.ondemandPCRErrs())
        return

    def seqErrs(self, ):
        for pn in range(self.permutation_num):
            simu_params = {
                'init_seq_setting': {
                    'seq_num': self.umi_num_fixed,
                    'umi_unit_pattern': self.umi_unit_pattern,
                    'umi_unit_len': self.umi_unit_len_fixed,
                    # 'seq_len': self.seq_len,
                    'is_seed': True,

                    'working_dir': self.sv_fp + '/permute_' + str(pn) + '/',
                    'is_sv_umi_lib': True,
                    'umi_lib_fpn': self.sv_fp + '/permute_' + str(pn) + '/umi.txt',

                    # 'is_sv_seq_lib': True if 'seq' in self.read_structure else False,
                    # 'seq_lib_fpn': self.sv_fp + '/permute_' + str(pn) + '/seq.txt',
                    'condis': self.read_structure,
                    'sim_thres': self.sim_thres_fixed,
                    'permutation': pn,
                },
                'transloc_rate': self.transloc_rate,
                'ampl_rate': self.ampl_rate_fixed,
                'pcr_num': self.pcr_num_fixed,
                'err_num_met': 'nbinomial',
                'pcr_error': self.pcr_err_fixed,
                'seq_errors': self.seq_errs,
                'seq_sub_spl_rate': self.seq_sub_spl_rate,
                'use_seed': False,
                'seed': None,
                'write': {
                    'fastq_fp': self.sv_fp + '/permute_' + str(pn) + '/',
                    'fastq_fn': '',
                }
            }
            p = simugeneral(simu_params)
            print(p.ondemandSeqErrs())
        return

    def umiLens(self, ):
        for pn in range(self.permutation_num):
            simu_params = {
                'init_seq_setting': {
                    'seq_num': self.umi_num_fixed,
                    'umi_unit_pattern': self.umi_unit_pattern,
                    'umi_unit_lens': self.umi_unit_lens,
                    # 'seq_len': self.seq_len,
                    'is_seed': True,
                    'working_dir': self.sv_fp + '/permute_' + str(pn) + '/',
                    'is_sv_umi_lib': True,
                    'umi_lib_fp': self.sv_fp + '/permute_' + str(pn) + '/',
                    # 'is_sv_seq_lib': True if 'seq' in self.read_structure else False,
                    'seq_lib_fp': self.sv_fp + '/permute_' + str(pn) + '/',
                    'condis': self.read_structure,
                    'sim_thres': self.sim_thres_fixed,
                    'permutation': pn,
                },
                'transloc_rate': self.transloc_rate,
                'ampl_rate': self.ampl_rate_fixed,
                'pcr_num': self.pcr_num_fixed,
                'err_num_met': 'nbinomial',
                'pcr_error': self.pcr_err_fixed,
                'seq_error': self.seq_err_fixed,
                'seq_sub_spl_rate': self.seq_sub_spl_rate,
                'use_seed': False,
                'seed': None,
                'write': {
                    'fastq_fp': self.sv_fp + '/permute_' + str(pn) + '/',
                    'fastq_fn': '',
                }
            }
            p = simugeneral(simu_params)
            print(p.ondemandUMILens())
        return

    def amplRates(self, ):
        for pn in range(self.permutation_num):
            simu_params = {
                'init_seq_setting': {
                    'seq_num': self.umi_num_fixed,
                    'umi_unit_pattern': self.umi_unit_pattern,
                    'umi_unit_len': self.umi_unit_len_fixed,
                    # 'seq_len': self.seq_len,
                    'is_seed': True,
                    'working_dir': self.sv_fp + '/permute_' + str(pn) + '/',
                    'is_sv_umi_lib': True,
                    'umi_lib_fpn': self.sv_fp + '/permute_' + str(pn) + '/umi.txt',
                    # 'is_sv_seq_lib': True if 'seq' in self.read_structure else False,
                    # 'seq_lib_fpn': self.sv_fp + '/permute_' + str(pn) + '/seq.txt',
                    'condis': self.read_structure,
                    'sim_thres': self.sim_thres_fixed,
                    'permutation': pn,
                },
                'transloc_rate': self.transloc_rate,
                'ampl_rates': self.ampl_rates,
                'pcr_num': self.pcr_num_fixed,
                'err_num_met': 'nbinomial',
                'pcr_error': self.pcr_err_fixed,
                'seq_error': self.seq_err_fixed,
                'seq_sub_spl_rate': self.seq_sub_spl_rate,
                'use_seed': False,
                'seed': None,
                'write': {
                    'fastq_fp': self.sv_fp + '/permute_' + str(pn) + '/',
                    'fastq_fn': '',
                }
            }
            p = simugeneral(simu_params)
            print(p.ondemandAmplRates())
        return


def run():
    from pyfiglet import Figlet
    vignette1 = Figlet(font='standard')
    print(vignette1.renderText('Resimpy Toolkit'))
    vignette2 = Figlet(font='doom')
    print(vignette2.renderText('Welcome'))
    p = umiDouble(
        mode='external',
    )
    if p.recipe == 'seq_errs':
        p.seqErrs()
    elif p.recipe == 'pcr_errs':
        p.pcrErrs()
    elif p.recipe == 'pcr_nums':
        p.pcrNums()
    elif p.recipe == 'umi_lens':
        p.umiLens()
    elif p.recipe == 'ampl_rates':
        p.amplRates()
    return 'job is finished now'


if __name__ == "__main__":
    p = umiDouble(
        mode='internal',
        # mode='external',

        ampl_rates=None,
        umi_unit_lens=None,
        pcr_nums=None,
        pcr_errs=None,
        seq_errs='1e-3;1e-2;0.1',
    )

    # print(p.pcrNums())

    # print(p.pcrErrs())

    print(p.seqErrs())

    # print(p.umiLens())

    # print(p.amplRates())