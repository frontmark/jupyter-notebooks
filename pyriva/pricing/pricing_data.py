from datetime import datetime


class CDSPricingData:
    def __init__(self, spec, val_date, discount_curve, survival_curve, recovery_curve=None):
        self.spec = spec
        self.val_date = val_date
        self.discount_curve = discount_curve
        self.survival_curve = survival_curve
        self.recovery_curve = recovery_curve
        self._pricer_type = 'ISDA'
        
    def price(self):
        pass