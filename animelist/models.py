from django.db import models
from django.utils.text import slugify


# Create your models here.
class Contents(models.Model):
    mal_id = models.IntegerField(unique=True)
    slug = models.SlugField(max_length=255, editable=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Studio(Contents):
    studio_name = models.CharField(max_length=255, unique=True)
    company_name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.studio_name)
        super(Studio, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.studio_name

    class Meta:
        ordering = ["studio_name"]


class GenreAnime(Contents):
    genre = models.CharField(max_length=50)

    class Meta:
        ordering = ["genre"]


class Anime(Contents):
    anime_title = models.CharField(max_length=255)
    anime_score = models.DecimalField(
        decimal_places=2, max_digits=10, default=0)
    airing_time = models.CharField(max_length=50, blank=True)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, default='')
    genre = models.ForeignKey(GenreAnime, on_delete=models.CASCADE, default='')
    api_url = models.CharField(blank=True, max_length=255)
    poster_url = models.CharField(blank=True, max_length=255)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.anime_title)
        super(Anime, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.anime_title

    class Meta:
        ordering = ["anime_title"]
