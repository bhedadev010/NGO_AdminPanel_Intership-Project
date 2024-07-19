from django.contrib import admin
from .models import category,country,state,city,volunteer,ngo,donor,donation

# Register your models here.

class Category(admin.ModelAdmin):
    list_display = ['name','description']

class Country(admin.ModelAdmin):
    list_display = ['name']

class State(admin.ModelAdmin):
    list_display= ['name','country_name']

class City(admin.ModelAdmin):
    list_display = ['name','state_name']

class Volunteer(admin.ModelAdmin):
    list_display=['name','age','email','phone','gender','description','city']

class Ngo(admin.ModelAdmin):
    list_display=['ngo_name','ngo_category','ngo_address','ngo_city','ngo_website']

class Donor(admin.ModelAdmin):
    list_display=['donor_name','donor_email','donor_phone','donor_gender']

class Donation(admin.ModelAdmin):
    list_display=['donor_name','ngo_name','amount','date']

admin.site.register(category, Category)
admin.site.register(country, Country)
admin.site.register(state, State)
admin.site.register(city, City)
admin.site.register(volunteer, Volunteer)
admin.site.register(ngo, Ngo)
admin.site.register(donor, Donor)
admin.site.register(donation, Donation)