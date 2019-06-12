from django.contrib import admin
from testapp.models import banglorejobs,jaipurjobs,gurgaonjobs
# Register your models here.
class banglorejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email',
    'phonenumber']

class jaipurjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email',
    'phonenumber']

class gurgaonjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email',
    'phonenumber']

admin.site.register(banglorejobs,banglorejobsAdmin)
admin.site.register(jaipurjobs,jaipurjobsAdmin)
admin.site.register(gurgaonjobs,gurgaonjobsAdmin)
