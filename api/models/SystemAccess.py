from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String

class SystemAccess(SQLModel, table=True):
    systemcode: str = Field(
        default="",
        primary_key=True
    )
    modcode: str = Field(
        default="",
        primary_key=True
    )
    seccode: str = Field(
        default="",
        primary_key=True
    )
    accessright: str = Field(
        default="",
        sa_column=Column("AccessRight", String)
    )