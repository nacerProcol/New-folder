from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException
from models import Product
from databse import session, engine
import database_models



app = FastAPI()
database_models.base.metadata.create_all(bind=engine)

products=[
    Product(id=1,name="apple",description="Iphone15",price=1005.5, quantite=5),
    Product(id=2,name="samsung",description="lass5",price=850.50,quantite=7)
]

def init_db():
    db = session()
    for product in products:
        db.add(database_models.Product(**product.model_dump()))
    db.commit()


init_db()

@app.get("/product")
def getallproduct():
    db=session()




@app.get("/")
def getlistProduct():
    return (products)


##dependency injection
# class Logger:
#     def log(self, message: str):
#         print(f"logging message : {message}")

# def get_logger():
#     return Logger()

# logger_dependency = Annotated[Logger, Depends(get_logger)]
# #METH1
# @app.get("/log/{message}")
# def log_message(message:str, logger: Logger = Depends (get_logger)):
#     logger.log(message)
#     return message
# #METH2
# @app.get("/ann/{message}")
# def log_message(message:str, logger: logger_dependency):
#     logger.log(message)
#     return 


# class EmailService:
#     def send_email(self, recipient: str, message: str):
#         print(f"Sendeng email to {recipient}: {message}")

# def get_email_service():
#     return EmailService()

# email_service_dependnecy = Annotated[EmailService, Depends(get_email_service)]

# @app.get("/ann/{message}")
# def send_email(recipient: str, message: str, email_service: email_service_dependnecy):
#     email_service.send_email(recipient, message)

# class AuthService:
#     def authenticate(self, token: str):
#         if token == 'Valid-token':
#             return True
#         else:
#             raise HTTPException(status_code=401, detail = 'Unauthorized')

# def get_auth_service():
#     return AuthService()

# auth_service_dependency = Annotated[AuthService, Depends(get_auth_service)]


# @app.get("/auth/")
# def get_secure_data(token: str, trak: str, auth_service:auth_service_dependency):
#     print(token)
#     if auth_service.authenticate(token):
#         return {"data": "this is secure data"}

