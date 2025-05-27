from sqlmodel import SQLModel, Field
from typing import Optional

class BrandLookUpSM(SQLModel, table=True):
    brandid: int = Field(default=None, primary_key=True)
    smbrandcode: str = ""
    vendorcode: str = ""
    deptcode: str = ""
    subdeptcode: str = ""
    classcode: str = ""
    isactive: bool = False