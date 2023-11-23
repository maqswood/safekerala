from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from safekerala_admin.models import StationsDB, CriminalDB, LabourDB, ComplaintDB, FeedbackDB, NotificationDB,UserDB
from safekerala_station.views import stn_index
from safekerala_user.views import usr_registration, usr_index
from datetime import datetime
from django.contrib.auth.decorators import login_required


# Create your views here.

def LoginAdmin(req):
    return render(req, "login_admin.html")


def save_usr_registration(req):
    if req.method == "POST":
        user_name = req.POST.get('user_name')
        user_password = req.POST.get('user_password')
        user_email = req.POST.get('user_email')
        user_phone = req.POST.get('user_phone')
        user_place = req.POST.get('user_place')
        user_post = req.POST.get('user_post')
        user_district = req.POST.get('user_district')
        user_pincode = req.POST.get('user_pincode')
        user_image = req.FILES['user_image']
        obj_save_usr_registration = UserDB(username=user_name, password=user_password, email=user_email,
                                           phone=user_phone, place=user_place, post=user_post, district=user_district,
                                           pin=user_pincode, photo=user_image)
        obj_save_usr_registration.save()
        return redirect(LoginAdmin)


def Login_admin_auth(req):
    if req.method == "POST":
        usr_name = req.POST.get('user_name')
        usr_password = req.POST.get('user_password')

        if User.objects.filter(username__contains=usr_name).exists():
            user = authenticate(username=usr_name, password=usr_password)
            if user is not None:
                login(req, user)
                req.session['username'] = usr_name
                req.session['password'] = usr_password
                return redirect(AdminIndex)
        elif StationsDB.objects.filter(username=usr_name, password=usr_password).exists():
            station = StationsDB.objects.get(username=usr_name, password=usr_password)
            req.session['station_id'] = station.id
            req.session['usr_name'] = usr_name
            req.session['password'] = usr_password

            return redirect(stn_index)
        elif UserDB.objects.filter(username=usr_name, password=usr_password).exists():
            user = UserDB.objects.get(username=usr_name, password=usr_password)
            req.session['user_id'] = user.id
            req.session['usr_name'] = usr_name
            req.session['password'] = usr_password

            return redirect(usr_index)
        else:
            return redirect(LoginAdmin)


def LogoutAdmin(req):
    del req.session['username']
    del req.session['password']
    return redirect(LoginAdmin)


def LogoutUser(req):
    if 'username' in req.session:
        del req.session['username']
    if 'password' in req.session:
        del req.session['password']
    return redirect(LoginAdmin)


def LogoutStation(req):
    if 'username' in req.session:
        del req.session['username']
    if 'password' in req.session:
        del req.session['password']
    if 'station_id' in req.session:
        del req.session['station_id']

    return redirect(LoginAdmin)


def AdminIndex(req):
    return render(req, "ad_index.html")


def AddStation(x):
    return render(x, "Add_station.html")


def save_station_data(request):
    if request.method == "POST":
        name = request.POST.get('textfield')
        email = request.POST.get('textfield2')
        phone = request.POST.get('textfield3')
        post = request.POST.get('textfield4')
        district = request.POST.get('textfield5')
        place = request.POST.get('textfield6')
        pin = request.POST.get('textfield7')
        latitude = request.POST.get('textfield8')
        longitude = request.POST.get('textfield9')
        username = request.POST.get('textfield11')
        password = request.POST.get('textfield12')
        save_data = StationsDB(StationName=name, Email=email, Phone=phone, Post=post, District=district, Place=place,
                               Pin=pin, Latitude=latitude, Longitude=longitude, username=username, password=password)
        save_data.save()
        return redirect(AddStation)


def view_stations(req):
    data = StationsDB.objects.all()
    query = req.POST.get('textfield')
    if query:
        data = data.filter(StationName__icontains=query)
    return render(req, "view_stations.html", {'data': data})


def Edit_stations(req, data_id):
    edit_data = StationsDB.objects.get(id=data_id)
    return render(req, "Edit_stations.html", {'data': edit_data})


def update_station_data(request, data_id):
    if request.method == "POST":
        name = request.POST.get('textfield')
        email = request.POST.get('textfield2')
        phone = request.POST.get('textfield3')
        post = request.POST.get('textfield4')
        district = request.POST.get('textfield5')
        place = request.POST.get('textfield6')
        pin = request.POST.get('textfield7')
        latitude = request.POST.get('textfield8')
        longitude = request.POST.get('textfield9')
        StationsDB.objects.filter(id=data_id).update(StationName=name, Email=email, Phone=phone, Post=post,
                                                     District=district, Place=place, Pin=pin, Latitude=latitude,
                                                     Longitude=longitude)
        return redirect(view_stations)


@login_required(login_url='/login')
def admin_change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('textfield')
        new_password = request.POST.get('textfield2')
        confirm_password = request.POST.get('textfield3')

        # Check if the current password is valid
        if not request.user.check_password(current_password):
            messages.error(request, 'Current password is incorrect.')
            return redirect('admin_change_password')  # Redirect back to the change password page

        # Check if the new password and confirm password match
        if new_password != confirm_password:
            messages.error(request, 'New password and confirm password do not match.')
            return redirect('admin_change_password')  # Redirect back to the change password page

        # Change the password for the authenticated user
        request.user.set_password(new_password)
        request.user.save()

        # Update the session to prevent the user from being logged out
        update_session_auth_hash(request, request.user)

        messages.success(request, 'Password changed successfully.')
        return redirect('admin_change_password')  # Redirect back to the change password page

    return render(request,
                  'change_password.html')  # Replace 'your_change_password_template.html' with your actual template name


def notification(req):
    return render(req, "notification.html")


def send_reply(req):
    return render(req, "send_reply.html")


def view_criminal(req):
    data = CriminalDB.objects.all().select_related('station')
    query = req.POST.get('textfield')
    if query:
        data = data.filter(cr_name__icontains=query)

    return render(req, "view_criminal_list.html", {'data': data})


def view_labour(req):
    data = LabourDB.objects.all().select_related('station')
    query = req.POST.get('textfield')
    if query:
        data = data.filter(lb_name__icontains=query)

    return render(req, "view labour.html", {'data': data})


def view_complaint(req):
    data = ComplaintDB.objects.all()
    if req.method == "POST":
        from_date_str = req.POST.get('textfield')
        to_date_str = req.POST.get('textfield2')

        if from_date_str and to_date_str:
            from_date = datetime.strptime(from_date_str, '%Y-%m-%d').date()
            to_date = datetime.strptime(to_date_str, '%Y-%m-%d').date()

            data = ComplaintDB.objects.filter(c_date__range=[from_date, to_date])
        else:
            data = ComplaintDB.objects.all()

        return render(req, "view_complaint.html", {'data': data})

    return render(req, "view_complaint.html", {'data': data})


def view_feedback(req):
    data = FeedbackDB.objects.all()
    if req.method == "POST":
        from_date_str = req.POST.get('textfield')
        to_date_str = req.POST.get('textfield2')

        if from_date_str and to_date_str:
            from_date = datetime.strptime(from_date_str, '%Y-%m-%d').date()
            to_date = datetime.strptime(to_date_str, '%Y-%m-%d').date()

            data = FeedbackDB.objects.filter(f_date__range=[from_date, to_date])
        else:
            data = FeedbackDB.objects.all()

        return render(req, "view_feedback.html", {'data': data})

    return render(req, "view_feedback.html", {'data': data})


def send_notification(req):
    return render(req, "notification.html")


def view_notification(req):
    data = NotificationDB.objects.all()
    return render(req, "view_notification.html", {'data': data})
