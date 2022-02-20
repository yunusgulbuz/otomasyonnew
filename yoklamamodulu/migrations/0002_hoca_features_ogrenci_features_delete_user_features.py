# Generated by Django 4.0.2 on 2022-02-20 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yoklamamodulu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hoca_Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ders', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='yoklamamodulu.dersler')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yoklamamodulu.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Ogrenci_Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('veli_tel', models.CharField(max_length=10)),
                ('ogr_no', models.IntegerField()),
                ('ders', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='yoklamamodulu.dersler')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yoklamamodulu.customuser')),
            ],
        ),
        migrations.DeleteModel(
            name='User_Features',
        ),
    ]
