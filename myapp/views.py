from django.shortcuts import render, redirect
from .models import Questions
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import QuestionSerializers
from rest_framework import status


class QuestionsList(APIView):

    def get(self, request):
        questions = Questions.objects.all()
        serializer = QuestionSerializers(questions, many=True)
        return Response(serializer.data)

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        question = request.POST['Question']
        form = Questions(name=name, question=question)
        form.save()
        return redirect('done')
    else:
        return render(request, 'files/index.html')


def done(request):
    return render(request, 'files/done.html')
