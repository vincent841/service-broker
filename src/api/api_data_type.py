from pydantic import BaseModel, Field
from typing import List


"""
ServiceData Type Definitions

"""

class Service(BaseModel):
    domain: str = Field(default="", title= "domain")
    application: str = Field(default="", title= "application")
    endpoint: str = Field(default="", title= "endpoint")
    data: dict = Field(default={}, title="user data")


class ServiceApiResult(BaseModel):
    event: str = Field(default="", title="event")
    message: str = Field(default="", title="message")
    data: Service = Field(default={}, title="data") 

