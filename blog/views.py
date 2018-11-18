from django.shortcuts import render


# Create your views here.
def form_list(request):
    return render(request, 'blog/form_list.html', {})
