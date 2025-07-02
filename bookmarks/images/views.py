from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from images.forms import ImageCreateForm


@login_required
def image_create(request):
    if request.method == "POST":
        # form is sent
        form = ImageCreateForm(data=request.POST)
        print("is it okay?")
        if form.is_valid():
            # form 데이터가 유효하다면
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            new_image.user = request.user
            print('it works')
            new_image.save()
            messages.success(request, "Image added successfully")
            return redirect(new_image.get_absolute_url())
    else:
        form = ImageCreateForm(data = request.GET)
    return render(
        request,
        'images/image/create.html',
        {'section':'images','form':form}
    )

