# Generated by Django 3.1.4 on 2021-01-04 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20210104_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.category'),
        ),
    ]
