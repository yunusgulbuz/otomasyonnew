from django.contrib import admin

from yoklamamodulu.models import Dersler, Vakitler, CustomUser, Sehirler, UserTypes, Cards, Namaz_Yoklama, \
    User_Yoklama_Status, Namaz_Yoklama_Users, Ders_Yoklama, Ders_Yoklama_Users, Hoca_Features, Ogrenci_Features

admin.site.register(Dersler)
admin.site.register(Vakitler)
admin.site.register(Sehirler)
admin.site.register(UserTypes)
admin.site.register(Cards)
admin.site.register(Namaz_Yoklama)
admin.site.register(User_Yoklama_Status)
admin.site.register(Namaz_Yoklama_Users)
admin.site.register(Ders_Yoklama)
admin.site.register(Ders_Yoklama_Users)
admin.site.register(Hoca_Features)
admin.site.register(Ogrenci_Features)
admin.site.register(CustomUser)

