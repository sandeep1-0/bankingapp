from django.db import models


class BankDetails(models.Model):
    ifsc = models.CharField(primary_key=True, max_length=20)
    bank_id = models.CharField(max_length=3)
    branch = models.CharField(max_length=25)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=50)

    def __self__(self):
        return self.ifsc


# ifsc,bank_id,branch,address,city,district,state,bank_name
