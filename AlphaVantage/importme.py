apikey='GOJKUKZEAK5QIOUW'
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key=apikey,output_format='pandas')