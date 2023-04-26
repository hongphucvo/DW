from django.db import models

# Create your models here.
from django.db import models
# from django.contrib.auth.models import User

class Customer(models.Model):
    loan_amnt = models.FloatField()
    term = models.TextField()
    int_rate = models.FloatField()
    installment = models.FloatField()
    grade  = models.TextField()
    sub_grade = models.TextField()
    emp_title = models.TextField()
    emp_length = models.TextField()
    home_ownership = models.TextField()
    annual_inc = models.FloatField()
    verification_status = models.TextField()
    isue_d = models.DateTimeField()
    loan_status = models.TextField()
    purpose  = models.TextField()
    title = models.TextField()
    dti  = models.FloatField()
    earliest_cr_line = models.TextField()
    open_acc = models.FloatField()
    pub_rec = models.FloatField()
    revol_bal = models.FloatField()
    revol_util = models.FloatField()
    total_acc = models.FloatField()
    initial_list_status = models.TextField()
    application_type = models.TextField()
    mort_acc = models.FloatField()
    pub_rec_bankruptcies = models.FloatField()
    address = models.TextField()

    def __str__(self):
        return self.loan_status
    def to_dict(self):
        return 