from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)


    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Resize the image to 300x300 pixels after saving
        if self.image:
            img = Image.open(self.image.path)
            img_resized = img.resize((300, 300), 3)
            img_resized.save(self.image.path)

    def __str__(self):
        return self.name