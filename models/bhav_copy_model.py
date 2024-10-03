import uuid

from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import DeclarativeBase


class BhavCopyModel(DeclarativeBase):
    __tablename__ = "bhav_data"

    id = Column(Integer, primary_key=True, default=uuid.uuid4())
    trade_date = Column(String)
    business_date = Column(String)
    segment = Column(String)
    source = Column(String)
    financial_instrument_type = Column(String)
    financial_instrument_id = Column(Integer)
    ticker_symbol = Column(String)
    expiry_date = Column(Date)
    actual_expiry_date = Column(Date)
    strike_price = Column(Integer)
    option_type = Column(String)
    financial_instrument_name = Column(String)
    open_price = Column(Float)
    high_price = Column(Float)
    low_price = Column(Float)
    close_price = Column(Float)
    last_price = Column(Float)
    previous_closing_price = Column(Float)
    underlying_price = Column(Float)
    settlement_price = Column(Float)
    open_interest = Column(Integer)
    change_in_open_interest = Column(Integer)
    total_trading_volume = Column(Integer)
    total_traded_value = Column(Integer)
    total_number_of_transactions_executed = Column(Integer)
    session_id = Column(Integer)
    new_board_lot_quantity = Column(Integer)
