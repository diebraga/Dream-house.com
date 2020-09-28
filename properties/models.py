from django.db import models
from django.utils.timezone import now
from auctioneers.models import Auctioneer
 
 
class Property(models.Model):
    """ model for creation prorperty """
    class SaleType(models.TextChoices):
        """ class defines atribute sale or rent """
        FOR_SALE = 'For Sale'
        FOR_RENT = 'For Rent'
    
    class HomeType(models.TextChoices):
        """ class defines atribute for properties types """
        HOUSE = 'House'
        APARTMENT = 'Apartment'
        STUDIO = 'Studio'

    auctioneer = models.ForeignKey(Auctioneer, on_delete=models.DO_NOTHING)
    slug = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=15)
    description = models.TextField(blank=True)
    sale_type = models.CharField(max_length=50, choices=SaleType.choices, default=SaleType.FOR_SALE)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    home_type = models.CharField(max_length=50, choices=HomeType.choices, default=HomeType.HOUSE)
    sqft = models.IntegerField()
    open_house = models.BooleanField(default=False)
    photo_main = models.ImageField(upload_to='photos/%d/%m/%Y/')
    photo_1 = models.ImageField(upload_to='photos/%d/%m/%Y/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%d/%m/%Y/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%d/%m/%Y/', blank=True)

    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.title