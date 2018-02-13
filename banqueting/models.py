from django.db import models



class CcAccount(models.Model):
    nickname = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    anagrafica_id = models.IntegerField(blank=True, null=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    passupdate_date = models.DateField(blank=True, null=True)
    lastupdate_date = models.DateTimeField(blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cc_account'


class CcAnagrafica(models.Model):
    dato1 = models.TextField(blank=True, null=True)
    dato2 = models.TextField(blank=True, null=True)
    aaaa = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'cc_anagrafica'
