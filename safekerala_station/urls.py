from django.urls import path
from safekerala_station import views

urlpatterns=[
    path('stn_index/',views.stn_index,name="stn_index"),
    path('station_add_labour/',views.station_add_labour,name="station_add_labour"),
    path('save_station_add_labour/',views.save_station_add_labour,name="save_station_add_labour"),
    path('station_labour_view/',views.station_labour_view,name="station_labour_view"),
    path('edit_labour/<int:labour_id>/',views.edit_labour,name="edit_labour"),
    path('SaveEdit_labour/<int:labour_id>/',views.SaveEdit_labour,name="SaveEdit_labour"),
    path('DeleteLabour/<int:labour_id>/',views.DeleteLabour,name="DeleteLabour"),
    path('station_add_criminal/',views.station_add_criminal,name="station_add_criminal"),
    path('save_station_add_criminal/',views.save_station_add_criminal,name="save_station_add_criminal"),
    path('station_view_criminal/',views.station_view_criminal,name="station_view_criminal"),
    path('DeleteCriminal/<int:criminal_id>',views.DeleteCriminal,name="DeleteCriminal"),
    path('EditCriminal/<int:criminal_id>',views.EditCriminal,name="EditCriminal"),
    path('SaveEditCriminal/<int:criminal_id>',views.SaveEditCriminal,name="SaveEditCriminal"),
    path('view_reported_labours_and_take_action/',views.view_reported_labours_and_take_action,name="view_reported_labours_and_take_action"),
    path('station_viewcomplaint_sendreplay/',views.station_viewcomplaint_sendreplay,name="station_viewcomplaint_sendreplay"),
    path('station_view_feedback/',views.station_view_feedback,name="station_view_feedback"),
    path('reply_to_complaint_stn/<int:complaint_id>/',views.reply_to_complaint_stn,name="reply_to_complaint_stn"),
    path('send_reply_to_complaint_stn/<int:complaint_id>/',views.send_reply_to_complaint_stn,name="send_reply_to_complaint_stn"),
    path('station_view_notification/',views.station_view_notification,name="station_view_notification"),
    path('station_view_profile/',views.station_view_profile,name="station_view_profile"),
    path('station_edit_profile/',views.station_edit_profile,name="station_edit_profile"),
    path('save_station_edit_profile/',views.save_station_edit_profile,name="save_station_edit_profile"),
    path('station_change_password/',views.station_change_password,name="station_change_password"),
]