from datetime import date

ano = date.today().year
contagemMaiores = 0 
contagemMenores = 0

for i in range (1,8):
    nasc = int(input(f"Digite o ano {i}º em que a pessoa nasceu: "))
    idade = ano - nasc

    if idade >= 18:
        contagemMaiores += 1
    else:
        contagemMenores += 1
            
print(f"{contagemMaiores} pessoas são maiores de idade e {contagemMenores} são menores de idade")            