# from django.shortcuts import render, redirect, HttpResponse
# from django.contrib import messages
# from django.contrib.auth.models import User, auth
# from accounts.forms import GuideForm, BookingForm
# from travello.models import Guide , Destination, Contact, Booking , Message
# from django.shortcuts import get_object_or_404
# from django.urls import reverse
# from django.contrib.auth.decorators import login_required



# def login(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]

#         user = auth.authenticate(username=username, password=password)

#         if user is not None:
#             auth.login(request, user)
#             return redirect("/")
#         else:
#             messages.info(request, "invalid credentials...")
#             return redirect("login")
#     else:
#         return render(request, "login.html")


# def register(request):
#     if request.method == "POST":
#         first_name = request.POST["first_name"]
#         last_name = request.POST["last_name"]
#         username = request.POST["username"]
#         email = request.POST["email"]
#         password1 = request.POST["password1"]
#         password2 = request.POST["password2"]

#         if password1 == password2:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, "username taken...")
#                 test = User.objects.all()
#                 print(test)
#                 return redirect("register")
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request, "email taken...")
#                 return redirect("register")
#             else:
#                 user = User.objects.create_user(
#                     username=username,
#                     password=password1,
#                     email=email,
#                     first_name=first_name,
#                     last_name=last_name,
#                 )
#                 user.save()
#                 messages.info(request, "user created...")
#                 return redirect("login")
#         else:
#             messages.info(request, "password not matched...")
#             return redirect("register")
#         return redirect("/")
#     else:
#         return render(request, "register.html")


# def logout(request):
#     auth.logout(request)
#     return redirect("/")


# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

       
#         Contact.objects.create(
#             name=name,
#             email=email,
#             subject=subject,
#             message=message,
#         )

#         messages.success(request, 'Your message has been sent successfully!')

      
#         return redirect('contact') 

#     return render(request, 'contact.html')  

# def about(request):
#     return render(request, "about.html")


# @login_required
# def dashboard(request):
#    if hasattr(request.user, 'guide'):
#       guide = request.user.guide
#       user_bookings = Booking.objects.filter(guide=guide)
#        # Get messages for current tour guide
#       guide_messages = Message.objects.filter(booking__guide=guide).order_by('timestamp')
#       return render(request, 'guide_dashboard.html', {'user_bookings': user_bookings, 'guide_messages':guide_messages})

#    else:
#         user_bookings = Booking.objects.filter(user=request.user)
#         return render(request, 'dashboard.html', {'user_bookings': user_bookings})
   

# def news(request):
#     guides = Guide.objects.all()
#     return render(request, "news.html", {"guides":guides})


# def destinations(request):
#     destinations = Destination.objects.all()
#     return render(request, 'destinations.html', {'destinations': destinations})




# def guide(request):
#     if request.method == "POST":
#         form = GuideForm(request.POST, request.FILES)
#         if form.is_valid():
#             guide_instance = form.save(commit=False)  # Do not save yet
#             guide_instance.user = request.user  # Associate with current user
#             guide_instance.save()  # Now save it
#             return redirect("/")
#     else:
#         form = GuideForm()
#     return render(request, "guideregistration.html", {"form": form})

# def guide_details(request, guide_id):
#     guide = get_object_or_404(Guide, id=guide_id)
#     return render(request, "guide_details.html", {"guide": guide})



# @login_required
# def contact_guide(request, guide_id):
#     guide = get_object_or_404(Guide, pk=guide_id)
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             # Process the form data
#             # we can add the data to booking model
#             booking = Booking(
#                 user=request.user,  # Associate the booking with the logged-in user
#                 guide=guide,
#                 first_name=form.cleaned_data['first_name'],
#                 last_name=form.cleaned_data['last_name'],
#                 email=form.cleaned_data['email'],
#                 preferred_date=form.cleaned_data['preferred_date'],
#                 party_size=form.cleaned_data['party_size'],
#                 message=form.cleaned_data['message'],
#                 accept_terms=form.cleaned_data['accept_terms'],
#                 accept_marketing_emails=form.cleaned_data['accept_marketing_emails'],
               
#             )
#             booking.save()

#             message = "Thank you for contacting " + guide.first_name + " " + guide.last_name + ". We will reach out to you soon."
#             messages.success(request, message)
#             return redirect(reverse('index'))
#     else:
#         form = BookingForm()
#     return render(request, 'message.html', {'form': form, 'guide':guide})


from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import GuideForm, BookingForm
from travello.models import Guide , Destination, Contact, Booking, Message
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

def login(request):
 if request.method == "POST":
   username = request.POST["username"]
   password = request.POST["password"]

   user = auth.authenticate(username=username, password=password)
   if user is not None:
       auth.login(request, user)
       if hasattr(user, 'guide'):
           return redirect(reverse("dashboard"))
       else:
           return redirect(reverse("index"))
   else:
      messages.info(request, "invalid credentials...")
      return redirect("login")
 else:
   return render(request, "login.html")


def register(request):
 if request.method == "POST":
     first_name = request.POST["first_name"]
     last_name = request.POST["last_name"]
     username = request.POST["username"]
     email = request.POST["email"]
     password1 = request.POST["password1"]
     password2 = request.POST["password2"]

     if password1 == password2:
         if User.objects.filter(username=username).exists():
             messages.info(request, "username taken...")
             test = User.objects.all()
             print(test)
             return redirect("register")
         elif User.objects.filter(email=email).exists():
             messages.info(request, "email taken...")
             return redirect("register")
         else:
             user = User.objects.create_user(
                 username=username,
                 password=password1,
                 email=email,
                 first_name=first_name,
                 last_name=last_name,
             )
             user.save()
             messages.info(request, "user created...")
             return redirect("admin:login")
     else:
         messages.info(request, "password not matched...")
         return redirect("admin:register")
     return redirect("/")
 else:
     return render(request, "register.html")


def logout(request):
 return auth_views.LogoutView.as_view(next_page="/")(request)

def contact(request):
 if request.method == 'POST':
     name = request.POST.get('name')
     email = request.POST.get('email')
     subject = request.POST.get('subject')
     message = request.POST.get('message')

    
     Contact.objects.create(
         name=name,
         email=email,
         subject=subject,
         message=message,
     )

     messages.success(request, 'Your message has been sent successfully!')

   
     return redirect('contact') 

 return render(request, 'contact.html')  

def about(request):
 return render(request, "about.html")

@login_required
def dashboard(request):
 if hasattr(request.user, 'guide'):
   guide = request.user.guide
   user_bookings = Booking.objects.filter(guide=guide)
    # Get messages for current tour guide
   guide_messages = Message.objects.filter(booking__guide=guide).order_by('timestamp')
   return render(request, 'guide_dashboard.html', {'user_bookings': user_bookings, 'guide_messages':guide_messages})

 else:
     user_bookings = Booking.objects.filter(user=request.user)
     return render(request, 'dashboard.html', {'user_bookings': user_bookings})


def news(request):
 guides = Guide.objects.all()
 return render(request, "news.html", {"guides":guides})


def destinations(request):
 destinations = Destination.objects.all()
 return render(request, 'destinations.html', {'destinations': destinations})

def guide(request):
 if request.method == "POST":
     form = GuideForm(request.POST, request.FILES)
     if form.is_valid():
          guide = form.save(commit=False)
          guide.user = request.user
          guide.save()
          return redirect("/") 
 else:
     form = GuideForm()
 return render(request, "guideregistration.html", {"form": form})


def guide_details(request, guide_id):
 guide = get_object_or_404(Guide, id=guide_id)
 return render(request, "guide_details.html", {"guide": guide})

@login_required
def contact_guide(request, guide_id):
 guide = get_object_or_404(Guide, pk=guide_id)
 if request.method == 'POST':
     form = BookingForm(request.POST)
     if form.is_valid():
         # Process the form data
         # we can add the data to booking model
         booking = Booking(
             first_name=form.cleaned_data['first_name'],
             last_name=form.cleaned_data['last_name'],
             email=form.cleaned_data['email'],
             preferred_date=form.cleaned_data['preferred_date'],
             party_size=form.cleaned_data['party_size'],
             message=form.cleaned_data['message'],
             accept_terms=form.cleaned_data['accept_terms'],
             accept_marketing_emails=form.cleaned_data['accept_marketing_emails'],
             guide=guide,
              user=request.user
         )
         booking.save()

         message = "Thank you for contacting " + guide.first_name + " " + guide.last_name + ". We will reach out to you soon."
         messages.success(request, message)
         return redirect(reverse('index'))
 else:
     form = BookingForm()
 return render(request, 'message.html', {'form': form, 'guide':guide})
@login_required
def edit_booking(request, booking_id):
 booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
 if request.method == 'POST':
     form = BookingForm(request.POST, instance=booking)
     if form.is_valid():
         form.save()
         messages.success(request, "Booking updated successfully.")
         return redirect(reverse('dashboard'))
 else:
     form = BookingForm(instance=booking)
 return render(request, 'edit_booking.html', {'form': form, 'booking': booking})


@login_required
def delete_booking(request, booking_id):
 booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
 if request.method == 'POST':
     booking.delete()
     messages.success(request, "Booking deleted successfully.")
     return redirect(reverse('dashboard'))
 return render(request, 'delete_booking.html', {'booking': booking})