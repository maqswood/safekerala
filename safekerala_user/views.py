from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password, make_password
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from safekerala_admin.models import StationsDB, CriminalDB, LabourDB, ActionDB, ReportDB
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
    data = LabourDB.objects.filter(is_blocked=False).select_related('station')
    query = req.POST.get('textfield')
    if query:
        data = data.filter(lb_name__icontains=query)
    return render(req, "labours.html", {'data': data})


def user_view_profile(req):
    username = req.session.get('usr_name')
    data = UserDB.objects.get(username=username)
    return render(req, "view_profile.html", {'data': data})


def user_edit_profile(req):
    username = req.session.get('usr_name')
    data = UserDB.objects.get(username=username)
    return render(req, "edit_user.html", {'data': data})


def save_user_edit_profile(req):
    user_id = req.session.get('user_id')
    if req.method == "POST":
        user_name = req.POST.get('textfield')
        user_email = req.POST.get('textfield2')
        user_phone = req.POST.get('textfield3')
        user_place = req.POST.get('textfield4')
        user_post = req.POST.get('textfield5')
        user_district = req.POST.get('textfield6')
        user_pincode = req.POST.get('textfield7')
        try:
            user_image = req.FILES['user_image']
            fs = FileSystemStorage()
            file = fs.save(user_image.name, user_image)
        except MultiValueDictKeyError:
            file = UserDB.objects.get(id=user_id).photo

        UserDB.objects.filter(id=user_id).update(username=user_name, email=user_email,
                                                 phone=user_phone, place=user_place, post=user_post,
                                                 district=user_district,
                                                 pin=user_pincode, photo=file)
        return redirect(user_view_profile)


def delete_usr_account(req):
    user_id = req.session.get('user_id')
    user_for_delete = UserDB.objects.get(id=user_id)
    del req.session['usr_name']
    del req.session['password']
    user_for_delete.delete()
    return redirect('LoginAdmin')


def user_change_password(request):
    if request.method == 'POST':
        # Get current user's username from session
        username = request.session.get('usr_name')

        # Get form data for old password, new password, and confirm password
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # Retrieve the user from the database
        user = UserDB.objects.get(username=username)

        # Verify if the old password matches the one in the database
        if not check_password(old_password, user.password):
            messages.error(request, 'Old password is incorrect.')
            return redirect('user_change_password')

        # Check if the new password and confirm password match
        if new_password != confirm_password:
            messages.error(request, 'New password and confirm password do not match.')
            return redirect('user_change_password')

        # Use set_password to hash and update the user's password
        user.set_password(new_password)
        user.save()

        # Update the password in the session
        request.session['password'] = user.password

        # Log the user in with the new password
        updated_user = authenticate(request, username=username, password=new_password)
        login(request, updated_user)

        messages.success(request, 'Password changed successfully.')
        return redirect('user_view_profile')

    return render(request, 'change_password_user.html')

def report_labor(request, labor_id):
    if request.method == 'POST':
        report_text = request.POST.get('report_text')
        labor = LabourDB.objects.get(id=labor_id)
        username = request.session.get('usr_name')
        data = UserDB.objects.get(username=username)  # Assuming user is authenticated
        report = ReportDB.objects.create(labor=labor, user=data, report_text=report_text)
        # You might want to redirect to a different page or show a success message

    return redirect('labours')  # Redirect to the user's labor list page
