# -*- coding: utf-8 -*-
#import numpy as np
import pyvacon.analytics as _analytics
from datetime import datetime as _datetime
from pyriva._converter import _add_converter

InflationIndexForwardCurve = _add_converter(_analytics.InflationIndexForwardCurve)

ComboSpecification = _add_converter(_analytics.ComboSpecification)
#Equity/FX
PayoffStructure = _add_converter(_analytics.PayoffStructure)
ExerciseSchedule = _add_converter(_analytics.ExerciseSchedule)
BarrierDefinition = _add_converter(_analytics.BarrierDefinition)
BarrierSchedule = _add_converter(_analytics.BarrierSchedule)
BarrierPayoff = _add_converter(_analytics.BarrierPayoff)
BarrierSpecification = _add_converter(_analytics.BarrierSpecification)
EuropeanVanillaSpecification = _add_converter(_analytics.EuropeanVanillaSpecification)
AmericanVanillaSpecification = _add_converter(_analytics.AmericanVanillaSpecification)
RainbowUnderlyingSpec = _add_converter(_analytics.RainbowUnderlyingSpec)
RainbowBarrierSpec = _add_converter(_analytics.RainbowBarrierSpec)
LocalVolMonteCarloSpecification = _add_converter(_analytics.LocalVolMonteCarloSpecification)
RainbowSpecification = _add_converter(_analytics.RainbowSpecification)
MultiMemoryExpressSpecification = _add_converter(_analytics.MultiMemoryExpressSpecification)
MemoryExpressSpecification = _add_converter(_analytics.MemoryExpressSpecification)
ExpressPlusSpecification = _add_converter(_analytics.ExpressPlusSpecification)
AsianVanillaSpecification = _add_converter(_analytics.AsianVanillaSpecification)
RiskControlStrategy = _add_converter(_analytics.RiskControlStrategy)
AsianRiskControlSpecification = _add_converter(_analytics.AsianRiskControlSpecification)


#Interest Rates
IrSwapLegSpecification = _add_converter(_analytics.IrSwapLegSpecification)
IrFixedLegSpecification = _add_converter(_analytics.IrFixedLegSpecification)
IrFloatLegSpecification = _add_converter(_analytics.IrFloatLegSpecification)
InterestRateSwapSpecification = _add_converter(_analytics.InterestRateSwapSpecification)
InterestRateBasisSwapSpecification = _add_converter(_analytics.InterestRateBasisSwapSpecification)
DepositSpecification = _add_converter(_analytics.DepositSpecification)
InterestRateFutureSpecification = _add_converter(_analytics.InterestRateFutureSpecification)



#Bonds/Credit
CouponDescription = _add_converter(_analytics.CouponDescription)
BondSpecification = _add_converter(_analytics.BondSpecification)

def ZeroBondSpecification(obj_id: str, curr: str,  issue_date: _datetime, expiry: _datetime, notional: float = 100.0, 
                        issuer: str = 'dummy_issuer', sec_level: str='NONE')->BondSpecification:
    """[summary]

    Args:
        obj_id (str): [description]
        curr (str): [description]
        issue_date (_datetime): [description]
        expiry (_datetime): [description]
        notional (float, optional): [description]. Defaults to 100.0.
        issuer (str, optional): [description]. Defaults to 'dummy_issuer'.
        sec_level (str, optional): [description]. Defaults to 'NONE'.

    Returns:
        BondSpecification: [description]
    """
    return BondSpecification(obj_id, issuer, sec_level, curr, expiry, issue_date, notional, 'ACT365FIXED', [], [], '', [], [])


InflationLinkedBondSpecification = _add_converter(_analytics.InflationLinkedBondSpecification)
CallableBondSpecification = _add_converter(_analytics.CallableBondSpecification)

GasStorageSpecification = _add_converter(_analytics.GasStorageSpecification)

ScheduleSpecification = _add_converter(_analytics.ScheduleSpecification)

SpecificationManager = _add_converter(_analytics.SpecificationManager)

vectorCouponDescription = _analytics.vectorCouponDescription
vectorRainbowBarrierSpec = _analytics.vectorRainbowBarrierSpec
vectorRainbowUdlSpec = _analytics.vectorRainbowUdlSpec

#ProjectToCorrelation = _analytics.ProjectToCorrelation

