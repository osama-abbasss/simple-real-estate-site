from django.db import models
from django.utils.text import slugify

class AboutUs(models.Model):
    image   = models.ImageField(upload_to= 'about/')
    mission = models.TextField()
    vision  = models.TextField()

    class Meta:
        verbose_name = 'about us'
        verbose_name_plural = 'about us'


class Blogs(models.Model):
    title = models.CharField(max_length= 50)
    slug = models.SlugField(blank=True, null=True)
    sub_title = models.CharField(max_length= 50, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to= 'blogs/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    active = models.BooleanField(default=False)

    def __str__(self):
        return self.sub_title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.sub_title)
        super().save( *args, **kwargs)

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'
