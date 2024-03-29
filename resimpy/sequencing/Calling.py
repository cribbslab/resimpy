__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "MIT"
__lab__ = "cribbslab"

from resimpy.sequencing.Error import error as seqerr
from resimpy.util.random.Sampling import sampling as ranspl


class calling(object):

    def __init__(self, seq_params):
        self.seq_params = seq_params

    def np(self, ):
        self.seq_params['spl_num'] = int(self.seq_params['data'].shape[0] * self.seq_params['seq_sub_spl_rate'])
        res_flow = self.flow(params=self.seq_params)
        # print(res_flow)
        return res_flow

    @seqerr(method='default')
    @ranspl(method='uniform')
    def flow(self, params):
        return params