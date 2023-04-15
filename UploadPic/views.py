from django.shortcuts import render,redirect,reverse
from .form import UploadModelForm
from .models import Photo
# Create your views here.

def index(request):
    photos = Photo.objects.all()  #查詢所有資料
    form = UploadModelForm()
    if request.method == "POST":
        form = UploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('Index'))
    context = {
        'photos': photos,
        'form': form
    }
    return render(request, 'UploadPic/index.html', context)
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Photo

def delete_photo(request, pk):
    photo = Photo.objects.get(id=pk)
    if request.method == 'POST':
        photo.delete()
        return redirect(reverse('Index'))
    context = {
        'photo': photo
               }

    return render(request, 'UploadPic/delete.html', context)
