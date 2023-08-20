from animelist.models import Anime as DaftarAnime
from django.shortcuts import render
import requests


def index(request):
    """
    Function ini adalah function yang akan dieksekusi pertama kali ketika halaman web dibuka.\n
    Panjang atau banyaknya data adalah 221 data
    """
    anime = DaftarAnime.objects.all()

    context = {
        # "Anime" : anime,
        "Anime": anime,
        "Hero": "Portal Komunitas Anime",
        "Lead": "Terupdate se-Indonesia",
        "page": "Beranda",
        "website": "Anime Indonesia",
    }

    return render(request, "index.html", context)
