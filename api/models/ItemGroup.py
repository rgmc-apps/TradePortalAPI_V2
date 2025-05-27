from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String, Integer
from typing import Optional

class ItemGroup(SQLModel, table=True):
    item_group_id: int = Field(
        default=0,
        sa_column=Column("ItemGroupId", Integer, primary_key=True)
    )
    item_group_code: str = Field(
        default="",
        sa_column=Column("ItemGroupCode", String)
    )
    name: Optional[str] = Field(
        default="",
        sa_column=Column("Name", String)
    )
    remark: Optional[str] = Field(
        default="",
        sa_column=Column("Remark", String)
    )