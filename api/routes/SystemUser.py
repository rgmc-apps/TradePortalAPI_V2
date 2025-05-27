import logging
from fastapi import FastAPI, HTTPException, status, Depends, APIRouter
from api.models import SystemUser
from sqlmodel import Session, select
from logger import LogHandler
from db.dbconn import ConnHandlerMSSQL

systemuser_router = APIRouter(prefix="/api/systemuser", tags=["systemuser"])

LogHandler('api-systemuser-logs')
logger = logging.getLogger('api-systemuser-logs')

db = ConnHandlerMSSQL(logger)
session = db.get_session()
engine = db.get_engine()

@systemuser_router.get('/get/all')
async def get_all_address():
    try:
        with Session(engine) as temp_session:
            query = select(SystemUser).where(SystemUser.isactive == True)
            data = temp_session.exec(query).all()
            return data
    except Exception as e:
        logger.error('Error on getting all users. {}'.format(e))
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail='Error on getting all users. {}'.format(e)
        )