from io import BytesIO

import requests
from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify

from images.models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url', 'description']
        widgets = {
            'url': forms.HiddenInput,
        }


    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        print(extension)
        if extension not in valid_extensions:
            raise forms.ValidationError(
                'The given URL does not match valid image extensions.'
            )
        return url

    # url 에서 이미지 Request 후 저장
    def save(self, force_insert=False, force_update=False, commit=True):
        image = super().save(commit=False)
        image.url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image.url.split('.', 1)[1].lower()
        image_name = f"{name}.{extension}"
        # 사용자가 입력한 URL 에서 이미지 다운로드
        response = requests.get(image.url)
        image.image.save(
            image_name,
            ContentFile(response.content),
            save=False
        )
        if commit:
            image.save()
        return image