from pydantic import BaseModel

class Product(BaseModel):
    id:int
    name:str
    description:str
    price:float
    quantite:int

#with basemode on a pas besoin de ca
    # def __init__(self, id:int, name:str, description:str, price:float, quantite:int):
    #     self.id=id
    #     self.name=name
    #     self.description=description
    #     self.price=price
    #     self.quantite=quantite