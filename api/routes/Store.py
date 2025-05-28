import logging
import traceback
from fastapi import FastAPI, HTTPException, status, Depends, APIRouter
from sqlmodel import Session, select
from logger import LogHandler
from db.dbconn import ConnHandlerMSSQL
from api.models import Store

store_router = APIRouter(prefix="/store", tags=["Store"])

LogHandler('api-systemuser-logs')
logger = logging.getLogger('api-systemuser-logs')

db = ConnHandlerMSSQL(logger)
session = db.get_session()
engine = db.get_engine()

@store_router.get('/get/all')
async def get_all_stores():
    with Session(engine) as temp_session:
        query = select(Store).where(Store.isactive == True)
        data = temp_session.exec(query).all()

        return data