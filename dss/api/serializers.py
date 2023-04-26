from rest_framework import serializers
from .models import Customer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['loan_amnt' ,
    'term' ,
    'int_rate' ,
    'installment' ,
    'grade'  ,
    'sub_grade' ,
    'emp_title' ,
    'emp_length' ,
    'home_ownership' ,
    'annual_inc' ,
    'verification_status' ,
    'isue_d' ,
    'loan_status' ,
    'purpose'  ,
    'title' ,
    'dti'  ,
    'earliest_cr_line' ,
    'open_acc' ,
    'pub_rec' ,
    'revol_bal' ,
    'revol_util' ,
    'total_acc' ,
    'initial_list_status' ,
    'application_type' ,
    'mort_acc' ,
    'pub_rec_bankruptcies' ,
    'address' ]