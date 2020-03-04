from django.db import models
from users.models import CustomUser
# Create your models here.


class BaseModel(models.Model):
    """Model definition for BaseModel."""
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for BaseModel."""

        verbose_name = 'BaseModel'
        verbose_name_plural = 'BaseModels'


class CitizenReport(BaseModel):
    citizen = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, limit_choices_to={
        'account_type': 'citizen'
    })
    status = models.CharField(max_length=20, null=True, blank=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)
    images = models.TextField()
    multiple = models.BooleanField(default=False)
