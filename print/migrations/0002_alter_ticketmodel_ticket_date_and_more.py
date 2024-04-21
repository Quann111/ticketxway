# Generated by Django 5.0.3 on 2024-03-28 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('print', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketmodel',
            name='ticket_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='ticketmodel',
            name='ticket_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
