from sqlmodel import SQLModel, Field
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, date

class StockPullOut(SQLModel, table=True):
    stockpulloutid: int = Field(default=-1, primary_key=True)
    pulloutdate: date = Field(default_factory=date.today)
    pullouttype: str = Field(default="", sa_column=Column("PullOutType", String))
    pulloutnumber: str = Field(default="", sa_column=Column("PullOutNumber", String))
    customerid: int = Field(default=-1, sa_column=Column("CustomerId", Integer))
    sourcerefnumber: str = Field(default="", sa_column=Column("SourceRefNumber", String))
    sourcebrandid: int = Field(default=-1, sa_column=Column("SourceBrandId", Integer))
    sourcestoreid: int = Field(default=-1, sa_column=Column("SourceStoreId", Integer))
    sourcesiteid: int = Field(default=-1, sa_column=Column("SourceSiteId", Integer))
    destnbrandid: int = Field(default=-1, sa_column=Column("DestnBrandId", Integer))
    destnstoreid: int = Field(default=-1, sa_column=Column("DestnStoreId", Integer))
    destnsiteid: int = Field(default=-1, sa_column=Column("DestnSiteId", Integer))
    filepath: str = Field(default="", sa_column=Column("FilePath", String))
    downloadby: str = Field(default="", sa_column=Column("DownloadBy", String))
    downloaddate: datetime = Field(default_factory=datetime.now)
    createby: str = Field(default="", sa_column=Column("CreateBy", String))
    createdate: datetime = Field(default_factory=datetime.now)
    updateby: str = Field(default="", sa_column=Column("UpdateBy", String))
    updatedate: datetime = Field(default_factory=datetime.now)
