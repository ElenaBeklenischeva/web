from bottle import route, \
    static_file, redirect, \
    run, Bottle, error, request, \
    post, get, template, response
from db_methods import *


app = application = Bottle()

conn = sqlite3.connect('users.db')
c = conn.cursor()

conn.execute('CREATE TABLE if not exists users'
             '(ip text, '
             'visited_count int,'
             'visited_count_today int,'
             'last_visit_date text,'
             'last_visit_time text)')
conn.commit()


conn_chat_index = create_table("chat_index")
conn_chat_hw = create_table("chat_hw")
conn_chat_gal = create_table("chat_gallery")
conn_chat_con = create_table("chat_contacts")


class StripPathMiddleware(object):
    def __init__(self, a):
        self.a = a

    def __call__(self, e, h):
        e['PATH_INFO'] = e['PATH_INFO'].rstrip('/')
        return self.a(e, h)


def update_ip(ip):
    return update_ip_cur(ip, conn, c)


def get_all_visiting():
    return get_all_visiting_curr(conn)


def get_today_visiting():
    return get_today_visiting_curr(conn)


def get_last_visit(ip):
    return get_last_visit_curr(ip, conn)


def get_info(db, conn_db):
    return get_info_curr(db, conn_db, conn, c)


@app.route("/")
def index():
    browser, ip, messages = get_info('chat_index', conn_chat_index)
    print(ip)
    return template(
        'templates/index',
        all=get_all_visiting(),
        today=get_today_visiting(),
        last_visit=get_last_visit(ip),
        browser=browser,
        messages=messages
    )


@app.route("/index.html")
def index_r():
    browser, ip, messages = get_info('chat_index', conn_chat_index)
    return template(
        'templates/index',
        all=get_all_visiting(),
        today=get_today_visiting(),
        last_visit=get_last_visit(ip),
        browser=browser,
        messages=messages
    )


@app.route("/hw.html")
def hw():
    browser, ip, messages = get_info('chat_hw', conn_chat_hw)
    return template(
        'templates/hw',
        messages=messages,
        all=get_all_visiting(),
        today=get_today_visiting(),
        last_visit=get_last_visit(ip),
        browser=browser
    )


@app.route("/galery.html")
def gallery():
    browser, ip, messages = get_info('chat_gallery', conn_chat_gal)
    return template(
        'templates/gallery',
        all=get_all_visiting(),
        today=get_today_visiting(),
        last_visit=get_last_visit(ip),
        browser=browser,
        messages=messages
    )


@app.route("/contacts.html")
def contacts():
    browser, ip, messages = get_info('chat_contacts', conn_chat_con)
    return template(
        'templates/contacts',
        all=get_all_visiting(),
        today=get_today_visiting(),
        last_visit=get_last_visit(ip),
        browser=browser,
        messages=messages
    )


@app.route("/styles/<filename>")
def styles(filename):
    return static_file(filename, './styles/')


@app.route("/css/<filename>")
def css(filename):
    return static_file(filename, './css/')


@app.route('/favicon.ico')
def favicon():
    return static_file('favicon.ico', root='./')


@app.route("/images/<filename>")
def styles(filename):
    return static_file(filename, './images/', mimetype='image/jpg')


@app.route("/js/<filename>")
def get_script(filename):
    print(filename)
    return static_file(filename, root='./js/')


@app.route("/hw/<filename:path>")
def hw_files(filename):
    print(filename)
    return static_file(filename, root="./hw")


@app.error(404)
def error404(err):
    print('error')
    return static_file("index.html", './')


@app.post('/')
def get_comment_ind():
    print('It"s post index')
    add_new_message("chat_index", conn_chat_index)
    redirect("/")


@app.post('/')
def get_comment_ind_n():
    print('It"s post index')
    add_new_message("chat_index", conn_chat_index)
    redirect("/index.html")


@app.post('/hw.html')
def get_comment_hw():
    print('It"s post hw')
    add_new_message("chat_hw", conn_chat_hw)
    redirect("/hw.html")


@app.post('/galery.html')
def get_comment_gal():
    print('It"s post gallery')
    add_new_message("chat_gallery", conn_chat_gal)
    redirect("/galery.html")


@app.post('/contacts.html')
def get_comment_cont():
    print('It"s post contacts')
    add_new_message("chat_contacts", conn_chat_con)
    redirect("/contacts.html")


if __name__ == "__main__":
    print('main')
    run(app=StripPathMiddleware(app),
        host='0.0.0.0',
        port=40000,
        debug=True, reloader=True)

