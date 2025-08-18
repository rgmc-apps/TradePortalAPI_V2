from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String, Integer, Date, DateTime
import datetime

class StockPullOutRequest(SQLModel, table=True):
    brandid: int = Field(sa_column=Column("brandId", Integer, nullable=False))
    storeid: int = Field(sa_column=Column("storeId", Integer, primary_key=True))
    pulloutdate: datetime.date = Field(sa_column=Column("pullOutDate", Date, nullable=False))
    refnumber: str = Field(sa_column=Column("refNumber", String(50), primary_key=True))
    barcode: str = Field(sa_column=Column("barcode", String(20), primary_key=True))
    pulloutqty: int = Field(sa_column=Column("pullOutQty", Integer, nullable=False))
    requeststatus: str = Field(sa_column=Column("requestStatus", String(20), nullable=False), default="NEW")
    stockpulloutid: int = Field(sa_column=Column("stockPullOutId", Integer, nullable=False))
    createby: str = Field(sa_column=Column("createBy", String(50), nullable=False))
    createdate: datetime.datetime = Field(sa_column=Column("createDate", DateTime, nullable=False))
    updateby: str = Field(sa_column=Column("updateBy", String(50), nullable=False))
    updatedate: datetime.datetime = Field(sa_column=Column("updateDate", DateTime, nullable=False))