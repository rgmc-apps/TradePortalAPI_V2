from sqlmodel import Field, Session, SQLModel
from typing import Optional
from datetime import datetime, date
from sqlalchemy import String, Column

class SystemUser(SQLModel, table=True):
    seccode: str = Field(default=None,primary_key=True)
    typecode: str
    name: str
    password: Optional[str] = None
    expirationdate: Optional[date] = Field(default_factory=datetime.now)
    graceloginleft: int = 5
    isactive: Optional[bool] = None

