"""
Description:
Called on CircleCI tests finished

Documentation:
https://circleci.com/docs/api#build

Installation:
In circleci.yml add:

    notify:
      webhooks:
        - url: https://yohooks.com/circleci/<your-yo-username>/
"""


def translate(request):
    payload = request.get_json().get('payload')
    subject = payload.get('subject')
    status = u'👍' if payload.get('status') == "success" or \
                        payload.get('status') == "fixed" else u'👎'

    text = subject[:25] + u'... ' + status

    return text