from datetime import datetime, time, timedelta
import numpy as np
from pyriva.instruments.cds_specification import CDSSpecification
from pyriva.marketdata import DiscountCurve, DatedCurve
from pyriva import enums, DayCounter
from pyriva.pricing import PricingResults


class CDSPricingData:
    def __init__(self, spec: CDSSpecification, val_date: datetime, discount_curve: DiscountCurve, 
                survival_curve: DiscountCurve, recovery_curve: DatedCurve=None):
        self.spec = spec
        self.val_date = val_date
        self.discount_curve = discount_curve
        self.survival_curve = survival_curve
        self.recovery_curve = recovery_curve
        self._pricer_type = 'ISDA'

    @staticmethod  
    def _pv_protection_leg(valuation_date: datetime, dc: DiscountCurve, spec: CDSSpecification, sc: DiscountCurve, rr_curve)->float:
        result=0
        n_timesteps_per_year = 12
        min_timesteps = 5
        dc_daycounter = DayCounter(dc.getDayCounterType())
        maturity = dc_daycounter.yf(valuation_date,spec.expiry)
        n_timesteps = np.minimum(int(maturity*n_timesteps_per_year), min_timesteps)
        times = np.linspace(0.0, maturity, num=n_timesteps)
        n_days_dist = 30
        times=[valuation_date + timedelta(days=i)]
        for i in range(1,len(times)):
            risk_adj_factor_protection = dc.value(valuation_date,times[i])*(sc.value(valuation_date,times[i-1], dc_daycounter)
                                                                            -sc.value(valuation_date,times[i], dc_daycounter))
            if spec.cash_settled or spec.recovery is None:
                risk_adj_factor_protection *= (1.0-rr_curve.value(valuation_date, 0.5*(times[i]+times[i-1], dc_daycounter)))
            else:
                risk_adj_factor_protection *= (1.0-spec.recovery)
            result += risk_adj_factor_protection
        return spec.notional*result

    @staticmethod  
    def _pv_premium_leg(valuation_date: datetime, dc: DiscountCurve, spec: CDSSpecification, sc: DiscountCurve):
        result=0
        prev_p = spec.premium_start_date
        dc_daycounter = DayCounter(dc.getDayCounterType())
        for p in spec.premium_pay_dates:
            if p < valuation_date:
                continue
            result += dc_daycounter.yf(prev_p, p)*spec.premium*dc.value(valuation_date, p)*sc.value(valuation_date, p)
        return spec.notional*result
        
    def price(self):
        protection_leg = CDSPricingData._pv_protection_leg(self.val_date, self.discount_curve, self.spec, self.survival_curve, self.recovery_curve)
        premium_leg = CDSPricingData._pv_premium_leg(self.val_date, self.discount_curve, self.spec, self.survival_curve)
        results = PricingResults()
        results.pv_protection_leg = protection_leg
        results.pv_premium_leg = premium_leg
        results.getPrice = lambda: protection_leg-premium_leg
