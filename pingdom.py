"""
Description:
Called on incident created or changed

Documentation:
https://help.pingdom.com/hc/en-us/articles/203611322-Setting-up-a-Webhook-and-an-Alerting-Endpoint

Installation:
https://help.pingdom.com/hc/en-us/articles/203611322-Setting-up-a-Webhook-and-an-Alerting-Endpoint
"""
import json


def translate(request):
    message = request.args.get('message')
    data = json.loads(message)
    text = data.get('host') + ' ' + data.get('down')
    return text