
def translate(request):
	if request.json.get('text'):
		return request.json.get('text')
	else:
    	return 'Yo'