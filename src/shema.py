from pydantic import BaseModel

class MarketData(BaseModel):
    ticker: str
    period: str
    date: str
    time: str
    open: float
    high: float
    low: float
    close: float
    volume: int