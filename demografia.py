print("Olá, a fim de manter o compromisso com a verdade, afinal, não sou um programa adepto de sofismos, utilize dados demográficos concernentes com a última estimativa populacional do IBGE.")

#Considere utilizar o Microsoft Excel como recurso de trabalho braçal.

comarca=input("Digite o nome do município e da unidade federativa:")
população=float(input("Digite a população atual:"))
nascimentos=float(input("Digite o número atual de nascimentos:"))
óbitos=float(input("Digite o número atual de óbitos:"))

diferença=(nascimentos) - (óbitos)
crescimento=(população) + (diferença)
natalidade=((nascimentos)*(1000))//(população)
mortalidade=((óbitos)*(1000))//(população)

if diferença>0:
   print("Esse município possui um crescimento demográfico positivo, necessitando de políticas públicas e privadas que visem à construção de Escolas e parques infantis para crianças. Ademais, municípios assim possuem enormes capacidades de expandirem suas economias utilizando-se de uma mão de obra jovem e ativa.")
   print("Sendo, portanto, o número atual de habitantes igual a", crescimento, "tendo uma taxa de natalidade igual a", natalidade, "nascidos vivos por mil habitantes e uma taxa de mortalidade igual a", mortalidade, "por mil habitantes.")
else: 
   print("Esse município possui um crescimento demográfico negativo, fazendo-se necessária, portanto, a atuação dos diversos segmentos sociais em promover assistência médica e recursos culturais aos idosos. Destarte, municípios com essa característica demográfica possuem maiores chances de se tornarem lugares idílicos, conforme imaginou Mário Quintana em seus poemas.")
   print("Sendo, logo, o número total de habitantes igual a", crescimento, "tendo uma taxa de natalidade igual a", natalidade, "nascidos vivos por mil habitantes e uma taxa de mortalidade igual a", mortalidade, "por mil habitantes.")
if diferença==0:
   print("Hum, podemos ver claramente um município com variação populacional constante e igual a zero, um lugar idílico, tal como imaginou Mário Quintana em seus poemas.")
   

