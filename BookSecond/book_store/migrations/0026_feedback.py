# Generated by Django 3.2 on 2021-05-25 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0025_product_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
