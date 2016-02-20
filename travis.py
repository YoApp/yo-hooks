"""
Description:
Called on Travis tests done

Documentation:
https://docs.travis-ci.com/user/notifications/#Webhook-notification

Installation:
In circleci.yml add:

    notify:
      webhooks: https://yohooks.com/travis/<your-yo-username>/

"""


def translate(request):
    payload = request.json.get('payload')
    subject = payload.get('message')
    status = payload.get('status_message')
    text = subject[:25] + u'... ' + status
    return text
