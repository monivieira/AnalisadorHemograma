from faker import Faker
import pandas as pd
import matplotlib.pyplot as plt

# Instanciando gerador de nomes em pt-br
fake = Faker('pt_br')

# Carrega os dados do csv
df = pd.read_csv('dados.csv', sep=',')

# Geração randômica de nomes fictícios, apenas o primeiro
df['Paciente'] = [fake.first_name() for _ in range(len(df))]

# Arredonda os valores para facilitar leitura no output
df = df.round({'Leucocitos': 0, 'Hemacias': 1, 'Plaquetas': 0})

# Exibição das estatísticas
print(df.describe().round(1))

# Filtrar pacientes com leucócitos acima de 11k
alterados = df[df['Leucocitos'] > 11000]
print("\nPacientes com leucócitos alterados:")
print(alterados)

# Criação/Exibição de gráfico de barras com leucócitos por paciente
plt.figure(figsize=(8, 6))
plt.bar(df['Paciente'], df['Leucocitos'], color='red')
plt.xlabel('\nPacientes')
plt.ylabel('Leucócitos')
plt.title('Contagem de leucócitos por paciente')
plt.show()