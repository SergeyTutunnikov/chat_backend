from django.urls import path
from .views import *
urlpatterns = [
    path('send_message/',SendMessage.as_view(),name='ssend_message'),
    path('get_messages/<sender_id>/<receiver_id>/',GetMessages.as_view(),name='get_messsages')
    

]
