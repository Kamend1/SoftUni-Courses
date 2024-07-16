from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'postgresql+psycopg2://Kamend1:123456@localhost/sqlalchemy_db'

engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)

Session = sessionmaker(bind=engine)
