
import math
import random
import datetime
import statistics
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# ENTRADAS
capital = float(input('Capital inicial: '))
aporte = float(input('Aporte mensal: '))
meses = int(input('Prazo (meses): '))
cdi_anual = float(input('CDI anual %: ')) / 100
perc_cdb = float(input('Percentual do CDI - CDB (%): ')) / 100
per_lci = float(input('Percentual do CDI - LCI (%): ')) / 100
taxa_fii = float(input('Rentabilidade do FII (%): ')) / 100
meta = float(input('Meta financeira (R$): '))

# conversão CDI
cdi_mensal = math.pow((1 + cdi_anual), 1/12) - 1

# total investido
total_investido = capital + (aporte * meses)

# CDB
taxa_cdb = cdi_mensal * perc_cdb
montante_cdb = (capital * math.pow((1 + taxa_cdb), meses)) + (aporte * meses)
lucro_cdb = montante_cdb - total_investido
montante_cdb_liquido = total_investido + (lucro_cdb * 0.85)

# LCI/LCA
taxa_lci = cdi_mensal * per_lci
montante_lci = (capital * math.pow((1 + taxa_lci), meses)) + (aporte * meses)

# poupança
taxa_poupanca = 0.005
montante_poupanca = (capital * math.pow((1 + taxa_poupanca), meses)) + (aporte * meses)

# estatística FII
fii1 = (capital * math.pow((1 + taxa_fii), meses)) + (aporte * meses)
fii1 = fii1 * (1 + random.uniform(-0.03, 0.03))

fii2 = (capital * math.pow((1 + taxa_fii), meses)) + (aporte * meses)
fii2 = fii2 * (1 + random.uniform(-0.03, 0.03))

fii3 = (capital * math.pow((1 + taxa_fii), meses)) + (aporte * meses)
fii3 = fii3 * (1 + random.uniform(-0.03, 0.03))

fii4 = (capital * math.pow((1 + taxa_fii), meses)) + (aporte * meses)
fii4 = fii4 * (1 + random.uniform(-0.03, 0.03))

fii5 = (capital * math.pow((1 + taxa_fii), meses)) + (aporte * meses)
fii5 = fii5 * (1 + random.uniform(-0.03, 0.03))

# statistics
media_fii = statistics.mean([fii1, fii2, fii3, fii4, fii5])
mediana_fii = statistics.median([fii1, fii2, fii3, fii4, fii5])
desvio_fii = statistics.stdev([fii1, fii2, fii3, fii4, fii5])

# datetime
data_simulacao = datetime.datetime.now()
dias = meses * 30
data_resgate = data_simulacao + datetime.timedelta(days=dias)

# meta
meta_atingida = media_fii >= meta

# gráficos
grafico_cdb = "█" * int(montante_cdb_liquido / 1000)
grafico_lci = "█" * int(montante_lci / 1000)
grafico_poupanca = "█" * int(montante_poupanca / 1000)
grafico_fii = "█" * int(media_fii / 1000)

print("\nRELATÓRIO DE INVESTIMENTOS\n")

print("Data da simulação:", data_simulacao.strftime("%d/%m/%Y"))
print("Data estimada de resgate:", data_resgate.strftime("%d/%m/%Y"))

print("\nTotal investido:", locale.currency(total_investido, grouping=True))

print("\nValores finais")

print("CDB:", locale.currency(montante_cdb_liquido, grouping=True))
print("LCI/LCA:", locale.currency(montante_lci, grouping=True))
print("Poupança:", locale.currency(montante_poupanca, grouping=True))
print("FII (média):", locale.currency(media_fii, grouping=True))

print("\nEstatísticas do FII")
print("Média:", locale.currency(media_fii, grouping=True))
print("Mediana:", locale.currency(mediana_fii, grouping=True))
print("Desvio padrão:", locale.currency(desvio_fii, grouping=True))

print("\nMeta atingida:", meta_atingida)

print("\nGráficos")

print("CDB      ", grafico_cdb)
print("LCI/LCA  ", grafico_lci)
print("Poupança ", grafico_poupanca)
print("FII      ", grafico_fii)
