# Generated by Django 4.0.3 on 2022-04-18 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_booking_orderdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
