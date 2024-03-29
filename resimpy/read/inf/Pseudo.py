__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "MIT"
__lab__ = "cribbslab"

from abc import ABCMeta, abstractmethod


class pseudo(metaclass=ABCMeta):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    @abstractmethod
    def general(self, **kwargs):
        return ''.join([
            self.kwargs['dna_map'][i] * self.kwargs['umi_unit_pattern'] for i in
            self.kwargs['pseudorandom_num']
        ])