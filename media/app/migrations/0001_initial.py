# Generated by Django 2.2.5 on 2019-11-08 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
                ('patient_name', models.CharField(max_length=250)),
                ('doctor', models.CharField(max_length=250)),
                ('time', models.CharField(max_length=250)),
                ('file_number', models.CharField(max_length=20)),
                ('is_doctor', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consultation_number', models.CharField(max_length=250)),
                ('doctor_name', models.CharField(max_length=250)),
                ('patient_name', models.CharField(max_length=250)),
                ('file_number', models.CharField(max_length=20)),
                ('is_doctor', models.BooleanField(default=False)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Appointment')),
            ],
        ),
    ]
