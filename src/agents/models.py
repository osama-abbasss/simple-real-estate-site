from django.db import models
from django.utils.text import slugify


TITLE_CHOICES=(
('Real Estate Brooker','REB'),
('Buying Agent','BA'),
('Selling Agent','SA'),
('Other','O')
)

GENDER_CHOICES=(
('Male','M'),
('Female','F'),

)

class Agent(models.Model):
    name  = models.CharField(max_length=100)
    title = models.CharField(max_length=20, choices=TITLE_CHOICES)
    slug  = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to='agent/', blank=True, null=True)
    email = models.EmailField()
    phone = models.IntegerField()
    description = models.TextField()
    username    = models.CharField(max_length=100, unique=True)
    gender      = models.CharField(max_length=6, choices=GENDER_CHOICES)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save( *args, **kwargs)

    def __str__(self):
        return self.name
