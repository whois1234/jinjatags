from django.shortcuts import render

# Create your views here.

def jinjatags(request):
    d={'name':'rocky'}
    return render(request,'jinjatags.html',context=d)

def conditional(request):
    dic={'a':76}
    return render(request,'conditional.html',dic)