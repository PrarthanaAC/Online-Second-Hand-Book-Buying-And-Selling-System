# Generated by Django 3.2 on 2021-05-04 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0021_auto_20210504_0954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellproduct',
            name='b_image',
        ),
        migrations.RemoveField(
            model_name='sellproduct',
            name='f_image',
        ),
        migrations.RemoveField(
            model_name='sellproduct',
            name='m_image',
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='backimage',
            field=models.ImageField(null=True, upload_to='uploads/sell'),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='frontimage',
            field=models.ImageField(null=True, upload_to='uploads/sell'),
        ),
        migrations.AddField(
            model_name='sellproduct',
            name='indeximage',
            field=models.ImageField(null=True, upload_to='uploads/sell'),
        ),
    ]
