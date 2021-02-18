# Generated by Django 2.2.13 on 2021-02-18 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('province', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('confirm', models.IntegerField(blank=True, null=True)),
                ('confirm_add', models.IntegerField(blank=True, null=True)),
                ('heal', models.IntegerField(blank=True, null=True)),
                ('dead', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('ds', models.DateTimeField(primary_key=True, serialize=False)),
                ('confirm', models.IntegerField(blank=True, null=True)),
                ('confirm_add', models.IntegerField(blank=True, null=True)),
                ('suspect', models.IntegerField(blank=True, null=True)),
                ('suspect_add', models.IntegerField(blank=True, null=True)),
                ('heal', models.IntegerField(blank=True, null=True)),
                ('heal_add', models.IntegerField(blank=True, null=True)),
                ('dead', models.IntegerField(blank=True, null=True)),
                ('dead_add', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'history',
                'managed': False,
            },
        ),
    ]
