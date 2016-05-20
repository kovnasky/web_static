from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from qa.views import test

urlpatterns = patterns('',
    url(r'^$', main_list, name='home'),
    url(r'^login/', login_form),
    url(r'^signup/', signup_form),
    url(r'^question/(\d+)/', question_details, name='question-details'),
    url(r'^ask/', ask_form),
    url(r'^popular/', popular_list),
    url(r'^new/', test),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^answer/', post_answer),
)
