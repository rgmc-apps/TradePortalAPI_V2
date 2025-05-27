from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Company(SQLModel, table=True):
    companyid: int = Field(default=None, primary_key=True)
    companycode: Optional[str] = ""
    name: Optional[str] = ""
    initials: Optional[str] = ""
    address: Optional[str] = ""
    businessstyle: Optional[str] = ""
    tin: Optional[str] = ""
    remark: Optional[str] = ""
    isactive: bool = True
    createdby: Optional[int] = -1
    createdate: datetime = Field(default_factory=datetime.now)
    updateby: Optional[int] = -1
    updatedate: datetime = Field(default_factory=datetime.now)