#// quiz/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .serializers import QuizSerializer
import random
# Create your views here.
@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    #// sample의 두번째 인자는 length
    randomQuizs = random.sample(list(totalQuizs), id)
    #// serializer에 many=True를 주면, 다수의 데이터도 직렬화해줍니다.
    serializer = QuizSerializer(randomQuizs, many=True)
    return Response(serializer.data)
