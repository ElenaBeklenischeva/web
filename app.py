from bottle import route, \
    static_file, redirect, \
    run, Bottle, error, request, \
    post, get, template, response
import io
from db_methods import *
import xml.etree.ElementTree as ET


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


conn_last_likes = sqlite3.connect('last_likes.db')
conn_last_likes.execute('CREATE TABLE if not exists last_likes'
                   '(ip text,'
                   'last_like int)')
conn_last_likes.commit()


conn_likes = sqlite3.connect('likes.db')
conn_likes.execute('CREATE TABLE if not exists likes'
                   '(id_img text,'
                   'count int)')
conn_likes.commit()


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
    text = "Всего посещений: " + str(get_all_visiting()) + \
           "\nСегодня: " + str(get_today_visiting()) +\
           "\nВаше последнее посещение:\n" + str(get_last_visit(ip))
    return template(
        'templates/index',
        text=text,
        browser=browser,
        messages=messages
    )


@app.route("/index.html")
def index_r():
    browser, ip, messages = get_info('chat_index', conn_chat_index)
    # print(messages)
    text = "Всего посещений: " + str(get_all_visiting()) + \
           "\nСегодня: " + str(get_today_visiting()) +\
           "\nВаше последнее посещение:\n" + str(get_last_visit(ip))
    return template(
        'templates/index',
        text=text,
        browser=browser,
        messages=messages
    )


@app.route("/hw.html")
def hw():
    browser, ip, messages = get_info('chat_hw', conn_chat_hw)
    text = "Всего посещений: " + str(get_all_visiting()) + \
           "\nСегодня: " + str(get_today_visiting()) +\
           "\nВаше последнее посещение:\n" + str(get_last_visit(ip))
    return template(
        'templates/hw',
        messages=messages,
        text=text,
        browser=browser
    )



@app.route("/galery.html")
def gallery():
    browser, ip, messages = get_info('chat_gallery', conn_chat_gal)
    text = "Всего посещений: " + str(get_all_visiting()) + \
           "\nСегодня: " + str(get_today_visiting()) +\
           "\nВаше последнее посещение:\n" + str(get_last_visit(ip))
    return template(
        'templates/gallery',
        text=text,
        browser=browser,
        messages=messages
    )


@app.route("/contacts.html")
def contacts():
    browser, ip, messages = get_info('chat_contacts', conn_chat_con)
    text = "Всего посещений: " + str(get_all_visiting()) + \
           "\nСегодня: " + str(get_today_visiting()) +\
           "\nВаше последнее посещение:\n" + str(get_last_visit(ip))
    return template(
        'templates/contacts',
        text=text,
        browser=browser,
        messages=messages
    )


@app.route("/styles/<filename>")
def styles(filename):
    return static_file(filename, './styles/')


@app.route("/css/<filename>")
def css(filename):
    return static_file(filename, './css/')


@app.route("/images/<filename>")
def styles(filename):
    return static_file(filename, './images/', mimetype='image/jpg')


@app.route('/favicon.ico')
def favicon():
    return static_file('f1.ico', root='./images')


@app.route("/js/<filename>")
def get_script(filename):
    return static_file(filename, root='./js/')


@app.route("/hw/<filename:path>")
def hw_files(filename):
    return static_file(filename, root="./hw")


@app.error(404)
def error404(err):
    return static_file("index.html", './')


@app.post('/index.html')
@app.post('/')
def get_comment_ind_n():
    # print('It"s post index')
    add_new_message("chat_index", conn_chat_index)
    messages = get_messages("chat_index", conn_chat_index)
    return get_chat_template('templates/comments', messages, True)


@app.post('/hw.html')
def get_comment_hw():
    # print('It"s post hw')
    add_new_message("chat_hw", conn_chat_hw)
    messages = get_messages('chat_hw', conn_chat_hw)
    return get_chat_template('templates/comments', messages, True)


@app.post('/contacts.html')
def get_comment_cont():
    # print('It"s post contacts')
    add_new_message("chat_contacts", conn_chat_con)
    messages = get_messages("chat_contacts", conn_chat_con)
    return get_chat_template('templates/comments', messages, True)


@app.post('/galery.html')
def get_comment_cont():
    # print('It"s post galery')
    add_new_message("chat_gallery", conn_chat_gal)
    messages = get_messages("chat_gallery", conn_chat_gal)
    return get_chat_template('templates/comments', messages, True)


@app.post('/galery.html/counter')
def getLikeCount():
    # print('correct path')
    ip = bottle.request.environ["REMOTE_ADDR"]
    id_img = request.body.getvalue().decode()
    last_like = conn_last_likes.execute("select last_like from last_likes where ip='" + ip + "'").fetchone()
    if not last_like or time.time() - int(last_like[0]) > 5:
        if not last_like:
            conn_last_likes.execute("insert into last_likes (ip, last_like) VALUES(?, ?)", (ip, time.time()))
        else:
            conn_last_likes.execute("update last_likes set last_like=" + str(time.time()) + " where ip='" + ip + "'")
        conn_last_likes.commit()
        count_likes = conn_likes.execute("select count from likes where id_img='" + id_img + "'").fetchall()
        if count_likes:
            conn_likes.execute('update likes set count=' + str(int(count_likes[0][0]) + 1) + " where id_img='" + id_img + "'")
            count_likes = count_likes[0][0] + 1
        else:
            conn_likes.execute('insert into likes (id_img, count) VALUES(?, ?)', (id_img, 1))
            count_likes = 1
        conn_likes.commit()
        return {'new_count': count_likes}


@app.post('/galery.html/start')
@app.post('/galery.html#/start')
def getStartCounts():
    id_img = 'img' + request.body.getvalue().decode().split('=')[1]
    # print('start')
    # print(id_img)
    count_likes = conn_likes.execute("select count from likes where id_img='" + id_img + "'").fetchall()
    if count_likes:
        return {'new_count': count_likes[0][0]}
    else:
        return {'new_count': 0}


@app.route('/galery.html/file')
def create_likes_xml():
    # print('likes xml')
    with open('likes.xml', 'w') as f:
        f.write('<root>')
        f.write('</root>')
    data = ET.parse('likes.xml')
    root = data.getroot()
    images = conn_likes.execute("select * from likes").fetchall()
    for image in images:
        child = ET.Element('img')
        root.append(child)
        child.attrib['name'] = image[0]
        child.attrib['count'] = str(image[1])
    data.write('likes.xml')
    # print('ok')
    return static_file('likes.xml', './')


if __name__ == "__main__":
    run(app=StripPathMiddleware(app),
        host='0.0.0.0',
        port=40000,
        debug=True, reloader=True)


