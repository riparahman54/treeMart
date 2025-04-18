# Generated by Django 5.1.3 on 2024-11-22 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': [('can_add_profile', 'Can add profile'), ('can_change_profile', 'Can change profile'), ('can_delete_profile', 'Can delete profile'), ('can_view_profile', 'Can view profile')]},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_normal_user',
        ),
        migrations.AddField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('admin', 'Admin'), ('seller', 'Seller'), ('buyer', 'Buyer')], default='buyer', max_length=10),
        ),
    ]
