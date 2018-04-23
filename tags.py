from clarifai.rest import ClarifaiApp


app = ClarifaiApp(api_key='a59ba86af07b4ea699677c516b226ff6')

def get_relevant_tags(image_url):
	response_data = app.tag_urls([image_url])

	tag_urls = []
	for concept in response_data['outputs'][0]['data']['concepts']:
		tag_urls.append(concept['name'])


	return tag_urls

#print('\n'.join(get_relevant_tags('https://cars.usnews.com/static/images/Auto/izmo/i55764847/2018_ford_mustang_angularfront.jpg')))
print('\n'.join(get_relevant_tags('https://cars.usnews.com/static/images/Auto/izmo/i55764847/2018_ford_mustang_angularfront.jpg')))


#http://photos.visitphilly.com/lovepark-bkrist-900vp.jpg

