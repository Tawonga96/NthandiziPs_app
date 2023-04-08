# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alert(models.Model):
    alert_id = models.IntegerField(primary_key=True)
    a_time = models.DateTimeField()
    code = models.CharField(max_length=128)
    author = models.ForeignKey('Member', models.DO_NOTHING, db_column='author')
    origin = models.TextField(blank=True, null=True)  # This field type is a guess.
    a_type = models.CharField(max_length=20)
    false_alarm = models.IntegerField()
    voided_by = models.IntegerField()
    closed_at = models.DateTimeField(blank=True, null=True)
    closed_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alert'


class AlertMultimedia(models.Model):
    alert = models.OneToOneField(Alert, models.DO_NOTHING, primary_key=True)
    path = models.IntegerField()
    ext = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alert_multimedia'


class AlertText(models.Model):
    alert = models.OneToOneField(Alert, models.DO_NOTHING, primary_key=True)
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'alert_text'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Citizen(models.Model):
    cid = models.OneToOneField('User', models.DO_NOTHING, db_column='cid', primary_key=True)
    occupation = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'citizen'


class Community(models.Model):
    community_id = models.IntegerField(primary_key=True)
    district = models.CharField(max_length=30)
    comm_name = models.CharField(max_length=35)
    area = models.TextField(blank=True, null=True)  # This field type is a guess.
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'community'


class CommunityIntervention(models.Model):
    intervention = models.OneToOneField('Intervention', models.DO_NOTHING, primary_key=True)
    initiated_by = models.ForeignKey('Member', models.DO_NOTHING, db_column='initiated_by')

    class Meta:
        managed = False
        db_table = 'community_intervention'


class CommunityLeader(models.Model):
    leader = models.OneToOneField('Member', models.DO_NOTHING, primary_key=True)
    community = models.ForeignKey(Community, models.DO_NOTHING)
    elected_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'community_leader'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Household(models.Model):
    hhid = models.IntegerField(primary_key=True)
    date_added = models.DateTimeField()
    hh_name = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'household'


class Housemember(models.Model):
    hm_id = models.IntegerField(primary_key=True)
    mid = models.ForeignKey('Member', models.DO_NOTHING, db_column='mid')
    hhid = models.ForeignKey(Household, models.DO_NOTHING, db_column='hhid')
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'housemember'


class Intervention(models.Model):
    intervention_id = models.IntegerField(primary_key=True)
    time_initiated = models.DateTimeField()
    alert = models.ForeignKey(Alert, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'intervention'


class JobPosting(models.Model):
    posting_id = models.IntegerField(primary_key=True)
    pid = models.ForeignKey('Policeofficer', models.DO_NOTHING, db_column='pid')
    psid = models.ForeignKey('Policestation', models.DO_NOTHING, db_column='psid')
    assigned_on = models.DateTimeField()
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'job_posting'


class Member(models.Model):
    mid = models.IntegerField(primary_key=True)
    cid = models.ForeignKey(Citizen, models.DO_NOTHING, db_column='cid')
    community = models.ForeignKey(Community, models.DO_NOTHING)
    date_joined = models.DateTimeField()
    left_on = models.DateTimeField(blank=True, null=True)
    citizen_typ = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'member'


class PoliceIntevention(models.Model):
    intervention = models.OneToOneField(Intervention, models.DO_NOTHING, primary_key=True)
    initiated_by = models.ForeignKey(JobPosting, models.DO_NOTHING, db_column='initiated_by')

    class Meta:
        managed = False
        db_table = 'police_intevention'


class Policeofficer(models.Model):
    pid = models.OneToOneField('User', models.DO_NOTHING, db_column='pid', primary_key=True)
    fname = models.CharField(max_length=35)
    lname = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'policeofficer'


class Policestation(models.Model):
    psid = models.IntegerField(primary_key=True)
    ps_name = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'policestation'


class Status(models.Model):
    istatus = models.IntegerField(db_column='iStatus', primary_key=True)  # Field name made lowercase.
    intervention = models.ForeignKey(Intervention, models.DO_NOTHING)
    status = models.TextField()
    updated_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'status'


class Subscribe(models.Model):
    subscription_id = models.IntegerField(primary_key=True)
    psid = models.ForeignKey(Policestation, models.DO_NOTHING, db_column='psid')
    community = models.ForeignKey(Community, models.DO_NOTHING)
    suscribed_on = models.DateTimeField()
    until = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscribe'


class User(models.Model):
    uid = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    pnumber = models.CharField(max_length=15)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50, blank=True, null=True)
    otp = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user'
