# Yo Hooks

Simpe predefined URLs for your webhooks.

Supported services for now:
- Heroku: http://yohooks.com/heroku/[your-yo-username]/ will Yo you when your app is deployed
- CircleCI: http://yohooks.com/circleci/[your-yo-username]/ will Yo you when your tests are done 
- Runscope: http://yohooks.com/runscope/[your-yo-username]/ will Yo you when your tests are done
- GitHub: http://yohooks.com/github/[your-yo-username]/ will Yo you when code is pushed

### How to add Heroku webhook:
In your terminal:
```heroku addons:create deployhooks:http --url=http://yohooks.com/heroku/[your-yo-username]/```
![](http://cl.ly/2K0Z0G0U0w2z/Screen%20Shot%202016-02-11%20at%2010.58.33%20PM.png)

### How to add GitHub webhook:

In your GitHub repo settings -> webhooks:
![](http://cl.ly/0N3J1A280E3g/Screen%20Shot%202016-02-12%20at%2012.48.10%20PM.png)

---

![](http://cl.ly/0A0n0q2y050e/Screen%20Shot%202016-02-12%20at%203.57.34%20PM.png)  

---

#Contribute

## Motivation
* Many providers support webhooks, but each provider has a different payload.
* Webhooks are HTTP POST requests which means that if you want to receive it you'll need a server running and parsing these incoming requests.
* Sometimes you just want a simple push notification to your phone when something happens, providers don't support push notifications mostly, but they do support webhooks.
* This project means you don't need to run a server, you don't need to parse the payload, basically you don't need anything besides the Yo app to receive the pushes.
* The URLs are predifined for you to paste in your provider webhook configuration.

## How?
* Each supported provider (like heroku, circleci, etc..) has a python module with a single function called `translate` - [Example 1](https://github.com/YoApp/yo-hooks/blob/master/heroku.py), [Example 2](https://github.com/YoApp/yo-hooks/blob/master/github.py), [Example 3](https://github.com/YoApp/yo-hooks/blob/master/circleci.py)
* The `translate` function accepts a Flask request and translates its payload into a very short string.
* A Flask server runs and listens to webhooks from supported providers.
* Once a provider trigger a webhook, the server takes the request's payload and `translate`s it into the short string.
* A Yo with the short string is sent to the username provided by the webhook URL path.

*Submissions for more providers are welcome.*

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

