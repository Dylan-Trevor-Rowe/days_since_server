from dayssinceapi.views.dayssinceboard import DaysSinceBoardView
from django.conf.urls import include
from django.urls import path
from dayssinceapi.views.auth import register_user, login_user
from dayssinceapi.views import WellBeingView, JournalEntryView, GoalsViewset, ArticlesViewset
DaysSinceBoardView
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'wellbeing', WellBeingView, 'emotionalWellBeing')
router.register(r'journal', JournalEntryView, 'journalentry')
router.register(r'goals', GoalsViewset, 'goals')
router.register(r'articles', ArticlesViewset, 'articles')
router.register(r'home', DaysSinceBoardView, 'dayssinceboard')



urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),

]