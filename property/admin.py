# from django.contrib import admin

# Register your models here.


# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.contrib import admin
from property import models


# Register your models here.


from property.models import Listing,Image,Booking,Timeslot


admin.site.site_header="RentOrBuy"
admin.site.site_title="Admin"

@admin.register(models.Listing)
class ListingAdmin(admin.ModelAdmin):

    # date_hierarchy = 'created'
    search_fields = ['title', 'location',]
    list_display = ('id','title','location','bedrooms','pricing','category',)
    # list_filter = ('status',)

# @admin.register(models.Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('pub_date','profile_photo','bio',)



@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id','title','pub_date','image_path')


@admin.register(models.Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name','email','contact','address') 


@admin.register(models.Timeslot)
class TimeslotAdmin(admin.ModelAdmin):
    list_display = ('date','start_time','end_time')




    
    

    # admin.site.register(Profile)
    # admin.site.register(Image)
    # admin.site.register(Booking)
    # admin.site.register(Timeslot)
    # admin.site.register(Apartment)
    # admin.site.register(Bungalow)

