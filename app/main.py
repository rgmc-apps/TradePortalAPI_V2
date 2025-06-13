import logging
from logger import LogHandler
from datetime import datetime
from fastapi import FastAPI, HTTPException, status
from db.dbconn import ConnHandlerMSSQL
from sqlalchemy import text
from api.models import SystemUser
from api.routes import (systemuser_router, 
                        company_router,
                        customer_router,
                        store_router,
                        brand_router
                        )
from sqlmodel import select, Session
from fastapi.middleware.cors import CORSMiddleware

LogHandler('activity-logs')
origins = [
    "http://localhost",
    "https://localhost",
    "http://localhost:8080",
]

try:
    logger = logging.getLogger('activity-logs')
    logger.info('Start Trade Portal API: {}'.format(datetime.now().strftime("%Y-%m-%d %H:%M")))
    db = ConnHandlerMSSQL(logger)
    db.initialize_conn()
    app = FastAPI(title="RGMC Trade Portal API", version="1.0.0", openapi_url="/tradeportalapi.json", root_path='/api/v1')
    app.include_router(systemuser_router)
    app.include_router(company_router)
    app.include_router(customer_router)
    app.include_router(store_router)
    app.include_router(brand_router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
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
        engine = db.get_engine()
        with Session(engine) as temp_session:
            result = temp_session.exec(text("SELECT GETDATE()"))
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
        engine = db.get_engine()
        with Session(engine) as temp_session:
            query = select(SystemUser).where(SystemUser.isactive == True)
            data = temp_session.exec(query).all()
            return data
    except Exception as e:
        logger.error('SystemUser - Error: {}'.format(e))
