# from django.db import models

# Create your models here.


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from tinymce.models import HTMLField

# # Create your models here.
# from collectionfield.models import CollectionField
from django.contrib.auth.models import User
from datetime import datetime as dt
# from model_utils import Choices
# from moneyfield import MoneyField


# class Profile(models.Model):

#     user=models.OneToOneField(User, on_delete=models.CASCADE, blank=True, related_name='profile')
#     pub_date = models.DateField(auto_now_add=True)
#     profile_photo = models.ImageField(upload_to = 'profile/') 
#     bio = models.TextField(max_length=255) 
    

    

    # @classmethod  
    # def find_profile(cls,first_name):
    #     profile = Profile.objects.filter(user=username).all()
    #     return profile

    # def save_user(self):
    #      self.save()

    # def delete_profile(self):
    #     self.delete()     

    # def __str__(self):
    #     return self.user.username


class Booking(models.Model):

    name = models.CharField(max_length=30,null=True)
    email = models.EmailField(max_length=70,blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,null=True, related_name='user_booking')
    listing = models.ForeignKey('Listing', on_delete=models.CASCADE, related_name='listing_booking')
    Timeslot = models.ForeignKey('Timeslot', on_delete=models.CASCADE, related_name='timeslot_booking')
   
    

    @classmethod  
    def find_bookings(cls,name):
        bookings = Bookings.objects.filter_by_name(name__icontains=name).all()

        return profile

    @classmethod   
    def get_all_booking(cls,id):
        booking=Booking.objects.filter(id=id).all()

    def save_user(self):
         self.save()

    def delete_bookings(self):
        self.delete()     

    def __str__(self):
        return self.name





class Timeslot(models.Model):

    # title = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True,blank=True, null=True)
    start_time = models.DateField(auto_now_add=True,blank=True, null=True)
    end_time = models.DateField(auto_now_add=True,blank=True, null=True)
    # booking = models.ForeignKey(Booking,null=True,related_name='timeslot_booking')
    # user = models.OneToOneField(User,on_delete=models.CASCADE,null=True, blank=True, related_name='timeslot_user')

    class meta:
        ordering = ['-date'] 


    def save_timeslot(self):
        self.save()

    @classmethod
    def get_all_timeslots(cls,id):
        timeslots = cls.objects.filter(id=id).order_by('-date')
        return timeslots

    def __str__(self):
        return str(self.date)



class Image(models.Model):
   
    title = models.CharField(max_length=50)
    # listing = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now_add=True)
    image_path = models.ImageField(upload_to = 'images/')
    # image = models.OneToOneField(User, related_name='image_likes',null=True , blank=True)
    # profile = models.ForeignKey('Profile', on_delete=models.CASCADE, default=0, related_name='timeslot_booking')
  



    class meta:
        ordering = ['-pub_date'] 


    @classmethod
    def get_all(cls, id):
        images = cls.objects.filter(id=id).all()
        return images


    def save_image(self):
        self.save()


    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls, id, update):
        updated =cls.objects.filter(id=id).update(image = update)

        return updated
      
        
    @classmethod
    def search_users(cls, search_term):
        profiles = cls.objects.filter(username__icontains=search_term)
        return profiles
                
        

    class meta:
        ordering = ['-pub_date'] 



    def __str__(self):
        return self.title


class Listing(models.Model):
    apartments = "apartments"
    Bungalows = "bungalows"
    Massionettes = "mansionattes"

    PROPERTY_CHOICES = [
    (apartments, "apartments"),
    (Bungalows, "bungalows"),
    (Massionettes, "massionattes")
    ]



    title = models.CharField(max_length=50,)
    location = models.CharField(max_length=100,null=True)
    category = models.CharField(max_length=255,null=True, choices=PROPERTY_CHOICES, default=apartments)
    description = models.CharField(max_length=255,null=True)
    bedrooms = models.CharField(max_length=255,null=True)
    # pricing = MoneyField(decimal_places=2,default=0,default_currency='USD',max_digits=11,)
    pricing = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    featured_pic_path = models.ImageField(upload_to = 'list/')
    user = models.ForeignKey(User,related_name='listings', null=True, on_delete=models.CASCADE, blank=True,)
    timeslot = models.ForeignKey(Timeslot,null=True, on_delete=models.CASCADE, related_name='timeslots')
    booking = models.ForeignKey(Booking,null=True, on_delete=models.CASCADE, related_name='bookings')
    # profile = models.ForeignKey('Profile', on_delete=models.CASCADE, default=0, related_name='listing_profile')
    # apartment = models.ForeignKey("Apartment",related_name='apartment')

    @classmethod
    def get_all(cls):
        listing = cls.objects.all()
        return listing

    def get_listing(self,id):
        listing = Listing.objects.filter(listing_id=id).all()
        return listing
            

    @classmethod
    def search_by_name(cls,search_term):
        listing = cls.objects.filter(title__icontains=search_term)
        return listing

    @classmethod
    def show_by_category(cls, category):
        listing = cls.objects.filter(category=category).all()
        return listing
    

    def save_listing(self):
        self.save()  

    def delete_listing(self):
        self.delete()      


    def __str__(self):
        return self.category

    
