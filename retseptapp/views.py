
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Recipe


def home(request):
    # Barcha retseptlarni olish
    retseptlar = Recipe.objects.all()

    # Qidiruv
    qidiruv = request.GET.get("q", "").strip()

    if qidiruv:
        retseptlar = retseptlar.filter(
            Q(nom__icontains=qidiruv)
            | Q(tavsif__icontains=qidiruv)
            | Q(masalliqlar__icontains=qidiruv)
        )

    # Tanlangan kategoriya
    tanlangan_tur = request.GET.get("tur", "").strip()

    if tanlangan_tur:
        retseptlar = retseptlar.filter(tur=tanlangan_tur)

    # Bazadagi kategoriyalar ro'yxati
    kategoriyalar = (
        Recipe.objects
        .exclude(tur__isnull=True)
        .exclude(tur="")
        .values_list("tur", flat=True)
        .distinct()
        .order_by("tur")
    )

    # HTML sahifaga yuboriladigan ma'lumotlar
    context = {
        "retseptlar": retseptlar,
        "qidiruv": qidiruv,
        "tanlangan_tur": tanlangan_tur,
        "kategoriyalar": kategoriyalar,
    }

    return render(request, "retseptapp/home.html", context)


def recipe_detail(request, pk):
    # Tanlangan retseptni topish
    retsept = get_object_or_404(Recipe, pk=pk)

    # Retseptning batafsil sahifasini ochish
    return render(
        request,
        "retseptapp/recipe_datali.html",
        {"retsept": retsept},
    )
