# Generated by Django 3.2.5 on 2021-07-17 22:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tblAdvtBsc',
            fields=[
                ('AdvtNo', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('AdvtTpCd', models.CharField(max_length=30)),
                ('AdvtTitl', models.CharField(max_length=200)),
                ('AdvtStaDate', models.CharField(max_length=8)),
                ('AdvtEndDate', models.CharField(max_length=8)),
                ('AdvtDesc', models.CharField(max_length=3000)),
                ('AdvtGrdCd', models.CharField(max_length=30)),
                ('DelYN', models.CharField(max_length=1)),
                ('FstAddTmst', models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 18, 7, 56, 51, 271395))),
                ('FstAddID', models.CharField(max_length=30)),
                ('LastUptTmst', models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 18, 7, 56, 51, 271395))),
                ('LastUptID', models.CharField(max_length=30)),
            ],
        ),
    ]
