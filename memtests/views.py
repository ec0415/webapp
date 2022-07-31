from django.shortcuts import render
from django.http import HttpResponse

#dummy data
tests = [
	{
		'title': 'Match the Cards',
		'description': 'memorize the layout of the mixed up cards and find the matching pairs',
		'type': 'shape/image'
	},
	{
		'title': 'Picture Flash',
		'description': 'as the images flash on the screen, click the yes button if the image flashed before',
		'type': 'shape/image'
	},
	{
		'title': 'Simon Says',
		'description': 'memorize the colors and press them in the order they appeared',
		'type': 'shape/image'

	}
]


def index(request):
	context = {
		'tests': tests
	}
	return render(request, 'memtests/index.html', context)

#fixme
def matchingTest(request):
	return render(request, 'memtests/matching.html', {'title': 'Matching'})

