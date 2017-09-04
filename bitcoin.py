import urllib.request, json 

# TICKER

# Retorna informações com o resumo das últimas 24 horas de negociações.

#  high: Maior preço unitário de negociação das últimas 24 horas. Tipo: Decimal
#  low: Menor preço unitário de negociação das últimas 24 horas. Tipo: Decimal
#  vol: Quantidade negociada nas últimas 24 horas. Tipo: Decimal
#  last: Preço unitário da última negociação. Tipo: Decimal
#  buy: Maior preço de oferta de compra das últimas 24 horas. Tipo: Decimal
#  sell: Menor preço de oferta de venda das últimas 24 horas. Tipo: Decimal
#  date: Data e hora da informação em Era Unix. Tipo: Inteiro

with urllib.request.urlopen("https://www.mercadobitcoin.net/api/BTC/ticker/") as url:
    data = json.loads(url.read().decode())

ticker = data['ticker']
print("Volume = ",ticker['vol'])

# ORDERBOOK

# Livro de ofertas é composto por duas listas: 
# (1) uma lista com as ofertas de compras ordenadas pelo maior valor; 
# (2) uma lista com as ofertas de venda ordenadas pelo menor valor. 
# O livro mostra até 1000 ofertas de compra e até 1000 ofertas de venda.

# Uma oferta é constituída por uma ou mais ordens, sendo assim, a quantidade da oferta é o resultado da soma 
#		das quantidades das ordens de mesmo preço unitário. Caso uma oferta represente mais de uma ordem, 
#		a prioridade de execução se dá com base na data de criação da ordem, da mais antiga para a mais nova.

# bids: Lista de ofertas de compras, ordenadas do maior para o menor preço.
# Tipo: Array
# [0]: Preço unitário da oferta de compra.
# Tipo: Decimal
# [1]: Quantidade da oferta de compra.
# Tipo: Decimal
#  asks: Lista de ofertas de venda, ordenadas do menor para o maior preço.
# Tipo: Array
# [0]: Preço unitário da oferta de venda.
# Tipo: Decimal
# [1]: Quantidade da oferta de venda.
# Tipo: Decimal

with urllib.request.urlopen("https://www.mercadobitcoin.net/api/BTC/orderbook/") as url:
    data = json.loads(url.read().decode())

buybook = data['bids']
sellbook = data['asks']
i = 0;
for buy in buybook:
    i = i + 1
    print(i, " : ", buy)

i = 0;
for sell in sellbook:
    i = i + 1
    print(i, " : ", sell)
#print("Volume = ",ticker['vol'])    


# TRADES

# Histórico de operações executadas ou negociações realizadas.

#  []: Lista de operações realizadas.
# date: Data e hora da operação em Era Unix 
# Tipo: Decimal
# price: Preço unitário da operação.
# Tipo: Decimal
# amount: Quantidade da operação.
# Tipo: Decimal
# tid: Identificador da operação.
# Tipo: Inteiro
# type: Indica a ponta executora da operação 
# Tipo: String
# Domínio de dados:
# buy : indica ordem de compra executora
# sell : indica ordem de venda executora