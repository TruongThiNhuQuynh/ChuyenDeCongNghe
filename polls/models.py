from django.db import models

class Person(models.Model):
    SHIRT_SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]

    name = models.CharField(max_length=100)
    shirt_size = models.CharField(max_length=2, choices=SHIRT_SIZE_CHOICES)

    def __str__(self):
        return self.name

    def get_shirt_size_display(self):
        return dict(self.SHIRT_SIZE_CHOICES).get(self.shirt_size, "Unknown")