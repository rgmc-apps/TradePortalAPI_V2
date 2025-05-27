from sqlmodel import SQLModel, Field
from sqlalchemy import Column, Integer, String, Float, DateTime
from typing import Optional
from datetime import datetime

class SMMarkdown(SQLModel, table=True):
    brandid: int = Field(
        default=-1,
        primary_key=True
    )
    subclasscode: str = Field(
        default="",
        primary_key=True
    )
    vendorpartstockno: str = Field(
        default="",
        primary_key=True
    )
    retailamount: float = Field(
        default=0, 
        primary_key=True
    )
    sm_stock_code: str = Field(
        default="",
        sa_column=Column("SMStockCode", String)
    )
    barcode: str = Field(
        default="",
        sa_column=Column("Barcode", String)
    )
    created_by: Optional[str] = Field(
        default="",
        sa_column=Column("CreatedBy", String),
    )
    create_date: datetime = Field(
        default_factory=datetime.now,
        sa_column=Column("CreateDate", DateTime)
    )
    update_by: Optional[str] = Field(
        default="",
        sa_column=Column("UpdateBy", String),
    )
    update_date: datetime = Field(
        default_factory=datetime.now,
        sa_column=Column("UpdateDate", DateTime)
    )
    site_id: int = Field(
        default=-1,
        sa_column=Column("SiteId", Integer)
    )
