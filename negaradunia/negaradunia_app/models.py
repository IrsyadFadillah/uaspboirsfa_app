from django.db import models

# Create your models here.

class Benua(models.Model):
   nama_benua = models.CharField(max_length=20)
   keterangan = models.TextField()

   def __str__(self):
      return self.nama_benua

class Negara(models.Model):
   nama_negara = models.CharField(max_length=50)
   letak_astronomi = models.CharField(max_length=40)
   ibu_kota = models.CharField(max_length=40)
   mata_uang = models.CharField(max_length=40)
   bahasa_resmi = models.CharField(max_length=40)
   bentuk_pemerintahan = models.CharField(max_length=70)
   gambar = models.CharField(max_length=70, null=True)
   benua_id = models.ForeignKey(Benua, on_delete=models.CASCADE, null=True)

   def __str__(self):
      return self.nama_negara

class Konservasi(models.Model):
   nama_konservasi = models.CharField(max_length=300)
   titik_koordinat = models.CharField(max_length=300)
   letak_negara = models.CharField(max_length=50)
    
   def __str__(self):
      return self.nama_konservasi
   