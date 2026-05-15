receita = input()
quantidade_pao, quantidade_salsicha, quantidade_queijo = map(int, input().split())
preco_pao, preco_salsicha, preco_queijo = map(int,input().split())
dinheiro = int(input())

quantidade_receita_pao = receita.count("B")
quantidade_receita_salsicha = receita.count("S")
quantidade_receita_queijo = receita.count("C")


l = 0
r = 10 ** 14
res = 0
while l <= r:
    mid = (l + r) // 2

    total_paes = quantidade_receita_pao * mid
    total_salsicha = quantidade_receita_salsicha * mid
    total_queijo = quantidade_receita_queijo * mid

    comprar_paes = max(0,total_paes - quantidade_pao)
    comprar_salsicha = max(0,total_salsicha - quantidade_salsicha)
    comprar_queijo = max(0,total_queijo - quantidade_queijo)

    gastar_pao = comprar_paes * preco_pao
    gastar_salsicha = comprar_salsicha * preco_salsicha
    gastar_queijo = comprar_queijo * preco_queijo

    total = gastar_pao + gastar_salsicha + gastar_queijo

    possivel = dinheiro >= total

    if possivel:
        res = mid
        l = mid + 1
    else:
        r = mid - 1

print(res)
