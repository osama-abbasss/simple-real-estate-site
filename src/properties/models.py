from django.db import models
from location_field.models.plain import PlainLocationField
from django.utils.text import slugify




TYPE_OPTIONS = (
('sale', 'S'),
('rent', 'R'),
)

class Property(models.Model):
    name  = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(blank=True, null= True)
    image = models.ImageField(upload_to='property/')
    location = PlainLocationField(based_fields=['governorate.governorate_name'], zoom=7)
    governorate = models.ForeignKey('Governorate', on_delete=models.CASCADE)
    city = models.CharField(max_length=400)
    area     = models.DecimalField(decimal_places=2 ,max_digits=8)
    price = models.PositiveIntegerField()
    type  = models.CharField(max_length=4, choices=TYPE_OPTIONS)
    installment = models.BooleanField(default=True)
    beds_room_number = models.PositiveIntegerField()
    baths_number     = models.PositiveIntegerField()
    garages_number   = models.PositiveIntegerField()
    floor_number     = models.PositiveIntegerField()
    description   = models.TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'


class Governorate(models.Model):
    governorate_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='governorate/')

    def __str__(self):
        return self.governorate_name



class ReserveProperty(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    email   = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Reserve Property'
        verbose_name_plural = 'Reserve Properties'
