from django.shortcuts import render, redirect
from negaradunia_app.models import *
from negaradunia_app.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib import messages
# Create your views here.


def daftar(request):
    form= UserCreationForm()

    if request.method == "POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Akun ' + user + ' telah dibuat')

            return redirect('masuk')
        
    context ={'form': form}
    return render(request, 'registration/register.html', context)


@login_required(login_url=settings.LOGIN_URL)
def index(request):
    data = {
        'Title' : "Negara",
    }
    return render(request, 'index.html', data)

@login_required(login_url=settings.LOGIN_URL)
def halaman1(request):
    country = Negara.objects.all()
    conservation = Konservasi.objects.all()
    data = {
        'Title' : "UAS PBO",
        'Heading' : "UAS PBO",
        'country' : country,
        'conservation' : conservation,
    }
    return render(request, 'halaman1.html', data)

@login_required(login_url=settings.LOGIN_URL)
def halaman2(request, id):
    detailnegara = Negara.objects.get(pk=id)
    data = {
        'Title' : "Detail ",
        'negara' :detailnegara,
    }
    return render(request, 'halaman2.html', data)

@login_required(login_url=settings.LOGIN_URL)
def tambah_data(request):
    if request.POST:
        form = FormNegara(request.POST)
        if form.is_valid():
            form.save()
            form= FormNegara()
            pesan = "Data Berhasil Ditambahkan"
            data = {
            'Title' : "Tambah Data",
            'form' : form,
            'pesan' : pesan,
        }
        return render(request, 'tambah_data.html', data)
    else:
        form = FormNegara()
        data = {
        'Title' : "Tambah Data",
        'form' : form,
        }
    return render(request, 'tambah_data.html', data)

@login_required(login_url=settings.LOGIN_URL)
def update_data(request, id):
    negara = Negara.objects.get(pk=id)

    if request.POST:
        form= FormNegara(request.POST, instance=negara)
        if form.is_valid():
            form.save()
            pesan = "Data Berhasil Diupdate"
        data = {
            'Title' : "Edit Data",
            'form' : form, 
            'pesan' : pesan,
            'negara' : negara,
        }
        return render(request, 'update_data.html', data)
    else:
        form = FormNegara(instance=negara)
        data = {
        'Title' : "Edit Data",
        'form' : form,
        'negara' : negara,
        }
    return render(request, 'update_data.html', data)    


def delete_data(request, id):
    negara = Negara.objects.get(pk=id)
    negara.delete()

    return redirect("/halaman1/")

@login_required(login_url=settings.LOGIN_URL)
def tambah_datapeta(request):
    if request.POST:
        form = FormKonservasi(request.POST)
        if form.is_valid():
            form.save()
            form= FormKonservasi()
            pesan = "Data Berhasil Ditambahkan"
            data = {
            'Title' : "Tambah Data",
            'form' : form,
            'pesan' : pesan,
        }
        return render(request, 'tambah_datapeta.html', data)
    else:
        form = FormKonservasi()
        data = {
        'Title' : "Tambah Data",
        'form' : form,
        }
    return render(request, 'tambah_datapeta.html', data)

@login_required(login_url=settings.LOGIN_URL)
def update_datapeta(request, id):
    konservasi = Konservasi.objects.get(pk=id)

    if request.POST:
        form= FormKonservasi(request.POST, instance=konservasi)
        if form.is_valid():
            form.save()
            pesan = "Data Berhasil Diupdate"
        data = {
            'Title' : "Edit Data",
            'form' : form, 
            'pesan' : pesan,
            'konservasi' : konservasi,
        }
        return render(request, 'update_datapeta.html', data)
    else:
        form = FormKonservasi(instance=konservasi)
        data = {
        'Title' : "Edit Data",
        'form' : form,
        'konservasi' : konservasi,
        }
    return render(request, 'update_datapeta.html', data)    

def delete_datapeta(request, id):
    konservasi = Konservasi.objects.get(pk=id)
    konservasi.delete()

    return redirect("/halaman1/")