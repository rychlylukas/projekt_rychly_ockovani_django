from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


def qr_path(instance, filename):
    return"ockovani/"+ str(instance.id) + "/qr/"+ filename


class Vakcina(models.Model):
    nazev_firmy = models.CharField(max_length=50, null=False, blank=False, verbose_name="Název firmy")
    ucinnost_vakciny = models.IntegerField(null=False, blank=False, verbose_name="Účinnost vakcíny v %")
    cena_vakciny = models.IntegerField(verbose_name="Cena vakcíny v Kč", null=True)
    typ_vakciny = models.CharField(max_length=50, verbose_name="Typ vakcíny")
    pocet_davek = models.IntegerField(verbose_name="Počet dávek")
    schvaleno_v_EU = models.BooleanField(verbose_name="Schváleno v EU")

    class Meta:
        ordering = ["nazev_firmy"]

    def __str__(self):
        return self.nazev_firmy


class Povolani(models.Model):
    nazev_povolani = models.CharField(max_length=50, null=False, blank=False, verbose_name="Název povolání")

    class Meta:
        ordering = ["nazev_povolani"]

    def __str__(self):
        return self.nazev_povolani


class Ockovani(models.Model):
    jmeno = models.CharField(max_length=50, null=False, blank=False, verbose_name="Jméno")
    prijmeni = models.CharField(max_length=50, null=False, blank=False, verbose_name="Příjmení")
    datum_narozeni = models.DateField(null=False, blank=False, verbose_name="Datum narození")
    datum_prvni_ockovani = models.DateField(null=False, blank=False, verbose_name="Datum prvního očkování")
    datum_druhe_ockovani = models.DateField(null=True, blank=True, verbose_name="Datum druhého očkování - dle počtu dávek vakcíny")
    kod_ockovaneho = models.CharField(max_length=10, null=False, blank=False, verbose_name="Kód k očkování")
    kod_pojistovny = models.IntegerField(null=False, blank=False, verbose_name="Kód pojišťovny")
    qr = models.ImageField(upload_to=qr_path, blank=True, null=True, verbose_name="QR kód")
    vakcina = models.ManyToManyField(Vakcina, verbose_name="Vyberte vakcínu")
    povolani = models.ManyToManyField(Povolani, verbose_name="Vyberte povolani")


    class Meta:
        ordering = ["datum_narozeni", "prijmeni"]

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}, datum narození: {self.datum_narozeni}"

    def get_absolute_url(self):
        return reverse('ockovani-detail', args=[str(self.id)])