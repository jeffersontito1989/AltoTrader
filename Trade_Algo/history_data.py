import pandas as pd

class history(object):
    def __init__(self, input):
        self.input = input
        self.time_series = []

    def import_history(self):
        path = self.input.asset1+self.input.asset2 +'_data'
        '''
        if self.input.asset1 == 'XETH':
            path = 'ETH_data/' + self.input.series_name
        elif self.input.asset1 == 'XXBT':
            path = 'BTC_data/' + self.input.series_name
            # und dann für andere Assets auch noch ...
        elif self.input.asset1 == 'XREP':
            path = ''
        '''
        __raw = pd.read_csv(path)
        self.time_series = pd.Series(__raw['Price'])

    def getRollingMean(self, __window):

        self.import_history()

        try:
            if type(self.time_series) != pd.core.series.Series:
                raise TypeError
        except TypeError:
            print('Zeitreihe muss im Format pd.Series sein!')

        __rolling_mean = self.time_series.rolling(__window).mean()
        return __rolling_mean
