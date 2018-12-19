from django.shortcuts import render

# Create your views her.def 
def post_list(request):
        return render(request, 'blog/post_list.html'  ,{})