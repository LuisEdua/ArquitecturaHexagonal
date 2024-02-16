from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

DATABASE_URL = 'mysql+pymysql://root:RcBaR_-315@127.0.0.1:3306/BDAH'

engine = create_engine(DATABASE_URL)
