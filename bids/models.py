from django.db import models
from django.conf import settings


# Create your models here.
class Bid(models.Model):
    BID_SETTINGS = {
        "high": "HIGH",
        "medium": "medium",
        "low": "LOW"
    }
    title = models.CharField(max_length=200, blank=False, null=False)
    first_name = models.CharField(max_length=200, blank=False, null=False),
    last_name = models.CharField(max_length=200, blank=False, null=False),
    dob = models.DateField(null=False, blank=False),
    company_name = models.CharField(max_length=200, blank=False, null=False),
    address = models.CharField(max_length=200, blank=False, null=False),
    telephone = models.CharField(max_length=200, blank=False, null=False),
    bidding_settings = models.CharField(choices=BID_SETTINGS),
    google_ads_id = models.CharField(max_length=10, blank=False, null=False)
    bidder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
