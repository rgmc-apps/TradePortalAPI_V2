from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String, Integer, Boolean, DateTime
from datetime import datetime

class SMCompany(SQLModel, table=True):
    smcompanycode: str = Field(
        default="",
        primary_key=True
    )
    name: str = Field(
        default="",
        sa_column=Column("Name", String)
    )
    tin: str = Field(
        default="",
        sa_column=Column("TIN", String)
    )
    address: str = Field(
        default="",
        sa_column=Column("Address", String)
    )
    contact_person: str = Field(
        default="",
        sa_column=Column("ContactPerson", String)
    )
    telephone_number: str = Field(
        default="",
        sa_column=Column("TelephoneNumber", String)
    )
    fax_number: str = Field(
        default="",
        sa_column=Column("FaxNumber", String)
    )
    email_address: str = Field(
        default="",
        sa_column=Column("EmailAddress", String)
    )
    remark: str = Field(
        default="",
        sa_column=Column("Remark", String)
    )
    customer_company_id: int = Field(
        default=-1,
        sa_column=Column("CustomerCompanyId", Integer)
    )
    is_active: bool = Field(
        default=True,
        sa_column=Column("IsActive", Boolean)
    )
    create_by: str = Field(
        default="",
        sa_column=Column("CreateBy", String)
    )
    create_date: datetime = Field(
        default_factory=datetime.now,
        sa_column=Column("CreateDate", DateTime)
    )
    update_by: str = Field(
        default="",
        sa_column=Column("UpdateBy", String)
    )
    update_date: datetime = Field(
        default_factory=datetime.now,
        sa_column=Column("UpdateDate", DateTime)
    )
