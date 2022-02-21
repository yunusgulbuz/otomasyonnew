from django.contrib.auth.models import User
from django.db import models


class Sehirler(models.Model):
    sehir_name = models.CharField(max_length=30, null=False, blank=False)


class Kurumlar(models.Model):
    kurum_name = models.CharField(max_length=70)
    sehir = models.ForeignKey(Sehirler, on_delete=models.CASCADE, blank=False, null=False)


class UserTypes(models.Model):
    type_name = models.CharField(max_length=30, null=False, blank=False)


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    kurum = models.ForeignKey(Kurumlar, on_delete=models.CASCADE, blank=True, null=False)
    type = models.ForeignKey(UserTypes, on_delete=models.CASCADE, blank=True, null=False)
    isim=models.CharField(max_length=20,blank=False,null=False)
    soyisim=models.CharField(max_length=20,blank=False,null=False)


class Cards(models.Model):
    barkod = models.CharField(max_length=50)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, blank=False, null=False)


class Vakitler(models.Model):
    vakit_name = models.CharField(max_length=70, blank=False, null=False)


class Namaz_Yoklama(models.Model):
    vakit = models.ForeignKey(Vakitler, on_delete=models.CASCADE, blank=False, null=False)
    kurum = models.ForeignKey(Kurumlar, on_delete=models.CASCADE, blank=False, null=False)


class User_Yoklama_Status(models.Model):
    statu_name = models.CharField(max_length=40, null=False, blank=False)


class Namaz_Yoklama_Users(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False, null=False)
    yoklama = models.ForeignKey(Namaz_Yoklama, on_delete=models.CASCADE, blank=False, null=False)
    user_statu = models.ForeignKey(User_Yoklama_Status, on_delete=models.CASCADE, blank=False, null=False)


class Dersler(models.Model):
    ders_name = models.CharField(max_length=40, blank=False, null=False)


class Ders_Yoklama(models.Model):
    ders = models.ForeignKey(Dersler, on_delete=models.CASCADE, blank=False, null=False)
    kurum = models.ForeignKey(Kurumlar, on_delete=models.CASCADE, blank=False, null=False)


class Ders_Yoklama_Users(models.Model):
    yoklama = models.ForeignKey(Ders_Yoklama, on_delete=models.CASCADE, blank=False, null=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False, null=False)
    user_statu = models.ForeignKey(User_Yoklama_Status, on_delete=models.CASCADE, blank=False, null=False)


class Hoca_Features(models.Model):
    ders = models.ForeignKey(Dersler, on_delete=models.CASCADE, blank=True, null=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False, null=False)


class Ogrenci_Features(models.Model):
    ders = models.ForeignKey(Dersler, on_delete=models.CASCADE, blank=True, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
    isim = models.CharField(max_length=20, blank=False, null=False)
    soyisim = models.CharField(max_length=20, blank=False, null=False)
    veli_tel = models.CharField(max_length=10)
    ogr_no = models.IntegerField(blank=False, null=False)

