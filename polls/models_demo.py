from django.db import models

class DemoFields(models.Model):
    name = models.CharField(max_length=100, help_text="Tên")
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    score = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    birth_date = models.DateField(null=True, blank=True)
    website = models.URLField(blank=True)
    slug = models.SlugField(max_length=50, unique=True)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
    json_data = models.JSONField(default=dict, blank=True)
    # Relationship fields
    # For demo, you can add ForeignKey, ManyToManyField, OneToOneField if needed

    def __str__(self):
        return self.name