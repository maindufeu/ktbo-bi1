from configparser import ConfigParser
import datetime as dt
import pandas as pd
import requests

parser = ConfigParser()
#parser.read('config.cfg')
#username = parser.get('','')
#password = parser.get('','')
#authentication_url =  parser.get('','')

def drive_checker(username,secret_client):
    print('working on it')
    mp = []
    return mp

def mail_checker(username,token):
    print('working on it')
    mp = []
    return(mp)

def mp_validate(mp):
    print('working on it')
    valid_status = 1
    if valid_status == 0:
        print('el mediaplan contiene todos los parametros necesarios')
    else:
        print('el mediaplan contiene errores')
    return valid_status

def mail_sender(message):
    print('working on it')
    mail_receiver = ['belem.viniegra@mediacom.com', 'edher@ktbo.com']
    message_status = 0
    if message_status == 0:
        print(f'No se ha enviado un correo a {mail_receiver} con la siguiente información{message}')
    else:
        print(f'Se ha enviado un correo a {mail_receiver} con la siguiente información{message}')
    return message_status

def mp_enrich(mp):
    print('working on it')
    mp_status = 0
    if mp_status ==0:
        print('el plan de medios se ha actualizado correctamente')
    else:
        print('el plan de medios no se ha podido actualizar')
    return mp_status
