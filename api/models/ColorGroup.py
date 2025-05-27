from sqlmodel import SQLModel, Field
from datetime import datetime

class ColorGroup(SQLModel, table=True):
    colorgroupid: int = Field(default=-1, primary_key=True)
    colorgroupcode: str = ""
    name: str = ""
    remark: str = ""
    isactive: bool = True
    createby: str = ""
    createdate: datetime = Field(default_factory=datetime.now)
    updateby: str = ""
    updatedate: datetime = Field(default_factory=datetime.now)