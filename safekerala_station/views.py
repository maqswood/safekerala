from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from safekerala_admin.models import LabourDB, CriminalDB, ComplaintDB, FeedbackDB, NotificationDB, StationsDB, ActionDB, \
    ReportDB


# Create your views here.
def stn_index(req):
    return render(req, "stn_index.html",
                  {'usr_name': req.session.get('usr_name'), 'password': req.session.get('password')})


def station_add_labour(req):
    return render(req, "add labour.html")


def save_station_add_labour(req):
    if req.method == "POST":
        name = req.POST.get('Name')
        gender = req.POST.get('male')
        phone = req.POST.get('phone')
        email = req.POST.get('email')
        place = req.POST.get('place')
        post = req.POST.get('post')
        pin = req.POST.get('pin')
        district = req.POST.get('district')
        category = req.POST.get('category')
        dob = req.POST.get('dob')
        photo1 = req.FILES['photo1']
        photo2 = req.FILES['photo2']
        id_proof = req.FILES['id_proof']
        station_id = req.session.get('station_id')
        station = StationsDB.objects.get(id=station_id)
        obj_save_station_add_labour = LabourDB(lb_name=name, lb_email=email, lb_phone=phone, lb_id_proof=id_proof,
                                               lb_place=place, lb_post=post, lb_district=district, lb_pincode=pin,
                                               lb_photo1=photo1, lb_photo2=photo2, lb_category=category,
                                               lb_gender=gender, lb_dob=dob, station=station)
        obj_save_station_add_labour.save()
        return redirect(station_add_labour)


def station_labour_view(req):
    data = LabourDB.objects.all().select_related('station')
    query = req.POST.get('textfield')
    if query:
        data = data.filter(lb_name__icontains=query)
    return render(req, "view labour.html", {'data': data})


def edit_labour(req, labour_id):
    data = LabourDB.objects.get(id=labour_id)
    return render(req, "edit_labour.html", {'data': data})


def SaveEdit_labour(req, labour_id):
    if req.method == "POST":
        name = req.POST.get('textfield')
        gender = req.POST.get('male')
        phone = req.POST.get('textfield2')
        email = req.POST.get('textfield3')
        place = req.POST.get('textfield4')
        post = req.POST.get('textfield5')
        pin = req.POST.get('textfield6')
        district = req.POST.get('textfield7')
        category = req.POST.get('textfield8')
        dob = req.POST.get('textfield9')
        station_id = req.session.get('station_id')
        station = StationsDB.objects.get(id=station_id)

        try:
            photo1 = req.FILES['fileField']
            fs = FileSystemStorage()
            file1 = fs.save(photo1.name, photo1)
        except MultiValueDictKeyError:
            file1 = LabourDB.objects.get(id=labour_id).lb_photo1

        try:

            photo2 = req.FILES['fileField2']
            fs = FileSystemStorage()
            file2 = fs.save(photo2.name, photo2)

        except MultiValueDictKeyError:
            # If the files are not provided in the form, use existing files for the update

            file2 = LabourDB.objects.get(id=labour_id).lb_photo2

        try:
            id_proof = req.FILES['fileField1']
            fs = FileSystemStorage()
            file3 = fs.save(id_proof.name, id_proof)
        except MultiValueDictKeyError:
            file3 = LabourDB.objects.get(id=labour_id).lb_id_proof

        LabourDB.objects.filter(id=labour_id).update(
            lb_name=name, lb_email=email, lb_phone=phone, lb_id_proof=file3,
            lb_place=place, lb_post=post, lb_district=district, lb_pincode=pin,
            lb_photo1=file1, lb_photo2=file2, lb_category=category,
            lb_gender=gender, lb_dob=dob, station=station
        )
        print("After update query")
        messages.success(req, "Updated successfully")
        return redirect('station_labour_view')


def DeleteLabour(req, labour_id):
    labour_data = LabourDB.objects.filter(id=labour_id)
    labour_data.delete()
    messages.error(req, "deleted successfully")
    return redirect(station_labour_view)


def station_add_criminal(req):
    station_id = req.session.get('station_id')
    station = StationsDB.objects.get(id=station_id)
    return render(req, "add criminal.html", {'station': station})


def save_station_add_criminal(req):
    if req.method == "POST":
        name = req.POST.get('textfield')
        gender = req.POST.get('textfield2')
        phone = req.POST.get('textfield8')
        place = req.POST.get('textfield4')
        post = req.POST.get('textfield5')
        pin = req.POST.get('textfield7')
        district = req.POST.get('textfield6')
        dob = req.POST.get('textfield3')
        photo1 = req.FILES['imageField']
        photo2 = req.FILES['imageField2']
        cr_identification_mark1 = req.POST.get('textfield9')
        cr_identification_mark2 = req.POST.get('textfield10')
        cr_case = req.POST.get('textfield11')
        cr_action = req.POST.get('textfield12')

        # Get the station information from the session
        station_id = req.session.get('station_id')
        station = StationsDB.objects.get(id=station_id)

        # Create and save the CriminalDB object with the associated station
        obj_save_station_add_criminal = CriminalDB(
            cr_name=name, cr_phone=phone, cr_place=place, cr_post=post,
            cr_district=district, cr_pincode=pin, cr_photo1=photo1,
            cr_photo2=photo2, cr_gender=gender, cr_dob=dob,
            cr_identification_mark1=cr_identification_mark1,
            cr_identification_mark2=cr_identification_mark2,
            cr_case=cr_case, cr_action=cr_action, station=station
        )
        obj_save_station_add_criminal.save()

        return redirect('station_add_criminal')  # Adjust the URL name as per your configuration


def station_view_criminal(req):
    data = CriminalDB.objects.all().select_related('station')
    query = req.POST.get('textfield')
    if query:
        data = data.filter(cr_name__icontains=query)
    return render(req, "view criminal.html", {'data': data})


def EditCriminal(req, criminal_id):
    data = CriminalDB.objects.get(id=criminal_id)
    return render(req, "edit criminal.html", {'data': data})


def SaveEditCriminal(req, criminal_id):
    if req.method == "POST":
        name = req.POST.get('textfield')
        gender = req.POST.get('textfield2')
        phone = req.POST.get('textfield8')
        place = req.POST.get('textfield4')
        post = req.POST.get('textfield5')
        pin = req.POST.get('textfield7')
        district = req.POST.get('textfield6')
        dob = req.POST.get('textfield3')
        cr_identification_mark1 = req.POST.get('textfield9')
        cr_identification_mark2 = req.POST.get('textfield10')
        cr_case = req.POST.get('textfield11')
        cr_action = req.POST.get('textfield12')
        station_id = req.session.get('station_id')
        station = StationsDB.objects.get(id=station_id)
        try:
            photo1 = req.FILES['imageField']
            fs = FileSystemStorage()
            file1 = fs.save(photo1.name, photo1)
        except MultiValueDictKeyError:
            file1 = CriminalDB.objects.get(id=criminal_id).cr_photo1
        try:
            photo2 = req.FILES['imageField2']
            fs = FileSystemStorage()
            file2 = fs.save(photo2.name, photo2)
        except MultiValueDictKeyError:
            file2 = CriminalDB.objects.get(id=criminal_id).cr_photo2

        CriminalDB.objects.filter(id=criminal_id).update(
            cr_name=name, cr_phone=phone, cr_place=place, cr_post=post,
            cr_district=district, cr_pincode=pin, cr_photo1=file1,
            cr_photo2=file2, cr_gender=gender, cr_dob=dob,
            cr_identification_mark1=cr_identification_mark1,
            cr_identification_mark2=cr_identification_mark2,
            cr_case=cr_case, cr_action=cr_action, station=station
        )

        messages.success(req, "Updated successfully")
        return redirect(station_view_criminal)


def DeleteCriminal(req, criminal_id):
    criminal_data = CriminalDB.objects.filter(id=criminal_id)
    criminal_data.delete()
    messages.error(req, "deleted successfully")
    return redirect(station_view_criminal)


def view_reported_labours_and_take_action(request):
    station_id = request.session.get('station_id')

    # Get reported labors with the status 'blocked'
    reports = ReportDB.objects.filter(report_text='blocked', labor__station=station_id)
    Action = ActionDB.objects.all()

    if request.method == "POST":
        report_id = request.POST.get('labor_id_to_block')
        is_blocked = request.POST.get('is_blocked')

        try:
            data = get_object_or_404(ReportDB, id=report_id)
            u_instance = data.user
            lb_instance = data.labor
            action = 'blocked'

            obj = ActionDB(labor=lb_instance, u_loginid=u_instance, a_status=action)
            obj.save()

            # After blocking the labor, update the report status to 'resolved'
            data.report_text = 'resolved'
            data.save()
            if is_blocked:
                # Update the LabourDB record to indicate it is blocked
                LabourDB.objects.filter(id=lb_instance.id).update(is_blocked=True)

                # Optional: You may want to delete the LabourDB record entirely after moving it to BlockedLabourDB
                LabourDB.objects.filter(id=lb_instance.id).delete()

            else:
                # Update the LabourDB record if it is not blocked
                LabourDB.objects.filter(id=lb_instance.id).update(is_blocked=False)


        except ReportDB.DoesNotExist:
            # Handle the case where the specified report_id does not exist
            pass

    return render(request, "view_reported_labours.html", {'reports': reports, 'data': Action})


def station_viewcomplaint_sendreplay(req):
    data = ComplaintDB.objects.all()
    return render(req, "view complaint and send reply.html", {'data': data})


def station_view_feedback(req):
    data = FeedbackDB.objects.all()
    return render(req, "view feedback.html", {'data': data})


def station_view_notification(req):
    data = NotificationDB.objects.all()
    return render(req, "view notification.html", {'data': data})


def station_view_profile(req):
    username = req.session.get('usr_name')
    data = StationsDB.objects.get(username=username)
    return render(req, "view profile.html", {'data': data})
