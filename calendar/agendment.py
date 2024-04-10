import calendar
import datetime

# Cria um calendário
cal = calendar.TextCalendar(calendar.SUNDAY)

# Define o mês e o ano que deseja exibir no calendário
mês = 3
ano = 2024

# Imprime a legenda do calendário
print(cal.formatyear(ano,w=1,l=1,c=6))

# Imprime o calendário do mês e ano definidos
class print_calendar():
    
    for semana in cal.monthdayscalendar(ano,mês):
        for dia in semana:
            if dia:
                print(f"{dia:2d} ", end="")
            else:
                print("  ", end="")
        print()


agenda = {}

# Adiciona uma reunião
agenda[datetime.date(2024, 3, 26)] = {
    "nome": "Reunião 1",
    "hora": "10:00",
    "duração": "1:00"
}

# Imprime a agenda automatizada
for dia, reuniões in sorted(agenda.items()):
    print(f"\n{dia.strftime('%A, %B %d, %Y')}")
    print(f"{reuniões['nome']} - {reuniões['hora']} às {reuniões['hora'] + reuniões['duração']}")
