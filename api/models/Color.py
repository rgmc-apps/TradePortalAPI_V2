from sqlmodel import SQLModel, Field
from typing import Optional

class Color(SQLModel, table=True):
    colorid: int = Field(default=-1, primary_key=True)
    colorcode: str = ""
    name: str = ""
    colorgroupid: int = -1
    remark: str = ""
    isactive: bool = True
    createdby: str = ""