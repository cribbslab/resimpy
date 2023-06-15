__version__ = "v1.0"
__copyright__ = "Copyright 2023"
__license__ = "MIT"
__lab__ = "cribbslab"


class hamming(object):

    def __init__(self, ):
        pass

    def general(self, s1, s2):
        return sum(i != j for i, j in zip(s1, s2))