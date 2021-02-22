# Generated by Django 2.2.13 on 2021-02-22 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cov', '0002_history_shanghai'),
    ]

    operations = [
        migrations.CreateModel(
            name='History_Shanghai_Prov',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provinceName', models.CharField(blank=True, max_length=50, null=True)),
                ('provinceCode', models.CharField(blank=True, max_length=50, null=True)),
                ('cityName', models.CharField(blank=True, max_length=50, null=True)),
                ('confirmedCount', models.IntegerField(blank=True, null=True)),
                ('curedCount', models.IntegerField(blank=True, null=True)),
                ('currentConfirmedCount', models.IntegerField(blank=True, null=True)),
                ('deadCount', models.IntegerField(blank=True, null=True)),
                ('suspectedCount', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'history_shanghai_prov',
                'managed': True,
            },
        ),
    ]
