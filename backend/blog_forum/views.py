from django.shortcuts import render
from django.http import JsonResponse
import json
from .services.ai_converter_service import convert_content
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# Note: You could use pydantic here to validate the body


    # For testing reference the following post request returns 200...
    # resp = requests.post("http://localhost:8000/blog_forum/add_post",json={"content": "Nice weather were having today in Ireland", "author": "Darth Vader"})

@csrf_exempt
def add_post(request):
    # post and topic valid make call to service
    # save to db
    
    data = json.loads(request.body)
    post = data.get('content')
    author = data.get('author')

    # If the author doesn't make sense, default to some character you predefined
    # TO DO here 

    resp = convert_content(post, author)
    if resp['status'] == 'error':
        return JsonResponse({'status': 'error', 'message': resp['message']})
    
    return JsonResponse({'status': 'success', 'converted_content': resp['converted_content'], 'author': author})


        