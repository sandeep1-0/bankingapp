from django.db import models


class BankDetails(models.Model):
    ifsc = models.CharField(primary_key=True, max_length=50)
    bank_id = models.CharField(max_length=20)
    branch = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)

    def __self__(self):
        return self.ifsc


# ifsc,bank_id,branch,address,city,district,state,bank_name
