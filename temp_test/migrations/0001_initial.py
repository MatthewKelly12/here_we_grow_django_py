# Generated by Django 2.0.7 on 2018-09-10 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.CharField(max_length=100)),
                ('humidity', models.CharField(max_length=100)),
                ('pH', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inside_temperature', models.CharField(max_length=50)),
                ('inside_humidity', models.CharField(max_length=50)),
                ('outside_temperature', models.CharField(max_length=50)),
                ('outside_humidity', models.CharField(max_length=50)),
                ('water_temperature', models.CharField(max_length=50)),
                ('water_pH', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=50)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Grow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('description', models.CharField(max_length=200)),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='temp_test.Condition')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Variety',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='temp_test.Category')),
            ],
        ),
        migrations.AddField(
            model_name='dataset',
            name='grow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='temp_test.Grow'),
        ),
        migrations.AddField(
            model_name='condition',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='temp_test.Type'),
        ),
        migrations.AddField(
            model_name='condition',
            name='variety',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='temp_test.Variety'),
        ),
    ]
