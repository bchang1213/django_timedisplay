from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime

def index(request):
	context = {
	"time": strftime("%H:%M %p", gmtime()),
	"date": strftime("%Y-%m-%d", gmtime())
	}
	return render(request, "time_display/index.html", context)
