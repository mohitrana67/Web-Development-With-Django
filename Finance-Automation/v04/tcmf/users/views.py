from django.shortcuts import render,HttpResponse

# Create your views here.
def home_view(request,*args,**kwargs):
    return render(
        request=request,
        template_name='users/index.html',
        context=None
    )

# this is an  api to create a user
def create_user(request,*args,**kwargs):
    return HttpResponse("Hello you are here")