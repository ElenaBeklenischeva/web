import base64
from io import BytesIO
import sqlite3
import datetime
import time
import bottle
from PIL import Image, ImageDraw, ImageFont
import httpagentparser


def create_table(db):
    connect = sqlite3.connect(db + ".db")

    connect.execute('CREATE TABLE if not exists ' + db + '('
                                                         'id integer primary key autoincrement,'
                                                         'ip text,'
                                                         'date integer,'
                                                         'data text not null'
                                                         ')')
    connect.commit()
    return connect


def add_message(ip, text, db, conn_db):
    text.replace("'", "\'")

    conn_db.execute("INSERT INTO " + db + "(ip, date, data) VALUES(?, ?, ?)", (str(ip), str(time.time()), text))
    conn_db.commit()


def get_messages(db, conn_db):
    request = "select ip, data from " + db + " order by id desc"
    return conn_db.execute(request).fetchall()


def update_ip_cur(ip, conn, c):
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
                cur_count_1 = 1
            else:
                cur_count_1 = (conn.execute("select visited_count_today from users where ip='" + ip + "'")).fetchone()[
                                  0] + 1
            cur_count = int(cur_count[0]) + 1

            c.execute("update users set visited_count='" + str(cur_count) + "' where ip='" + ip + "'")
            c.execute("update users set last_visit_date='" + str(datetime.date.today()) + "' where ip='" + ip + "'")
            c.execute("update users set last_visit_time='" + str(time.time()) + "' where ip='" + ip + "'")
            c.execute("update users set visited_count_today='" + str(cur_count_1) + "' where ip='" + ip + "'")
            conn.commit()
        # else:
        #     print("It's F5")


def get_all_visiting_curr(conn):
    res = conn.execute("select sum(visited_count) from users").fetchone()
    if res:
        return res[0]
    else:
        return


def get_today_visiting_curr(conn):
    cur_day = datetime.date.today()
    res = (
        conn.execute(
            "select sum(visited_count_today) from users where last_visit_date='" + str(cur_day) + "'")).fetchone()
    if res:
        return res[0]
    else:
        return


def get_last_visit_curr(ip, conn):
    res = conn.execute("select last_visit_date from users where ip='" + str(ip) + "'").fetchone()
    if res:
        return res[0]
    else:
        return


def get_info_curr(db, conn_db, conn, c):
    agent = bottle.request.environ.get('HTTP_USER_AGENT')
    if agent:
        browser = httpagentparser.detect(agent)
        browser = browser['browser']['name'] + ' version:'+browser['browser']['version']
    else:
        browser = None
    ip = bottle.request.environ["REMOTE_ADDR"]
    update_ip_cur(ip, conn, c)
    messages_r = get_messages(db, conn_db)
    return browser, ip, messages_r


def add_new_message(db, conn_db):
    data = bottle.request.forms.get('answer_form')
    ip = bottle.request.environ["REMOTE_ADDR"]
    print('data: ' + str(data))
    if data:
        add_message(ip, data.strip(), db, conn_db)


def get_chat_template(address, messages, is_ajax, template_name=None, template_text=None, browser=None):
    if is_ajax:
        # response.content_type = 'application/json'
        bottle.response.content_type = 'text/html; charset=utf-8'
        return bottle.template(address
                               , messages=messages
                               , addr='#')
    else:
        return bottle.template(template_name,
                        text=template_text,
                        browser=browser,
                        messages=messages)


def generate_img(new_text):
    width = 250
    height = 80
    img = Image.new('RGB', (width, height), color=(152, 152, 152))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('arialbd.ttf', 12)
    draw.text((25, 5), new_text, (255, 255, 255), font=font)

    buffer = BytesIO()
    img.save(buffer, format="JPEG")
    image_result = 'data:image/jpeg;base64,' + str(base64.b64encode(buffer.getvalue()))[2:-1]
    return image_result
