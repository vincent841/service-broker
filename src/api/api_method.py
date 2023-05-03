from service_broker.service_broker_handler import SercieBrokerHandler

import sys
from helper.logger import Logger


log_message = Logger.get("apimtd", Logger.Level.INFO, sys.stdout)

log_debug = log_message.debug
log_info = log_message.info
log_warning = log_message.warning
log_error = log_message.error


def api_register(input_req):
    log_info(f"request register: {input_req}")
    pending_event_handler = SercieBrokerHandler()
    return pending_event_handler.register(input_req)

def api_get_list(input_req):
    log_info(f"request get list: {input_req}")
    pending_event_handler = SercieBrokerHandler()
    return pending_event_handler.get_list(input_req)

