# Generated by Django 2.2.5 on 2020-03-01 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_worker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv',
            name='csv_file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
