# Generated by Django 5.0.1 on 2024-02-02 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank_system', '0004_alter_user_wallet_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historytransfer',
            options={'verbose_name': 'Историе', 'verbose_name_plural': 'История'},
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
