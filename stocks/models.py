from django.db import models
#from django.core.exceptions import ValidationError

# def validate_date(value):
#     try:
#         models.DateField().clean(value,None)
#     except ValidationError:
#         raise ValidationError("Invalid date format. Use YYYY-MM-DD.")

class Stock(models.Model):
    date = models.DateField()
    trade_code = models.CharField(max_length=50)
    high = models.FloatField()
    low = models.FloatField()
    open = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()