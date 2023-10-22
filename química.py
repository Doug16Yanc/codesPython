print("Programa baseado nos exercícios disponibilizados pelo Instituto de Matemática e Estatística da Universidade de São Paulo")

print("Arla 32 é uma solução de aproximadamente 32 g de ureia(H2NCONH2) em 100 mL de água utilizada em veículos a diesel")
print("para diminuir as emissões de óxidos de nitrogênio(NO e NO2), que podem causar problemas ambientais, quando em")
print("excesso na atmosfera. A solução de Arla, ao ser adicionada aos gases de escape do motor, em alta temperatura, forma")
print("amônia. Em uma segunda etapa, a amônia reage com NO2 e gera gás nitrogênio e água.")
print("Analise os cálculos estequiométricos")
quilômetros=input("Digite a quantidade de quilômetros rodados:")
dióxido_de_nitrogênio=input("Digite a quantidade de dióxido de nitrogênio produzida em gramas por km rodado:")
Quantidade=float(dióxido_de_nitrogênio)*float(quilômetros)
Estequiometria=(Quantidade*240)//(6*46)
Volume=(Estequiometria*0.1)/32
print("Serão liberados", Estequiometria, "g de Arla 32, o que equivalem a", Volume, "litros de solução")