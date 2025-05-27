from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from sqlalchemy import Column, String, Boolean, Integer, DateTime

class Customer(SQLModel, table=True):
    customer_id: Optional[int] = Field(
        default=-1,
        sa_column=Column("CustomerId", Integer, primary_key=True)
    )
    customer_code: Optional[str] = Field(
        default="",
        sa_column=Column("CustomerCode", String)
    )
    initials: Optional[str] = Field(
        default="",
        sa_column=Column("Initials", String)
    )
    remark: Optional[str] = Field(
        default="",
        sa_column=Column("Remark", String)
    )
    is_active: Optional[bool] = Field(
        default=True,
        sa_column=Column("IsActive", Boolean)
    )
    create_by: Optional[str] = Field(
        default="",
        sa_column=Column("CreateBy", String)
    )
    create_date: Optional[datetime] = Field(
        default_factory=datetime.now,
        sa_column=Column("CreateDate", DateTime)
    )
    update_by: Optional[str] = Field(
        default="",
        sa_column=Column("UpdateBy", String)
    )
    update_date: Optional[datetime] = Field(
        default_factory=datetime.now,
        sa_column=Column("UpdateDate", DateTime)
    )