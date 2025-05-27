from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String

class SystemMember(SQLModel, table=True):
    groupcode: str = Field(
        default="",
        primary_key=True
    )
    seccode: str = Field(
        default="",
        primary_key=True
    )