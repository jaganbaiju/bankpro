# Generated by Django 5.0 on 2023-12-23 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp2', '0006_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='name',
            field=models.CharField(default=None, max_length=300),
        ),
    ]