from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String, DateTime
from datetime import datetime

class SMSize(SQLModel, table=True):
    sm_size_code: str = Field(
        default="",
        sa_column=Column("SMSizeCode", String, primary_key=True)
    )
    look_up_code: str = Field(
        default="",
        sa_column=Column("LookUpCode", String, primary_key=True)
    )
    remark: str = Field(
        default="",
        sa_column=Column("Remark", String)
    )
    create_by: str = Field(
        default="",
        sa_column=Column("CreateBy", String)
    )
    create_date: datetime = Field(
        default_factory=datetime.now,
        sa_column=Column("CreateDate", DateTime)
    )