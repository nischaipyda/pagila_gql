# Generated by Django 3.1.7 on 2021-03-03 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20210303_1416'),
        ('customers', '0003_auto_20210303_0647'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='store_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.store'),
        ),
    ]