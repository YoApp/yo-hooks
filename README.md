# Yo Hooks
Turn any webhook into a Yo

## For when you just want a simple Yo out of webhooks.

## Why? (Motivation)
1. No more spinning up server just to receive webhooks.
2. No more coding whole project just to parse webhooks payload that is different at each web service.

## How?
* Each web service has a `python module` with a single function called `translate`
* The `translate` function accepts a Flask request and translates its payload into a very short string.
* A Flask server runs and listens to webhooks from supported webservices.
* Once a webhook occures, the server take the request payload and `translate`s it into the short string.
* A Yo is sent to the username provided by the webhook URL path.

## What should I do to use this:
* URLs are predefined in the pattern: https://yohooks.com/[webservice-name]/[your-yo-username]/
* All you have to do is set a webhook at your webservice as this URL and you'll get a Yo with the short text when the webhook fires.

So from now, if there is a service you use that provides webhooks and you want a simple way to get them - this is the place.
Submissions for more webservices are welcome.

Supported services for now:
- Heroku: http://yohooks.com/heroku/[your-yo-username]/ will Yo you when your app is deployed
- CircleCI: http://yohooks.com/circleci/[your-yo-username]/ will Yo you when your tests finished running

## Example

Heroku's docs describe the payload here:

![](http://cl.ly/2d0w360A2P1J/Screen%20Shot%202016-02-11%20at%207.26.03%20PM.png)

All we need is the deployed app name. So the translate function is:
```
def translate(request):
    text = 'Deployed ' + request.form.get('app')
    return text
```
That's it.
It's that simple.


