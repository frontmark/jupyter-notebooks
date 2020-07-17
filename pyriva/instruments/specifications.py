# -*- coding: utf-8 -*-
# import numpy as np
import pyvacon.analytics as _analytics
from datetime import datetime as _datetime
from pyriva._converter import _add_converter
from typing import List as _List

InflationIndexForwardCurve = _add_converter(_analytics.InflationIndexForwardCurve)

ComboSpecification = _add_converter(_analytics.ComboSpecification)
# Equity/FX
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

# Interest Rates
IrSwapLegSpecification = _add_converter(_analytics.IrSwapLegSpecification)
IrFixedLegSpecification = _add_converter(_analytics.IrFixedLegSpecification)
IrFloatLegSpecification = _add_converter(_analytics.IrFloatLegSpecification)
InterestRateSwapSpecification = _add_converter(_analytics.InterestRateSwapSpecification)
InterestRateBasisSwapSpecification = _add_converter(_analytics.InterestRateBasisSwapSpecification)
DepositSpecification = _add_converter(_analytics.DepositSpecification)
InterestRateFutureSpecification = _add_converter(_analytics.InterestRateFutureSpecification)

# Bonds/Credit
CouponDescription = _add_converter(_analytics.CouponDescription)
BondSpecification = _add_converter(_analytics.BondSpecification)


def ZeroBondSpecification(obj_id: str, curr: str, issue_date: _datetime, expiry: _datetime,
                          notional: float = 100.0, issuer: str = 'dummy_issuer', sec_level: str = 'NONE'
                          ) -> BondSpecification:
    """ Specifies zero coupon bonds by a minimal set of required information. The specification feeds into
    pyvacon.analytics' general BondSpecification. A more extensive zero bond specification also allows for
    the definition of issuer and securitization level.

    Args:
        obj_id (str): Unique zero bond identifier.
        curr (str): Zero bond's currency (ISO 4217).
        issue_date (_datetime): Zero bond's issue date.
        expiry (_datetime): Zero bond's maturity date.
        notional (float, optional): Zero bond's face value. Defaults to 100.0.
        issuer (str, optional): Issuer of the zero bond. Defaults to 'dummy_issuer'.
        sec_level (str, optional): Zero bond's securitization level. Defaults to 'NONE'.

    Returns:
        BondSpecification: The general bond specification for pyvacon including all relevant parameters for
        the zero bond specification based on the function's arguments.
    """
    return BondSpecification(obj_id, issuer, sec_level, curr, expiry, issue_date, notional, 'ACT365FIXED',
                             [], [], '', [], [])


def FixedRateBondSpecification(obj_id: str, curr: str, issue_date: _datetime, expiry: _datetime,
                               coupon_dates: _List[_datetime], coupons: _List[float], notional: float = 100.0,
                               day_count: str = 'ACT365FIXED', issuer: str = 'dummy_issuer',
                               sec_level: str = 'NONE') -> BondSpecification:
    """ Specifies fixed rate bond by minimal set of required information. The specification feeds into
    pyvacon.analytics' general BondSpecification. A more extensive fixed rate bond specification also allows
    for the definition of issuer and securitization level.

    Args:
        obj_id (str): Unique fixed rate bond identifier.
        curr (str): Fixed rate bond's currency (ISO 4217).
        issue_date (_datetime): Fixed rate bond's issue date.
        expiry (_datetime): Fixed rate bond's maturity date.
        coupon_dates (_List[_datetime]): List of coupon payment dates.
        coupons (_List[float]): List of annualized rates of each coupon.
        notional (float, optional): Fixed rate bond's face value. Defaults to 100.0.
        day_count (_datetime, optional): Day count convention method for coupon period length calculation.
        Defaults to 'ACT365FIXED'.
        issuer (str, optional): Issuer of the fixed rate bond. Defaults to 'dummy_issuer'.
        sec_level (str, optional): Fixed rate bond's securitization level. Defaults to 'NONE'.

    Returns:
        BondSpecification: The general bond specification for pyvacon including all relevant parameters for
        the fixed rate bond specification based on the function's arguments.
    """
    return BondSpecification(obj_id, issuer, sec_level, curr, expiry, issue_date, notional, day_count,
                             coupon_dates, coupons, '', [], [])


def FloatingRateNoteSpecification(obj_id: str, curr: str, issue_date: _datetime, expiry: _datetime,
                                  coupon_periods: _List[_datetime], spreads: _List[float],
                                  reference_index: str = '', notional: float = 100.0,
                                  day_count: str = 'ACT365FIXED', issuer: str = 'dummy_issuer',
                                  sec_level: str = 'NONE') -> BondSpecification:
    """ Specifies floating rate note by minimal set of required information. The specification feeds into
    pyvacon.analytics' general BondSpecification. A more extensive floating rate bond specification also
    allows for the definition of issuer and securitization level.

    Args:
        obj_id (str): Unique floating rate note identifier.
        curr (str): Floating rate note's currency (ISO 4217).
        issue_date (_datetime): Floating rate note's issue date.
        expiry (_datetime): Floating rate note's maturity date.
        coupon_periods (_List[_datetime]: Accrual periods (start and end dates) for floating rate coupons.
        spreads (_List[_datetime]): Add-on on top of floating rate determined by fixing of reference index.
        reference_index (str, optional): Underlying of floating rate coupon rates. Defaults to ''.
        notional (float, optional): Floating rate note's face value. Defaults to 100.0.
        day_count (_datetime, optional): Day count convention method for coupon period length calculation.
        Defaults to 'ACT365FIXED'.
        issuer (str, optional): Issuer of the floating rate note. Defaults to 'dummy_issuer'.
        sec_level (str, optional): Fixed floating note's securitization level. Defaults to 'NONE'.

    Returns:
        BondSpecification: The general bond specification for pyvacon including all relevant parameters for
        the floating rate bond specification based on the function's arguments.
    """
    return BondSpecification(obj_id, issuer, sec_level, curr, expiry, issue_date, notional, day_count,
                             [], [], reference_index, coupon_periods, spreads)


def GeneralBondSpecification(obj_id: str, curr: str, issue_date: _datetime, expiry: _datetime,
                             coupon_dates: _List[_datetime], coupons: _List[float],
                             coupon_periods: _List[_datetime], spreads: _List[float],
                             reference_index: str = '', notional: float = 100.0,
                             day_count: str = 'ACT365FIXED', issuer: str = 'dummy_issuer',
                             sec_level: str = 'NONE') -> BondSpecification:
    """ Specifies bonds with both fixed and floating rate coupons by minimal set of required information. The
     specification feeds into pyvacon.analytics' general BondSpecification. A more extensive specification
     also allows for the definition of issuer and securitization level.


    Args:
        obj_id (str): Unique bond note identifier.
        curr (str): Bond's currency (ISO 4217).
        issue_date (_datetime): Bond's issue date.
        expiry (_datetime): Bond's maturity date.
        coupon_dates (_List[_datetime]): List of fixed coupon payment dates.
        coupons (_List[float]): List of annualized rates of each fixed coupon.
        coupon_periods (_List[_datetime]: Accrual periods (start and end dates) for floating rate coupons.
        spreads (_List[_datetime]): Add-on on top of floating rate determined by fixing of reference index.
        reference_index (str, optional): Underlying of floating rate coupon rates. Defaults to ''.
        notional (float, optional): Bonds's face value. Defaults to 100.0.
        day_count (_datetime, optional): Day count convention method for coupon period length calculation.
        Defaults to 'ACT365FIXED'.
        issuer (str, optional): Issuer of the bond. Defaults to 'dummy_issuer'.
        sec_level (str, optional): Bond's securitization level. Defaults to 'NONE'.

    Returns:
        BondSpecification: The general bond specification for pyvacon including all relevant parameters for
        the specificaiton of bonds with both fixed and floating rate coupons based on the function's
        arguments.
    """
    return BondSpecification(obj_id, issuer, sec_level, curr, expiry, issue_date, notional, day_count,
                             coupon_dates, coupons, reference_index, coupon_periods, spreads)


InflationLinkedBondSpecification = _add_converter(_analytics.InflationLinkedBondSpecification)
CallableBondSpecification = _add_converter(_analytics.CallableBondSpecification)

GasStorageSpecification = _add_converter(_analytics.GasStorageSpecification)

ScheduleSpecification = _add_converter(_analytics.ScheduleSpecification)

SpecificationManager = _add_converter(_analytics.SpecificationManager)

vectorCouponDescription = _analytics.vectorCouponDescription
vectorRainbowBarrierSpec = _analytics.vectorRainbowBarrierSpec
vectorRainbowUdlSpec = _analytics.vectorRainbowUdlSpec

# ProjectToCorrelation = _analytics.ProjectToCorrelation
