from django.contrib import admin

# Register your models here.
from django.contrib.gis import admin
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from .models import Crop, Customer, FieldCrop, FieldCustomer, FieldInvoice, Invoice, RateStructure,Adjustment,Config, District, Field,Payment, QCDailyField,RateAcre, RateCrop, RateVol, VolDate, CustomerContact,DistrictsAdmin, ServiceYear

class CropAdmin(admin.ModelAdmin):
    list_display=('name','description','crop_duty_ft','area_enable','crop_enable','vol_enable')

class CustomerAdmin(admin.ModelAdmin):
    list_display=('name','attn','company','address_1','address_2','city','state','zip','home_phone','office_phone','mobile_phone','fax','email','accounting_key','active_date','inactive_date','active','comment')

class FieldCropAdmin(admin.ModelAdmin):
    list_display=('service_year','rate','field','crop','pct_planted','comment')

class FieldCustomerAdmin(admin.ModelAdmin):
    list_display=('customer','rate','field','service_year','pct_farmed', 'comment')

class FieldInvoiceAdmin(admin.ModelAdmin):
    list_display=('invoice','field','crop','acreage','pct_farmed','acre_rate','acre_charge','crop_rate','crop_charge','vol_start_date','vol_end_date','vol_rate','vol_del','vol_charge','field_charge','create_at','mod_at')

class InvoiceAdmin(admin.ModelAdmin):
    list_display=('customer_id','rate_id','service_year','total_acres','acre_due_date','total_acre_charge','crop_due_date','total_crop_charge','total_vol_del','vol_due_date','total_vol_charge','total_charge','total_pay','total_adj','total_remain','is_vol_final','is_void','is_final','create_at','mod_at','comments')

class RateStructureAdmin(admin.ModelAdmin):
    list_display=('name','acre_basis','acre_comp','acre_due_mn','acre_due_day','acre_year_offset','crop_comp','crop_due_mn','crop_due_day','crop_year_offset','vol_comp','vol_due_mn','vol_due_day','vol_year_offset','vol_start_mn','vol_start_day','vol_start_year_offset','vol_end_mn','vol_end_mn','vol_end_year_offset','comments')

class AdjustmentAdmin(admin.ModelAdmin):
    list_display=('invoice_id','amount','date','is_void','mod_date','comments','void_comments')

class ConfigAdmin(admin.ModelAdmin):
    list_display = ('district','qc_fall_start_mn' ,'qc_fall_start_dy' ,'qc_spring_start_dy' ,'qc_spring_start_mn' ,'use_wis')

class DistrictAdmin(admin.ModelAdmin):
    list_display = (
        'district', 'full_name', 'address', 'po_box', 'city_state_zip', 
        'office_phone', 'office_email', 'office_fax', 'website', 'county', 
        'country', 'acreage', 'established', 
    )
 
class FieldAdmin(admin.ModelAdmin,DynamicArrayMixin):
    list_display = ('field_id' , 'description' , 'acres' ,'irrig_acres', 'standby_acres','parcel_id','vol_rate_adj_id','active_date','inactive_date','active','attributes','comment')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('invoice' , 'amount' , 'date' ,'pay_number', 'is_deposit','is_void','create_at','mod_at','comments','void_comments')

class QCDailyFieldAdmin(admin.ModelAdmin):
    list_display = ('field_id' , 'date' , 'vol_af' ,'method', 'qc_flag')

class RateAcreAdmin(admin.ModelAdmin):
    list_display =('acre_rate',)

class RateCropAdmin(admin.ModelAdmin):
    list_display = ('crop'  ,'crop_rate', 'crop_enabled')

class RateVolAdmin(admin.ModelAdmin):
    list_display = ('rate','vol_rate_adj_id'  ,'vol_rate', 'vol_enabled')

class VolDateAdmin(admin.ModelAdmin):
    list_display=('service_year' , 'rate' , 'customer' ,'field', 'vol_start_date','vol_end_date','mod_at','comment')

class CustomerContactAdmin(admin.ModelAdmin):
    list_display = ('customer','name'  ,'email', 'phone','role')

class DistrictsAdminAdmin(admin.ModelAdmin):
    list_display=('district', 'role' ,'user','email')

class ServiceYearAdmin(admin.ModelAdmin):
    list_display=('service_year',)



admin.site.register(Crop , CropAdmin)
admin.site.register(Customer , CustomerAdmin)
admin.site.register(FieldCrop , FieldCropAdmin)
admin.site.register(FieldCustomer, FieldCustomerAdmin)
admin.site.register(FieldInvoice, FieldInvoiceAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(RateStructure, RateStructureAdmin)
admin.site.register(Adjustment, AdjustmentAdmin)
admin.site.register(Config, ConfigAdmin)
admin.site.register(District , DistrictAdmin)
admin.site.register(Field , FieldAdmin)
admin.site.register(Payment , PaymentAdmin)
admin.site.register(QCDailyField, QCDailyFieldAdmin)
admin.site.register(RateAcre, RateAcreAdmin)
admin.site.register(RateCrop, RateCropAdmin)
admin.site.register(RateVol, RateVolAdmin)
admin.site.register(VolDate, VolDateAdmin)
admin.site.register(DistrictsAdmin ,DistrictsAdminAdmin)
admin.site.register(ServiceYear ,ServiceYearAdmin)