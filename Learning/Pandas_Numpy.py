import pandas as pd
import numpy as np
from pandas import DataFrame, Series
series_obj=Series(np.arange(8), index =['row1','row2','row3','row4','row5','row6','row7','row8'])
series_obj
series_obj[[0,7]]=10
series_obj