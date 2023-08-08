from django.shortcuts import render,HttpResponse

# Create your views here.
def news(request):
   return HttpResponse ("به دیجی کالا خوش آمدید") 

def abouts(request):
   return HttpResponse ("<h1>درباره ما</hi>")
