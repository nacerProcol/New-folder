
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#db_url = "mysql+pymysql://root:nacer@localhost:3306/logimage" 
db_url = "postgresql://podprd:podprd123@localhost:5432/pod_prd"

engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine) 