# Generated by Django 4.2 on 2023-04-26 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("loan_amnt", models.FloatField()),
                ("term", models.TextField()),
                ("int_rate", models.FloatField()),
                ("installment", models.FloatField()),
                ("grade", models.TextField()),
                ("sub_grade", models.TextField()),
                ("emp_title", models.TextField()),
                ("emp_length", models.TextField()),
                ("home_ownership", models.TextField()),
                ("annual_inc", models.FloatField()),
                ("verification_status", models.TextField()),
                ("isue_d", models.DateTimeField()),
                ("loan_status", models.TextField()),
                ("purpose", models.TextField()),
                ("title", models.TextField()),
                ("dti", models.FloatField()),
                ("earliest_cr_line", models.TextField()),
                ("open_acc", models.FloatField()),
                ("pub_rec", models.FloatField()),
                ("revol_bal", models.FloatField()),
                ("revol_util", models.FloatField()),
                ("total_acc", models.FloatField()),
                ("initial_list_status", models.TextField()),
                ("application_type", models.TextField()),
                ("mort_acc", models.FloatField()),
                ("pub_rec_bankruptcies", models.FloatField()),
                ("address", models.TextField()),
            ],
        ),
    ]
