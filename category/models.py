from django.db import models

class Category(models.Model):
    """ Category Model """
    
    name = models.CharField(primary_key=True, max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural="Categories"