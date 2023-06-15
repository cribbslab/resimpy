__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "MIT"
__lab__ = "cribbslab"

import os


class folder(object):

    def __init__(self, ):
        pass

    def osmkdir(self, DIRECTORY):
        if not os.path.exists(DIRECTORY):
            os.makedirs(DIRECTORY)
        return 0
