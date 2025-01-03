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


# from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
# from django.contrib import messages
# from django.contrib.auth.models import User, auth
# from django.contrib.auth import authenticate, login
# from .forms import GuideForm, BookingForm
# from travello.models import Guide , Destination, Contact, Booking, Message
# from django.urls import reverse
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import views as auth_views
# from .forms import ReplyForm

# def login(request):
#  if request.method == "POST":
#    username = request.POST["username"]
#    password = request.POST["password"]

#    user = auth.authenticate(username=username, password=password)
#    if user is not None:
#        auth.login(request, user)
#        if hasattr(user, 'guide'):
#            return redirect(reverse("dashboard"))
#        else:
#            return redirect(reverse("index"))
#    else:
#       messages.info(request, "invalid credentials...")
#       return redirect("login")
#  else:
#    return render(request, "login.html")


# def register(request):
#  if request.method == "POST":
#      first_name = request.POST["first_name"]
#      last_name = request.POST["last_name"]
#      username = request.POST["username"]
#      email = request.POST["email"]
#      password1 = request.POST["password1"]
#      password2 = request.POST["password2"]

#      if password1 == password2:
#          if User.objects.filter(username=username).exists():
#              messages.info(request, "username taken...")
#              test = User.objects.all()
#              print(test)
#              return redirect("register")
#          elif User.objects.filter(email=email).exists():
#              messages.info(request, "email taken...")
#              return redirect("register")
#          else:
#              user = User.objects.create_user(
#                  username=username,
#                  password=password1,
#                  email=email,
#                  first_name=first_name,
#                  last_name=last_name,
#              )
#              user.save()
#              messages.info(request, "user created...")
#              return redirect("admin:login")
#      else:
#          messages.info(request, "password not matched...")
#          return redirect("admin:register")
#      return redirect("/")
#  else:
#      return render(request, "register.html")


# def logout(request):
#  return auth_views.LogoutView.as_view(next_page="/")(request)

# def contact(request):
#  if request.method == 'POST':
#      name = request.POST.get('name')
#      email = request.POST.get('email')
#      subject = request.POST.get('subject')
#      message = request.POST.get('message')

    
#      Contact.objects.create(
#          name=name,
#          email=email,
#          subject=subject,
#          message=message,
#      )

#      messages.success(request, 'Your message has been sent successfully!')

   
#      return redirect('contact') 

#  return render(request, 'contact.html')  

# def about(request):
#  return render(request, "about.html")

# @login_required
# def dashboard(request):
#  if hasattr(request.user, 'guide'):
#    guide = request.user.guide
#    user_bookings = Booking.objects.filter(guide=guide)
#     # Get messages for current tour guide
#    guide_messages = Message.objects.filter(booking__guide=guide).order_by('timestamp')
#    return render(request, 'guide_dashboard.html', {'user_bookings': user_bookings, 'guide_messages':guide_messages})

#  else:
#      user_bookings = Booking.objects.filter(user=request.user)
#      return render(request, 'dashboard.html', {'user_bookings': user_bookings})


# def news(request):
#  guides = Guide.objects.all()
#  return render(request, "news.html", {"guides":guides})


# def destinations(request):
#  destinations = Destination.objects.all()
#  return render(request, 'destinations.html', {'destinations': destinations})

# def guide(request):
#  if request.method == "POST":
#      form = GuideForm(request.POST, request.FILES)
#      if form.is_valid():
#           guide = form.save(commit=False)
#           guide.user = request.user
#           guide.save()
#           return redirect("guide_login") 
#  else:
#      form = GuideForm()
#  return render(request, "guideregistration.html", {"form": form})


# def guide_details(request, guide_id):
#  guide = get_object_or_404(Guide, id=guide_id)
#  return render(request, "guide_details.html", {"guide": guide})

# @login_required
# def contact_guide(request, guide_id):
#  guide = get_object_or_404(Guide, pk=guide_id)
#  if request.method == 'POST':
#      form = BookingForm(request.POST)
#      if form.is_valid():
#          # Process the form data
#          # we can add the data to booking model
#          booking = Booking(
#              first_name=form.cleaned_data['first_name'],
#              last_name=form.cleaned_data['last_name'],
#              email=form.cleaned_data['email'],
#              preferred_date=form.cleaned_data['preferred_date'],
#              party_size=form.cleaned_data['party_size'],
#              message=form.cleaned_data['message'],
#              accept_terms=form.cleaned_data['accept_terms'],
#              accept_marketing_emails=form.cleaned_data['accept_marketing_emails'],
#              guide=guide,
#               user=request.user
#          )
#          booking.save()

#          message = "Thank you for contacting " + guide.first_name + " " + guide.last_name + ". We will reach out to you soon."
#          messages.success(request, message)
#          return redirect(reverse('index'))
#  else:
#      form = BookingForm()
#  return render(request, 'message.html', {'form': form, 'guide':guide})


# @login_required
# def edit_booking(request, booking_id):
#  booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
#  if request.method == 'POST':
#      form = BookingForm(request.POST, instance=booking)
#      if form.is_valid():
#          form.save()
#          messages.success(request, "Booking updated successfully.")
#          return redirect(reverse('dashboard'))
#  else:
#      form = BookingForm(instance=booking)
#  return render(request, 'edit_booking.html', {'form': form, 'booking': booking})


# @login_required
# def delete_booking(request, booking_id):
#  booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
#  if request.method == 'POST':
#      booking.delete()
#      messages.success(request, "Booking deleted successfully.")
#      return redirect(reverse('dashboard'))
#  return render(request, 'delete_booking.html', {'booking': booking})


# from django.contrib.auth.hashers import check_password
# #Guide User Login
# def guide_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         try:
#             guide = Guide.objects.get(username=username) #Get guide by user name
#             if check_password(password, guide.password):
#                 request.session['guide_id'] = guide.id #Set session variable with guide id
#                 return redirect('guide_dashboard')  # Redirect to guide dashboard
#             else:
#                 return render(request, 'login.html', {'error': 'Invalid credentials'})
#         except Guide.DoesNotExist:
#             return render(request, 'login.html', {'error': 'Invalid credentials'})
#     return render(request, 'login.html')

# @login_required
# def guide_dashboard(request):
#     try:
#         guide_id = request.session.get('guide_id')
#         guide = Guide.objects.get(id=guide_id)
#         messages = Message.objects.filter(recipient=guide).order_by('-timestamp')  # Get messages for this guide
#         bookings = Booking.objects.filter(guide=guide).order_by('-booking_date')
#         return render(request, 'guide_dashboard.html', {'guide': guide, 'messages': messages, 'bookings': bookings})
#     except Guide.DoesNotExist:
#         return HttpResponse("Guide profile not found for this user.")
# @login_required
# def guide_message_reply(request, message_id):
#     message = get_object_or_404(Message, id=message_id)
#     if request.method == 'POST':
#         form = ReplyForm(request.POST)
#         if form.is_valid():
#             reply_text = form.cleaned_data['reply']
#             # In the future, we might want to create a new message
#             # Or implement a conversation thread
#             return redirect('guide_dashboard')
#     else:
#         form = ReplyForm()
#     return render(request, 'reply.html', {'form': form, 'message': message})



# def guide_logout(request):
#    try:
#      del request.session['guide_id']
#      return redirect('home')
#    except KeyError:
#     return redirect('home')




# from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
# from django.contrib import messages
# from django.contrib.auth.models import User, auth
# from django.contrib.auth import authenticate, login as auth_login #Use django auth login to override your login
# from .forms import GuideForm, BookingForm
# from travello.models    import Guide , Destination, Contact, Booking, Message
# from django.urls import reverse
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import views as auth_views
# from .forms import ReplyForm
# from django.contrib.auth.hashers import check_password
# #Regular User Login
# #Regular User Login
# def login(request):
#  if request.method == "POST":
#    username = request.POST["username"]
#    password = request.POST["password"]

#    user = authenticate(username=username, password=password)
#    if user is not None:
#        auth_login(request, user) #Use the django's login to login the user
#        if hasattr(user, 'guide'):
#            return redirect(reverse("guides_dashboard", kwargs={"guide_id":user.guide.id}))
#        else:
#            return redirect(reverse("dashboard"))
#    else:
#       messages.info(request, "invalid credentials...")
#       return redirect("login")
#  else:
#    return render(request, "login.html")


# def register(request):
#  if request.method == "POST":
#      first_name = request.POST["first_name"]
#      last_name = request.POST["last_name"]
#      username = request.POST["username"]
#      email = request.POST["email"]
#      password1 = request.POST["password1"]
#      password2 = request.POST["password2"]

#      if password1 == password2:
#          if User.objects.filter(username=username).exists():
#              messages.info(request, "username taken...")
#              test = User.objects.all()
#              print(test)
#              return redirect("register")
#          elif User.objects.filter(email=email).exists():
#              messages.info(request, "email taken...")
#              return redirect("register")
#          else:
#              user = User.objects.create_user(
#                  username=username,
#                  password=password1,
#                  email=email,
#                  first_name=first_name,
#                  last_name=last_name,
#              )
#              user.save()
#              messages.info(request, "user created...")
#              return redirect("admin:login")
#      else:
#          messages.info(request, "password not matched...")
#          return redirect("admin:register")
#      return redirect("/")
#  else:
#      return render(request, "register.html")


# def logout(request):
#  return auth_views.LogoutView.as_view(next_page="/")(request)

# def contact(request):
#  if request.method == 'POST':
#      name = request.POST.get('name')
#      email = request.POST.get('email')
#      subject = request.POST.get('subject')
#      message = request.POST.get('message')

    
#      Contact.objects.create(
#          name=name,
#          email=email,
#          subject=subject,
#          message=message,
#      )

#      messages.success(request, 'Your message has been sent successfully!')

   
#      return redirect('contact') 

#  return render(request, 'contact.html')  

# def about(request):
#  return render(request, "about.html")

# @login_required
# def dashboard(request):
#  if hasattr(request.user, 'guide'):
#    guide = request.user.guide
#    user_bookings = Booking.objects.filter(guide=guide)
#     # Get messages for current tour guide
#    guide_messages = Message.objects.filter(booking__guide=guide).order_by('timestamp')
#    return render(request, 'guide_dashboard.html', {'user_bookings': user_bookings, 'guide_messages':guide_messages, 'guide':guide})

#  else:
#      user_bookings = Booking.objects.filter(user=request.user)
#      return render(request, 'dashboard.html', {'user_bookings': user_bookings})


# def news(request):
#  guides = Guide.objects.all()
#  return render(request, "news.html", {"guides":guides})


# def destinations(request):
#  destinations = Destination.objects.all()
#  return render(request, 'destinations.html', {'destinations': destinations})

# def guide(request):
#  if request.method == "POST":
#      form = GuideForm(request.POST, request.FILES)
#      if form.is_valid():
#           guide = form.save(commit=False)
#           guide.save()
#           return redirect(reverse("guide_dashboard",kwargs={'guide_id':guide.id})) #redirect to the guide dashboard page
#  else:
#      form = GuideForm()
#  return render(request, "guideregistration.html", {"form": form})


# def guide_details(request, guide_id):
#  guide = get_object_or_404(Guide, id=guide_id)
#  return render(request, "guide_details.html", {"guide": guide})

# @login_required
# def contact_guide(request, guide_id):
#  guide = get_object_or_404(Guide, pk=guide_id)
#  if request.method == 'POST':
#      form = BookingForm(request.POST)
#      if form.is_valid():
#          # Process the form data
#          # we can add the data to booking model
#          booking = Booking(
#              first_name=form.cleaned_data['first_name'],
#              last_name=form.cleaned_data['last_name'],
#              email=form.cleaned_data['email'],
#              preferred_date=form.cleaned_data['preferred_date'],
#              party_size=form.cleaned_data['party_size'],
#              message=form.cleaned_data['message'],
#              accept_terms=form.cleaned_data['accept_terms'],
#              accept_marketing_emails=form.cleaned_data['accept_marketing_emails'],
#              guide=guide,
#               user=request.user
#          )
#          booking.save()

#          message = "Thank you for contacting " + guide.first_name + " " + guide.last_name + ". We will reach out to you soon."
#          messages.success(request, message)
#          return redirect(reverse('index'))
#  else:
#      form = BookingForm()
#  return render(request, 'message.html', {'form': form, 'guide':guide})


# @login_required
# def edit_booking(request, booking_id):
#  booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
#  if request.method == 'POST':
#      form = BookingForm(request.POST, instance=booking)
#      if form.is_valid():
#          form.save()
#          messages.success(request, "Booking updated successfully.")
#          return redirect(reverse('dashboard'))
#  else:
#      form = BookingForm(instance=booking)
#  return render(request, 'edit_booking.html', {'form': form, 'booking': booking})


# @login_required
# def delete_booking(request, booking_id):
#  booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
#  if request.method == 'POST':
#      booking.delete()
#      messages.success(request, "Booking deleted successfully.")
#      return redirect(reverse('dashboard'))
#  return render(request, 'delete_booking.html', {'booking': booking})

# #Guide User Login
# def guide_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         try:
#             guide = Guide.objects.get(username=username) #Get guide by user name
#             if check_password(password, guide.password):
#                 return redirect(reverse('guides_dashboard', kwargs={'guide_id': guide.id}))  # Redirect to guide dashboard
#             else:
#                 return render(request, 'login.html', {'error': 'Invalid credentials'})
#         except Guide.DoesNotExist:
#             return render(request, 'login.html', {'error': 'Invalid credentials'})
#     return render(request, 'login.html')

# def guide_dashboard(request, guide_id):
#     guide = Guide.objects.get(id=guide_id) #Get the guide using the guide id from url
#     messages = Message.objects.filter(recipient=guide).order_by('-timestamp')  # Get messages for this guide
#     bookings = Booking.objects.filter(guide=guide).order_by('-booking_date')
#     return render(request, 'guide_dashboard.html', {'guide': guide, 'messages': messages, 'bookings': bookings})
# def guide_message_reply(request, message_id):
#     message = get_object_or_404(Message, id=message_id)
#     if request.method == 'POST':
#         form = ReplyForm(request.POST)
#         if form.is_valid():
#             reply_text = form.cleaned_data['reply']
#             # In the future, we might want to create a new message
#             # Or implement a conversation thread
#             return redirect('guide_dashboard')
#     else:
#         form = ReplyForm()
#     return render(request, 'reply.html', {'form': form, 'message': message})

# def guide_logout(request):
#    try:
#      del request.session['guide_id']
#      return redirect('home')
#    except KeyError:
#     return redirect('home')







# from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
# from django.contrib import messages
# from django.contrib.auth.models import User, auth
# from django.contrib.auth import authenticate, login as auth_login #Use django auth login to override your login
# from .forms import GuideForm, BookingForm
# from travello.models    import Guide , Destination, Contact, Booking, Message
# from django.urls import reverse
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import views as auth_views
# from .forms import ReplyForm
# from django.contrib.auth.hashers import check_password


# def login(request):
#  if request.method == "POST":
#    username = request.POST["username"]
#    password = request.POST["password"]

#    user = authenticate(username=username, password=password)
#    if user is not None:
#        auth_login(request, user) #Use the django's login to login the user
#        if hasattr(user, 'guide'):
#             return redirect(reverse("guides_dashboard", kwargs={"guide_id":user.guide.id}))
#        else:
#            return redirect(reverse("dashboard"))
#    else:
#       messages.info(request, "invalid credentials...")
#       return redirect("login")
#  else:
#    return render(request, "login.html")


# def register(request):
#  if request.method == "POST":
#      first_name = request.POST["first_name"]
#      last_name = request.POST["last_name"]
#      username = request.POST["username"]
#      email = request.POST["email"]
#      password1 = request.POST["password1"]
#      password2 = request.POST["password2"]

#      if password1 == password2:
#          if User.objects.filter(username=username).exists():
#              messages.info(request, "username taken...")
#              test = User.objects.all()
#              print(test)
#              return redirect("register")
#          elif User.objects.filter(email=email).exists():
#              messages.info(request, "email taken...")
#              return redirect("register")
#          else:
#              user = User.objects.create_user(
#                  username=username,
#                  password=password1,
#                  email=email,
#                  first_name=first_name,
#                  last_name=last_name,
#              )
#              user.save()
#              messages.info(request, "User Created...")
#              return redirect("admin:login")
#      else:
#          messages.info(request, "Password Not Matched...")
#          return redirect("admin:register")
#      return redirect("/")
#  else:
#      return render(request, "register.html")


# def logout(request):
#  return auth_views.LogoutView.as_view(next_page="/")(request)

# def contact(request):
#  if request.method == 'POST':
#      name = request.POST.get('name')
#      email = request.POST.get('email')
#      subject = request.POST.get('subject')
#      message = request.POST.get('message')

    
#      Contact.objects.create(
#          name=name,
#          email=email,
#          subject=subject,
#          message=message,
#      )

#      messages.success(request, 'Your message has been sent successfully!')

   
#      return redirect('contact') 

#  return render(request, 'contact.html')  

# def about(request):
#  return render(request, "about.html")

# @login_required
# def dashboard(request):
#  if hasattr(request.user, 'guide'):
#    guide = request.user.guide
#    user_bookings = Booking.objects.filter(guide=guide)
#     # Get messages for current tour guide
#    guide_messages = Message.objects.filter(booking__guide=guide).order_by('timestamp')
#    return render(request, 'guide_dashboard.html', {'user_bookings': user_bookings, 'guide_messages':guide_messages, 'guide':guide})

#  else:
#      user_bookings = Booking.objects.filter(user=request.user)
#      return render(request, 'dashboard.html', {'user_bookings': user_bookings})


# def news(request):
#  guides = Guide.objects.all()
#  return render(request, "news.html", {"guides":guides})


# def destinations(request):
#  destinations = Destination.objects.all()
#  return render(request, 'destinations.html', {'destinations': destinations})

# def guide(request):
#  if request.method == "POST":
#      form = GuideForm(request.POST, request.FILES)
#      if form.is_valid():
#           guide = form.save(commit=False)
#           guide.save()
#           return redirect(reverse("guide_dashboard",kwargs={'guide_id':guide.id})) #redirect to the guide dashboard page
#  else:
#      form = GuideForm()
#  return render(request, "guideregistration.html", {"form": form})


# def guide_details(request, guide_id):
#  guide = get_object_or_404(Guide, id=guide_id)
#  return render(request, "guide_details.html", {"guide": guide})

# @login_required
# def contact_guide(request, guide_id):
#  guide = get_object_or_404(Guide, pk=guide_id)
#  if request.method == 'POST':
#      form = BookingForm(request.POST)
#      if form.is_valid():
#          # Process the form data
#          # we can add the data to booking model
#          booking = Booking(
#              first_name=form.cleaned_data['first_name'],
#              last_name=form.cleaned_data['last_name'],
#              email=form.cleaned_data['email'],
#              preferred_date=form.cleaned_data['preferred_date'],
#              party_size=form.cleaned_data['party_size'],
#              message=form.cleaned_data['message'],
#              accept_terms=form.cleaned_data['accept_terms'],
#              accept_marketing_emails=form.cleaned_data['accept_marketing_emails'],
#              guide=guide,
#               user=request.user
#          )
#          booking.save()

#          message = "Thank you for contacting " + guide.first_name + " " + guide.last_name + ". We will reach out to you soon."
#          messages.success(request, message)
#          return redirect(reverse('index'))
#  else:
#      form = BookingForm()
#  return render(request, 'message.html', {'form': form, 'guide':guide})


# @login_required
# def edit_booking(request, booking_id):
#  booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
#  if request.method == 'POST':
#      form = BookingForm(request.POST, instance=booking)
#      if form.is_valid():
#          form.save()
#          messages.success(request, "Booking updated successfully.")
#          return redirect(reverse('dashboard'))
#  else:
#      form = BookingForm(instance=booking)
#  return render(request, 'edit_booking.html', {'form': form, 'booking': booking})


# @login_required
# def delete_booking(request, booking_id):
#  booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
#  if request.method == 'POST':
#      booking.delete()
#      messages.success(request, "Booking deleted successfully.")
#      return redirect(reverse('dashboard'))
#  return render(request, 'delete_booking.html', {'booking': booking})

# #Guide User Login
# def guide_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         try:
#             guide = Guide.objects.get(username=username) #Get guide by user name
#             if check_password(password, guide.password):
#                 return redirect(reverse('guides_dashboard', kwargs={'guide_id': guide.id}))  # Redirect to guide dashboard
#             else:
#                 return render(request, 'login.html', {'error': 'Invalid credentials'})
#         except Guide.DoesNotExist:
#             return render(request, 'login.html', {'error': 'Invalid credentials'})
#     return render(request, 'login.html')

# def guide_dashboard(request, guide_id):
#     guide = Guide.objects.get(id=guide_id)
#     messages = Message.objects.filter(recipient=guide).order_by('-timestamp')  # Get messages for this guide
#     bookings = Booking.objects.filter(guide=guide).order_by('-booking_date')
#     return render(request, 'guide_dashboard.html', {'guide': guide, 'messages': messages, 'bookings': bookings})

# def guide_message_reply(request, message_id):
#     message = get_object_or_404(Message, id=message_id)
#     if request.method == 'POST':
#         form = ReplyForm(request.POST)
#         if form.is_valid():
#             reply_text = form.cleaned_data['reply']
#             #Get Guide from session id
#             guide_id = request.session.get('guide_id')
#             guide = Guide.objects.get(id = guide_id)

#             #create a message
#             Message.objects.create(
#                 sender=request.user,
#                  recipient = guide,
#                 content = reply_text,
#                 booking = message.booking
#             )
#             return redirect('guide_dashboard',guide_id = guide.id)
#     else:
#         form = ReplyForm()
#     return render(request, 'reply.html', {'form': form, 'message': message})

# def guide_logout(request):
#    try:
#      del request.session['guide_id']
#      return redirect('home')
#    except KeyError:
#     return redirect('home')

from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login as auth_login #Use django auth login to override your login
from .forms import GuideForm, BookingForm, ReplyForm, AvailabilityForm
from travello.models import Guide , Destination, Contact, Booking, Message
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail
from django.conf import settings

#Regular User Login
def login(request):
 if request.method == "POST":
   username = request.POST["username"]
   password = request.POST["password"]

   user = authenticate(username=username, password=password)
   if user is not None:
       auth_login(request, user) #Use the django's login to login the user
       print(f"user logged in: user_id = {request.user.id}")
       return redirect(reverse("dashboard"))
   else:
      messages.error(request, "invalid credentials...")
      return redirect(reverse("login"))
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
            guide.save()
            request.session['guide_id'] = guide.id
            return redirect(reverse("guide_dashboard",kwargs={'guide_id':guide.id}))
    else:
        form = GuideForm()
    return render(request, "guideregistration.html", {"form": form})

from datetime import datetime, timedelta
from calendar import monthrange


def guide_details(request, guide_id):
    guide = get_object_or_404(Guide, id=guide_id)
    today = datetime.today()
    availabilities = guide.availabilities.all()
    cal_data = []
    for i in range(0, 2):
        month_date = today.replace(month=today.month + i)
        year = month_date.year
        month = month_date.month

        num_days = monthrange(year, month)[1]
        first_day_of_month = datetime(year, month, 1).weekday()
        days = []
        for day in range(1, num_days + 1):
            date = datetime(year, month, day)
            is_available = False
            for availability in availabilities:
              if availability.start_date.date() <= date.date() <= availability.end_date.date():
                  is_available = True
                  break
            days.append({
                    'date': date,
                    'day': day,
                    'is_available': is_available,
                })
        
        # Calculate range in view
        first_day_range = list(range(first_day_of_month))

        cal_data.append(
            {
                "month_name": month_date.strftime("%B %Y"),
                "first_day_range": first_day_range,
                "days": days,
            }
        )

    return render(request, "guide_details.html", {"guide": guide, 'calendar_data': cal_data})


@login_required
def contact_guide(request, guide_id):
 guide = get_object_or_404(Guide, pk=guide_id)
 if request.method == 'POST':
     form = BookingForm(request.POST)
     if form.is_valid():
          message_content = request.POST.get('message')
          booking = Booking(
             first_name=form.cleaned_data['first_name'],
             last_name=form.cleaned_data['last_name'],
             email=form.cleaned_data['email'],
             preferred_date=form.cleaned_data['preferred_date'],
             party_size=form.cleaned_data['party_size'],
             message=message_content,
             accept_terms=form.cleaned_data['accept_terms'],
             accept_marketing_emails=form.cleaned_data['accept_marketing_emails'],
             guide=guide,
             user=request.user
         )
          booking.save()
     
     Message.objects.create(
            sender=request.user,
            recipient=guide,
            content=message_content,
            booking=booking
         )
     message = "Thank you for contacting " + guide.first_name + " " + guide.last_name + ". We will reach out to you soon."
     messages.success(request, message)
     return redirect(reverse('index'))
 else:
     form = BookingForm()
 return render(request, 'message.html', {'form': form, 'guide':guide})




# @login_required
# def edit_booking(request, booking_id):
#  booking = get_object_or_404(Booking, pk=booking_id)
#  if request.method == 'POST':
#      form = BookingForm(request.POST, instance=booking)
#      if form.is_valid():
#          form.save()
#         #Send email when the booking is updated
#          subject = "Booking Status Updated"
#          message = f"Your booking status has been updated by {booking.guide.first_name} {booking.guide.last_name} \n Please login to view the booking status:  "  + settings.EMAIL_HOST
#          email_from = settings.EMAIL_HOST_USER
#          recipient_list = [booking.email, ]
#          send_mail( subject, message, email_from, recipient_list )
#          messages.success(request, "Booking updated successfully.")
#          return redirect(reverse('dashboard'))
#  else:
#      form = BookingForm(instance=booking)
#  return render(request, 'edit_booking.html', {'form': form, 'booking': booking})



@login_required
def edit_booking(request, booking_id):
    try:
      booking = get_object_or_404(Booking, pk=booking_id)
    except Booking.DoesNotExist:
     messages.error(request, "Booking Not found.")
     return redirect(reverse("dashboard"))
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

def guide_login(request):
    print("guide_login view hit")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"username is : {username} and password is {password}")
        try:
            guide = Guide.objects.get(username=username)
            if check_password(password, guide.password):
                request.session['guide_id'] = guide.id
                print(f"Guide logged in: guide_id = {request.session.get('guide_id')}")
                return redirect(reverse('guide_dashboard', kwargs={'guide_id': guide.id}))
            else:
                print("Invalid credentials - Password mismatch")
                messages.error(request, 'Invalid credentials')
                return redirect(reverse("guide_login"))
        except Guide.DoesNotExist:
           print("Invalid credentials - User Does not exist")
           messages.error(request, 'Invalid credentials')
           return redirect(reverse("guide_login"))
    return render(request, 'login.html')



def guide_dashboard(request, guide_id):
    guide = get_object_or_404(Guide, id=guide_id)
    messages = Message.objects.filter(recipient=guide).order_by('-timestamp')
    bookings = Booking.objects.filter(guide=guide).order_by('-booking_date')

    availabilities = guide.availabilities.all()

    if request.method == "POST":
         form = AvailabilityForm(request.POST)
         if form.is_valid():
             #check if guide has availablity object if not create one
             if availabilities:
                 availability = availabilities.first()
                 availability.start_date = form.cleaned_data['start_date']
                 availability.end_date = form.cleaned_data['end_date']
                 availability.save()
             else:
                  availability = form.save(commit=False)
                  availability.guide = guide
                  availability.save()

             return redirect(reverse('guide_dashboard', kwargs={'guide_id': guide.id}))

    else:
        form = AvailabilityForm()

    return render(request, 'guide_dashboard.html', {'guide': guide, 'messages': messages,
                                                     'bookings': bookings, "form":form,
                                                     'availabilities': availabilities})
def guide_message_reply(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply_text = form.cleaned_data['reply']
            #Check if the sender is a guide or not
            try:
                guide = Guide.objects.get(username=request.user.username)
            except Guide.DoesNotExist:
                messages.error(request, "You are not logged in or your session has expired. Please login again.")
                return redirect(reverse("guide_login"))

            #create a message
            Message.objects.create(
                 sender=guide,
                 recipient = message.sender,
                 content = reply_text,
                 booking = message.booking
             )
            messages.success(request, f"Message sent to {message.sender.username}")
            return redirect(reverse('guide_dashboard', kwargs={'guide_id': guide.id}))
    else:
        form = ReplyForm()
    return render(request, 'reply.html', {'form': form, 'message': message})

def guide_logout(request):
   try:
     del request.session['guide_id']
     return redirect('index')
   except KeyError:
    return redirect('index')