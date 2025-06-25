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
    try:
        with Session(engine) as temp_session:
            query = select(Store).where(Store.isactive == True)
            data = temp_session.exec(query).all()

            return data
    except Exception as e:
        logger.error('Error on getting Store Data. {}'.format(e))
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail='Error on getting Store Data. {}'.format(e)
        )
