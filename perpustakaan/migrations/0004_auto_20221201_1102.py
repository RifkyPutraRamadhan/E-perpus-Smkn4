# Generated by Django 3.2.15 on 2022-12-01 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0003_auto_20221127_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='buku',
            name='cover',
            field=models.ImageField(null=True, upload_to='cover/'),
        ),
        migrations.AddField(
            model_name='buku',
            name='tanggal',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
