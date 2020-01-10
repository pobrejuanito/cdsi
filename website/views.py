from django.shortcuts import render_to_response

def index(request):

    page_data = {}
    return render_to_response('home.html', page_data)
