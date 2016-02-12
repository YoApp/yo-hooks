# Yo Hooks
Turn any webhook into a Yo

## For when you just want a simple Yo out of webhooks.

## Why? (Motivation)
1. No more spinning up server just to receive webhooks.
2. No more coding whole project just to parse webhooks payload that is different at each web service.

## How?
Each web service has a python module with a single function that `translate` a Flask request into a very short string.
URLs are predifined in the pattern: https://yohooks.com/<web-service-name>/<your-yo-username>/
All you have to do is configure your webhook to point to this URL and you'll get a Yo with the short text when the webhook fires.

So from now, if there is a service you use that provides webhooks and you want a simple way to get them - this is the place.
Contibutions are welcome.

Supported services for now:
- Heroku: https://yohooks.com/heroku/<your-yo-username>/ will Yo you when your app is deployed
- CircleCI: https://yohooks.com/circleci/<your-yo-username>/ will Yo you when your tests finished running
