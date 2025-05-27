from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String, DateTime, Numeric
from datetime import datetime

class SMSKU(SQLModel, table=True):
    smstockdesc: str = Field(default="", primary_key=True)
    smstockcode: str = Field(default="", primary_key=True)
    vendorcode: str = Field(default="", sa_column=Column("VendorCode", String))
    deptcode: str = Field(default="", sa_column=Column("DeptCode", String))
    subdeptcode: str = Field(default="", sa_column=Column("SubDeptCode", String))
    classcode: str = Field(default="", sa_column=Column("ClassCode", String))
    unitretailamount: float = Field(default=0, sa_column=Column("UnitRetailAmount", Numeric(10, 2)))
    vendorupccode: str = Field(default="", sa_column=Column("VendorUpcCode", String))
    smupccode: str = Field(default="", sa_column=Column("SMUpcCode", String))
    createby: str = Field(default="", sa_column=Column("CreateBy", String))
    createdate: datetime = Field(default_factory=datetime.now, sa_column=Column("CreateDate", DateTime))
