# Generated by Django 2.2 on 2020-08-14 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20200812_0753'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='updated_at',
            field=models.DateField(auto_now=True, verbose_name='Дата обновления'),
        ),
    ]
