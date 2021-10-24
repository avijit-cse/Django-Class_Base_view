from django.urls import path

from view_main import views

urlpatterns = [
    #path('',views.indexview.as_view(),name="index"),
    path('',views.list_view.as_view(),name="index"),
    path('details/<pk>/',views.Details_view.as_view(),name="Details_view"),
    path('cre/',views.Addview.as_view(),name="create_view"),
    path('upv/<pk>/',views.update_view.as_view(),name="update_view"),
    path('del/<pk>/',views.delect_view.as_view(),name="delect_view"),
]
