# Generated by Django 2.0.7 on 2019-03-29 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190329_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('entrees', 'entrees'), ('drinks', 'drinks'), ('appetizers', 'appetizers'), ('treats', 'treats')], max_length=60),
        ),
    ]