# Consulta RUC Sunat

API que permite obtener la información de una empresa o persona juridica mediante el RUC.

Hace uso de Web Scrapping a la página de la SUNAT: 
https://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/frameCriterioBusqueda.jsp

Ofrece las siguientes ventajas:
  - Permite obtener informacion de una empresa en tiempo real mediante el RUC.
  - No es necesario descargar la base de datos que SUNAT ofrece.

### Guia de uso
Esta API está desarrollada en usando las siguientes tecnologias:
  - Python 3.7 
  - Flask
  - BeautifulSoup

Instalar las depencias usando el siguiente comando:
```sh
pip install -r requirements.txt
```
Instalar **Tesseract** de la siguiente página y elegir el instalador de 32 bits o 64 bits (depende de la PC a ejecutar el API):
```sh
https://github.com/UB-Mannheim/tesseract/wiki
```
Despues de la instalación, configurar la ruta de donde se ha instalado **Tesseract** en el archivo config.py
Ejemplo:
```sh
TESSERACT_ROUTE = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

Para empezar la aplicación usar:
```sh
flask run
```

