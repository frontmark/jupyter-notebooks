# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 17:51:16 2016

@author: oeltz
"""

class DBUdl:
    DAX = '4517'
    STOXX50E = '2676'
    BASF = '123'
    APPLE = '91'
    EON = '48'
    EXXON = '1'
    DOWJOWNS = '4612' 
    SPX= '13'
    NASDAX = '17'
    ADS = '600' #ADIDAS
    ALV = '66' # Allianz
    BASF = '123'
    BAYER = '150'
    BEIERSDORF = '1356'
    BMW = '374'
    COMMERZBANK = '273'
    CONTINENTAL = '428'
    DAIMLER = '109'
    DBK = '80'
    DEUTSCHE_BOERSE = '414'
    DB11 = '20261'
    DEUTSCHE_POST = '314'
    DTE = '113'
    EON = '48'
    FRESENIUS = '14880'
    FRESENIUS_MEDICAL_CARE = '748'
    HEIDELBER_CEMENT = '1578'
    HENKEL = '797'
    INFINEON = '697'
    LINDE = '665'
    LUFTHANSA = '1117'
    MERCK = '1073'
    MUV = '180'
    PRO_SIEBEN = '1539'
    RWE = '129'
    SAP = '131'
    SIEMENS = '61'
    THYSSEN = '439'
    VW = '4623'
    VONOVIA = '18078'
    DAX_list = {'DAX':DAX,
                        'ADS':ADS, 'ALV':ALV, 'BASF':BASF, 
                        'BAYER':BAYER, 'BEIERSDORF':BEIERSDORF, 
                        'BMW':BMW, 'COMMERZBANK':COMMERZBANK, 'CONTINENTAL':CONTINENTAL, 
                        'DAIMLER':DAIMLER,  'DBK':DBK, 'DEUTSCHE_BOERSE':DEUTSCHE_BOERSE,
                        'DB11': DB11,
                        'DEUTSCHE_POST':DEUTSCHE_POST, 'DTE':DTE, 'EON':EON, 'FRESENIUS':FRESENIUS,
                         'FRESENIUS_MEDICAL_CARE':FRESENIUS_MEDICAL_CARE, 'HEIDELBER_CEMENT':HEIDELBER_CEMENT, 
                         'HENKEL':HENKEL, 'INFINEON':INFINEON, 'LINDE':LINDE, 'LUFTHANSA':LUFTHANSA,
                        'MERCK':MERCK, 'MUV':MUV, 'PRO_SIEBEN':PRO_SIEBEN, 'RWE':RWE, 'SAP':SAP,  
                        'SIEMENS':SIEMENS, 'THYSSEN':THYSSEN, 'VW': VW, 'VONOVIA':VONOVIA}

class InterpolationType:
    CONSTANT = "CONSTANT"
    LINEAR = "LINEAR"
    LINEARLOG = "LINEARLOG"
    CONSTRAINED_SPLINE = "CONSTRAINED_SPLINE"
    HAGAN = "HAGAN"
    HAGAN_DF = "HAGAN_DF"

class ExtrapolationType:
    NONE = "NONE"
    CONSTANT = "CONSTANT"
    LINEAR = "LINEAR"
    LINEARLOG = "LINEARLOG"

class SecuritizationLevel:
    NONE = 'NONE'
    COLLATERALIZED = 'COLLATERALIZED' #,,,'','SUBORDINATED','MEZZANINE','EQUITY']
    SENIOR_SECURED = 'SENIOR_SECURED'
    SENIOR_UNSECURED = 'SENIOR_UNSECURED'
    SUBORDINATED = 'SUBORDINATED'
    MEZZANINE = 'MEZZANINE'
    EQUITY = 'EQUITY'


class ProductType:
       BOND = 'BOND'
       CALLABLE_BOND = 'CALLABLE_BOND'
       
       
class PricerType:
    ANALYTIC = 'ANALYTIC'
    PDE = 'PDE'
    MONTE_CARLO = 'MONTE_CARLO'
    COMBO = 'COMBO'
    
       
class Model:
    BLACK76 = 'BLACK76'
    CIR ='CIR'
    HULL_WHITE = 'HULL_WHITE'
    HESTON = 'HESTON'
    LV = 'LV'
    GBM = 'GBM'
    G2PP = 'G2PP'
    VASICEK = 'VASICEK'
    
class Period:
    A = 'A'
    SA = 'SA'
    Q = 'Q'
    M = 'M'
    D = 'D'
    
class RollConvention:
    FOLLOWING = 'Following'
    MODIFIED_FOLLOWING = 'ModifiedFollowing'
    MODIFIED_FOLLOWING_EOM = 'ModifiedFollowingEOM'
    PRECEDING = 'Preceding'
    MODIFIED_PRECEDING = 'ModifiedPreceding'
    UNADJUSTED = 'Unadjusted'
    
class DayCounter:
    ACTACT = 'ActAct'
    ACT365_FIXED = 'ACT365FIXED'
    ACT360 = 'Act360'
    ThirtyU360 = '30U360'
    ThirtyE360 = '30E360'
    ACT252 = 'Act252'

class VolatilityStickyness:
    NONE = 'NONE'
    StickyStrike = 'StickyStrike'
    StickyXStrike = 'StickyXStrike'
    StickyFwdMoneyness = 'StickyFwdMoneyness'

class InflationInterpolation:
    UNDEFINED = 'UNDEFINED'
    GERMAN = 'GERMAN'
    JAPAN = 'JAPAN'
    CONSTANT = 'CONSTANT'
