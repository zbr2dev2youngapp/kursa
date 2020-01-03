from django.contrib import admin
from django.urls import path, re_path
from api.views import *

urlpatterns = [
    re_path(r'admin/', admin.site.urls),
    re_path(r'auth/login/', LoginView.as_view(), name="auth-login"),
    re_path(r'auth/register/', RegisterUsersView.as_view(), name="auth-register"),
    re_path(r'user/get/by/token/', GetUserByTokenView.as_view(), name="user/get/by/token"),

    re_path(r'profile/create/', ProfileCreateView.as_view(), name="profile/create"),
    re_path(r'profile/rud/(?P<pk>\d+)/$', ProfileRudView.as_view(), name="profile/rud"),
    re_path(r'profile/get/by/user/(?P<user>\d+)/$', ProfileGetByUserView.as_view(), name="profile/get/by/user"),
    re_path(r'profile/list/', ProfileListView.as_view(), name="profile/list"),

    re_path(r'subject/create/', SubjectCreateView.as_view(), name="subject/create"),
    re_path(r'subject/rud/(?P<pk>\d+)/$', SubjectRudView.as_view(), name="subject/rud"),
    re_path(r'subject/list/', SubjectListView.as_view(), name="subject/list"),

    re_path(r'timertype/create/', TimerTypeCreateView.as_view(), name="timertype/create"),
    re_path(r'timertype/rud/(?P<pk>\d+)/$', TimerTypeRudView.as_view(), name="timertype/rud"),
    re_path(r'timertype/list/', TimerTypeListView.as_view(), name="timertype/list"),

    re_path(r'timer/create/', TimerCreateView.as_view(), name="timer/create"),
    re_path(r'timer/rud/(?P<pk>\d+)/$', TimerRudView.as_view(), name="timer/rud"),
    re_path(r'timer/list/', TimerListView.as_view(), name="timer/list"),
]