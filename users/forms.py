from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(
	UserCreationForm):  # avval yaratilgan formaga yangi forma qushamiz,saytni uzida ruyxatga olish uchun ishlatiladi
	class Meta(UserCreationForm):
		model = CustomUser
		fields = UserCreationForm.Meta.fields + ('age', 'address', 'job')


class CustomUserChangeForm(
	UserChangeForm):  # uzini taxrirlash uchun foydalanuvchilani bu imkoniyat superadminga berilgan
	class Meta(UserChangeForm):
		model = CustomUser
		fields = UserChangeForm.Meta.fields
