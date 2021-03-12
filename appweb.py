from flask import Flask, render_template

import pandas as pd

app = Flask(__name__) #instancia para correr el flask

datos = pd.read_csv('CSV/Saber_11_2012_instituciones.csv',sep=';')

@app.route('/')
def index():
    return render_template('hom.html')
#endHola





@app.route('/Punto1/')
def punto1():

    proing=datos.loc[(datos['PROMEDIOINGLES'].str.replace(',','.').astype(float)>=75)&(datos['PROMEDIOINGLES'].str.replace(',','.').astype(float)<=99)]
    return render_template('Punto1.html', tables=[proing.to_html(classes='data')], titles=proing.columns.values)


@app.route('/Punto2/')
def punto2():
    prol=datos.loc[(datos['EVALUADOS']>200)&(datos['PROMEDIOLENGUAJE'].str.replace(',','.').astype(float)>55)]
    return render_template('Punto2.html', tables=[prol.to_html(classes='data')], titles=prol.columns.values)


@app.route('/Punto3/')
def punto3():
    
    df=datos[datos.PROMEDIOMATEMATICA==datos.PROMEDIOMATEMATICA.min()]
    return render_template('Punto3.html', tables=[df.to_html(classes='data')], titles=df.columns.values)


@app.route('/Punto4/')
def punto4():
    df=datos.loc[(datos['PROMEDIOMATEMATICA'].str.replace(',','.').astype(float)>datos['PROMEDIOMATEMATICA'].str.replace(',','.').astype(float).mean())]
    df=df.head(10)
    return render_template('Punto4.html', tables=[df.to_html(classes='data')], titles=df.columns.values)


@app.route('/Punto5/')
def punto5():
    df=len(datos.loc[(datos['NOMBREMUNICIPIO']=='BARRANQUILLA') & (datos['PROMEDIOINGLES'].str.replace(',','.').astype(float)>70)])
    return render_template('Punto5.html', instituciones=df)

@app.route('/Punto6/')
def punto6():
    df=len(datos.loc[(datos['NATURALEZA']=='OFICIAL') & datos.loc[(datos[''])])
    return render_template('Punto5.html', instituciones=df)