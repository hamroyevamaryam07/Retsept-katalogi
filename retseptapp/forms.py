
from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "nom",
            "tavsif",
            "tur",
            "vaqt",
            "rasm",
            "masalliqlar",
            "tayyorlash_usuli",
        ]

        labels = {
            "nom": "Retsept nomi",
            "tavsif": "Taom haqida",
            "tur": "Taom turi",
            "vaqt": "Tayyorlash vaqti",
            "rasm": "Rasm manzili (URL)",
            "masalliqlar": "Masalliqlar",
            "tayyorlash_usuli": "Tayyorlash usuli",
        }

        help_texts = {
            "masalliqlar": "Har bir masalliqni yangi qatordan yozing.",
            "tayyorlash_usuli": "Tayyorlash bosqichlarini yangi qatordan yozing.",
            "rasm": "Taom rasmining internetdagi manzilini kiriting.",
        }

        widgets = {
            "nom": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Masalan: O‘zbek palovi",
            }),
            "tavsif": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Taom haqida qisqacha ma’lumot...",
            }),
            "tur": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Masalan: Milliy taom",
            }),
            "vaqt": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Masalan: 1 soat 30 daqiqa",
            }),
            "rasm": forms.URLInput(attrs={
                "class": "form-control",
                "placeholder": "https://example.com/taom.jpg",
            }),
            "masalliqlar": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 6,
                "placeholder": "500 g go‘sht\n2 ta piyoz\nTuz va ziravorlar",
            }),
            "tayyorlash_usuli": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 8,
                "placeholder": "1. Masalliqlarni tayyorlang.\n2. Taomni pishiring.",
            }),
        }
