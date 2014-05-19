from django.conf.urls import patterns, url

from enrollment import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(),name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^add/(?P<id>\d+)/$',views.StuCreate.as_view(),name='stu_add'),
)
