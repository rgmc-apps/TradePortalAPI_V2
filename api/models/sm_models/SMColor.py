from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime

class SMColor(SQLModel, table=True):
    sm_color_code: str = Field(
        default="",
        sa_column=Column("SMColorCode", String, primary_key=True)
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
    tmp_color_id: int = Field(
        default=-1,
        sa_column=Column("TmpColorId", Integer)
    )
