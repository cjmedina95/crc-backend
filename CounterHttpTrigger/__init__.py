import logging
import json
import azure.functions as func
import os

def main(req: func.HttpRequest, doc:func.DocumentList) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    logging.info(doc[0].to_json())
    count = doc[0]["count"]
    #doc[0]["count"] = doc[0]["count"] + 1

    if not count is None:
        return func.HttpResponse(
            doc[0].to_json(),
            mimetype="application/json"
        )
    else:
        return func.HttpResponse(
            "Count returned null / undefined.",
            status_code=200
        )