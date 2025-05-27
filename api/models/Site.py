from sqlmodel import SQLModel, Field
from sqlalchemy import Column, Integer, String

class Site(SQLModel, table=True):
    siteid: int = Field(default=-1, primary_key=True)
    sitecode: str = Field(default="", sa_column=Column("SiteCode", String))
    name: str = Field(default="", sa_column=Column("Name", String))