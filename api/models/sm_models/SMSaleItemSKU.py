from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String, Integer, Float, DateTime
from datetime import datetime

class SMSaleItemSKU(SQLModel, table=True):
    brandid: int = Field(default=-1, primary_key=True)
    subclasscode: str = Field(default="", primary_key=True)
    retailamount: float = Field(default=0, primary_key=True)

    smstockcode: str = Field(default="", sa_column=Column("SMStockCode", String))
    createdby: str = Field(default="", sa_column=Column("CreatedBy", String))
    createdate: datetime = Field(default_factory=datetime.now, sa_column=Column("CreateDate", DateTime))
    updateby: str = Field(default="", sa_column=Column("UpdateBy", String))
    updatedate: datetime = Field(default_factory=datetime.now, sa_column=Column("UpdateDate", DateTime))
    siteid: int = Field(default=-1, sa_column=Column("SiteId", Integer))