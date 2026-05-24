from pydantic import BaseModel

class ApikeyCreate(BaseModel):
    name: str
    description: str 

class ApikeyCreateResponse(BaseModel):
    key: str

class ApikeyDecoded(BaseModel):
    prefix: str
    secret: str