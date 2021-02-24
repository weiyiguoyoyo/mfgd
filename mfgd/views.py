from django.http import HttpResponse
from pygit2 import *

def index(request):
	return HttpResponse("Test")
