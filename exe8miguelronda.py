#Escreva um programa que pergunte a velocidade do carro de um usuário. 
# Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.
print("miguel do amaral paes ronda")

velo = int(input("qual era a velocidsade do carro" ))
if velo > 80:
    multa =(velo-80)*5
    print("a multa e de:",multa)
    

