from ..config import config
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


username = config.get("DB", "USER")
password = config.get("DB", "PASSWORD")
db_name = config.get("DB", "DB_NAME")
domain = config.get("DB", "DOMAIN")
port = config.get("DB", "DB_PORT")


#  f'postgresql://username:password@domain_name:port/database_name'

DB_CONNECTION_URL = f"postgresql://{username}:{password}@{domain}:{port}/{db_name}"

engine = create_engine(DB_CONNECTION_URL)
DBSession = sessionmaker(bind=engine)
db_session = DBSession()