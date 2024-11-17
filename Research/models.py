from django.contrib.gis.db import models
from django_better_admin_arrayfield.models.fields import ArrayField
from django.contrib.auth.models import User

class Canal(models.Model):
    canal_id=models.CharField(max_length=3 , unique=True , blank=False , null=False)#CanalID: Three digit canal name abbreviation used in SiteIDs.
    name=models.CharField(blank=False , null=False,unique=True )#Canal: Unique canal names shown on RemoteTracker program.
    parent_canal=models.ForeignKey('Canal', null=True, blank=True, on_delete=models.CASCADE)
    carriage_loss=models.FloatField(blank=False , null=False)#CarriageLossCFS: Average seepage rate from Canal in CFS.
    description=models.TextField(blank=True,null=True) #Description: Description of Canal.

    def __str__(self):
        return self.canal_id

class MsmtMethod(models.Model):
    msmt_method_name=models.CharField(  blank=False , unique=True , null=False)#MsmtMethod: Measurement method associated with RemoteTracker SiteID.
    msmt_method_desc=models.TextField( blank=True ,null=True ) #MsmtMethodDesc: Description of measurement method.

    def __str__(self):
        return self.msmt_method_name

class QcCode(models.Model):
    qccode_name=models.CharField(blank=False , unique=True, null=False)#QCCode
    category=models.CharField(blank=False ,null=False)
    qccode_desc=models.TextField(blank=True ,null=True, )#QCDescription

    def __str__(self):
        return self.qccode_name

class Config(models.Model):
    district=models.ForeignKey('District',  null=False, blank=False, on_delete=models.CASCADE, default="")#District: District name
    qc_fall_start_mn=models.IntegerField()#QCFallStartMn: Start date to use for fall/winter water for filtering QC Reports
    qc_fall_start_dy=models.IntegerField()#QCFallStartDy: End date to use for fall/winter water for filtering QC Reports
    qc_spring_start_mn=models.IntegerField()#QCSpringStartMn: Start date to use for spring/summer water for filtering QC Reports
    qc_spring_start_dy=models.IntegerField()#QCSpringStartDy: End date to use for spring/summer water for filtering QC Reports
    allotment_ft = models.FloatField()#AllotmentFT: Allotment in FT during a drought
    days_to_export = models.IntegerField()#DaysToExport: Number of days of data to export to districtHistory.csv and districtOrders.csv files for RemoteTracker program.
    show_co_mingled_mult  = models.BooleanField(default=False)#ShowCoMingledMult: Show Returns times multiplier in DistrictWide comments.  Returns can be used to account for district/private wells that are adding water to the system.
    co_mingled_mult = models.FloatField()#CoMingledMult: Number to multiply CoMingledGW by to account for carriage losses.  Only used in comments section of DistrictHistory export.
    use_standBby_flow_duty = models.BooleanField(default=False)#UseStandbyFlowDuty: Should StandbyAcres be used for FLOW duty calculations?  Default is FarmedAcres.
    use_wad = models.BooleanField(default=False) #UseWAD: Is the WAD used as the District's Water Accounting Database?
    use_wad_cost_flow = models.BooleanField(default=False)#UseWADCustFLOW: Should WAD Water Users and WAD Water User-Field Associations be used for FLOW?
    canal_mgmt_return = models.BooleanField(default=False)#CanalMgmtReturn: Show returns (CoMIngledGW, RecycleGrav, and RecyclePump) as negative value on reports tab specifically for canal management report
    flow_spring_start_mn = models.IntegerField()#FLOWSpringStartMn: Spring start month for FLOW
    flow_spring_start_dy = models.IntegerField()#FLOWSpringStartDy: Spring start day for FLOW
    flow_fall_start_mn = models.IntegerField()#FLOWFallStartMn: Fall start month for FLOW
    flow_fall_start_dy = models.IntegerField()#FLOWFallStartDy: Fall start day for FLOW
    rate_id_spring_flow = models.IntegerField() #RateIDSpringFLOW: If the WAD is used for FLOW, what RateID should be used for the Spring Season Water User-Field associations?
    rate_id_fall_flow = models.IntegerField()#RateIDFallFLOW: If the WAD is used for FLOW, what RateID should be used for the Fall Season Water User-Field associations?
    use_wad_owner_flow =  models.BooleanField(default=False)#UseWADOwnerFLOW: Should WAD Landowners and WAD Landowner-Field Associations be used for FLOW?
    rate_id_spring_owner_flow = models.IntegerField() #RateIDSpringOwnerFLOW: If the WAD is used for FLOW, what RateID should be used for the Spring Season Landowner-Field associations?
    rate_id_fall_owner_flow = models.IntegerField() #RateIDFallOwnerFLOW: If the WAD is used for FLOW, what RateID should be used for the Fall Season Landowner-Field associations?

    def __str__(self):
        return self.district
    
class Constant(models.Model):
    constant_name = models.CharField( null=False, blank=False, unique=True)#ConstantName
    constant_value = models.FloatField()#ConstantValue
    ACTIVE_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]
    
    active = models.CharField(
        max_length=1,
        choices=ACTIVE_CHOICES,
        default='N',
    )#Y or N used to mark the most current record
    description = models.TextField()#note

    def __str__(self):
        return self.constant_name

class Day(models.Model):
    rec_date = models.DateTimeField()#RecDate: Date.
    season = models.CharField(null=False ,blank=False)#season: The season of the year for the corresponding date.
    ACTIVE_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]
    holiday =  models.BooleanField( max_length=1,
        choices=ACTIVE_CHOICES,
        default='N',)#holiday: Indicates whether the corresponding date represents a holiday, Y/N.

    def __str__(self):
        return self.rec_date

class DelType(models.Model):
    msmt_type_name = models.CharField() #DeliverySpill: DelType of site.
    msmt_type_desc = models.TextField()#Description: Description of DelType.

    def __str__(self):
        return self.msmt_type_name

class District(models.Model):
    district = models.CharField( null=False, blank=False, unique=True)# District: District Abbreviation
    full_name = models.CharField()#DistrictFullName: District Full Name
    address = models.CharField()#Address:Street Address
    po_box = models.CharField()#POBox: P.O. Box Address
    state = models.CharField(default="")
    city=models.CharField(default="")
    zip=models.CharField(default="")
    office_phone = models.CharField()#OfficePhone: Office Phone Number
    office_email = models.EmailField()#OfficeEmail: Office Email
    office_fax = models.CharField()#OfficeFax: Office Fax Number
    website = models.URLField()#Website: Website url
    county = models.CharField()#County: County (or Counties) that District service area is a part of
    country = models.CharField()#Country: Country
    acreage = models.FloatField(blank=True, null=True)#Acreage: Acreage within District service area
    established = models.DateField()#Established: Year of Formation
    
    def __str__(self):
        return self.district

class fgToVol(models.Model):
    fg_id = models.CharField()
    district=models.ForeignKey('District',  null=False, blank=False, on_delete=models.CASCADE, default="")
    date = models.DateField()
    vol_af_sum = models.IntegerField()
    vol_af_count = models.IntegerField()

    def __str__(self):
        return self.fg_id

class FieldGroupName(models.Model):
    site_id = models.CharField()
    msmt_point= models.ForeignKey('MsmtPoint', null=False, blank=False, on_delete=models.CASCADE, default = "")
    name = models.CharField(unique=True, blank=False, null=False)#common_name:
    field_group_no = models.CharField()

    def __str__(self):
        return self.site_id

class FieldGrower(models.Model):
    grower = models.ForeignKey('Grower', null=False, blank=False, on_delete=models.CASCADE, default = "")#GrowerID from the Grower table.
    field = models.ForeignKey('Field', null=False, blank=False, on_delete=models.CASCADE, default="")#FieldID from the Fields table.
    ACTIVE_CHOICES = [
        ('1', 'Spring'),
        ('2', 'fall'),
    ]
    season_id = models.IntegerField(
        choices=ACTIVE_CHOICES,
        default='1') #SeasonID for the association.  1 = Spring; 2 = Fall.
    service_year = models.ForeignKey('ServiceYear', on_delete=models.CASCADE,default="")

    def __str__(self):
        return self.service_year
class Field(models.Model):
    field_id = models.CharField() 
    description = models.TextField()
    acres = models.FloatField()
    irrig_acres = models.FloatField()
    standby_acres = models.FloatField()
    parcel_id = models.CharField()  
    vol_rate_adj_id = models.IntegerField()  # Amount of lift required to irrigate the field
    active_date = models.DateField()
    inactive_date = models.DateField()  # Allow inactive_date to be blank or null

    ACTIVE_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]

    active = models.CharField(
        max_length=1,
        choices=ACTIVE_CHOICES,
        default='N',
    )  # Y or N used to mark the most current record

    # Storing up to 5 attributes, default to an empty list if not provided
    attributes = ArrayField(
        models.CharField(max_length=100), 
        size=4, 
        default=list,  # default empty array
        blank=True, 
        null=True
    )
    comment=models.TextField()

    def __str__(self):
        return self.field_id

class FieldSite(models.Model):
    site_id = models.CharField()#SiteID for the record.
    field = models.ForeignKey('Field', null=False, blank=False, on_delete=models.CASCADE)#FieldID for the record.
    ChooseMethod = [
        ('Direct' , 'Direct'),
        ('Apportioned', 'Apportioned'),
    ]
    method = models.CharField(
        max_length=15,
        choices=ChooseMethod,
        default='Direct',
    )#Calculation method.
    active_date = models.DateField()#Active date for Field-Site linkage.
    inactive_date = models.DateField()
    ACTIVE_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]
    
    active= models.CharField(
        max_length=1,
        choices=ACTIVE_CHOICES,
        default='N',
    )
    comment = models.TextField(max_length=200)

    def __str__(self):
        return self.site_id
    
class FieldTurnout(models.Model):
    msmt_point= models.ForeignKey('MsmtPoint', null=False, blank=False, on_delete=models.CASCADE, default = "") #TurnoutID based on canal, stationing, and delivery side
    field=models.ForeignKey('Field', null=False, blank=False, on_delete=models.CASCADE)#Field Identifier (District Abbreviation followed by integer)
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
    ) #Y or N used to mark the most current record
    comment= models.CharField(max_length=200)

    def __str__(self):
        return self.msmt_point

class FinalData(models.Model):
    site_id = models.CharField()
    rec_date_time=models.DateTimeField()
    q_cfs=models.FloatField()
    msmt_method=models.ForeignKey('MsmtMethod', null=False, blank=False, on_delete=models.CASCADE, default = "")
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    ft_avg_signal_beam1=models.FloatField()
    ft_avg_signal_beam2=models.FloatField()
    ft_avg_noise_beam1=models.FloatField()
    ft_avg_noise_beam2=models.FloatField()
    ft_avg_snr_beam1=models.FloatField()
    ft_avg_snr_beam2=models.FloatField()
    ft_avg_temp_f=models.FloatField()
    ft_avg_batt_voltage_v=models.FloatField()
    ft_avg_vx_fps=models.FloatField()
    ft_stdev_vx_fps=models.FloatField()
    ft_avg_vy_fps=models.FloatField()
    ft_stdev_vy_fps=models.FloatField()
    ft_area_sqft=models.FloatField()
    ft_avg_q_cfs=models.FloatField()
    ft_avg_q_angle_deg=models.FloatField()
    ACTIVE_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]
    auto_start= models.CharField(
        max_length=1,
        choices=ACTIVE_CHOICES,
        default='N',
    )
    auto_sample= models.CharField(
        max_length=1,
        choices=ACTIVE_CHOICES,
        default='N',
    )
    auto_locate= models.CharField(
        max_length=1,
        choices=ACTIVE_CHOICES,
        default='N',
    )
    gate_full_stem_ft=models.FloatField()
    gate_us_level_ft=models.FloatField()
    gate_ds_level_ft=models.FloatField()
    gate_q_cfs=models.FloatField()
    weir_height_ft=models.FloatField()
    weir_q_cfs=models.FloatField()
    meter_total_af=models.FloatField()
    meter_q_cfs=models.FloatField()
    rt_manual_q_cfs=models.FloatField()
    iq_avg_depth_ft=models.FloatField()
    iq_avg_temp_c=models.FloatField()
    iq_avg_vxc_fps=models.FloatField()
    iq_stdev_vxc_fps=models.FloatField()
    iq_avg_vzc_fps=models.FloatField()
    iq_avg_vxl_fps=models.FloatField()
    iq_stdev_vxl_fps=models.FloatField()
    iq_avg_vxr_fps=models.FloatField()
    iq_stdev_vxr_fps=models.FloatField()
    iq_avg_batt_voltage_v=models.FloatField()
    iq_avg_pitch_deg=models.FloatField()
    iq_avg_roll_deg=models.FloatField()
    iq_avg_in_water=models.FloatField()
    iq_avg_snr_beam1=models.FloatField()
    iq_avg_snr_beam2=models.FloatField()
    iq_avg_snr_beam3=models.FloatField()
    iq_avg_snr_beam4=models.FloatField()
    iq_avg_stage_ft=models.FloatField()
    iq_avg_area_sqft=models.FloatField()
    iq_avg_vx_fps=models.FloatField()
    batch_datetime=models.DateTimeField()
    qc_code=models.ForeignKey('QcCode', null=False, blank=False, on_delete=models.CASCADE, default = "")
    row_id=models.IntegerField()
    recompute= models.CharField(
        max_length=1,
        choices=ACTIVE_CHOICES,
        default='N',
    )
    comments=models.CharField()

    def __str__(self):
        return self.site_id

class FinalOrder(models.Model):
    site_id=models.CharField()
    order_date_time=models.DateTimeField()
    rec_date_time=models.DateTimeField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    order_q_cfs=models.FloatField()
    current_q_cfs=models.IntegerField()
    delivered_q_cfs=models.IntegerField()
    batch_datetime=models.DateTimeField()
    qc_code=models.ForeignKey('QcCode', null=False, blank=False, on_delete=models.CASCADE, default = "")
    row_id=models.IntegerField()
    ACTIVE_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]
    recompute=models.CharField(
        max_length=1,
        choices=ACTIVE_CHOICES,
        default='N',
    )
    comments=models.TextField()
    
    def __str__(self):
        return self.site_id

class Grower(models.Model):
    customer_id = models.IntegerField(unique=True,null=False, blank=False)#Unique ID (autonumber) for each Customer in the WAD.
    name=models.CharField()
    phone=models.CharField()
    email=models.EmailField()
    ACTIVE_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]
    active=models.CharField(
        max_length=1,
        choices=ACTIVE_CHOICES,
        default='N',
    )#Y or N used to mark the most current record.
    comment = models.TextField()

    def __str__(self):
        return self.customer_id

class GrowerCredit(models.Model):
    grower= models.ForeignKey('Grower', null=False, blank=False, on_delete=models.CASCADE , default ="")
    credit_date=models.DateTimeField()
    credit_af=models.IntegerField()
    comment=models.TextField()

    def __str__(self):
        return self.grower

class LoadData(models.Model):
    site_id=models.CharField()
    date_time=models.DateTimeField()
    q_cfs=models.IntegerField()
    msmt_method=models.ForeignKey('MsmtMethod', null=False, blank=False, on_delete=models.CASCADE, default = "")
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    ft_avg_signal_beam1=models.FloatField()
    ft_avg_signal_beam2=models.FloatField()
    ft_avg_noise_beam1=models.FloatField()
    ft_avg_noise_beam2=models.FloatField()
    ft_avg_snr_beam1=models.FloatField()
    ft_avg_snr_beam2=models.FloatField()
    ft_avg_temp_f=models.FloatField()
    ft_avg_batt_voltage_v=models.FloatField()
    ft_avg_vx_fps=models.FloatField()
    ft_stdev_vx_fps=models.FloatField()
    ft_avg_vy_fps=models.FloatField()
    ft_stdev_vy_fps=models.FloatField()
    ft_area_sqft=models.FloatField()
    ft_avg_q_cfs=models.FloatField()
    ft_avg_q_angle_deg=models.FloatField()
    ACTIVE_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]
    auto_start= models.CharField(
        max_length=1,
        choices=ACTIVE_CHOICES,
        default='N',
    )
    auto_sample= models.CharField(
        max_length=1,
        choices=ACTIVE_CHOICES,
        default='N',
    )
    auto_locate= models.CharField(
        max_length=1,
        choices=ACTIVE_CHOICES,
        default='N',
    )
    gate_full_stem_ft=models.FloatField()
    gate_us_level_ft=models.FloatField()
    gate_ds_level_ft=models.FloatField()
    gate_q_cfs=models.FloatField()
    weir_height_ft=models.FloatField()
    weir_q_cfs=models.FloatField()
    meter_total=models.FloatField()
    meter_q=models.FloatField()
    rt_manual_q_cfs=models.FloatField()
    iq_avg_depth_ft=models.FloatField()
    iq_avg_temp_c=models.FloatField()
    iq_avg_vxc_fps=models.FloatField()
    iq_stdev_vxc_fps=models.FloatField()
    iq_avg_vzc_fps=models.FloatField()
    iq_avg_vxl_fps=models.FloatField()
    iq_stdev_vxl_fps=models.FloatField()
    iq_avg_vxr_fps=models.FloatField()
    iq_stdev_vxr_fps=models.FloatField()
    iq_avg_batt_voltage_v=models.FloatField()
    iq_avg_pitch_deg=models.FloatField()
    iq_avg_roll_deg=models.FloatField()
    iq_avg_in_water=models.FloatField()
    iq_avg_snr_beam1=models.FloatField()
    iq_avg_snr_beam2=models.FloatField()
    iq_avg_snr_beam3=models.FloatField()
    iq_avg_snr_beam4=models.FloatField()
    iq_avg_stage_ft=models.FloatField()
    iq_avg_area_sqft=models.FloatField()
    iq_avg_vx_fps=models.FloatField()
    comments=models.CharField()

    def __str__(self):
        return self.site_id
  
class LoadOrder(models.Model):
    site_id=models.CharField()
    order_date_time=models.DateTimeField()
    rec_date_time=models.DateTimeField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    order_q_cfs=models.IntegerField()
    current_q_cfs=models.IntegerField()
    delivered_q_cfs = models.IntegerField()
    comment =models.TextField()

    def __str__(self):
        return self.site_id

class MeterInfo(models.Model):
    msmt_point= models.ForeignKey('MsmtPoint', null=False, blank=False, on_delete=models.CASCADE, default = "")#TurnoutID of the location of the meter.
    meter_no = models.IntegerField()#Meter identification number.
    make=models.CharField()#Make of the meter (e.g. McCrometer, etc.).
    model=models.CharField()#model of the meter (e.g. EX201, etc.).
    flow_units=models.CharField()#Flow rate units (e.g. GPM, CFS, etc.).
    flow_multiplier=models.FloatField()#A conversion factor used to multiply raw flow values from the field to convert to CFS.
    totalizer_units=models.CharField()#Totalizer units (e.g. USG, AF, etc.).
    totalizer_reset_value=models.FloatField()#the maximum totalizer reading.  If the highest totalizer reading is 9999, use 10000.
    totalizer_multiplier=models.IntegerField()
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
    comments= models.TextField()

    def __str__(self):
        return self.msmt_point

class QCDailyFieldGroup(models.Model):
    site_id= models.CharField()
    rec_date=models.DateField()
    volume_af=models.FloatField()
    duration_hr= models.FloatField()
    no_rec=models.IntegerField()
    code=models.CharField()
    mode_date=models.DateField()

    def __str__(self):
        return self.site_id

class QCDailyField(models.Model):
    field=models.ForeignKey('Field', null=False, blank=False, on_delete=models.CASCADE , default="")
    date=models.DateField()
    vol_af=models.FloatField()
    method=models.IntegerField()
    qc_flag=models.CharField()

    def __str__(self):
        return self.field
    
class QCDailyFieldSite(models.Model):
    site_id= models.CharField()
    field=models.ForeignKey('Field', null=False, blank=False, on_delete=models.CASCADE, default="")
    rec_date=models.DateField()
    ChooseMethod = [
        ('Direct' , 'Direct'),
        ('Apportioned', 'Apportioned'),
    ]
    method = models.CharField(
        max_length=15,
        choices=ChooseMethod,
        default='Direct',
    )#Calculation method.
    total_vol_af=models.FloatField()
    duration_hr=models.IntegerField()
    no_rec=models.IntegerField()
    total_ac=models.IntegerField()
    field_acres=models.FloatField()
    area_adj_fac=models.FloatField()
    app_vol_af=models.FloatField()
    qc_flag=models.CharField()

    def __str__(self):
        return self.site_id

class QCDailyTurnout(models.Model):
    site_id=models.CharField()
    rec_date= models.DateField()
    volume_af=models.FloatField()
    duration_hr= models.FloatField()
    no_rec=models.IntegerField()
    code=models.CharField()
    mod_date=models.DateTimeField()

    def __str__(self):
        return self.site_id
    
class QCParam(models.Model):
    msmt_point=models.ForeignKey('MsmtPoint', null=False, blank=False, on_delete=models.CASCADE, default = "")
    us_min=models.FloatField(default=2)
    us_max=models.FloatField(default= 1000)
    ds_min=models.FloatField(default= 0)
    ds_max=models.FloatField(default= 1000)
    gate_min=models.FloatField(default= 0)
    gate_max=models.FloatField(default= 1000)
    q_ang_min=models.FloatField(default= -15)
    q_ang_max=models.FloatField(default=15)
    temp_min=models.FloatField(default=33)
    temp_max=models.FloatField(default=120)
    snr1_min=models.IntegerField(default=3)
    snr2_min=models.IntegerField(default=3)
    weir_min=models.IntegerField(default=0)
    weir_max=models.IntegerField(default=3)
    q_min=models.FloatField(default=50)
    q_max=models.FloatField(default=0)
    meter_total_min=models.FloatField(default=0)
    meter_total_max=models.FloatField(default=999999)
    meter_q_min=models.FloatField(default=0)
    meter_q_max=models.FloatField(default=20)
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

    def __str__(self):
        return self.msmt_point

class RawData(models.Model):
    site_id=models.CharField()
    date_time=models.DateTimeField()
    q_cfs=models.IntegerField()
    msmt_method=models.ForeignKey('MsmtMethod', null=False, blank=False, on_delete=models.CASCADE , default="")
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    ft_avg_signal_beam1=models.FloatField()
    ft_avg_signal_beam2=models.FloatField()
    ft_avg_noise_beam1=models.FloatField()
    ft_avg_noise_beam2=models.FloatField()
    ft_avg_snr_beam1=models.FloatField()
    ft_avg_snr_beam2=models.FloatField()
    ft_avg_temp_f=models.FloatField()
    ft_avg_batt_voltage_v=models.FloatField()
    ft_avg_vx_fps=models.FloatField()
    ft_stdev_vx_fps=models.FloatField()
    ft_avg_vy_fps=models.FloatField()
    ft_stdev_vy_fps=models.FloatField()
    ft_area_sqft=models.FloatField()
    ft_avg_q_cfs=models.FloatField()
    ft_avg_q_angle_deg=models.FloatField()
    ACTIVE_CHOICES = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]
    auto_start= models.CharField(
        max_length=1,
        choices=ACTIVE_CHOICES,
        default='N',
    )
    auto_sample= models.CharField(
        max_length=1,
        choices=ACTIVE_CHOICES,
        default='N',
    )
    auto_locate= models.CharField(
        max_length=1,
        choices=ACTIVE_CHOICES,
        default='N',
    )
    gate_full_stem_ft=models.FloatField()
    gate_us_level_ft=models.FloatField()
    gate_ds_level_ft=models.FloatField()
    gate_q_cfs=models.FloatField()
    weir_height_ft=models.FloatField()
    weir_q_cfs=models.FloatField()
    meter_total=models.FloatField()
    meter_q=models.FloatField()
    rt_manual_q_cfs=models.FloatField()
    iq_avg_depth_ft=models.FloatField()
    iq_avg_temp_c=models.FloatField()
    iq_avg_vxc_fps=models.FloatField()
    iq_stdev_vxc_fps=models.FloatField()
    iq_avg_vzc_fps=models.FloatField()
    iq_avg_vxl_fps=models.FloatField()
    iq_stdev_vxl_fps=models.FloatField()
    iq_avg_vxr_fps=models.FloatField()
    iq_stdev_vxr_fps=models.FloatField()
    iq_avg_batt_voltage_v=models.FloatField()
    iq_avg_pitch_deg=models.FloatField()
    iq_avg_roll_deg=models.FloatField()
    iq_avg_in_water=models.FloatField()
    iq_avg_snr_beam1=models.FloatField()
    iq_avg_snr_beam2=models.FloatField()
    iq_avg_snr_beam3=models.FloatField()
    iq_avg_snr_beam4=models.FloatField()
    iq_avg_stage_ft=models.FloatField()
    iq_avg_area_sqft=models.FloatField()
    iq_avg_vx_fps=models.FloatField()
    batch_datetime=models.DateTimeField()
    qcd_flag=models.BooleanField(default=False)
    row_id= models.IntegerField()
    qc_code=models.ForeignKey('QcCode', null=False, blank=False, on_delete=models.CASCADE , default="")
    comments=models.CharField()

    def __str__(self):
        return self.site_id

class RawOrder(models.Model):
    site_id=models.CharField()
    order_date_time=models.DateTimeField()
    rec_date_time=models.DateTimeField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    order_q_cfs=models.FloatField()
    current_q_cfs=models.FloatField()
    delivered_q_cfs=models.FloatField()
    batch_datetime=models.DateTimeField()
    qcd_flag=models.BooleanField(default=False)
    row_id=models.IntegerField()
    comments=models.TextField()

    def __str__(self):
        return self.site_id
    
class Route(models.Model):
    district=models.ForeignKey('district', null=False, blank=False, on_delete=models.CASCADE , default="")
    name=models.CharField()
    operators = ArrayField(
        models.CharField(max_length=100), 
        size=4, 
        default=list,  # default empty array
        blank=True, 
        null=True
    )
    description=models.TextField

    def __str__(self):
        return self.name
    
class MsmtPoint(models.Model):
    msmt_point_id= models.CharField()
    district=models.ForeignKey('District', null=False, blank=False, on_delete=models.CASCADE, default="")
    msmt_point_name=models.CharField()
    type=models.CharField()
    route=models.ForeignKey('Route', null=False, blank=False, on_delete=models.CASCADE, default="")
    canal=models.ForeignKey('Canal', null=True, blank=True, on_delete=models.CASCADE, default="")
    geopoint=models.PointField(srid=4326, null=True, blank=True)
    site_type=models.CharField()
    sample_time_seconds=models.IntegerField(default=40)
    pipe_dia_ft=models.FloatField()
    rect_full_width_ft=models.IntegerField(default=0)
    rect_full_depth_ft=models.IntegerField(default=0)
    trap_full_tw_ft=models.IntegerField(default=0)
    trap_full_bw_ft=models.IntegerField(default=0)
    trap_full_depth_ft=models.IntegerField(default=0)
    CHOICES = [
        ('Unknown', 'Unknown'),
        ('Gate Brand', 'Gate Brand'),
    ]
    gate_brand= models.CharField(
        max_length=15,
        choices=CHOICES,
        default='Unknown',
    )
    gate_type=models.CharField(default="circular_circular")
    gate_size_in=models.IntegerField(default=0)
    dead_stem_ft=models.IntegerField(default=0)
    pipe_length_ft=models.IntegerField(default=0)
    pipe_c_factor=models.IntegerField(default=0)
    minorloss_k_factor=models.IntegerField(default=0)
    weir_length_ft=models.IntegerField(default=0)
    weir_crest_type=models.CharField(default="1.5_board")
    index_vel_coeff=models.FloatField(default=0.95)
    '''index_vel_stage_coeff=models.IntegerField(default=0)
    index_offset=models.IntegerField(default=0)
    instrument_height_in_ft=models.IntegerField(default=0)
    center_beam_x_vel_coeff=models.IntegerField(default=0)
    left_beam_x_vel_coeff=models.IntegerField(default=0)
    right_beam_x_vel_coeff=models.IntegerField(default=0)
    x0=models.IntegerField(default=0)
    x1=models.IntegerField(default=1)
    x2=models.IntegerField(default=1)
    x3=models.IntegerField(default=1)
    x4=models.IntegerField(default=1)'''
    del_type=models.ForeignKey('DelType', null=False, blank=False, on_delete=models.CASCADE, default="")
    linked_turnout=models.CharField()

    def __str__(self):
        return self.msmt_point_id

class MsmtDate(models.Model):
    service_year=models.ForeignKey('ServiceYearPeriod', null=False, blank=False, on_delete=models.CASCADE, default="")
    type=models.ForeignKey('DateType', null=False, blank=False, on_delete=models.CASCADE, default="")
    start_date=models.DateField()
    end_date=models.DateField()

    def __str__(self):
        return self.service_year

class DateType(models.Model):
    name=models.CharField(null=False, blank=False, unique= True)
    description=models.TextField(unique=False, blank=True, null=False)

    def __str__(self):
        return self.name

class ServiceYearPeriod(models.Model):
    service_year=models.ForeignKey('ServiceYear', null=False, blank=False, on_delete=models.CASCADE, default="")
    service_name=models.CharField()
    period_name=models.CharField()
    start_date=models.DateField(blank=False, unique= True)
    end_date=models.DateField(blank=False, unique= True)

    def __str__(self):
        return self.service_year

class RateId(models.Model):
    rate=models.IntegerField(null=False, blank=False)
    type=models.CharField(null=False,blank=False)
    config=models.ForeignKey('Config', null=False, blank=False, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.rate

class  DistrictsAdmin(models.Model):
    district=models.ForeignKey('District',  null=False, blank=False, on_delete=models.CASCADE, default="")
    role=models.CharField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.district

class ServiceYear(models.Model):
    service_year=models.IntegerField()

    def  __str__(self):
        return self.service_year

class FieldAttribute(models.Model):
    field=models.ForeignKey('Field', null=False, blank=False, on_delete=models.CASCADE, default="")
    field_attribute_option=models.ForeignKey('FieldAttributeOption', null=False, blank=False, on_delete=models.CASCADE, default="")
    field_attribute_value=models.CharField()

    def __str__(self):
        return self.field
    
class FieldAttributeOption(models.Model):
    district=models.ForeignKey('District', null=False, blank=False, on_delete=models.CASCADE, default="")
    attribute_name=models.CharField()
    attribute_desc=models.CharField()
    attribute_datatype=models.CharField()

    def __str__(self):
        return self.district