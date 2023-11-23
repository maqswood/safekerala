from django.urls import path
from safekerala_admin import views

urlpatterns = [
    path('', views.LoginAdmin, name="LoginAdmin"),
    path('save_usr_registration/', views.save_usr_registration, name="save_usr_registration"),
    path('Login_admin_auth/', views.Login_admin_auth, name="Login_admin_auth"),
    path('LogoutAdmin/', views.LogoutAdmin, name="LogoutAdmin"),
    path('LogoutUser/',views.LogoutUser,name="LogoutUser"),
    path('AdminIndex/', views.AdminIndex, name="AdminIndex"),
    path('AddStation/', views.AddStation, name="AddStation"),
    path('save_station_data/', views.save_station_data, name="save_station_data"),
    path('view_stations/', views.view_stations, name="view_stations"),
    path('Edit_stations/<int:data_id>/', views.Edit_stations, name="Edit_stations"),
    path('update_station_data/<int:data_id>/', views.update_station_data, name="update_station_data"),
    path('admin_change_password/', views.admin_change_password, name="admin_change_password"),
    path('notification/', views.notification, name="notification"),
    path('send_reply/', views.send_reply, name="send_reply"),
    path('view_criminal/', views.view_criminal, name="view_criminal"),
    path('view_labour/', views.view_labour, name="view_labour"),
    path('view_complaint/', views.view_complaint, name="view_complaint"),
    path('view_feedback/', views.view_feedback, name="view_feedback"),
    path('send_notification/', views.send_notification, name="send_notification"),
    path('view_notification/', views.view_notification, name="view_notification"),


]
