# Generated by Django 5.0 on 2023-12-22 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp2', '0004_rename_city_branch_rename_country_district_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='person',
            name='district',
        ),
        migrations.DeleteModel(
            name='Branch',
        ),
        migrations.DeleteModel(
            name='District',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]