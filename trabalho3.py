from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as ps

url_toyshow = "https://www.toyshow.com.br/blackfriday"
url_amocanecas ="https://www.amocanecas.com.br/canecas-copos-precos-especiais-promocao-outlet?pagina=1"

toyshow = requests.get(url_toyshow)
amo = requests.get(url_amocanecas)

htmltoy = BeautifulSoup(toyshow.content, "html.parser")
htmlamo = BeautifulSoup(amo.content,"html.parser")

produtos_promo = []
produtos_outlet = []
converteListaToy = []
converteListaAmo = []
juntar =[]
total = []
auxToy = 0;
auxAmo = 0
def total_Media():
    totalAmo = 0
    totalToy = 0
    soma = 0
    
    for i in juntar:
        totalToy = totalToy + i
    for i in total:
        totalAmo = totalAmo + i 
    soma = totalAmo + totalToy 
    print("\n Total dos valores entres as duas Lojas")
    print("------------------------------------------")
    print("{:.2f}".format(soma))
    print("\n Total da loja Amo Canecas")
    print("------------------------------------------")
    print("{:.2f}".format(totalAmo))
    print("\n Total da loja ToyShow")
    print("------------------------------------------")
    print("{:.2f}".format(totalToy))
    
def pesquisar(value):
    for produto in produtos_outlet:
        if value in produto['descricao']:
            print(f"O produto {produto['descricao']} foi encontrado em AMO CANECAS!")
        
    for produto in produtos_promo:
        if value in produto['descricao']:
            print(f"O produto {produto['descricao']} foi encontrado em TOYSHOW!")
        
########## BUSCA HTML amoPROMOCAO #############
produtos_amopromocao = htmlamo.find_all("a", attrs={"class":"produto-sobrepor"})
precoAmo = htmlamo.find_all("s", attrs={"class":"preco-venda"})
descontoAmo = htmlamo.find_all("strong", attrs={"class": "preco-promocional"})


for i in range(0,len(produtos_amopromocao)):
    output = produtos_amopromocao[i]['title'] 
    produtos_outlet.append({"descricao": output, "preco":precoAmo[i].text.strip(),"desconto":descontoAmo[i].text.strip()}) 

########## BUSCA HTML TOYPROMOCAO #############
produtos_toypromocao = htmltoy.find_all("h2")
precoToy = htmltoy.find_all("div", attrs={"class":"price"})
descontoToy = htmltoy.find_all("span", attrs={"class":"price-off"})

for i in range(0,len(precoToy)):
    
    produtos_promo.append({"descricao" : produtos_toypromocao[i].text.strip(), "precoToy": precoToy[i].text.strip(), "descontoToy":descontoToy[i].text.strip().replace("\n","") })


       ####CONVERSÃO PRECOS TOYSHOW########  
for preco in produtos_promo:
    converteListaToy.append(list(preco['precoToy']))
    
for valores in range(0,len(converteListaToy)):
    
        auxToy = converteListaToy[valores]
        if len(auxToy) == 10:
            quebrar = auxToy[6] + auxToy[7] + auxToy[8] + auxToy[9]
            quebrar = quebrar.replace(',','.')
            
            juntar.append(float(quebrar))
        if len(auxToy) == 11:
            quebrar = auxToy[6] + auxToy[7] +auxToy[8] +auxToy[9] +auxToy[10]
            quebrar = quebrar.replace(',','.')
            
            juntar.append(float(quebrar))
        if len(auxToy) == 12:
            quebrar = auxToy[6] + auxToy[7] +auxToy[8] +auxToy[9] +auxToy[10] + auxToy[11]
            quebrar = quebrar.replace(',','.')
         
            juntar.append(float(quebrar))

####CONVERSÃO PRECOS AMO CANECAS########  
for preco in produtos_outlet:
    converteListaAmo.append(list(preco['preco']))
    
for valores in range(0,len(converteListaAmo)):
    
        auxAmo = converteListaAmo[valores]
       
        if len(auxAmo) == 7:
            quebrar = auxAmo[3] + auxAmo[4] + auxAmo[5] + auxAmo[6]
            quebrar = quebrar.replace(',','.')
            total.append(float(quebrar))
        if len(auxAmo) == 8:
            quebrar = auxAmo[3] + auxAmo[4] +auxAmo[5] +auxAmo[6] +auxAmo[7]
            quebrar = quebrar.replace(',','.')
            total.append(float(quebrar))
                

def titulos(produto,precoToy,espacador="."):
    print()
    print(f"{produto}{espacador*74} {precoToy}")
    
    
def toy_show():
    titulos('Produto','Preço')
    for produto in produtos_promo:
    
        print(f"{produto['descricao']:80s}  {produto['precoToy']:20s} {produto['descontoToy']}")

def amo_canecas():
    titulos('Produto','Preço')
    for produto in produtos_outlet:
    
        print(f"{produto['descricao']:80s}  {produto['preco']:20s} {produto['desconto']}")

def ordenar():
    
    print("Listando por ordem de preço")
    
    byName = []
    
    for nome in produtos_promo:
        byName.append(f" {nome['descricao']} ")
    
    lista=sorted(byName)
    
    for nome in lista:
        print(nome)
        
def todos_produtos():  
    todos = set()     

    for produto in produtos_promo:
        todos.add(f"{produto['descricao']:80s} Toyshow")

    for produto in produtos_outlet:
        todos.add(f"{produto['descricao']:80s} Amo Canecas")

    # print(todos)
    
    # converte set (que não mantém ordem) em lista (que mantém)
    lista = list(todos)

    # classifica em ordem a lista
    lista2 = sorted(lista)

    print("Todos os produtos nas loja")

    for produto in lista2:
        print(produto)
        
def diferenca_toy():
    toyDif = set()     
    amoDif = set()

    for produto in produtos_promo:
       toyDif.add(produto['descricao'])

    for produto in produtos_outlet:
        amoDif.add(produto['descricao'])

    produtosToyshow = toyDif.difference(amoDif)

    print("Produtos Apenas da Toyshow")

    
    for produto in produtosToyshow:
            print(produto)
            
def diferenca_amo():
    toyDif = set()     
    amoDif = set()

    for produto in produtos_promo:
       toyDif.add(produto['descricao'])

    for produto in produtos_outlet:
        amoDif.add(produto['descricao'])

    produtosAmo = amoDif.difference(toyDif)

    print("Produtos Apenas da Amo Canecas")

    
    for produto in produtosAmo:
            print(produto)
            
def comuns():
    toyIgual = set()
    amoIgual = set()
    
    for produto in produtos_promo:
        toyIgual.add(produto['descricao'])
    for produto in produtos_outlet:
        amoIgual.add(produto['descricao'])
    produtosComuns = toyIgual.intersection(amoIgual)
    
    print("\nProdutos em comum nas lojas")
    
    if len(produtosComuns) == 0:
        print("\nNão há produtos em comum nas lojas")
    else:
        for produto in produtosComuns:
            print(produto)
   

         
        # print(type({preco['precoToy']}))
        
        
while True:
    # precoTotaleMedida()
    print("\n           Artigos GEEK - Toyshow e Amo Canecas")    
    print("1. Toyshow")
    print("2. Amo Canecas")
    print("3. Todos produtos")
    print("4. Diferenca(Toyshow)")
    print("5. Diferenca(Amo canecas)")
    print("6. Comuns nas lojas")
    print("7. Preco total")
    print("8. Pesquisar produto")
    print("Para sair pressione qualquer tecla")    
    opcao = int(input("Opção: "))
    if opcao == 1:
         toy_show()
    elif opcao == 2:
        amo_canecas()
    elif opcao == 3:
        todos_produtos() 
    elif opcao == 4:
        diferenca_toy()
    elif opcao == 5:
        diferenca_amo()
    elif opcao == 6:
        comuns()
    elif opcao == 7:
        total_Media()
    elif opcao == 8:
        value = str(input("Produto pesquisa:"))
        pesquisar(value)
    else:
        break
