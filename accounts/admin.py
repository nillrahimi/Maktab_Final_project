from django.contrib import admin
from .models import *

from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin


@admin.register(CustomUser)
class CustomUserInAdmin(ModelAdminJalaliMixin, admin.ModelAdmin): 
    model = CustomUser
    list_display = ['email','username','is_staff','is_superuser']
    list_editable = ['username']
    empty_value_display = '---'
    list_filter = ['first_name','last_name']
    search_fields = ['username', 'last_name']
    list_per_page = 5
    def created_time_jalali(self, obj):
        return datetime2jalali(obj.created_time).strftime('%y/%m/%d _ %H:%M:%S')


@admin.register(Customer)
class CustomCustomer(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ["id",'email','username','first_name','last_name', 'created_time_jalali']
    list_display_links = ['username']
    list_editable = ['first_name','last_name']
    list_filter = ['first_name','last_name']
    search_fields = ['username', 'last_name']
    # date_hierarchy = 'created_at'
    empty_value_display = '---'
    list_per_page = 5

    def get_queryset(self, request):
        return Customer.objects.filter(is_staff= False)

    def created_time_jalali(self, obj):
        return datetime2jalali(obj.date_joined).strftime('%y/%m/%d _ %H:%M:%S')


@admin.register(Admin)
class CustomAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ["id",'email','username', 'created_time_jalali']
    list_display_links = ['username']
    # list_editable = ['']
    list_filter = ['first_name','last_name'] #status
    search_fields = ["username", "last_name"]
    empty_value_display = '---'
    list_per_page = 5

    def get_queryset(self, request):
        return Admin.objects.filter(is_superuser = True)
        
    def created_time_jalali(self, obj):
        return datetime2jalali(obj.date_joined).strftime('%y/%m/%d _ %H:%M:%S')


@admin.register(Manager)
class CustomManager(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ["id",'email','username','first_name','last_name', 'created_time_jalali']
    list_display_links = ['username']
    list_editable = ['first_name','last_name']
    list_filter = ['first_name','last_name']
    # search_fields = ["username", "last_name"]
    empty_value_display = '---'
    list_per_page = 5

    def get_queryset(self, request):
        return Manager.objects.filter(is_staff= True, is_superuser = False)

    def created_time_jalali(self, obj):
        return datetime2jalali(obj.date_joined).strftime('%y/%m/%d _ %H:%M:%S')



   



