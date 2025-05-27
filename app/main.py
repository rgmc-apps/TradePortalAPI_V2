import logging
from logger import LogHandler
from fastapi import FastAPI, HTTPException, status
from db.dbconn import ConnHandlerMSSQL
from sqlalchemy import text
from api.models import SystemUser
from api.routes import systemuser_router
from sqlmodel import select, Session

# from api.routes.address import address_routes

LogHandler('activity-logs')

try:
    logger = logging.getLogger('activity-logs')
    
    db = ConnHandlerMSSQL(logger)
    session = db.get_session()
    engine = db.get_engine()

    logger.info('Start Trade Portal API')
    app = FastAPI(title="RGMC Trade Portal API", version="1.0.0", openapi_url="/tradeportalapi.json")
    app.include_router(systemuser_router)
    logger.info('Initialization Complete')
except Exception as e:
    logger.error('Error on Initializing program. Details:{}'.format(e))


@app.get("/index")
def index():
    return {"status": "Api is running"}

@app.get("/checkconn")
def check_conn():
    curr_time = ''
    try:
        result = session.execute(text("SELECT GETDATE()"))
        for row in result:
            print("Current time from SQL Server:", row[0])
            curr_time = row 
        return {"status": "Ok", "message": 'Connection Established: Database current time {}'.format(curr_time)}
    except Exception as e:
        logger.error('Error on Database connection')
        raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail='Error on connecting to database. {}'.format(e)
            )
    
@app.get("/systemusers/get")
def get_systemusers():
    try:
        with Session(engine) as temp_session:
            query = select(SystemUser).where(SystemUser.isactive == True)
            data = temp_session.exec(query).all()
            return data
    except Exception as e:
        logger.error('SystemUser - Error: {}'.format(e))
        