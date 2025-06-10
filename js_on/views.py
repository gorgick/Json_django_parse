from django.shortcuts import render
from django.db import connection


def create_data(request):
    with connection.cursor() as cursor:
        cursor.execute("""INSERT INTO js_on_DestAnime VALUES
        ('50',
            '{"genre": ["романтика", "фантастика"],
            "studio": "Arvo Animation",
            "director": "Ёсиаки Ивасаки",
            "amount_series": 10}'
        ),
        ('51',
            '{"genre": ["экшен", "фантастика"],
            "studio": "MAPPA",
            "director": "Норихиро Наганума",
            "amount_series": 25}'
        );""")
        row = cursor.fetchall()

    return render(request, 'js_on/index.html', {'row': row})


def index(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM js_on_DestAnime")
        cursor.execute("""SELECT * FROM js_on_DestAnime Where data @> '{"genre": ["романтика"]}'::jsonb""")
        row = cursor.fetchall()
    print(row)
    return render(request, 'js_on/index.html', {'row': row})
