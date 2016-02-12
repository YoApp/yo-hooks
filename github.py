"""
Description:
Called on GitHub Push event

Documentation:
https://developer.github.com/v3/activity/events/types/#pushevent

Installation:
In GitHub project settings -> Webhooks
"""


def translate(request):
	payload = request.json()
	repo_name = payload.get('repository').get('name')
	pusher_name = payload.get('pusher').get('name')
    text = pusher_name + ' pushed to ' + repo_name
    return text
