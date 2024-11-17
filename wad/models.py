from django.contrib.gis.db import models
from django_better_admin_arrayfield.models.fields import ArrayField
from django.contrib.auth.models import User

class Crop(models.Model):
    name=models.CharField( unique=True , blank=False , null=False)
    crop_duty_ft=models.FloatField()
    area_enable=models.BooleanField(default=False)
    crop_enable=models.BooleanField(default=False)
    vol_enable=models.BooleanField(default=False)
    description=models.TextField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    name=models.CharField( unique=True , blank=False , null=False)
    attn=models.CharField()
    company=models.CharField()
    address_1=models.CharField()
    address_2=models.CharField()
    city=models.CharField()
    state=models.CharField()
    zip=models.IntegerField()
    home_phone=models.CharField()
    office_phone=models.CharField()
    mobile_phone=models.CharField()
    fax=models.CharField()
    email=models.EmailField()
    accounting_key=models.CharField()
    active_date=models.DateField()
    inactive_date=models.DateField()
    ACTIVE_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]
    active=models.CharField(
        max_length=1,
        choices=ACTIVE_CHOICES,
        default='N',
    )
    comment=models.TextField()

    def __str__(self):
        return self.name

class FieldCrop(models.Model):
    service_year=models.ForeignKey('ServiceYear', null=False, blank=False, on_delete=models.CASCADE, default = "")
    rate=models.ForeignKey('RateStructure', null=False, blank=False, on_delete=models.CASCADE, default = "")
    field=models.ForeignKey('Field', null=False, blank=False, on_delete=models.CASCADE, default = "")
    crop=models.ForeignKey('Crop', null=False, blank=False, on_delete=models.CASCADE, default = "")
    pct_planted=models.FloatField()
    comment=models.TextField()

    def __str__(self):
        return self.rate
    
class FieldCustomer(models.Model):
    field_customer_id = models.IntegerField(null=True, blank=True, default=None)
    customer=models.ForeignKey('Customer', null=False, blank=False, on_delete=models.CASCADE, default="")
    rate=models.ForeignKey('RateStructure', null=False, blank=False, on_delete=models.CASCADE, default = "")
    field=models.ForeignKey('Field', null=False, blank=False, on_delete=models.CASCADE, default = "")
    service_year= models.DateField()
    pct_farmed=models.FloatField()
    comment=models.TextField(default="")

    def __str__(self):
        return self.customer

class FieldInvoice(models.Model):
    invoice=models.ForeignKey('Invoice', null=False, blank=False, on_delete=models.CASCADE, default="")
    field=models.ForeignKey('Field', null=False, blank=False, on_delete=models.CASCADE, default = "")
    crop=models.ForeignKey('Crop', null=False, blank=False, on_delete=models.CASCADE, default="")
    acreage=models.FloatField()
    pct_farmed= models.FloatField()
    acre_rate=models.FloatField()
    acre_charge=models.FloatField()
    crop_rate= models.FloatField()
    crop_charge=models.FloatField()
    vol_start_date=models.DateField()
    vol_end_date=models.DateField()
    vol_rate=models.FloatField()
    vol_del=models.FloatField()
    vol_charge=models.FloatField()
    field_charge=models.FloatField()
    create_at=models.DateTimeField()
    mod_at=models.DateTimeField()

    def __str__(self):
        return self.invoice

class Invoice(models.Model):
    customer=models.ForeignKey('Customer', null=False, blank=False, on_delete=models.CASCADE, default="")
    rate=models.ForeignKey('RateStructure', null=False, blank=False, on_delete=models.CASCADE, default = "")
    service_year=models.ForeignKey('ServiceYear', null=False, blank=False, on_delete=models.CASCADE, default = "")
    total_acres=models.FloatField()
    acre_due_date= models.DateField()
    total_acre_charge= models.FloatField()
    crop_due_date=models.DateField()
    total_crop_charge=models.FloatField()
    crop_due_date= models.DateField()
    total_vol_charge=models.FloatField()
    total_vol_del=models.FloatField()
    vol_due_date= models.DateField()
    tot_vol_charge=models.FloatField()
    total_charge=models.FloatField()
    total_pay=models.FloatField()
    total_adj=models.FloatField()
    total_remain=models.FloatField()
    ACTIVE_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]
    is_vol_final=models.CharField(
        max_length=1,
        choices=ACTIVE_CHOICES,
        default='N',
    )
    is_void=models.CharField(
        max_length=1,
        choices=ACTIVE_CHOICES,
        default='N',
    )
    is_final=models.CharField(
        max_length=1,
        choices=ACTIVE_CHOICES,
        default='N',
    )
    create_at=models.DateTimeField()
    mod_at=models.DateTimeField()
    comments=models.TextField()

    def __str__(self):
        return self.customer

class RateStructure(models.Model):
    name=models.CharField()
    acre_basis=models.IntegerField()
    acre_comp=models.BooleanField(default=False)
    acre_due_mn=models.IntegerField()
    acre_due_day=models.IntegerField()
    acre_year_offset=models.IntegerField()
    crop_comp=models.BooleanField(default=False)
    crop_due_mn=models.IntegerField()
    crop_due_day=models.IntegerField()
    crop_year_offset=models.IntegerField()
    vol_comp=models.BooleanField(default=False)
    vol_due_mn=models.IntegerField()
    vol_due_day=models.IntegerField()
    vol_year_offset=models.IntegerField()
    vol_start_mn=models.IntegerField()
    vol_start_day=models.IntegerField()
    vol_start_year_offset=models.IntegerField()
    vol_end_mn=models.IntegerField()
    vol_end_day=models.IntegerField()
    vol_end_year_offset=models.IntegerField()
    comments=models.TextField()

    def __str__(self):
        return self.name

class Adjustment(models.Model):
    invoice=models.ForeignKey('Invoice', null=False, blank=False, on_delete=models.CASCADE, default="")
    amount=models.FloatField()
    date=models.DateField()
    ACTIVE_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]
    is_void=models.CharField(
        max_length=1,
        choices=ACTIVE_CHOICES,
        default='N',
    )
    mod_date=models.DateTimeField()
    comments=models.TextField()
    void_comments=models.TextField()

    def __str__(self):
        return self.invoice

class Config(models.Model):
    district=models.ForeignKey('District',  null=False, blank=False, on_delete=models.CASCADE, default="")
    qc_fall_start_mn=models.IntegerField()
    qc_fall_start_dy=models.IntegerField()
    qc_spring_start_mn=models.IntegerField()
    qc_spring_start_dy=models.IntegerField()
    use_wis=models.BooleanField(default=False)

    def __str__(self):
        return self.district


class District(models.Model):
    district = models.CharField( null=False, blank=False, unique=True)# District: District Abbreviation
    full_name = models.CharField()#DistrictFullName: District Full Name
    address = models.CharField()#Address:Street Address
    po_box = models.CharField()#POBox: P.O. Box Address
    city_state_zip = models.CharField()#CityStateZip: City, State, Zip Code
    office_phone = models.CharField()#OfficePhone: Office Phone Number
    office_email = models.EmailField()#OfficeEmail: Office Email
    office_fax = models.CharField()#OfficeFax: Office Fax Number
    website = models.URLField()#Website: Website url
    county = models.CharField()#County: County (or Counties) that District service area is a part of
    country = models.CharField()#Country: Country
    acreage = models.IntegerField(blank=True, null=True)#Acreage: Acreage within District service area
    established = models.DateField()#Established: Year of Formation
    
    def __str__(self):
        return self.district

class Field(models.Model):
    field_id = models.CharField()
    description = models.CharField()
    acres = models.FloatField()
    irrig_acres = models.FloatField()
    standby_acres = models.FloatField()
    parcel_id = models.CharField()#ParcelID for FieldID.  Could be Map-Number, FSA or APN.
    vol_rate_adj_id = models.IntegerField()#Amount of Lift required to irrigate the field
    active_date = models.DateField()
    inactive_date = models.DateField()
    ACTIVE_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]
    
    active= models.CharField(
        max_length=1,
        choices=ACTIVE_CHOICES,
        default='N',
    )#Y or N used to mark the most current record
    attributes = ArrayField(
        models.CharField(max_length=100), 
        size=5, 
        default=list,  # default empty array
        blank=True, 
        null=True
    )
    comment = models.TextField()

    def __str__(self):
        return self.field_id

class Payment(models.Model):
    invoice=models.ForeignKey('Invoice', null=False, blank=False, on_delete=models.CASCADE, default="")
    amount=models.FloatField()
    date=models.DateField()
    pay_number=models.IntegerField()
    is_deposit= models.BooleanField()
    ACTIVE_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]
    is_void=models.CharField(
        max_length=1,
        choices=ACTIVE_CHOICES,
        default='N',
    )
    create_at=models.DateTimeField()
    mod_at=models.DateTimeField()
    comments=models.TextField()
    void_comments=models.TextField()

    def __str__(self):
        return self.invoice 

class QCDailyField(models.Model):
    field=models.ForeignKey('Field', null=False, blank=False, on_delete=models.CASCADE , default="")
    date=models.DateField()
    vol_af=models.FloatField()
    method=models.IntegerField()
    qc_flag=models.CharField()

    def __str__(self):
        return self.field
    
class RateAcre (models.Model):
    acre_rate= models.FloatField()

    def __str__(self):
        return self.acre_rate
    
class RateCrop(models.Model):
    crop=models.ForeignKey('Crop', null=False, blank=False, on_delete=models.CASCADE, default="")
    crop_rate=models.FloatField()
    crop_enabled=models.BooleanField()

    def __str__(self):
        return self.crop

class RateVol(models.Model):
    rate=models.ForeignKey('RateStructure', null=False, blank=False, on_delete=models.CASCADE, default="")
    vol_rate_adj_id=models.IntegerField()
    vol_rate=models.FloatField()
    vol_enabled=models.BooleanField()

    def __str__(self):
        return self.rate
    
class VolDate(models.Model):
    service_year=models.ForeignKey('ServiceYear', null=False, blank=False, on_delete=models.CASCADE, default = "")
    rate=models.ForeignKey('RateStructure', null=False, blank=False, on_delete=models.CASCADE, default="")
    field=models.ForeignKey('Field', null=False, blank=False, on_delete=models.CASCADE , default="")
    customer=models.ForeignKey('Customer', null=False, blank=False, on_delete=models.CASCADE, default="")
    vol_start_date=models.DateField()
    vol_end_date= models.DateField()
    mod_at=models.DateField()
    comment=models.TextField()

    def __str__(self):
        return self.rate

class CustomerContact(models.Model):
    customer=models.ForeignKey('Customer', null=False, blank=False, on_delete=models.CASCADE, default="")
    name=models.CharField()
    email=models.EmailField()
    phone=models.CharField()
    role=models.CharField()

    def __str__(self):
        return self.customer

class  DistrictsAdmin(models.Model):
    district=models.ForeignKey('District',  null=False, blank=False, on_delete=models.CASCADE, default="")
    role=models.CharField()
    user=models.CharField()
    email=models.EmailField()

    def __str__(self):
        return self.district


class ServiceYear(models.Model):
    service_year=models.IntegerField()

    def __str__(self):
        return self.service_year