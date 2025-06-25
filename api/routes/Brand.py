import logging
import traceback
from fastapi import FastAPI, HTTPException, status, Depends, APIRouter
from sqlmodel import Session, select, col
from logger import LogHandler
from db.dbconn import ConnHandlerMSSQL
from api.models import Brand

brand_router = APIRouter(prefix="/brand", tags=["brand"])


LogHandler('api-systemuser-logs')
logger = logging.getLogger('api-systemuser-logs')

db = ConnHandlerMSSQL(logger)
session = db.get_session()
engine = db.get_engine()

@brand_router.get('/get/all')
async def get_all_brand():
    """Get All Active Brands."""
    try:
        with Session(engine) as temp_session:
            query = select(Brand).where(Brand.isactive == True)
            data = temp_session.exec(query).all()
            return data
    except Exception as e:
        logger.error('Error on getting Company Data. {}'.format(e))
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail='Error on getting Company Data. {}'.format(e)
        )
    
@brand_router.get('/get/compid')
async def get_by_complist(comp):
    if comp:
        complist = comp.split(',')
        try:
            with Session(engine) as temp_session:
                query = select(Brand).where(col(Brand.companyid).in_(complist))  
                data = temp_session.exec(query).all()
                return data
        except Exception as e:
            logger.error('Brand - Per Company - Error on getting brand details. {}'.format(e))
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail='Brand - Per Company - Error on getting brand details. {}'.format(e)
            )
    else:        
        logger.error('Brand - Per Company ID - No company id found')
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail='Brand - Per Company - Error on getting brand details. {}'.format(e)
        )
