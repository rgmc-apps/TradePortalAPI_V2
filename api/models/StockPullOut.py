from sqlmodel import SQLModel, Field
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class StockPullOut(SQLModel, table=True):
    stockpulloutid: int = Field(default=-1, primary_key=True)
    pulloutdate: datetime = Field(default_factory=datetime.now, sa_column=Column("PulLOutDate", DateTime))
    pullouttupe: str = Field(default="", sa_column=Column("PullOutTupe", String))
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
    downloaddate: datetime = Field(default_factory=datetime.now, sa_column=Column("DownloadDate", DateTime))
    createby: str = Field(default="", sa_column=Column("CreateBy", String))
    createdate: datetime = Field(default_factory=datetime.now, sa_column=Column("CreateDate", DateTime))
    updateby: str = Field(default="", sa_column=Column("UpdateBy", String))
    updatedate: datetime = Field(default_factory=datetime.now, sa_column=Column("UpdateDate", DateTime))
