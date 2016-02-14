"""
Description:
Called on specified or all events.

Documentation:
https://stripe.com/docs/webhooks

Installation:
Through Stripe's web dashboard.
"""


def translate(request):
    text = request.json.get('type').replace('.', ' ')
    return text