from sqlmodel import SQLModel, Field
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from typing import Optional

class Size(SQLModel, table=True):
    sizeid: int = Field(default=-1, primary_key=True)
    sizecode: Optional[str] = Field(default="", sa_column=Column("SizeCode", String))
    abbreviation: Optional[str] = Field(default="", sa_column=Column("Abbreviation", String))
    name: Optional[str] = Field(default="", sa_column=Column("Name", String))
    itemgroupid: Optional[int] = Field(default=-1, sa_column=Column("ItemGroupId", Integer))
    sequencenumber: Optional[int] = Field(default=0, sa_column=Column("SequenceNumber", Integer))
    remarks: Optional[str] = Field(default="", sa_column=Column("Remarks", String))
    isactive: bool = Field(default=True, sa_column=Column("IsActive", Boolean))
    createby: Optional[str] = Field(default="", sa_column=Column("CreateBy", String))
    createdate: Optional[datetime] = Field(default_factory=datetime.now, sa_column=Column("CreateDate", DateTime))
    updateby: Optional[str] = Field(default="", sa_column=Column("UpdateBy", String))
    updatedate: datetime = Field(default_factory=datetime.now, sa_column=Column("UpdateDate", DateTime))
