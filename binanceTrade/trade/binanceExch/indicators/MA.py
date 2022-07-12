class MA(object):
    """
    Investopedia:    https://www.investopedia.com/terms/e/ema.asp

    EMA=Price(t)×k+EMA(y)×(1−k)

    where:
    t=today
    y=yesterday
    N=number of days in EMA
    k=sm÷(N+1)
    sm=2 // While there are many possible choices for the smoothing factor, the most common choice is 2
    """
    SMOOTHING_FACTOR = 2

    @classmethod
    def ema(cls, price, ema, period):
        k = cls.SMOOTHING_FACTOR / (period + 1)

        return price * k + ema * (1 - k)

    @staticmethod
    def ema_delta(ema_0, ema_1):

        return ema_0 / ema_1 - 1
