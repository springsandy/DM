# from django.conf import settings
# from django.contrib.auth.models import User
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.urls import path, include
# from rest_framework import routers
#
# from drama import views
# from drama.views import ProjectList, ProjectCreateVeiw, ProjectUpdateView, ProjectDeleteView, ProjectDetailView, \
#     ProjectAList, ProjectBList, ProjectCList, ProjectDList
#
# app_name = 'drama'
#
# router = routers.DefaultRouter(trailing_slash=False)
# router.register(r'users', views.UserViewSet, basename='users')
# router.register(r'groups', views.GroupViewSet, basename='groups')
#
# urlpatterns = [
#     path('', ProjectList.as_view(), name='list'),
#     # path(r'', include('router.urls')),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     path('add/', ProjectCreateVeiw.as_view(), name='add'),
#     path('update/<int:pk>/', ProjectUpdateView.as_view(), name='update'),
#     path('delete/<int:pk>/', ProjectDeleteView.as_view(), name='delete'),
#     path('detail/<int:pk>/', ProjectDetailView.as_view(), name='detail'),
#     path('a/', ProjectAList.as_view(), name='a'),
#     path('b/', ProjectBList.as_view(), name='b'),
#     path('c/', ProjectCList.as_view(), name='c'),
#     path('d/', ProjectDList.as_view(), name='d'),
# ]
#
# urlpatterns += staticfiles_urlpatterns()