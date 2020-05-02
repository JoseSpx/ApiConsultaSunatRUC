from flask import Blueprint, jsonify, request
from app.helpers.tesseract import read_text_from_image_sunat
from app.helpers.sunatinfo import read_info, convert_sunat_obj
from app import app

SunatRoutes = Blueprint('sunat', __name__)


@SunatRoutes.route('/', methods=['GET'])
def consult_sunat_info():
    url_image = app.config['SUNAT_URL_IMG']
    ruc = request.args.get('ruc')
    if not ruc:
        response = jsonify({'message': 'RUC no enviado'})
        response.status_code = 400
        return response

    ruc = ruc.strip()
    if len(ruc) != 11:
        response = jsonify({'message': 'RUC no válido'})
        response.status_code = 400
        return response

    if ruc[0] != '1' and ruc[0] != '2':
        response = jsonify({'message': 'RUC no válido'})
        response.status_code = 400
        return response

    table_info = None
    attempts = 0
    max_attempts = 50
    while not table_info and attempts <= max_attempts:
        img_text, cookies = read_text_from_image_sunat(url_image)
        try:
            table_info = read_info(img_text, ruc, cookies)
        except BaseException:
            raise
        attempts = attempts + 1

    if not table_info:
        response = jsonify({'message': 'Ocurrio un Error'})
        response.status_code = 400
        return response

    sunat_obj = convert_sunat_obj(table_info, ruc)
    response = jsonify(sunat_obj.serialize())
    response.status_code = 200
    return response
