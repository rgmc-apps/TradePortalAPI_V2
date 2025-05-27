from sqlmodel import SQLModel, Field
from sqlalchemy import Column, Integer, String

class SMBrandSubClass(SQLModel, table=True):
    brand_id: int = Field(
        default=-1,
        sa_column=Column("BrandId", Integer, primary_key=True)
    )
    sub_class_code: str = Field(
        default="",
        sa_column=Column("SubClassCode", String, primary_key=True)
    )
    name: str = Field(
        default="",
        sa_column=Column("Name", String, primary_key=True)
    )