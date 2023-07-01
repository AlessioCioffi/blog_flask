from myblog import app

# Codigo de python para correr la app
if __name__=='__main__':
    '''
       El puerto no es necesario;
       en alternativa puede encontrarese en el .env '''
    app.run(port=8000)