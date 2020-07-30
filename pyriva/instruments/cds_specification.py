from datetime import datetime
from typing import List

class CDSSpecification:
    def __init__(self,  premium: float, premium_start_date: datetime, premium_pay_dates: List[datetime], notional: float = 1.0, expiry: datetime=None, 
                recovery: float = None, issuer: str = '', cash_settled: bool = True):
        """Constructor for credit default swap

        Args:
            premium (float): The premium as fraction of notional paid at each premium date.
            premium_start_date (datetime): The first date from when th first premium is accrued.
            premium_pay_dates (List[datetime]): List of dates for premium payments.
            maturity (datetime, optional): [description]. Defaults to None.
            recovery (float, optional): The protection is only paid for the real loss (notional minus recovery). If recovery is not specified, it is assumed that  recovery as specified in contract. If no fixed recovery is specified[description]. Defaults to None.
            issuer (str, optional): [description]. Defaults to ''.
            cash_settled (bool, optional): Flag indicating o instrument is physical settled (the protection buyer )
        """
        self.expiry = expiry
        self.premium = premium
        self.premium_start_date = premium_start_date
        self.premium_pay_dates = premium_pay_dates
        self.notional = notional
        if expiry is None:
            self.expiry = premium_pay_dates[-1]
        self.recovery = recovery
        self.issuer = issuer
        self.cash_settled = cash_settled
        self.validate()

    def validate(self):
        """Some simple validation
        """
        if len(self.premium_pay_dates) == 0:
            raise Exception('Premium payment dates mut not be empty.')
        
        