from django.shortcuts import render

# Create your views here.
def MainPage(request):
    context={

    }
    return render(request,'front/index.html',context)