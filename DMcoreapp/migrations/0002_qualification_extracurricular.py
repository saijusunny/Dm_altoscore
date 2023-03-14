# Generated by Django 4.0.2 on 2023-03-14 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plustwo', models.CharField(max_length=240, null=True)),
                ('schoolaggregate', models.CharField(max_length=240, null=True)),
                ('schoolcertificate', models.FileField(blank=True, null=True, upload_to='images/')),
                ('ugdegree', models.CharField(max_length=240, null=True)),
                ('ugstream', models.CharField(max_length=240, null=True)),
                ('ugpassoutyr', models.CharField(max_length=240, null=True)),
                ('ugaggregrate', models.CharField(max_length=240, null=True)),
                ('backlogs', models.CharField(max_length=240, null=True)),
                ('ugcertificate', models.FileField(blank=True, null=True, upload_to='images/')),
                ('pg', models.CharField(max_length=240, null=True)),
                ('status', models.CharField(default='', max_length=100)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='qualificationuser', to='DMcoreapp.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='extracurricular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internshipdetails', models.CharField(max_length=240, null=True)),
                ('internshipduration', models.CharField(max_length=240, null=True)),
                ('internshipcertificate', models.FileField(blank=True, null=True, upload_to='images/')),
                ('onlinetrainingdetails', models.CharField(max_length=240, null=True)),
                ('onlinetrainingduration', models.CharField(max_length=240, null=True)),
                ('onlinetrainingcertificate', models.FileField(blank=True, null=True, upload_to='images/')),
                ('projecttitle', models.CharField(max_length=240, null=True)),
                ('projectduration', models.CharField(max_length=240, null=True)),
                ('projectdescription', models.TextField(null=True)),
                ('projecturl', models.CharField(blank=True, default='', max_length=240, null=True)),
                ('skill1', models.CharField(blank=True, default='', max_length=240, null=True)),
                ('skill2', models.CharField(blank=True, default='', max_length=240, null=True)),
                ('skill3', models.CharField(blank=True, default='', max_length=240, null=True)),
                ('status', models.CharField(default='', max_length=240)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='extracurricularuser', to='DMcoreapp.user_registration')),
            ],
        ),
    ]
