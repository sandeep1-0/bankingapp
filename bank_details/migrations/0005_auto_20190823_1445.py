# Generated by Django 2.1.7 on 2019-08-23 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_details', '0004_auto_20190823_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankdetails',
            name='branch',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='bankdetails',
            name='ifsc',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
