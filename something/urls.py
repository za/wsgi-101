import views

urlpatterns = [
    (r'^$', views.index),
    (r'^hello/?$', views.hello),
    (r'^hello/(.+)$', views.hello)
]
