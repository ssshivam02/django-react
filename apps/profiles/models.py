from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeStampedUUIDModel

User = get_user_model()

class Gender(models.TextChoices):
    MALE = 'male', _('Male')
    FEMALE = 'female', _('Female')
    OTHER = 'other', _('Other')
    
class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = PhoneNumberField(verbose_name=_("Phone Number"), max_length=30, default ="+918210206878")
    about_me = models.TextField(verbose_name=_("About me"), default="Say something about yourself")
    license = models.CharField(verbose_name=_("Real Estate license"), max_length=20, blank = True, null= True)
    profile_photo = models.ImageField(verbose_name=_("Profile Photo"),default="/profile_default.png")
    gender = models.CharField(verbose_name=_("Gender"), max_length=10, choices=Gender.choices,default=Gender.OTHER)
    country = CountryField(verbose_name=_("Country"), default="IN", blank=False, null=False)
    city = models.CharField(verbose_name=_("City"), default="Pune", max_length=50, blank=False, null=False)
    is_buyer = models.BooleanField(verbose_name=_("Buyer"), default=False, help_text=_("Are you looking to Buy a Property?"))
    is_seller = models.BooleanField(verbose_name=_("Seller"), default=False, help_text=_("Are you looking to Sell a Property?"))
    is_agent = models.BooleanField(verbose_name=_("Agent"), default=False, help_text=_("Are you an agent?"))
    top_agent = models.BooleanField(verbose_name=_("Top Agent"), default=False, help_text=_("Are you a top agent?"))
    ratings = models.DecimalField(max_digits=4, decimal_places=2, null =True, blank=True)
    num_reviews = models.IntegerField(verbose_name=_("Number of Reviews"), default=0,null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"