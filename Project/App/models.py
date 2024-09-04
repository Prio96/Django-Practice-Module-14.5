from django.db import models
import datetime
# Create your models here.
class FormModel(models.Model):
    bigautofield=models.BigAutoField(primary_key=True)
    # bank_balance=models.BigIntegerField(default=None)
    bank_balance=models.PositiveBigIntegerField(default=None)
    name=models.CharField(max_length=70,default=None)
    # age=models.IntegerField(default=None)
    # age=models.PositiveIntegerField(default=None)
    # age=models.SmallIntegerField(default=None)
    age=models.PositiveSmallIntegerField(default=None)
    photo=models.BinaryField(default=None)
    dateofbirth=models.DateField(default=datetime.date.today)
    time=models.DateTimeField(default=datetime.datetime.now)
    weight=models.DecimalField(max_digits=5,decimal_places=3)
    height=models.FloatField()
    email=models.EmailField()
    facebook_id=models.URLField()
    ip=models.GenericIPAddressField()
    comment=models.TextField()
    
    
    