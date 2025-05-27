from sqlmodel import SQLModel, Field
from sqlalchemy import Column, Integer, String, Float, Boolean

class SMPullOutDetail(SQLModel, table=True):
    siteid: int = Field(default=-1, primary_key=True)
    smpulloutid: int = Field(default=-1, primary_key=True)
    destn_brand_id: int = Field(default=-1, sa_column=Column("DestnBrandId", Integer))
    destnstoreid: int = Field(default=-1, primary_key=True)
    destn_site_id: int = Field(default=-1, sa_column=Column("DestnSiteId", Integer))
    stockno: str = Field(default="", primary_key=True)
    description: str = Field(default="", sa_column=Column("Description", String))
    colorcode: str = Field(default="", primary_key=True)
    sizecode: str = Field(default="", primary_key=True)
    price: float = Field(default=0, primary_key=True)
    quantity: int = Field(default=0, sa_column=Column("Quantity", Integer))
    sm_stock_code: str = Field(default="", sa_column=Column("SMStockCode", String))
    sale_item: bool = Field(default=False, sa_column=Column("SaleItem", Boolean))
    remark: str = Field(default="", sa_column=Column("Remark", String))
