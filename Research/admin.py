from django.contrib import admin
from .models import Canal , MsmtMethod,QcCode, Config, Constant, Day , DelType, District  , fg_to_vol , FieldGroupName ,  FieldGrower, Field, FieldSite, FieldTurnout, FinalData, FinalOrder, Grower, GrowerCredit, LoadData, LoadOrder,MeterInfo, QCDailyFieldGroup, QCDailyField, QCDailyFieldSite, QCDailyTurnout,QCParam, RawData, RawOrder, Route, Turnout

class CanalAdmin(admin.ModelAdmin):
    list_display = ('canal_id', 'name',  'parent_canal','carriage_loss', 'description')
class Msmt_MethodAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'description')

class Qc_CodeAdmin(admin.ModelAdmin):
    list_display = ( 'name','category' , 'description' )

class ConfigAdmin(admin.ModelAdmin):
    list_display = ('district','qc_fall_start_mn' ,'qc_fall_start_dy' ,'qc_spring_start_dy' ,'qc_spring_start_mn' ,'allotment_ft' ,'days_to_export' ,'show_co_mingled_mult' ,'co_mingled_mult' ,'use_standBby_flow_duty' ,'use_wad' ,'use_wad_cost_flow' ,'canal_mgmt_return' ,'flow_spring_start_mn' ,'flow_spring_start_dy' ,'flow_fall_start_mn' ,'flow_fall_start_dy' ,'rate_id_spring_flow' ,'rate_id_fall_flow' ,'use_wad_owner_flow' ,'rate_id_spring_owner_flow' ,'rate_id_fall_owner_flow' )

class ConstantAdmin(admin.ModelAdmin):
    list_display = ('name' , 'value' , 'active_flag' ,'note')

class DayAdmin(admin.ModelAdmin):
    list_display =('rec_date','season','weekend','holiday','water_year','j_date')

class DelTypeAdmin(admin.ModelAdmin):
    list_display =('delivery_spill','description')

class DistrictAdmin(admin.ModelAdmin):
    list_display = (
        'district', 'full_name', 'address', 'po_box', 'city_state_zip', 
        'office_phone', 'office_email', 'office_fax', 'website', 'county', 
        'country', 'acerage', 'established', 
    )
class fg_to_volAdmin(admin.ModelAdmin):
    list_display = ('fg_id' , 'date' , 'sum_of_vol_af' ,'count_of_vol_af')

class FieldGroupNameAdmin(admin.ModelAdmin):
    list_display = ('site_id' , 'turnout_id' , 'name' ,'field_group_no')

class FieldGrowerAdmin(admin.ModelAdmin):
    list_display = ('grower', 'field','season_id' ,'service_year')

class FieldAdmin(admin.ModelAdmin):
    list_display = ('field_id' , 'description' , 'acres' ,'irrig_acres', 'standby_acres','parcel_id','vol_rate_adj_id','active_date','inactive_date','active_flag','comment')

class FieldSiteAdmin(admin.ModelAdmin):
    list_display = ('site_id' , 'field_id' , 'method' ,'active_date', 'inactive_date','active_flag','comment')

class FieldTurnoutAdmin(admin.ModelAdmin):
    list_display = ('turnout_id' , 'field_id','active_date', 'inactive_date','active_flag','comment')

class FinalDataAdmin(admin.ModelAdmin):
    list_display = ('site_id' , 'rec_date_time','q_cfs', 'msmt_method','user','ft_avg_signal_beam1', 'ft_avg_signal_beam2','ft_avg_noise_beam1', 'ft_avg_noise_beam2','ft_avg_snr_beam1','ft_avg_snr_beam2', 'ft_avg_temp_f','ft_avg_batt_voltage_v', 'ft_avg_vx_fps','ft_stdev_vx_fps','ft_avg_vy_fps', 'ft_stdev_vy_fps','ft_area_sqft', 'ft_avg_q_cfs','ft_avg_q_angle_deg','auto_start', 'auto_sample','auto_locate', 'gate_full_stem_ft','gate_us_level_ft','gate_ds_level_ft', 'gate_q_cfs','weir_height_ft', 'weir_q_cfs','meter_total_af','meter_q_cfs', 'rt_manual_q_cfs','iq_avg_depth_ft', 'iq_avg_temp_c','iq_avg_vxc_fps','iq_stdev_vxc_fps', 'iq_avg_vzc_fps','iq_avg_vxl_fps', 'iq_stdev_vxl_fps','iq_avg_vxr_fps','iq_stdev_vxr_fps', 'iq_avg_batt_voltage_v','iq_avg_pitch_deg', 'iq_avg_roll_deg','iq_avg_in_water','iq_avg_snr_beam1', 'iq_avg_snr_beam2','iq_avg_snr_beam3', 'iq_avg_snr_beam4','iq_avg_stage_ft','iq_avg_area_sqft', 'iq_avg_vx_fps','comments', 'batch_datetime','qc_code','row_id','recompute')

class FinalOrderAdmin(admin.ModelAdmin):
    list_display = ('site_id' , 'order_date_time' , 'rec_date_time' ,'user', 'order_q_cfs','current_q_cfs','delivered_q_cfs','comments','batch_datetime','qc_code','row_id','recompute')

class GrowerAdmin(admin.ModelAdmin):
    list_display = ('customer_id' , 'grower_name' , 'grower_phone' ,'grower_email', 'comment','active_flag')

class GrowerCreditAdmin(admin.ModelAdmin):
    list_display = ('grower_id' , 'credit_date' , 'credit_af' ,'comment')

class LoadDataAdmin(admin.ModelAdmin):
    list_display = ('site_id' , 'date_time','q_cfs', 'msmt_method','user','ft_avg_signal_beam1', 'ft_avg_signal_beam2','ft_avg_noise_beam1', 'ft_avg_noise_beam2','ft_avg_snr_beam1','ft_avg_snr_beam2', 'ft_avg_temp_f','ft_avg_batt_voltage_v', 'ft_avg_vx_fps','ft_stdev_vx_fps','ft_avg_vy_fps', 'ft_stdev_vy_fps','ft_area_sqft', 'ft_avg_q_cfs','ft_avg_q_angle_deg','auto_start', 'auto_sample','auto_locate', 'gate_full_stem_ft','gate_us_level_ft','gate_ds_level_ft', 'gate_q_cfs','weir_height_ft', 'weir_q_cfs','meter_total','meter_q', 'rt_manual_q_cfs','iq_avg_depth_ft', 'iq_avg_temp_c','iq_avg_vxc_fps','iq_stdev_vxc_fps', 'iq_avg_vzc_fps','iq_avg_vxl_fps', 'iq_stdev_vxl_fps','iq_avg_vxr_fps','iq_stdev_vxr_fps', 'iq_avg_batt_voltage_v','iq_avg_pitch_deg', 'iq_avg_roll_deg','iq_avg_in_water','iq_avg_snr_beam1', 'iq_avg_snr_beam2','iq_avg_snr_beam3', 'iq_avg_snr_beam4','iq_avg_stage_ft','iq_avg_area_sqft', 'iq_avg_vx_fps','comments',)

class LoadOrderAdmin(admin.ModelAdmin):
    list_display = ('site_id' , 'order_date_time' , 'rec_date_time' ,'user', 'order_q_cfs','current_q_cfs','delivered_q_cfs','comment')

class MeterInfoAdmin(admin.ModelAdmin):
    list_display = ('turnout_id' , 'meter_no' , 'make' ,'model', 'flow_units','flow_multiplier','totalizer_units','totalizer_reset_value','totalizer_multiplier','active_date','inactive_date','active_flag','comments')

class QCDailyFieldGroupAdmin(admin.ModelAdmin):
    list_display = ('site_id' , 'rec_date' , 'volume_af' ,'duration_hr', 'no_rec','code','mode_date')

class QCDailyFieldAdmin(admin.ModelAdmin):
    list_display = ('field_id' , 'date' , 'vol_af' ,'method', 'qc_flag')

class QCDailyFieldSiteAdmin(admin.ModelAdmin):
    list_display = ('site_id' , 'field_id' , 'rec_date' ,'method', 'total_vol_af' , 'duration_hr' , 'no_rec' ,'total_ac', 'field_acres' , 'area_adj_fac' , 'app_vol_af' ,'qc_flag')

class QCDailyTurnoutAdmin(admin.ModelAdmin):
    list_display=('site_id','rec_date' ,'volume_af', 'duration_hr' , 'no_rec' , 'code' ,'mod_date')

class QCParamAdmin(admin.ModelAdmin):
    list_display=('turnout_id','us_min' ,'us_max', 'ds_min' , 'ds_max' , 'gate_min' ,'gate_max','q_ang_min','q_ang_max' ,'temp_min', 'temp_max' , 'snr1_min' , 'snr2_min' ,'weir_min','weir_max','q_min' ,'q_max', 'meter_total_min' , 'meter_total_max' , 'meter_q_min' ,'meter_q_max','active_date','inactive_date' ,'active_flag')

class RawDataAdmin(admin.ModelAdmin):
    list_display = ('site_id' , 'date_time','q_cfs', 'msmt_method','user','ft_avg_signal_beam1', 'ft_avg_signal_beam2','ft_avg_noise_beam1', 'ft_avg_noise_beam2','ft_avg_snr_beam1','ft_avg_snr_beam2', 'ft_avg_temp_f','ft_avg_batt_voltage_v', 'ft_avg_vx_fps','ft_stdev_vx_fps','ft_avg_vy_fps', 'ft_stdev_vy_fps','ft_area_sqft', 'ft_avg_q_cfs','ft_avg_q_angle_deg','auto_start', 'auto_sample','auto_locate', 'gate_full_stem_ft','gate_us_level_ft','gate_ds_level_ft', 'gate_q_cfs','weir_height_ft', 'weir_q_cfs','meter_total','meter_q', 'rt_manual_q_cfs','iq_avg_depth_ft', 'iq_avg_temp_c','iq_avg_vxc_fps','iq_stdev_vxc_fps', 'iq_avg_vzc_fps','iq_avg_vxl_fps', 'iq_stdev_vxl_fps','iq_avg_vxr_fps','iq_stdev_vxr_fps', 'iq_avg_batt_voltage_v','iq_avg_pitch_deg', 'iq_avg_roll_deg','iq_avg_in_water','iq_avg_snr_beam1', 'iq_avg_snr_beam2','iq_avg_snr_beam3', 'iq_avg_snr_beam4','iq_avg_stage_ft','iq_avg_area_sqft', 'iq_avg_vx_fps', 'batch_datetime','qcd_flag','row_id','qc_code','comments')


class RawOrderAdmin(admin.ModelAdmin):
    list_display=('site_id', 'order_date_time','rec_date_time', 'user','order_q_cfs','current_q_cfs', 'delivered_q_cfs', 'batch_datetime','qcd_flag','row_id','comments')

class RouteAdmin(admin.ModelAdmin):
    list_display=('name', 'description','operator_1', 'operator_2','operator_3','operator_4')
    
class TurnoutAdmin(admin.ModelAdmin):
    list_display=('turnout_id','name' ,'type', 'route' , 'canal' , 'latitude' ,'longitude','site_type_flag','sample_time_seconds' ,'pipe_dia_ft', 'rect_full_width_ft' , 'rect_full_depth_ft' , 'trap_full_tw_ft' ,'trap_full_bw_ft','trap_full_depth_ft','gate_brand' ,'gate_type', 'gate_size_in' , 'dead_stem_ft' , 'pipe_length_ft' ,'pipe_c_factor','minorloss_k_factor','weir_length_ft' ,'weir_crest_type', 'index_vel_coeff' ,'index_vel_stage_coeff','index_offset','instrument_height_in_ft' ,'center_beam_x_vel_coeff','left_beam_x_vel_coeff' ,'right_beam_x_vel_coeff', 'x0' , 'x1' , 'x2' ,'x3','x4','del_type' ,'linked_turnout')


admin.site.register(Canal , CanalAdmin)
admin.site.register(MsmtMethod , Msmt_MethodAdmin)
admin.site.register(QcCode, Qc_CodeAdmin)
admin.site.register(Config, ConfigAdmin)
admin.site.register(Constant , ConstantAdmin)
admin.site.register(Day , DayAdmin)
admin.site.register(DelType , DelTypeAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(fg_to_vol , fg_to_volAdmin)
admin.site.register(FieldGroupName , FieldGroupNameAdmin)
admin.site.register(FieldGrower , FieldGrowerAdmin)
admin.site.register(Field , FieldAdmin)
admin.site.register(FieldSite , FieldSiteAdmin)
admin.site.register(FieldTurnout , FieldTurnoutAdmin)
admin.site.register(FinalData , FinalDataAdmin)
admin.site.register(FinalOrder , FinalOrderAdmin)
admin.site.register(Grower , GrowerAdmin)
admin.site.register(GrowerCredit , GrowerCreditAdmin)
admin.site.register(LoadData , LoadDataAdmin)
admin.site.register(LoadOrder , LoadOrderAdmin)
admin.site.register(MeterInfo , MeterInfoAdmin)
admin.site.register(QCDailyFieldGroup , QCDailyFieldGroupAdmin)
admin.site.register(QCDailyField , QCDailyFieldAdmin)
admin.site.register(QCDailyFieldSite , QCDailyFieldSiteAdmin)
admin.site.register(QCDailyTurnout , QCDailyTurnoutAdmin)
admin.site.register(QCParam, QCParamAdmin)
admin.site.register(RawData , RawDataAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Turnout, TurnoutAdmin)