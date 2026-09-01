# Acknowledgement: This file is based on the `__init__.py` file from the `cpsc375-classwork` repository 
# by Prof. Avery, which is licensed under the MIT License. The original file can be found at:
# https://github.com/ProfAvery/cpsc375-classwork/blob/main/cpsc375/__init__.py
#
# To import libraries and datasets into the global namespace:
#
#   from cpsc375 import *
#

import statsmodels.api as sm


iris_dataset = sm.datasets.get_rdataset("iris")
iris = iris_dataset.data

airquality_dataset = sm.datasets.get_rdataset("airquality")
airquality = airquality_dataset.data
