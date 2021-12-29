from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.


class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Phone_No = models.CharField(max_length=20)
    Email = models.CharField(max_length=200)
    Subject = models.CharField(max_length=400)
    Message = models.TextField(blank=True, null=True)
    Proposal = models.FileField(
        upload_to="uploads/%Y/%m/%d", blank=True, null=True)

    def __str__(self):
        return self.Name


class Blog(models.Model):
    Title = models.CharField(max_length=100)
    Description = RichTextField()
    Banner_Image = models.FileField(upload_to="uploads/%Y/%m/%d")
    Timestamp = models.DateTimeField(auto_now_add=True)
    Slug = models.SlugField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.Title

    def save(self, *args, **kwargs):
        self.Slug = slugify(self.Title)
        super(Blog, self).save(*args, **kwargs)


