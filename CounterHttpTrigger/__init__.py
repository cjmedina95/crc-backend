import logging
import json
import azure.functions as func
import os

async def main(req: func.HttpRequest, doc:func.DocumentList) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    #logging.info(doc[0].to_json())
    
    try:
        count = doc[0]["count"]        
    except IndexError as e:
        count = 0
    
    count_dict = {'count': count}
    
    return func.HttpResponse(
        json.dumps(count_dict),
        mimetype="application/json",
        status_code=200
    )