import web

urls = (
    '/', 'Index',
)

render = web.template.render('templates/')

class Index:
    def GET(self):
        return "Hola Mundo desde web.py"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
