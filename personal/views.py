from django.shortcuts import render
from datetime import datetime

patrias = ['18/05;Dìa de la Escarapela y Comienzo Semana de Mayo',
           '19/05;Petición a un Cabildo abierto',
           '20/05;Convocatoria del Cabilo abierto',
           '21/05;Se invita a los vecinos al Cabildo abierto',
           '22/05;Cabildo abierto, cese del mando del Virrey',
           '23/05;Junta de Gobierno con el Virrey como presidente',
           '24/05;Renuncia de todos los miembros de la Junta',
           '25/05;Se reconoce el primer Gobierno Patrio',
           '20/06;Dìa de la Bandera',
           '09/07;Dìa de la Independenca']

links = ['https://es.wikipedia.org/wiki/Escarapela_de_la_Argentina#Origen_de_la_fiesta_de_la_escarapela',
         'https://es.wikipedia.org/wiki/Revoluci%C3%B3n_de_Mayo#S.C3.A1bado_19_de_mayo',
         'https://es.wikipedia.org/wiki/Revoluci%C3%B3n_de_Mayo#Domingo_20_de_mayo',
         'https://es.wikipedia.org/wiki/Revoluci%C3%B3n_de_Mayo#Lunes_21_de_mayo',
         'https://es.wikipedia.org/wiki/Revoluci%C3%B3n_de_Mayo#Martes_22_de_mayo',
         'https://es.wikipedia.org/wiki/Revoluci%C3%B3n_de_Mayo#Mi.C3.A9rcoles_23_de_mayo',
         'https://es.wikipedia.org/wiki/Revoluci%C3%B3n_de_Mayo#Jueves_24_de_mayo',
         'https://es.wikipedia.org/wiki/Revoluci%C3%B3n_de_Mayo#Viernes_25_de_mayo',
         'https://es.wikipedia.org/wiki/D%C3%ADa_de_la_Bandera_(Argentina)',
         'https://es.wikipedia.org/wiki/D%C3%ADa_de_la_Independencia_de_la_Rep%C3%BAblica_Argentina']


def index(request):
    return render(request, 'personal/WIP.html')


def home(request):
    return render(request, 'personal/home.html')


def fechas(request):
    return render(request, 'personal/fechas.html', {
        'fechas': get_date_table(patrias, links), 'cercana': get_next(patrias)})


def get_next(flist):
    fpat = []

    today = datetime.today().strftime('%m%d')

    for dates in flist:
        date = '{}{}'.format(dates[3:5], dates[0:2])
        if int(date) >= int(today):
            fpat.append(date)

    cercana = min(fpat, key=lambda x: abs(int(x) - int(today)))

    return '{}/{}'.format(cercana[2:4], cercana[0:2])


def get_date_table(flist, llist):
    comb = []
    for n, t in enumerate(flist):
        comb.append([t[0:5], t[6:], llist[n]])
    return comb
