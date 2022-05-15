from django import forms
from django.shortcuts import render
from .models import Get
import tokenization_program.utils.helper as helper
from tokenization_program.tokenize.token_search import search_token

# Create your views here.
def token_search(request):
    return render(request, 'tokens_app/token_search.html', {})

def search_results(request):
    tokens = request.GET['token']
    tokens = helper.get_token_list(tokens)
    search_result = search_token(tokens)
    return render(request, 'tokens_app/search_results.html', {'tokens': tokens, 'results': search_result})

def resources(request):
    return render(request, 'files/hard.html',{})
