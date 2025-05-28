import logging
import traceback
from fastapi import FastAPI, HTTPException, status, Depends, APIRouter
from sqlmodel import Session, select
from logger import LogHandler
from db.dbconn import ConnHandlerMSSQL
from api.models import Company

company_router = APIRouter(prefix="/company", tags=["Company"])

LogHandler('api-systemuser-logs')
logger = logging.getLogger('api-systemuser-logs')

db = ConnHandlerMSSQL(logger)
session = db.get_session()
engine = db.get_engine()

@company_router.get('/get/all')
async def get_all_company():
    try:
        with Session(engine) as temp_session:
            query = select(Company).where(Company.isactive == True)
            data = temp_session.exec(query).all()

            return data
    except Exception as e:
        logger.error('Error on getting Company Data. {}'.format(e))
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail='Error on getting Company Data. {}'.format(e)
        )