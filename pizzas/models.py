from django.db import models

# Create your models here.


class Pizza(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.TextField()

    def __str__(self):
        return self.name


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "toppings"

    def __str__(self):
        return f"{self.name[:50]}..."


class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.comment


# class Image(models.Model):
#  pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
#  image = models.ImageField(upload_to="images", blank=True)
#  date_added = models.DateTimeField(auto_now_add=True, blank=True)
