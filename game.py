#Adivinhador de codigo 
# para jogar você deve inserir um codigo de 4 numeros, se seu codigo tiver numeros semelhantes ao codigo correto, ou posições das letras semelhantes
# você será notificado, junte as informações e descubra o codigo da maquina 
import random
numero_aleatorio = random.randint(1000, 9999)
m = numero_aleatorio // 1000
c = (numero_aleatorio % 1000) // 100
d = (numero_aleatorio % 100) // 10
u = numero_aleatorio % 10
cont = 20
qntd_p = 0
qntd_l = 0
while cont > 0:
    tent = input("Digite um número de 4 dígitos: ")
    mt = int(tent[0])
    ct = int(tent[1])
    dt = int(tent[2])
    ut = int(tent[3])
    # Se acertar
    if mt == m and ct == c and dt == d and ut == u:
        print("Parabéns! Você acertou o código com êxito.")
        break

    # quantidade de posições corretas
    if mt == m:
        qntd_p += 1
    if ct == c:
        qntd_p += 1
    if dt == d:
        qntd_p += 1
    if ut == u:
        qntd_p += 1
    print("quantidade de posições:", qntd_p)
    qntd_p = 0

    # quantidade de numeros corretos
    if mt == m or mt == c or mt == d or mt == u:
        qntd_l += 1 
    if ct == m or ct == c or ct == d or ct == u:
        qntd_l += 1 
    if dt == m or dt == c or dt == d or dt == u:
           qntd_l += 1 
    if ut == m or ut == c or ut == d or ut == u:
           qntd_l += 1 
    print("quantidade de números:", qntd_l)
    qntd_l = 0

    # contador descendo 1 a cada tentativa
    cont -= 1
    print(f"Ainda restam {cont} tentativas")
    # aqui volta ao while

    # quando acaba as chances
if cont == 0:
     print(f"Suas chances acabaram! Não foi dessa vez, mais sorte na próxima tentativa... O Código era {numero_aleatorio}")