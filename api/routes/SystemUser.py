import logging
import traceback
from fastapi import FastAPI, HTTPException, status, Depends, APIRouter
from api.models import SystemUser
from sqlmodel import Session, select
from logger import LogHandler
from db.dbconn import ConnHandlerMSSQL
from api.generic_functions import decrypt

systemuser_router = APIRouter(prefix="/systemuser", tags=["SystemUser"])

LogHandler('api-systemuser-logs')
logger = logging.getLogger('api-systemuser-logs')

db = ConnHandlerMSSQL(logger)
session = db.get_session()
engine = db.get_engine()

@systemuser_router.get('/get/all')
async def get_all_system_users():
    retval = list()
    try:
        with Session(engine) as temp_session:
            query = select(SystemUser).where(SystemUser.isactive == True)
            data = temp_session.exec(query).all()
            for row in data:
                temp_dict = {}
                temp_dict['seccode'] = row.seccode
                temp_dict['password'] = row.password
                temp_dict['password_decrypted'] = decrypt(row.password)
                temp_dict['graceloginleft'] = row.graceloginleft
                temp_dict['expirationdate'] = row.expirationdate
                temp_dict['typecode'] = row.typecode
                temp_dict['name'] = row.name
                temp_dict['isactive'] = row.isactive
                retval.append(temp_dict)
            # return json.dumps(retval, default=str, sort_keys=True)
            return retval
    except Exception as e:
        traceback.print_exc()
        logger.error('Error on getting all users. {}'.format(e))
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail='Error on getting all users. {}'.format(e)
        )