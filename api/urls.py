from django.urls import path, include

from .views import *
urlpatterns = [
    
    path('events/',EventList.as_view()),
    # path('events_detail/',EventDetail.as_view())
    path('blog_list/',BlogList.as_view()),
    path('game_record/',GameRecordList.as_view()),
]
