segundos = int( input("Por favor, entre com o número de segundos que deseja converter: ") )

dias = segundos // 86400
segundosRestante = segundos % 86400

horas = segundosRestante // 3600
segundosRestante = segundos % 3600

minutos = segundosRestante // 60
segundos = segundosRestante % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos")
