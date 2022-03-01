from django.db import models
from django.conf import settings


# Create your models here.
class Bid(models.Model):
    BID_SETTINGS = (
        ("HIGH", "HIGH"),
        ("MEDIUM", "MEDIUM"),
        ("LOW", "LOW"),
    )

    title = models.CharField(max_length=200, blank=False, null=False)
    first_name = models.CharField(max_length=200, blank=False, null=False, default="first_name")
    last_name = models.CharField(max_length=200, blank=False, null=False, default="last_name")
    dob = models.DateField(null=False, blank=False, default='2022-03-02')
    company_name = models.CharField(max_length=200, blank=False, null=False, default="company")
    address = models.CharField(max_length=200, blank=False, null=False, default="addy")
    telephone = models.CharField(max_length=200, blank=False, null=False, default="0")
    bidding_settings = models.CharField(max_length=10, choices=BID_SETTINGS, default="default")
    google_ads_id = models.CharField(max_length=10, blank=False, null=False)
    bidder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
