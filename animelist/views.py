from django.shortcuts import render
from .models import Anime as DaftarAnime
from .forms import Pencarian
import requests

# Create your views here.
api_url = "https://api.jikan.moe/v4/anime?q={keyword}&sfw"


def index(request):
    """
    Function untuk menampilkan halaman pencarian anime
    """
    anime = DaftarAnime.objects.all()
    form_pencarian = Pencarian()
    context = {
        "Anime": anime,
        "form_pencarian": form_pencarian,
        "Hero": "Portal Komunitas Anime",
        "Lead": "Terupdate se-Indonesia",
        "page": "Daftar Anime",
        "website": "Anime Indonesia",
    }

    # # Cara mengambil nilai atau query yang diketik dalam kolom pencarian
    # print(f"Hasil kata kunci pencarian anda adalah = {request.POST['search']}")
    if request.method == "POST":
        context["hasil_pencarian"] = request.POST["search"]
        # # Template variabel URL di atas akan diisi dengan kueri dari kolom pencarian
        # print(url.format(keyword=context['hasil_pencarian']))
        req = requests.get(
            url=api_url.format(keyword=context["hasil_pencarian"])
        )
        context["data_pencarian"] = req.json()["data"]

    return render(request, "animelist/index.html", context)
