from django.db import models

class dialecticapp(models.Model):
    night = models.CharField(max_length=15)
    morning = models.CharField(max_length=15)
    daytime = models.CharField(max_length=15)
    evening = models.CharField(max_length=15)
    beforeSleep = models.CharField(max_length=15)
    notes = models.TextField()    
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.night
    