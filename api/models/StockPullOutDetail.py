from sqlmodel import SQLModel, Field
from sqlalchemy import Column, Integer, String, Float, Boolean

class StockPullOutDetail(SQLModel, table=True):
    stockpulloutid: int = Field(default=-1, primary_key=True)
    destnstoreid: int = Field(default=-1, primary_key=True)
    productid: int = Field(default=-1, primary_key=True)

    pulloutnumber: str = Field(default="", sa_column=Column("PullOutNumber", String))
    destnbrandid: int = Field(default=-1, sa_column=Column("DestnBrandId", Integer))
    destnsiteid: int = Field(default=-1, sa_column=Column("DestnSiteId", Integer))
    price: float = Field(default=0.0, sa_column=Column("Price", Float))
    pulloutqty: int = Field(default=0, sa_column=Column("PullOutQty", Integer))
    ismarkdown: bool = Field(default=False, sa_column=Column("IsMarkdown", Boolean))
    remarks: str = Field(default="", sa_column=Column("Remarks", String))
