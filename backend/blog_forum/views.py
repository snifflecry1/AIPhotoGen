from django.shortcuts import render
from django.http import JsonResponse
from services.ai_converter_service import convert_content
# Create your views here.

def add_post(request):
    # post and topic valid make call to service
    # save to db
    post = request.GET.get('content')
    author = request.GET.get('author')

    # If the author doesn't make sense, default to some character you predefined
    # TO DO here 

    resp = convert_content(post, author)
    if resp['status'] == 'error':
        return JsonResponse({'status': 'error', 'message': resp['message']})
    
    return JsonResponse({'status': 'success', 'converted_content': resp['converted_content'], 'author': author})


        