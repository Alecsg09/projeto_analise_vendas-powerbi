import pandas as pd
import numpy as np
from faker import Faker
import random

# Inicializando Faker para gerar nomes fictícios
fake = Faker('pt_BR')

# Definição de parâmetros
num_linhas = 5000  # Número de vendas a serem geradas
categorias = {
    "Eletrônicos": ["Smartphone", "Notebook", "Tablet", "Fone de Ouvido"],
    "Móveis": ["Sofá", "Cadeira", "Mesa", "Estante"],
    "Vestuário": ["Camisa", "Calça", "Tênis", "Jaqueta"]
}
regioes = ["Sudeste", "Sul", "Centro-Oeste", "Nordeste", "Norte"]
vendedores = [fake.name() for _ in range(10)]

# Gerando dados
dados = []
for i in range(1, num_linhas + 1):
    categoria = random.choice(list(categorias.keys()))
    produto = random.choice(categorias[categoria])
    preco_unitario = round(random.uniform(50, 5000), 2)
    quantidade = random.randint(1, 10)
    receita = round(preco_unitario * quantidade, 2)
    
    dados.append([
        i,  # ID da venda
        fake.date_between(start_date='-2y', end_date='today'),  # Data da venda
        produto,
        categoria,
        preco_unitario,
        quantidade,
        receita,
        random.choice(vendedores),  # Nome do vendedor
        random.choice(regioes)  # Região de venda
    ])

# Criando DataFrame
colunas = ["ID Venda", "Data Venda", "Produto", "Categoria", "Preço Unitário", "Quantidade", "Receita", "Vendedor", "Região"]
df = pd.DataFrame(dados, columns=colunas)

# Salvando para Excel
df.to_excel("dados_vendas.xlsx", index=False)
print("Arquivo 'dados_vendas.xlsx' gerado com sucesso!")
