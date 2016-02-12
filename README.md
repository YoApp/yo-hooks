# Yo Hooks
Turn any webhook into a meaningful Yo.

## TL;DR

### Heroku
```heroku addons:create deployhooks:http --url=http://yohooks.com/heroku/<your-yo-username>/```

---

This:  
![](http://cl.ly/2K0Z0G0U0w2z/Screen%20Shot%202016-02-11%20at%2010.58.33%20PM.png)  
Becomes this:  
![](http://cl.ly/0n320c261C0J/IMG_4748%20copy.png)  

---
## Why?
1. No more spinning up servers just to receive webhooks.
2. No more coding a whole project just to parse webhook payloads that are different at each webservice.

## How?
* Each supported webservice (like heroku, circleci, etc..) has a python module with a single function called `translate` - [Example](https://github.com/YoApp/yo-hooks/blob/master/heroku.py)
* The `translate` function accepts a Flask request and translates its payload into a very short string.
* A Flask server runs and listens to webhooks from supported webservices.
* Once a webhook occures, the server takes the request's payload and `translate`s it into the short string.
* A Yo with the short string is sent to the username provided by the webhook URL path.

## What should I do to use this:
* URLs are predefined in the pattern: http://yohooks.com/[webservice-name]/[your-yo-username]/
* All you have to do is set a webhook at your webservice as this URL and you'll get a Yo with the short text when the webhook fires.

*Submissions for more webservices are welcome.*

Supported services for now:
- Heroku: http://yohooks.com/heroku/[your-yo-username]/ will Yo you when your app is deployed
- CircleCI: http://yohooks.com/circleci/[your-yo-username]/ will Yo you when your tests are done 
- Runscope: http://yohooks.com/runscope/[your-yo-username]/ will Yo you when your tests are done
- GitHub: http://yohooks.com/github/[your-yo-username]/ will Yo you code is pushed

## Examples

### How to create a `translate` function

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

### How to add GitHub webhook:

In your GitHub repo settings -> webhooks:
![](http://cl.ly/0N3J1A280E3g/Screen%20Shot%202016-02-12%20at%2012.48.10%20PM.png)



