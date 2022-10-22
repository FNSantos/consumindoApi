from flask import Flask, jsonify
import mysql.connector
from flask_cors import CORS, cross_origin

app = Flask(__name__)

@app.route('/v1/cadastrar',methods=["POST"])
def cadastrar():
    cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='medvet')
    cursor = cnx.cursor()
    query = ("INSERT INTO tbl_medico nome ")
    cursor.execute(query)

    return 'Cadastrado com sucesso' , 200

@app.route('/v1/consultar',methods=["GET"])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def consultar():
    cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='medvet')
    cursor = cnx.cursor()
    query = ("SELECT * FROM tbl_medico")
    cursor.execute(query)
    myresult = cursor.fetchall()

    # for x in myresult:
    #     print(x)
    # for (cpf) in cursor:
    #     # print(cpf)
    #     return cpf

    return jsonify(myresult), 200

    # return "Hello, World!"
    
    # cnx.close()

app.run(debug=True)