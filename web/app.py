import web
import requests


API_URL = "https://api-rest-ca5g.onrender.com/personas/"  

# Rutas 
urls = (
    '/', 'Index'
)


class Index:
    def GET(self):
        
        response = requests.get(API_URL)
    
        if response.status_code == 200:
            data = response.json()  
            print("RESPUESTA:",data)
            
        else:
            data = [] 

        return render.index(data)

render = web.template.render('templates/')

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
