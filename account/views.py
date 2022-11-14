from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view

from deep_translator import GoogleTranslator

# Create your views here.



@api_view(['POST',])
def texttranslation(request):
    if request.method == "POST":
        text = request.POST['text']

        result=GoogleTranslator('auto','en').translate(text)
        
        return JsonResponse(result,safe=False)


