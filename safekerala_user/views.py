from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from safekerala_admin.models import StationsDB, CriminalDB, LabourDB, ActionDB
from safekerala_admin.models import UserDB


# Create your views here.
def usr_registration(req):
    return render(req, "register_user.html")


def usr_index(req):
    return render(req, "usr_index.html",
                  {'usr_name': req.session.get('usr_name'), 'password': req.session.get('password')})


def police_stations(req):
    data = StationsDB.objects.all()
    query = req.POST.get('textfield')
    if query:
        data = data.filter(StationName__icontains=query)
    return render(req, "police_stations.html", {'data': data})


def criminals(req):
    data = CriminalDB.objects.all()
    query = req.POST.get('textfield')
    if query:
        data = data.filter(cr_name__icontains=query)
    return render(req, "criminals.html", {'data': data})


def labours(req):
    data = LabourDB.objects.all().select_related('station')
    query = req.POST.get('textfield')
    if query:
        data = data.filter(lb_name__icontains=query)
    return render(req, "labours.html", {'data': data})


def user_view_profile(req):
    username = req.session.get('usr_name')
    data = UserDB.objects.get(username=username)
    return render(req, "view_profile.html", {'data': data})


def user_change_password(req):
    return render(req, "change_password_user.html")


