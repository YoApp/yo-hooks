"""
Description:
Called on when runscope finishes testing

Documentation:
https://www.runscope.com/docs/api-testing/notifications#webhook

Installation:
https://www.runscope.com/docs/api-testing/notifications#webhook
"""


def translate(request):
    text = request.json.get('bucket_name') + ': ' + request.json.get('result')
    return text