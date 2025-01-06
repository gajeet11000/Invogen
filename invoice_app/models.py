from django.db import models
from django.core.validators import RegexValidator, EmailValidator

from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

# Create your models here.
class Address(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    city = models.CharField(max_length=25)
    
    postal_code = models.CharField(max_length=6,
        validators=[
            RegexValidator(
                regex=r'^\d{6}$',  # 6 digits only
                message='Postal code must be exactly 6 digits.',
                code='invalid_postal_code'
            )
        ]
    )
    
    state = models.CharField(max_length=50)
    
    email = models.EmailField(
         validators=[
            EmailValidator(message='Enter a valid email address.')
        ]
    )
    
    phone_number = PhoneNumberField()
    
    addr_type = models.CharField(max_length=10)
    
    country = CountryField()
    
    def __str__(self):
        return self.name[:8]
        