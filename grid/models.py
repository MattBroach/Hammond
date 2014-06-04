from django.db import models

# Create your models here.

class Grid_Square(models.Model):
    #Grid Metadata
    square_id = models.PositiveSmallIntegerField(unique=True)
    has_image = models.BooleanField()
    is_revealed = models.BooleanField(default=False)

    #Grid Actual data
    image_name = models.CharField(max_length=50, blank=True)
    image_code = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ('square_id',)

    def __str__(self):
        return self.image_name

class Command(models.Model):
    is_active = models.BooleanField()
    command = models.CharField(max_length=50)

    def __str__(self):
        return self.command