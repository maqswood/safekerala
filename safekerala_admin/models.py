from django.db import models


# Create your models here.
class StationsDB(models.Model):
    StationName = models.CharField(max_length=20, null=True, blank=True)
    Email = models.EmailField(max_length=50, null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True)
    Post = models.CharField(max_length=50, null=True, blank=True)
    District = models.CharField(max_length=20, null=True, blank=True)
    Place = models.CharField(max_length=20, null=True, blank=True)
    Pin = models.IntegerField(null=True, blank=True)
    Latitude = models.IntegerField(null=True, blank=True)
    Longitude = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=8, blank=True, null=True)


class UserDB(models.Model):
    username = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=8, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    place = models.CharField(max_length=50, blank=True, null=True)
    post = models.CharField(max_length=20, blank=True, null=True)
    district = models.CharField(max_length=20, blank=True, null=True)
    pin = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to="user profile", blank=True, null=True)


class CriminalDB(models.Model):
    cr_name = models.CharField(max_length=50, blank=True, null=True)
    cr_gender = models.CharField(max_length=5, blank=True, null=True)
    cr_dob = models.DateField(null=True, blank=True)
    cr_place = models.CharField(max_length=30, blank=True, null=True)
    cr_post = models.CharField(max_length=20, blank=True, null=True)
    cr_district = models.CharField(max_length=10, blank=True, null=True)
    cr_pincode = models.IntegerField(null=True, blank=True)
    cr_phone = models.IntegerField(null=True, blank=True)
    cr_photo1 = models.ImageField(upload_to="criminal photo", null=True, blank=True)
    cr_photo2 = models.ImageField(upload_to="criminal photo", null=True, blank=True)
    cr_identification_mark1 = models.CharField(max_length=50, blank=True, null=True)
    cr_identification_mark2 = models.CharField(max_length=50, blank=True, null=True)
    cr_case = models.CharField(max_length=200, blank=True, null=True)
    cr_action = models.CharField(max_length=50, blank=True, null=True)
    station = models.ForeignKey(StationsDB, on_delete=models.CASCADE, null=True, blank=True)


class LabourDB(models.Model):
    lb_name = models.CharField(max_length=50, blank=True, null=True)
    lb_email = models.EmailField(max_length=50, blank=True, null=True)
    lb_phone = models.IntegerField(null=True, blank=True)
    lb_id_proof = models.FileField(upload_to="id proof ", null=True, blank=True)
    lb_place = models.CharField(max_length=50, blank=True, null=True)
    lb_post = models.CharField(max_length=50, blank=True, null=True)
    lb_district = models.CharField(max_length=50, blank=True, null=True)
    lb_pincode = models.IntegerField(null=True, blank=True)
    lb_photo1 = models.ImageField(upload_to="media/labour photo", null=True, blank=True)
    lb_photo2 = models.ImageField(upload_to="media/labour photo", null=True, blank=True)
    lb_category = models.CharField(max_length=50, blank=True, null=True)
    lb_gender = models.CharField(max_length=5, blank=True, null=True)
    lb_dob = models.DateField(null=True, blank=True)
    station = models.ForeignKey(StationsDB, on_delete=models.CASCADE, null=True, blank=True)
    is_blocked = models.BooleanField(default=False)


class BlockedLabourDB(models.Model):
    lb_name = models.CharField(max_length=50, blank=True, null=True)
    lb_email = models.EmailField(max_length=50, blank=True, null=True)
    lb_phone = models.IntegerField(null=True, blank=True)
    lb_id_proof = models.FileField(upload_to="blocked_labour_id_proof", null=True, blank=True)
    lb_place = models.CharField(max_length=50, blank=True, null=True)
    lb_post = models.CharField(max_length=50, blank=True, null=True)
    lb_district = models.CharField(max_length=50, blank=True, null=True)
    lb_pincode = models.IntegerField(null=True, blank=True)
    lb_photo1 = models.ImageField(upload_to="blocked_labour_photo", null=True, blank=True)
    lb_photo2 = models.ImageField(upload_to="blocked_labour_photo", null=True, blank=True)
    lb_category = models.CharField(max_length=50, blank=True, null=True)
    lb_gender = models.CharField(max_length=5, blank=True, null=True)
    lb_dob = models.DateField(null=True, blank=True)
    station = models.ForeignKey(StationsDB, on_delete=models.CASCADE, null=True, blank=True)


class ComplaintDB(models.Model):
    c_date = models.DateField(null=True, blank=True)
    c_complaint = models.CharField(max_length=200, blank=True, null=True)
    u_loginid = models.ForeignKey(UserDB, on_delete=models.CASCADE, null=True)
    c_reply = models.CharField(max_length=200, blank=True, null=True)
    c_status = models.CharField(max_length=10, blank=True, null=True)


class FeedbackDB(models.Model):
    f_date = models.DateField(null=True, blank=True)
    f_feedback = models.CharField(max_length=200, blank=True, null=True)
    u_loginid = models.ForeignKey('UserDB', on_delete=models.CASCADE, null=True)


class NotificationDB(models.Model):
    n_date = models.DateField(null=True, blank=True)
    n_content = models.CharField(max_length=200, blank=True, null=True)


class ActionDB(models.Model):
    labor = models.ForeignKey(LabourDB, on_delete=models.CASCADE, null=True)
    u_loginid = models.ForeignKey(UserDB, on_delete=models.CASCADE, null=True)
    a_status = models.CharField(max_length=10, null=True, blank=True)
    # report = models.ForeignKey('ReportDB', on_delete=models.CASCADE, related_name='action_reports')


class ReportDB(models.Model):
    labor = models.ForeignKey(LabourDB, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(UserDB, on_delete=models.CASCADE)
    r_date = models.DateField(null=True, blank=True)
    report_text = models.TextField()
