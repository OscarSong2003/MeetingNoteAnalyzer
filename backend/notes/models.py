from django.db import models

# Create your models here.
class Notes(models.Model): 
    name = models.CharField(max_length=20)
    completed = models.BooleanField(default=False)
    def _str_(self): 
        return self.name; 

class Audio_store(models.Model):
    record=models.FileField(upload_to='documents/')
    class Meta:
        db_table='Audio_store'
