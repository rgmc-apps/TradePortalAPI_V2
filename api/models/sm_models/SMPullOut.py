from sqlmodel import SQLModel, Field
from sqlalchemy import Column, Integer, String, DateTime
from typing import Optional
from datetime import datetime

class SMPullOut(SQLModel, table=True):
    siteid: int = Field(default=-1, 
                         primary_key=True)
    smpulloutid: int = Field(default=-1, 
                                primary_key=True)
    sm_store_code: str = Field(default="", 
                               sa_column=Column("SMStoreCode", 
                                                String))
    scpoa_number: str = Field(default="", 
                              sa_column=Column("ScpoaNumber", 
                                               String))
    pull_out_date: datetime = Field(default_factory=datetime.now, 
                                    sa_column=Column("PullOutDate", 
                                                     DateTime))
    pull_out_number: str = Field(default="", 
                                 sa_column=Column("PullOutNumber", String))
    source_brand_id: int = Field(default=-1, 
                                 sa_column=Column("SourceBrandId", Integer))
    source_store_id: int = Field(default=-1, 
                                 sa_column=Column("SourceStoreId", Integer))
    source_site_id: int = Field(default=-1, 
                                sa_column=Column("SourceSiteId", Integer))
    destn_brand_id: int = Field(default=-1, 
                                sa_column=Column("DestnBrandId", Integer))
    destn_store_id: int = Field(default=-1, 
                                sa_column=Column("DestnStoreId", Integer))
    destn_site_id: int = Field(default=-1, 
                               sa_column=Column("DestnSiteId", Integer))
    file_path: str = Field(default="", 
                           sa_column=Column("FilePath", String))
    download_by: str = Field(default="", 
                             sa_column=Column("DownloadBy", String))
    download_date: datetime = Field(default_factory=datetime.now, 
                                    sa_column=Column("DownloadDate", DateTime))
    created_by: Optional[str] = Field(default="", 
                                      sa_column=Column("CreatedBy", String))
    create_date: datetime = Field(default_factory=datetime.now, 
                                  sa_column=Column("CreateDate", DateTime))
    update_by: Optional[str] = Field(default="", 
                                     sa_column=Column("UpdateBy", String))
    update_date: datetime = Field(default_factory=datetime.now, 
                                  sa_column=Column("UpdateDate", DateTime))
    old_sm_store_code: str = Field(default="", 
                                   sa_column=Column("OldSMStoreCode", String))
