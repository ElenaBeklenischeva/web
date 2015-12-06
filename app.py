from bottle import route, \
    static_file, redirect, \
    run, Bottle, error, request, \
    post, get, template, response
import sqlite3
import datetime
import time


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

conn_chat = sqlite3.connect('chat.db')

conn_chat.execute('CREATE TABLE if not exists chat'
                  '('
                  'id integer primary key autoincrement,'
                  'ip text,'
                  'date integer,'
                  'data text not null'
                  ')')
conn_chat.commit()


class StripPathMiddleware(object):
    def __init__(self, a):
        self.a = a

    def __call__(self, e, h):
        e['PATH_INFO'] = e['PATH_INFO'].rstrip('/')
        return self.a(e, h)


def add_message(ip, text):
    text.replace("'", "\'")
    conn_chat.execute("INSERT INTO chat(ip, date, data) VALUES(?, ?, ?)", (str(ip), str(time.time()), text))
    conn_chat.commit()


def get_messages():
    return conn_chat.execute("select ip, data from chat order by id desc").fetchall()


def update_ip(ip):
    cur_count = (conn.execute("select users.visited_count from users where ip='" + ip + "'")).fetchone()
    if cur_count is None:
        c.execute(
            "INSERT INTO users VALUES (?,?,?,?,?)", (str(ip), str(1), str(1), str(
                datetime.date.today()), str(time.time())))
        conn.commit()
    else:
        cur_time = (conn.execute("select users.last_visit_time from users where ip='" + ip + "'")).fetchone()[0]
        cur_date = (conn.execute("select users.last_visit_date from users where ip='" + ip + "'")).fetchone()[0]
        if abs(time.time() - float(cur_time)) > 3600 or cur_date != str(datetime.date.today()):
            if cur_date != str(datetime.datetime.today()):
                c.execute("update users set visited_count_today='" + '1' + "' where ip='" + ip + "'")
            cur_count = int(cur_count[0]) + 1
            cur_count_1 = (conn.execute("select visited_count_today from users where ip='" + ip + "'")).fetchone()[0] + 1

            c.execute("update users set visited_count_today='" + str(cur_count_1) + "' where ip='" + ip + "'")
            c.execute("update users set visited_count='" + str(cur_count) + "' where ip='" + ip + "'")
            c.execute("update users set visited_count_today='" + str(cur_count) + "' where ip='" + ip + "'")
            c.execute("update users set last_visit_date='" + str(datetime.date.today()) + "' where ip='" + ip + "'")
            c.execute("update users set last_visit_time='" + str(time.time()) + "' where ip='" + ip + "'")
            conn.commit()
        else:
            print("It's F5")


def get_all_visiting():
    res = conn.execute("select sum(visited_count) from users").fetchone()
    if res:
        return res[0]
    else:
        return


def get_today_visiting():
    cur_day = datetime.date.today()
    res = (conn.execute("select sum(visited_count_today) from users where last_visit_date='" + str(cur_day) + "'")).fetchone()
    if res:
        return res[0]
    else:
        return


def get_last_visit(ip):
    res = conn.execute("select last_visit_date from users where ip='" + str(ip) + "'").fetchone()
    if res:
        return res[0]
    else:
        return


@app.route("/")
def index():
    browser = request.environ.get('HTTP_USER_AGENT')
    ip = request.environ["REMOTE_ADDR"]
    update_ip(ip)
    print(ip)
    return template(
        'templates/index',
        all=get_all_visiting(),
        today=get_today_visiting(),
        last_visit=get_last_visit(ip),
        browser=browser
    )


@app.route("/index.html")
def index_r():
    ip = request.environ["REMOTE_ADDR"]
    update_ip(ip)
    cookie = ''
    if request.get_cookie('resolution'):
        cookie = request.get_cookie('resolution')
    return template(
        'templates/index',
        all=get_all_visiting(),
        today=get_today_visiting(),
        last_visit=get_last_visit(ip),
        resolution=cookie
    )


@app.route("/hw.html")
def hw():
    ip = request.environ["REMOTE_ADDR"]
    update_ip(ip)
    messages_r = get_messages()
    return template(
        'templates/comments',
        messages=messages_r,
        all=get_all_visiting(),
        today=get_today_visiting(),
        last_visit=get_last_visit(ip)
    )


@app.route("/galery.html")
def gallery():
    ip = request.environ["REMOTE_ADDR"]
    update_ip(ip)
    return static_file('galery.html', './')
    # return template(
    #     'templates/gallery',
    #     all=get_all_visiting(),
    #     today=get_today_visiting(),
    #     last_visit=get_last_visit(ip)
    # )


@app.route("/contacts.html")
def contacts():
    ip = request.environ["REMOTE_ADDR"]
    update_ip(ip)
    return template(
        'templates/contacts',
        all=get_all_visiting(),
        today=get_today_visiting(),
        last_visit=get_last_visit(ip)
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


@app.post('/hw.html')
def get_comment():
    print('It"s post')
    data = request.forms.get('answer_form')
    print(data)
    ip = request.environ["REMOTE_ADDR"]
    if data.strip():
        add_message(ip, data)
    redirect("/hw.html")


if __name__ == "__main__":
    print('main')
    run(
        app=StripPathMiddleware(app),
        host='0.0.0.0',
        port=40000)
        # reloader=True)
    # conn.close()
else:
    import bottle

    app = application = bottle.default_app()
    run(host='0.0.0.0', port=40000, reloader=True)

