from django.shortcuts import render
from django.db import connection


def index(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM js_on_DestAnime")
        row = cursor.fetchall()
    print(row)
    return render(request, 'js_on/index.html', {'row': row})
