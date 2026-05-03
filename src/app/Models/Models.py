from pydantic import BaseModel

class BookModelClass(BaseModel):
     name : str
     year : int