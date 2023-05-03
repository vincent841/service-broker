from fastapi import FastAPI
from typing import List

from api.api_method import (
    api_register,
    api_get_list,
)

from api.api_data_type import Service, ServiceApiResult
from service_broker.service_broker_handler import SercieBrokerHandler


fast_api = FastAPI(
    title="Service Broker API",
    description="This service broker manages the endpoints for operato MSA like a webhook.",
    contact={
        "name": "hatiolab",
        "url": "https://www.hatiolab.com",
        "email": "jinwon@hatiolab.com",
    },
)



@fast_api.on_event("startup")
async def startup_event():
    service_broker_handler = SercieBrokerHandler()
    service_broker_handler.initialize()


@fast_api.on_event("shutdown")
async def shutdown_event():
    pass


@fast_api.post("/service")
async def put_pending_queue(inputs: Service) -> ServiceApiResult:
    """
    register a service
    
    """
    return {"event": api_register(inputs.dict())}


