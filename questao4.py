#- Peça ao usuário para inserir sua cor favorita. 
# Se ele digitar "vermelho", "VERMELHO" ou "Vermelho" exibem a mensagem "Eu também gosto de vermelho", caso contrário, exibem a mensagem "Eu não gosto de [cor], eu prefiro vermelho".
print("miguel do amaral paes ronda")
cor = input("digite a sua cor favorita:")
if cor == "VERMELHO" or cor == "Vermelho" or cor == "vermelho":
    print("eu tambem gosto de vermelho")
else:
    print("eu nao gosto de",cor,"eu prefiro vermelho")
    