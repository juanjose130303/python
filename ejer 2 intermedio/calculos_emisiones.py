# calculos_emisiones.py

def calcular_emisiones_electricidad(consumo_electricidad, factor_emision_electricidad):
    return consumo_electricidad * factor_emision_electricidad

def calcular_emisiones_transporte(kilometros_recorridos, factor_emision_transporte):
    return kilometros_recorridos * factor_emision_transporte

def calcular_emisiones_total(consumos_por_dependencia, factor_emision_energia):
    return sum(consumos_por_dependencia) * factor_emision_energia
