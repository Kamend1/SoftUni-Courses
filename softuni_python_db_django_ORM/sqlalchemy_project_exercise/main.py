from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONNECTION_STRING = 'postgresql+psycopg2://Kamend1:123456@localhost/sqlalchemy_exercise'

engine = create_engine(CONNECTION_STRING, pool_size=10, max_overflow=20)
Session = sessionmaker(bind=engine)

