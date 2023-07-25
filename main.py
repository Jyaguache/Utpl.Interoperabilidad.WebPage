from flask import Flask, render_template, request, redirect, url_for

import requests

app = Flask(__name__)

#Declarar el API KEY generado de wso2 api manager desde la aplicacion
API_KEY = 'eyJ4NXQiOiJPREUzWTJaaE1UQmpNRE00WlRCbU1qQXlZemxpWVRJMllqUmhZVFpsT0dJeVptVXhOV0UzWVE9PSIsImtpZCI6ImdhdGV3YXlfY2VydGlmaWNhdGVfYWxpYXMiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhZG1pbkBjYXJib24uc3VwZXIiLCJhcHBsaWNhdGlvbiI6eyJvd25lciI6ImFkbWluIiwidGllclF1b3RhVHlwZSI6bnVsbCwidGllciI6IlVubGltaXRlZCIsIm5hbWUiOiJBcHBKaW1teSIsImlkIjo3LCJ1dWlkIjoiNzg3Yjk3ZjUtNDBkZi00Mjc0LTk0ZDgtNzc1YmMwODM4OWFiIn0sImlzcyI6Imh0dHBzOlwvXC91dHBsd3NvMi50azo0NDNcL2FwaW1cL29hdXRoMlwvdG9rZW4iLCJ0aWVySW5mbyI6eyJVbmxpbWl0ZWQiOnsidGllclF1b3RhVHlwZSI6InJlcXVlc3RDb3VudCIsImdyYXBoUUxNYXhDb21wbGV4aXR5IjowLCJncmFwaFFMTWF4RGVwdGgiOjAsInN0b3BPblF1b3RhUmVhY2giOnRydWUsInNwaWtlQXJyZXN0TGltaXQiOjAsInNwaWtlQXJyZXN0VW5pdCI6bnVsbH19LCJrZXl0eXBlIjoiU0FOREJPWCIsInN1YnNjcmliZWRBUElzIjpbeyJzdWJzY3JpYmVyVGVuYW50RG9tYWluIjoiY2FyYm9uLnN1cGVyIiwibmFtZSI6IlV0cGwtUHJvZHVjdG9zQXBpIiwiY29udGV4dCI6IlwvcHJvZHVjdG9zXC8xLjAiLCJwdWJsaXNoZXIiOiJhZG1pbiIsInZlcnNpb24iOiIxLjAiLCJzdWJzY3JpcHRpb25UaWVyIjoiVW5saW1pdGVkIn0seyJzdWJzY3JpYmVyVGVuYW50RG9tYWluIjoiY2FyYm9uLnN1cGVyIiwibmFtZSI6IlV0cGxQZXJzb25hcyIsImNvbnRleHQiOiJcL2FwaXBlcnNvbmFcLzMuMCIsInB1Ymxpc2hlciI6ImFkbWluIiwidmVyc2lvbiI6IjMuMCIsInN1YnNjcmlwdGlvblRpZXIiOiJVbmxpbWl0ZWQifSx7InN1YnNjcmliZXJUZW5hbnREb21haW4iOiJjYXJib24uc3VwZXIiLCJuYW1lIjoiVXRwbC1Qcm9kdWN0b3NBcGkiLCJjb250ZXh0IjoiXC9wcm9kdWN0b3NcLzIuMCIsInB1Ymxpc2hlciI6ImFkbWluIiwidmVyc2lvbiI6IjIuMCIsInN1YnNjcmlwdGlvblRpZXIiOiJVbmxpbWl0ZWQifSx7InN1YnNjcmliZXJUZW5hbnREb21haW4iOiJjYXJib24uc3VwZXIiLCJuYW1lIjoiVXRwbC1Qcm9kdWN0b3NBcGkiLCJjb250ZXh0IjoiXC9wcm9kdWN0b3NcLzMuMCIsInB1Ymxpc2hlciI6ImFkbWluIiwidmVyc2lvbiI6IjMuMCIsInN1YnNjcmlwdGlvblRpZXIiOiJVbmxpbWl0ZWQifSx7InN1YnNjcmliZXJUZW5hbnREb21haW4iOiJjYXJib24uc3VwZXIiLCJuYW1lIjoiVXRwbC1Qcm9kdWN0b3NBcGkiLCJjb250ZXh0IjoiXC9wcm9kdWN0b3NcLzQuMCIsInB1Ymxpc2hlciI6ImFkbWluIiwidmVyc2lvbiI6IjQuMCIsInN1YnNjcmlwdGlvblRpZXIiOiJVbmxpbWl0ZWQifV0sInRva2VuX3R5cGUiOiJhcGlLZXkiLCJpYXQiOjE2OTAyNDk5ODIsImp0aSI6IjA5ZGMwZmU2LTczNmMtNGM2Ny04Nzc4LTg0MTdjYjQ4MDhiZiJ9.LxD_DO5tOfV3b-kboQ-KAQANYyXLhqEaZJL03_Y8vzUjI9cD9-k1WKSycH9HQSHLYSaBfmgo4cLPYdRIKAc-0brl2yri_dA6FR_d-icQA_XK2I6ZyBI7dsPZE5PzATIcihzpU7m_4B39QOvEo_xB7IxFba-oOmwGFMCJyG_mRLj-VCApWdj6KLonaZOOCWSazraNIDgTWvZQo14npneTBDwMzCJTUoEzutoslgnYtgAexOgdlzyejFwgfrCerVzL51ED31OkfeBh7xFFG_4SxS4xZ6fcNkf1TQSkiU4ZHIjV5AKLp891GIYxv_xDDx6PARfLZ8Fxw8qtrCOhs1jPrA=='

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/personas')
def personas():
    headers = {'apikey': API_KEY}
    response = requests.get('https://utplwso2.tk/apipersona/3.0/personas', headers=headers)
    print(response)
    return render_template('personas.html', personas=response.json())

@app.route('/personas/delete/<idpersona>')
def delete_personas(idpersona):
    headers = {'apikey': API_KEY}
    response = requests.delete('https://utplwso2.tk/apipersona/3.0/personas/'+idpersona, headers=headers)
    print(response)
    return redirect(url_for('personas'))

@app.route('/personas', methods=['POST'])
def add():
    print("llego por aqui a guardar")
    nombre = request.form.get('nombre')
    identificacion = request.form.get('identificacion')
    edad = int(request.form.get('edad'))
    ciudad = request.form.get('ciudad')


    person_data = {"nombre": nombre, "edad": edad, "ciudad": ciudad, "identificacion": identificacion}

    headers = {'apikey': API_KEY}
    responseProductosS = requests.post('https://utplwso2.tk/apipersona/3.0/personas', json=person_data, headers=headers)

    return redirect(url_for('personas'))

@app.route('/productos')
def productos():
    headers = {'apikey': API_KEY}
    responseProductos = requests.get('https://utplwso2.tk/productos/4.0/producto', headers=headers)
    return render_template('productos.html', productosl=responseProductos.json())

@app.route('/productos', methods=['POST'])
def addProductos():
    print("llego por aqui a guardar productos")

    nombreValue = request.form.get('nombre')
    categoria = request.form.get('categoria')
    tipo = request.form.get('tipo')
    cod = request.form.get('cod')
    familia = request.form.get('familia')
    
    room_data = {
        "nombre": nombreValue,
        "categoria": categoria,
        "tipo": tipo,
        "cod": cod,
        "familia": familia
    }
    print(room_data)

    headers = {'apikey': API_KEY}
    responseProductosS = requests.post('https://utplwso2.tk/productos/4.0/producto', json=room_data, headers=headers)
    print(responseProductosS)
    return redirect(url_for('productos'))

if __name__ == '__main__':
    app.run(debug=True)