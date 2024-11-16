# Generated by Django 5.1.2 on 2024-11-16 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bankloan',
            fields=[
                ('loan_id', models.IntegerField(primary_key=True, serialize=False)),
                ('loan_type', models.CharField(max_length=100)),
                ('loan_amt', models.IntegerField()),
                ('cust_no', models.IntegerField()),
                ('cust_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
