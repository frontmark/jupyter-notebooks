import pyvacon.version as version
import pyriva.enums as enums
from pyvacon.analytics import setLogLevel as set_log_level


from pyvacon.analytics import registerSerialization as _register_serialization
_register_serialization('depp')

import pyriva.instruments as instruments
import pyvacon.pricing as pricing
import pyvacon.marketdata as marketdata

if version.is_beta:
    import warnings
    warnings.warn('Imported pyvacon is just beta version.')
