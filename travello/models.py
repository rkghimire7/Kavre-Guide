from django.db import models
from datetime import time
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Guide(models.Model):
    CIVILITY_CHOICES = [
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Ms', 'Ms'),
    ]

    civility = models.CharField(max_length=10, choices=CIVILITY_CHOICES)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(max_length=100)
    city_or_region = models.CharField(max_length=100)
    mother_tongue = models.CharField(max_length=50)
    tour_languages = models.TextField(help_text="Comma-separated list of languages")
    presentation = models.TextField()
    photo = models.ImageField(upload_to="pics/")
    certified_guide = models.BooleanField(default=False)
    guide_card = models.FileField(upload_to="pics/", blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this line
    
    # New price field
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.country})"


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"


class Booking(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    preferred_date = models.DateField(null=True, blank=True)  # Allow null and blank for optional field
    party_size = models.PositiveIntegerField(default=1)  # Use PositiveIntegerField for party size
    message = models.TextField()
    accept_terms = models.BooleanField(default=False)
    accept_marketing_emails = models.BooleanField(default=False)

        # Establishing a relationship with the Guide model
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(default=timezone.now)
    status_choices = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='pending')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"



class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(Guide, on_delete=models.CASCADE, related_name='received_messages')
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
         return f"From {self.sender.username} to {self.recipient.username}"


class Availability(models.Model):
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, related_name='availability_set')
    date = models.DateField()
    start_time = models.TimeField(default=time(0, 0))  # Default to 9:00 AM
    end_time = models.TimeField(default=time(23, 59))   # Default to 5:00 PM

    def __str__(self):
        return f"{self.guide} - {self.date}"