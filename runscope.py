"""
Description:
Called on when runscope finishes testing

Documentation:
https://www.runscope.com/docs/api-testing/notifications#webhook

Installation:
https://www.runscope.com/docs/api-testing/notifications#webhook
"""


def translate(request):
    text = request.form.get('test_name') + ': ' + request.form.get('result')
    return text