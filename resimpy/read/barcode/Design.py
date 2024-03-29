__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "MIT"
__lab__ = "cribbslab"

from resimpy.read.umi.Library import library as liblogginger
from resimpy.read.inf.Pseudo import pseudo as seqpseudo


class design(seqpseudo):

    def __init__(self, *args, **kwargs):
        super(design, self).__init__(*args, **kwargs)
        self.args = args
        self.kwargs = kwargs

    @liblogginger(method='default')
    def general(self, **kwargs):
        return ''.join([
            self.kwargs['dna_map'][i] for i in
            self.kwargs['pseudorandom_num']
        ])

    @liblogginger(method='default')
    def reoccur(self, **kwargs):
        return ''.join([
            self.kwargs['dna_map'][i] * self.kwargs['umi_unit_pattern'] for i in
            self.kwargs['pseudorandom_num']
        ])

    @liblogginger(method='separate')
    def write(self, **kwargs):
        return 'written'