import requests
from bs4 import BeautifulSoup
from app import app
from app.helpers import sunatconstants
from app.models.sunatinfo import SunatInfo


def read_info(img_text, ruc, cookies):
    url_info = app.config['SUNAT_URL_INFO']
    url_info = url_info.format(ruc, img_text)
    response_info = requests.get(url_info, cookies=cookies)
    html_info = BeautifulSoup(response_info.content, 'html.parser')
    table_info = html_info.find_all('tr')
    return table_info


def convert_sunat_obj(table_info, ruc):
    try:
        sunat_info = SunatInfo()

        # RUC - Razon Social
        numero_ruc = (table_info[0].find_all("td"))[1].contents[0]
        sunat_info.ruc = numero_ruc.split('-')[0]
        sunat_info.razon_social = numero_ruc.split('-')[1]

        # Tipo Contribuyente
        sunat_info.tipo_contribuyente = (table_info[1].find_all("td"))[1].contents[0]

        sunat_cons = None
        if ruc[0] == '1':
            # Verificar Nuevo RUS
            nuevo_rus = (table_info[3].find_all("td"))[2].contents[0].strip()
            if nuevo_rus == 'Afecto al Nuevo RUS:':
                sunat_cons = sunatconstants.PersonaNaturalNuevoRusConstant
            else:
                sunat_cons = sunatconstants.PersonaNaturalSinRusConstant
        elif ruc[0] == '2':
            sunat_cons = sunatconstants.PersonaJuridicaConstant

        # Nombre Comercial
        sunat_info.nombre_comercial = (table_info[sunat_cons.nombre_comercial.value].find_all("td"))[1].contents[0]

        # Fecha Inscripcion
        sunat_info.fecha_inscripcion = (table_info[sunat_cons.fecha_inscripcion.value].find_all("td"))[1].contents[0]

        # Estado Contribuyente
        sunat_info.estado_contibuyente = (table_info[sunat_cons.estado_contribuyente.value].find_all("td"))[1].contents[
            0]

        # Condicion Contribuyente
        sunat_info.condicion_contribuyente \
            = (table_info[sunat_cons.condicion_contribuyente.value].find_all("td"))[1].contents[0].replace('\r', '') \
            .replace('\n', '').strip()

        # Domicilio Fiscal
        domicilio = (table_info[sunat_cons.domicilio_fiscal.value].find_all("td"))[1].contents[0]
        sunat_info.domicilio_fiscal = ' '.join(domicilio.split())

        # Actividad Económica
        act_ec_td = ((table_info[sunat_cons.actividad_economica.value].find_all("td"))[1])
        sunat_info.actividad_economica = act_ec_td.find('select').find('option').contents[0]

        return sunat_info
    except Exception:
        raise Exception('HTML Incorrect')
