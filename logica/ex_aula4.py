def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media

def boletim(media):
    print(f"As notas inseridas foram: {nota1}, {nota2} e {nota3}")
    print(f"A média final foi: {media:.2f}")

    if media >= 7:
        print("Situação: Aprovado direto")
    elif media >= 4:
        print("Situação: Recuperação")
    else:
        print("Situação: Reprovado direto")

# Coletando as notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Chamando a função de boletim com o retorno da função calcular_media
boletim(calcular_media(nota1, nota2, nota3))