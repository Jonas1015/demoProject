from django.db import models
from django.utils import timezone
# from django.utils.timezone import utc
from datetime import datetime


# Create your models here.
class schedule(models.Model):
    full_name = models.CharField(max_length = 50)
    project_name = models.CharField(max_length = 20)
    appointment_date = models.DateTimeField(default = timezone.now)
    salary = models.PositiveIntegerField(default = 0)
    date_of_contract = models.DateTimeField(default = timezone.now)
    end_of_contract = models.DateTimeField(default = timezone.now)
    days_remained = models.PositiveIntegerField(default = 0)




    def startContract(self):
        return self.date_of_contract.strftime('%B %d %Y')
    def endContract(self):
        return self.end_of_contract.strftime('%B %d %Y')

    class Meta:
        verbose_name_plural = 'Schedules'

    def __str__(self):
        return self.full_name




class ourData(models.Model):
    region_list = (
        ('','Select region'),
        ('Arusha','Arusha'),
        ('Dar es Salaam','Dar es Salaam'),
        ('Dodoma','Dodoma'),
        ('Geita','Geita'),
        ('Iringa','Iringa'),('Kagera','Kagera'),
        ('Katavi','Katavi'),
        ('Kigoma','Kigoma'),
        ('Kilimanjaro','Kilimanjaro'),
        ('Lindi','Lindi'),
        ('Manyara','Manyara'),
        ('Mara','Mara'),
        ('Mbeya','Mbeya'),
        ('Morogoro','Morogoro'),
        ('Mtwara','Mtwara'),
        ('Njombe','Njombe'),
        ('Pemba North','Pemba North'),
        ('Pemba South','Pemba South'),
        ('Pwani','Pwani'),
        ('Rukwa','Rukwa'),
        ('Ruvuma','Ruvuma'),
        ('Shinyanga','Shinyanga'),
        ('Simiyu','Simiyu'),
        ('Singida','Singida'),
        ('Tabora','Tabora'),
        ('Tanga','Tanga'),
        ('Zanzibar North','Zanzibar North'),
        ('Zanzibar South','Zanzibar South'),
        ('Zanzibar Central','Zanzibar Central'),
        ('Zanzibar West','Zanzibar West')
    )
    region = models.CharField(choices = region_list, max_length=50)
    population = models.PositiveIntegerField(default = 0)
    number_of_district = models.PositiveIntegerField(default = 0)

    class Meta:
        verbose_name_plural = "Regional Lists"
    def __str__(self):
        return self.region
