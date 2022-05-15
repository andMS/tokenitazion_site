from django.shortcuts import render

# Create your views here.
def token_search(request):
    return render(request, 'tokens_app/token_search.html', {})
