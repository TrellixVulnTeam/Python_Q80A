# Generated by Django 2.0.7 on 2019-03-29 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('drinks', 'drinks'), ('appetizers', 'appetizers'), ('entrees', 'entrees'), ('treats', 'treats')], max_length=60),
        ),
    ]
