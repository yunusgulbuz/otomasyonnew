# Generated by Django 4.0.2 on 2022-02-19 20:10

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
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Ders_Yoklama',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Dersler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ders_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Kurumlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kurum_name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Namaz_Yoklama',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kurum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yoklamamodulu.kurumlar')),
            ],
        ),
        migrations.CreateModel(
            name='Sehirler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sehir_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User_Yoklama_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statu_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='UserTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Vakitler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vakit_name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='User_Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('veli_tel', models.CharField(max_length=10)),
                ('ders', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='yoklamamodulu.dersler')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yoklamamodulu.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Namaz_Yoklama_Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yoklamamodulu.customuser')),
                ('user_statu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yoklamamodulu.user_yoklama_status')),
                ('yoklama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yoklamamodulu.namaz_yoklama')),
            ],
        ),
        migrations.AddField(
            model_name='namaz_yoklama',
            name='vakit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yoklamamodulu.vakitler'),
        ),
        migrations.AddField(
            model_name='kurumlar',
            name='sehir',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yoklamamodulu.sehirler'),
        ),
        migrations.CreateModel(
            name='Ders_Yoklama_Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yoklamamodulu.customuser')),
                ('user_statu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yoklamamodulu.user_yoklama_status')),
                ('yoklama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yoklamamodulu.ders_yoklama')),
            ],
        ),
        migrations.AddField(
            model_name='ders_yoklama',
            name='ders',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yoklamamodulu.dersler'),
        ),
        migrations.AddField(
            model_name='ders_yoklama',
            name='kurum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yoklamamodulu.kurumlar'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='kurum',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='yoklamamodulu.kurumlar'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='yoklamamodulu.usertypes'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barkod', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='yoklamamodulu.customuser')),
            ],
        ),
    ]
