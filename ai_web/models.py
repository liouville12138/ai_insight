from django.db import models

# Create your models here.

class PmiLog(models.Model):
    id = models.AutoField(primary_key=True)
    log_id = models.CharField(max_length=50,null=False)
    log_name = models.CharField(max_length=50,null=False)
    string_id = models.CharField(max_length=50,null=False)
    current = models.FloatField(max_length=50)
    voltage = models.FloatField(max_length=50)

    def __str__(self):
        return "Pmi Log name:{}".format(self.log_name)