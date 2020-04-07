# from django.urls import path
# from .views import home, question, answer

# urlpatterns = [
#     path('', home, name='home'),
#     path('question', question, name='question'),
#     path('answer', answer, name='answer')
# ]

from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^question$', question, name='question'),
    url(r'answer$', answer, name='answer'),
    url(r'^delete_question/(?P<pk>\d+)$',delete_question,name='delete_question'),
    url(r'^add_answer/(?P<pk>\d+)$',add_answer,name='add_answer')
]