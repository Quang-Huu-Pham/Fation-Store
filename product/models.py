from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    icon = models.CharField(max_length=255, default=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/assets')
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    price = models.IntegerField()
    old_price = models.IntegerField()
    sale = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    sold = models.IntegerField(default=False)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

    def get_display_price(self):
        return self.price / 100
