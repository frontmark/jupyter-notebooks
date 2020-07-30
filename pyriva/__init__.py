import pyvacon.version as version
from pyvacon.analytics import DayCounter
from pyvacon.analytics import setLogLevel as set_log_level
from pyvacon.analytics import registerSerialization as _register_serialization

import pyriva.marketdata as marketdata
import pyriva.instruments as instruments
import pyriva.pricing as pricing

_register_serialization('depp')

if version.is_beta:
    import warnings
    warnings.warn('Imported pyvacon is just beta version.')
