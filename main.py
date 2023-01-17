import pandas as pd
from twilio.rest import Client
import os
# Passo a Passo da solução
# Abrir as bases de dados
# Para cada arquivo:
    # Verificar se possui algum valor superior a R$55.000
    # Se for encontrado algum valor superior a R$55.000 deve ser possível disparar um SMS indicando quem foi o vancedor

months = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

def sendSMS(client, to, sendFrom, body):
    client.messages.create(
        to=to,
        from_=sendFrom,
        body=body
    )

for month in months:
    file = pd.read_excel(f'{month}.xlsx')
    for j in file:
        for index, i in enumerate(file[j]):
            if j == 'Vendas':
                if i > 55000:
                    salesman = file['Vendedor'][index]
                    account_sid = 'Your Twillio account Id'
                    auth_token = 'Your Twillio auth token'
                    client = Client(account_sid, auth_token)
                    body = f'''
                    {salesman} venceu nosso desafio, completou com R${i} em vendas no mês de {month}!
                    Calma, isso é só um código de Matheus Guirra!'''
                    sendSMS(client, 'Send Message to', 'Sender', body)
                    break


