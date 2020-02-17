# from django.shortcuts import render

# # Create your views here.



# from django.http  import HttpResponse

# # Create your views here.
# def welcome(request):
#     return HttpResponse('Welcome to the Moringa Tribune')


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout,login
# from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from . models import Image,Listing,Booking,Timeslot
from .forms import NewImageForm,ListingForm,BookingForm,SignUpForm,TimeForm

# Create your views here.




def index(request):

    '''
    View home function that returns the home page
    '''
  
    listings = Listing.objects.all()
    print(listings)

    apartments = Listing.objects.filter(category__contains="apartments").all()
    print(apartments)

    mansionattes = Listing.objects.filter(category__contains="mansionattes").all()
    print(mansionattes)

    bungalows = Listing.objects.filter(category__contains="bungalows").all()
    print(bungalows)
    

    
    return render(request, 'home.html', {"listings":listings, "apartments": apartments,"mansionattes":mansionattes,"bungalows":bungalows})

# this code logs out the current user (logout function)
# def logout_view(request):
#     logout(request)
    # return HttpResponseRedirect('/index_page/')
    #  return HttpResponseRedirect('/loginpage/')
    # return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))



def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST, request.FILES)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username =username, password=raw_password)
			login(request, user)
		return redirect('index_page')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {"form":form})




@login_required(login_url='/accounts/login/')
def profile(request,username):

        '''
        View profile funtion that returns the profile page and data
        '''
    # if username:
    #     username = request.user.username
    # listing by user id
    
        listings = Listing.objects.filter(user_id=username)
        bookings = Booking.objects.filter(user_id=username)
        profiles = User.objects.filter(username=username)
    
    
   
        print('No such user')
        return render (request, 'profile/profile.html',  {'profiles':profiles, "listings":listings, "bookings": bookings})




@login_required(login_url='/accounts/login/')
def listing(request):

    '''
    View listing function that returns the listing page and data
    '''
    # form = ListingForm()
    current_user = request.user
    if request.method == 'POST':
        form = ListingForm(request.POST,request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user = current_user
            listing.save()
        return redirect('index_page') 
    else: 

        form = ListingForm() 

    return render(request, 'listing_form.html', {"form": form})




@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('index_page')

    else:
        form = NewImageForm()
    return render(request, 'registration/new_image.html', {"form": form})





@login_required(login_url='/accounts/login/')
def booking(request,id):

    '''
    View booking function that returns the booking page and data
    '''
    timeslot = Timeslot.objects.filter(id=id).all()
    listing = Listing.objects.filter(id=id).all()

    form = BookingForm()
    current_user = request.user
    print(current_user)
    if request.method == 'POST':
        form = BookingForm(request.POST,request.FILES)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = current_user
            booking.save()
        return redirect('index_page') 
    else: 

       form = BookingForm() 

    title = 'Home | Boma Listing'
    return render(request, 'booking_form.html', {"title":title,"form": form,"timeslot":timeslot,"listing":listing,"current_user":current_user})




@login_required(login_url='/accounts/login/')
def single_listing(request,id):

    '''
    View listing function that returns the listing page and data
    '''
     
    
    listings = Listing.objects.get(id=id)
    timeslots = Timeslot.objects.filter(id=id)
    user = User.objects.filter(id=id)

    

    title = 'Home | Boma Listing'
    return render(request, 'single_listing.html', {"listings": listings, "timeslots":timeslots, "user":user})


@login_required(login_url='/accounts/login/')
def listing_times(request,id):

    '''
    View listing function that returns the listing page and data
    '''
    # current_user = request.user

    listing = Listing.objects.get(id=id)
    timeslot = Timeslot.objects.filter(id=id).all()
    user = User.objects.filter(id=id)

    form = TimeForm()
    current_user = request.user
    print(current_user)
    if request.method == 'POST':
        # form = TimeForm(request.POST,request.FILES)
        # if form.is_valid():
            # date =request.GET.get("party-date")
            # start =request.GET.get("party-time")
            # end =request.GET.get("party-time2")    
            # times = Timeslot..save(commit=False)
            # time.user = current_user
            # time.save()
            if request.POST.get("party_date") and request.POST.get("party-time") and request.POST.get("party-time2"):
                timeslots = Timeslot()
                timeslot.party_date = request.POST.get("party_date")
                print(timeslot.party_date)
                timeslot.party_time = request.POST.get("party_time")
                print(timeslot.party_date)
                timeslot.party_time2 = request.POST.get("party_time2")
                print(timeslot.party_time2)
                timeslot.save()
                
            return redirect('index_page') 
    else: 
        
        form = TimeForm() 
        

        # title = 'Home | Boma Listing'
        return render(request, 'listing_time.html', {"listing": listing, "timeslot":timeslot, "user":user})








