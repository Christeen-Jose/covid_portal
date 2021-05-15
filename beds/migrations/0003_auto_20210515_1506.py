# Generated by Django 3.2 on 2021-05-15 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beds', '0002_alter_patient_aadharno'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='patient',
            name='district',
            field=models.CharField(choices=[('AL', 'Alappuzha'), ('ER', 'Ernakulam'), ('ID', 'Idukki'), ('KN', 'Kannur'), ('KS', 'Kasaragod'), ('KL', 'Kollam'), ('KT', 'Kottayam'), ('KZ', 'Kozhikode'), ('MA', 'Malappuram'), ('PL', 'Palakkad'), ('PT', 'Pathanamthitta'), ('TV', 'Thiruvananthapuram'), ('TS', 'Thrissur'), ('WA', 'Wayanad')], default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hospital',
            name='district',
            field=models.CharField(choices=[('AL', 'Alappuzha'), ('ER', 'Ernakulam'), ('ID', 'Idukki'), ('KN', 'Kannur'), ('KS', 'Kasaragod'), ('KL', 'Kollam'), ('KT', 'Kottayam'), ('KZ', 'Kozhikode'), ('MA', 'Malappuram'), ('PL', 'Palakkad'), ('PT', 'Pathanamthitta'), ('TV', 'Thiruvananthapuram'), ('TS', 'Thrissur'), ('WA', 'Wayanad')], max_length=2),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='phone',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='patient',
            name='aadharno',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='location',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='patient',
            name='status',
            field=models.CharField(blank=True, choices=[('W', 'Waiting'), ('A', 'Admitted'), ('D', 'Discharged')], default='W', max_length=2),
        ),
    ]
