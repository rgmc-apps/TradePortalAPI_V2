from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime

class Product(SQLModel, table=True):
    product_id: int = Field(
        sa_column=Column("ProductId", Integer, primary_key=True)
    )
    brand_id: Optional[int] = Field(
        default=None,
        sa_column=Column("BrandId", Integer)
    )
    item_group_id: Optional[int] = Field(
        default=None,
        sa_column=Column("ItemGroupId", Integer)
    )
    category_id: Optional[int] = Field(
        default=None,
        sa_column=Column("CategoryId", Integer)
    )
    stock_number: Optional[str] = Field(
        default=None,
        sa_column=Column("StockNumber", String)
    )
    barcode: Optional[str] = Field(
        default=None,
        sa_column=Column("Barcode", String)
    )
    description: Optional[str] = Field(
        default=None,
        sa_column=Column("Description", String)
    )
    color_id: Optional[int] = Field(
        default=None,
        sa_column=Column("ColorId", Integer)
    )
    size_id: Optional[int] = Field(
        default=None,
        sa_column=Column("SizeId", Integer)
    )
    original_price: Optional[float] = Field(
        default=0,
        sa_column=Column("OriginalPrice", Float)
    )
    selling_price: Optional[float] = Field(
        default=0,
        sa_column=Column("SellingPrice", Float)
    )
    is_active: bool = Field(
        default=True,
        sa_column=Column("IsActive", Boolean)
    )
    is_markdown: bool = Field(
        default=False,
        sa_column=Column("IsMarkdown", Boolean)
    )
    create_by: Optional[str] = Field(
        default="",
        sa_column=Column("CreateBy", String)
    )
    create_date: datetime = Field(
        default_factory=datetime.now,
        sa_column=Column("CreateDate", DateTime)
    )
    update_by: Optional[str] = Field(
        default="",
        sa_column=Column("UpdateBy", String)
    )
    update_date: datetime = Field(
        default_factory=datetime.now,
        sa_column=Column("UpdateDate", DateTime)
    )
