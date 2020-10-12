from django.http import HttpResponse
import datetime


def index(request) :
	return HttpResponse("Hello Django")


def today_is(request):
	now = datetime.datetime.now()
	html = "<html><body><h1>Welcome to AGORAZ</h1><br><br>Current date and time: {0}</body></html>".format(now)
	return HttpResponse(html)