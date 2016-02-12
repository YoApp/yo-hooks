"""
Description:
Called on heroku deploy

Documentation:
https://devcenter.heroku.com/articles/deploy-hooks#http-post-hook

Installation:
heroku addons:create deployhooks:http --url=http://yobar.herokuapp.com/heroku/<your-yo-username>/
"""


def translate(request):
    text = 'Deployed ' + request.form.get('app')
    return text