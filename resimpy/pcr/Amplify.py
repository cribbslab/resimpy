__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "MIT"
__lab__ = "cribbslab"

from resimpy.util.random.Ordering import ordering as ranord
from resimpy.util.random.Sampling import sampling as ranspl
from resimpy.util.random.Number import number as rannum
from resimpy.pcr.Error import error as pcrerr


class amplify(object):

    def __init__(self, pcr_params):
        self.pcr_params = pcr_params

    def np(self, ):
        for ipcr in range(self.pcr_params['pcr_num']):
            print('===>at PCR {}'.format(ipcr + 1))
            self.pcr_params['ipcr'] = ipcr
            self.pcr_params = self.flow(params=self.pcr_params)
            # print(std_flow_params.keys())
        return self.pcr_params

    @pcrerr(method='default')
    @ranspl(method='uniform')
    @rannum(type='binomial')
    @ranord(method='uniform')
    def flow(self, params):
        return params