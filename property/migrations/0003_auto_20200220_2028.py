# Generated by Django 3.0.2 on 2020-02-20 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20200207_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('apartments', 'apartments'), ('bungalows', 'bungalows'), ('mansionattes', 'mansionattes')], default='apartments', max_length=255, null=True),
        ),
    ]