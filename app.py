from bottle import route, static_file, redirect, run, Bottle

app = application = Bottle()


class StripPathMiddleware(object):
    def __init__(self, a):
        self.a = a

    def __call__(self, e, h):
        e['PATH_INFO'] = e['PATH_INFO'].rstrip('/')
        return self.a(e, h)


@route("/")
def index():
    print('there1')
    # print(request.environ["REMOTE_ADDR"])
    # read_xml(request.environ["REMOTE_ADDR"])
    redirect('index.html')


@route("/index.html")
def index_r():
    return static_file('index.html', "./")


@route("/hw.html")
def hw():
    return static_file('hw.html', "./")


@route("/galery.html")
def gallery():
    return static_file('galery.html', "./")


@route("/contacts.html")
def contacts():
    return static_file('contacts.html', "./")


@route("/styles/<filename>")
def styles(filename):
    return static_file(filename, './styles/')


@route("/css/<filename>")
def css(filename):
    return static_file(filename, './css/')


@route('/favicon.ico')
def favicon():
    return static_file('favicon.ico', root='./')


@route("/images/<filename>")
def styles(filename):
    return static_file(filename, './images/', mimetype='image/jpg')


@route("/js/<filename>")
def get_script(filename):
    return static_file(filename, root='./js/')


@route("/hw/<filename:path>")
def hw_files(filename):
    print(filename)
    return static_file(filename, root="./hw")


if __name__ == "__main__":
    run(app=StripPathMiddleware(app))
else:
    import bottle
    app = application = bottle.default_app()    
        # host='0.0.0.0',
        # port=40000,
        # reloader=True)
    # run(debug=True, port=4000, reloader=True)
