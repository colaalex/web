from django.urls import path

from .views import test, new_questions, question_details, popular_questions


urlpatterns = [
    path('', new_questions),
    path('login/', test),
    path('signup/', test),
    path('question/<int:id>/', question_details, name='question-details'),
    path('ask/', test),
    path('popular/', popular_questions),
    path('new/', test),
]
