import web

urls = (
    '/', 'Index',
)

render = web.template.render('templates/')

class Index:
    def GET(self):
        
        return render.index("Mundo")

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
