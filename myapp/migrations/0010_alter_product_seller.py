# Generated by Django 4.2.6 on 2023-10-31 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
        ),
    ]
