from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String, Float

class SMProduct(SQLModel, table=True):
    bar_code: str = Field(
        default="",
        sa_column=Column("BarCode", String, primary_key=True)
    )
    stock_no: str = Field(
        default="",
        sa_column=Column("StockNo", String)
    )
    category: str = Field(
        default="",
        sa_column=Column("Category", String)
    )
    color_code: str = Field(
        default="",
        sa_column=Column("ColorCode", String)
    )
    size_code: str = Field(
        default="",
        sa_column=Column("SizeCode", String)
    )
    description: str = Field(
        default="",
        sa_column=Column("Description", String)
    )
    season: str = Field(
        default="",
        sa_column=Column("Season", String)
    )
    srp: float = Field(
        default=0,
        sa_column=Column("Srp", Float)
    )
