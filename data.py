# -*- coding: utf-8 -*-
"""
Created on Mon May 14 15:25:59 2018

@jls2
"""
from datetime import date, datetime

def data():
    hoje = date.today()
    dia = hoje.day
    mes = hoje.month
    ano = hoje.year
    
    return (str(dia)+"/"+str(mes)+"/"+str(ano))


def hora():

    agora = datetime.now()
    horas=agora.hour
    minutos=agora.minute
    segundos=agora.second

    return(str(horas)+":"+str(minutos)+":"+str(segundos))
    