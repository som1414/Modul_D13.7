from django.forms import ModelForm
from django import forms
from .models import Announcement, Files


class AnnouncementForm(ModelForm):
    class Meta:
        model = Announcement
        fields = ['Announcement_title', 'Announcement_text', 'Category']


class VideoFormEdit(ModelForm):
    class Meta:
        model = Files
        fields = ['File']
