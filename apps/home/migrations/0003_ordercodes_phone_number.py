# Generated by Django 3.2.6 on 2024-01-14 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20231008_0647'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordercodes',
            name='phone_number',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='شماره تماس'),
        ),
    ]
