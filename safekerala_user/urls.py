from django.urls import path
from safekerala_user import views
urlpatterns=[
    path('usr_registration/',views.usr_registration,name="usr_registration"),
    path('usr_index/',views.usr_index,name="usr_index"),
    path('police_stations/',views.police_stations,name="police_stations"),
    path('criminals/',views.criminals,name="criminals"),
    path('labours/',views.labours,name="labours"),
    path('report_labor/<int:labor_id>/',views.report_labor,name="report_labor"),
    path('user_view_profile/',views.user_view_profile,name="user_view_profile"),
    path('user_change_password/',views.user_change_password,name="user_change_password"),

]