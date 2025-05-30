from csv import DictReader

from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from io import TextIOWrapper
from django.shortcuts import render, redirect
from django.urls import path

from .models import DestAnime
from .forms import CSVImportForm


@admin.register(DestAnime)
class AnimeAdmin(admin.ModelAdmin):
    change_list_template = 'js_on/anime_changelist.html'
    list_display = ("data",)

    def import_csv(self, request: HttpRequest) -> HttpResponse:
        if request.method == "GET":
            form = CSVImportForm()
            context = {
                'form': form
            }
            return render(request, 'admin/csv_form.html', context)
        form = CSVImportForm(request.POST, request.FILES)
        if not form.is_valid():
            context = {
                'form': form
            }
            return render(request, 'admin/csv_form.html', context, status=400)




    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path('import-products-csv', self.import_csv, name='import_products_csv'),
        ]
        return new_urls + urls
