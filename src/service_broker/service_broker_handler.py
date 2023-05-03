import json
from deepdiff import DeepDiff
from datetime import datetime, timezone
from fastapi import HTTPException

from config import Config
from direct_queue.local_queue import LocalQueue
from direct_queue.pg_queue import PGQueue


import sys
from helper.logger import Logger

log_message = Logger.get("svcbrk", Logger.Level.INFO, sys.stdout)

log_debug = log_message.debug
log_info = log_message.info
log_warning = log_message.warning
log_error = log_message.error


class SercieBrokerHandler:
    # singleton constructor set
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # to be called once
        cls = type(self)
        if not hasattr(cls, "_init"):
            try:
                # TODO: need to the generalization of schedule_queue creation...
                (queue_type, queue_info) = Config.queue_info()
                if queue_type == "local":
                    self.pending_queue_db = LocalQueue(queue_info)
                elif queue_type == "pg":
                    self.pending_queue_db = PGQueue(queue_info)
                
                cls._init = True
            except Exception as ex:
                raise HTTPException(status_code=500, detail=f"Exception: {ex}")

    def initialize(self):
        try:
            log_info("initialization done..")
        except Exception as ex:
            log_error(f"Initializaiton Error: {ex}")

    def register(self, pending_event: dict):
        try:
            # TODO: check the duplicated event here...
            db_key = self.create_db_key(pending_event)

            # store the updated schedule event
            self.pending_queue_db.put(db_key, pending_event)
            return pending_event
        except Exception as ex:
            print(f"Exception: {ex}")
            raise HTTPException(status_code=500, detail=f"Exception: {ex}")

    def get_list(self, tag: str = ""):
        result_list = list()
        try:
            key_value_list = self.pending_queue_db.get_key_value_list()
            for key_value in key_value_list:
                (_, pending_event) = key_value
                if tag == pending_event["tag"]:
                    result_list.append(pending_event)
            return result_list
        except Exception as ex:
            raise HTTPException(status_code=500, detail=f"Exception: {ex}")


  
