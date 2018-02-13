# Generated by Django 2.0.2 on 2018-02-13 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CcAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, max_length=45, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('anagrafica_id', models.IntegerField(blank=True, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=20, null=True)),
                ('passupdate_date', models.DateField(blank=True, null=True)),
                ('lastupdate_date', models.DateTimeField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cc_account',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CcAnagrafica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dato1', models.TextField(blank=True, null=True)),
                ('dato2', models.TextField(blank=True, null=True)),
                ('aaaa', models.NullBooleanField()),
            ],
            options={
                'db_table': 'cc_anagrafica',
                'managed': False,
            },
        ),
    ]
