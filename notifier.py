def verificar_preco(preco, preco_alvo):
    if preco and preco < preco_alvo:
        print(f"PROMOÇÃO! Preço caiu para R$ {preco}")
    else:
        print(f"Preço atual: R$ {preco}")