#from django.conf.urls import include, url
#
#from . import views
#
#urlpatterns = [
#
#    url(r'^$', views.home_page , name='index'),
#    url(r'^login/.*$', views.user_login, name='login'),
#    url(r'^signup/.*$', views.user_signup, name='signup'),
#    url(r'^question/(?P<id>[0-9]+)/$', views.question_details, name='question'),
#    url(r'^ask/.*$', views.add_question, name='ask'),
#    url(r'^popular/.*$', views.popular_questions, name='popular'),
#    url(r'^new/.*$', 'qa.views.test', name='new'),
#]


from .views import test
from django.conf.urls import url


urlpatterns = [
    url(r'^$', test),
    url(r'^login/$', test),
    url(r'^signup/$', test),
    url(r'^question/([0-9]+)/$', test),
    url(r'^ask/\w*/ $', test),
    url(r'^popular/$', test),
    url(r'^new/$', test),
     url(r'^popular/', list_popular, name='list-popular'),
     url(r'^answer/', post_answer, name='post_answer'),
     url(r'^question/(?P<slug>\w+)/$', show_question, name='show-question'),
]
