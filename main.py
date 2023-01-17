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
                    account_sid = 'AC8cbf0b36ba66fb051ae0f4882f8fccc4'
                    auth_token = 'b9b215066988889815593fefde175adf'
                    client = Client(account_sid, auth_token)
                    body = f'''
                    {salesman} venceu nosso desafio, completou com R${i} em vendas no mês de {month}!
                    Calma, isso é só um código de Matheus Guirra!'''
                    sendSMS(client, '+5561992839756', '+17753777603', body)
                    break


