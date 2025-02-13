#Escreva um programa que faça o cálculo do imposto de renda 2025. Consulte a tabela no site da Receita federal.
print("miguel do amaral paes ronda")
salario = float(input("digite seu salario:"))
if salario <= 2259.20:
    print("voce esta insento")
else: 
  if  salario >= 2259.21 and salario <= 2828.65:
    aliquota = salario*7.5/100
    print("voce vai pagar ",aliquota)
  else:
   if salario >= 2828.66 and salario <= 3751.05:
       aliquota = salario*15/100
       print("voce vai pagar",aliquota)
   else:
        if salario >= 3751.06 and salario <= 4664.68:
            aliquota = salario*22.5/100
            print("voce vai pagar",aliquota)
        else:
            if salario > 4664.68: 
                aliquota = salario*27.5/100
                print("voce vai pagar",aliquota)


   
      
