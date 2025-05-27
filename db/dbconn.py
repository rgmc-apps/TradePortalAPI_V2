from config import DB_NAME, DATABASE_URL, DB_PASSWORD, DB_URL, DB_USER
from sqlmodel import SQLModel, Field, create_engine, Session, select
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError

class ConnHandlerMSSQL(object):
    def __init__(self, logger):
        self.__engine = create_engine(DATABASE_URL)
        self.__SessionLocal = sessionmaker(bind=self.__engine)
        self.__logger = logger
    
    def get_engine(self):
        return self.__engine

    def get_session(self):
        self.__logger.info('Establishing Database Connection in {}'.format(DATABASE_URL))
        try:
            session = self.__SessionLocal()         
            return session
        except Exception as e:
            self.__logger.error('Error In Establishing database Connection: {}'.format(e))
            raise 

    def close(self):
        self.__engine.dispose()