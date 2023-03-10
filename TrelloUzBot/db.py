import psycopg2
from psycopg2.extras import RealDictCursor
from environs import Env

from trello import TrelloManager

env = Env()
env.read_env()

dbname = env("DBNAME")
user = env("USER")
password = env("PASSWORD")
host = env("HOST")
port = env("PORT")
connection = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port
)


def show_board_name_id(username):
    doska = []
    cur = connection.cursor()
    cur.execute(f"select board_name, trello_id from boards where trello_username='{username}'")
    name = cur.fetchall()
    for i in name:
        doska.append({"name": i[0],
                      "id": i[1]})
    return doska


def write_board(username):
    boards = TrelloManager(username).get_boards()
    cur = connection.cursor()

    for board_index in range(len(boards)):
        print(boards[board_index].get("id"))
        # if boards[board_index].get("id") not in show_board_name_id(username)[board_index].values():
        #     print("Sassas")
        # cur.execute(f"delete from boards where trello_id <> '{(boards[board_index].get('id'))}'")
        sql = "insert into boards(board_name, trello_id, trello_username) values (%s,%s,%s) on conflict (trello_id)do update set board_name = EXCLUDED.board_name"
        values = (boards[board_index].get("name"), boards[board_index].get("id"), username)
        cur.execute(sql, values)
        connection.commit()
    cur.close()


def show_lists(board_id):
    doska = []
    cur = connection.cursor()
    cur.execute(f"select list_name, trello_id from lists where board_id='{board_id}'")
    name = cur.fetchall()
    for i in name:
        doska.append({"name": i[0],
                      "id": i[1]})
    print(doska)
    return doska


def write_lists(trello_username, board_id):
    lists = TrelloManager(trello_username).get_lists_on_a_board(board_id)
    cur = connection.cursor()
    cur1 = connection.cursor()
    for list_index in range(len(lists)):
        sql = "insert into lists(list_name, trello_id, board_id) values (%s,%s, %s) on conflict (trello_id) do update set list_name = EXCLUDED.list_name"
        values = (lists[list_index].get("name"), lists[list_index].get("id"), board_id)
        cur.execute(sql, values)
        connection.commit()
    cur1.close()
    cur.close()


def write_cards(username, list_id):
    msg = ""
    curr = connection.cursor()
    for i in card_data:
        if member_id in i.get("idMembers"):
            sql = 'insert into cards(cards_name,cards_id,des,url,list_id,cards_coid) values (%s,%s,%s,%s,%s,%s) ' \
                  'on conflict (cards_id) do update set cards_name = EXCLUDED.cards_name'
            curr.execute(f"select id from lists  where trello"
                         f"_id='{list_id}'")
            name = curr.fetchall()
            curr.execute(sql,
                         (i.get('name'), i.get('id'), i.get('desc'), i.get('url'), list_id, name[0][0]))
            connection.commit()
            with connection.cursor() as cars:
                cars.execute(f"select cards_name from cards where cards_id='{i['id']}'and list_id='{list_id}'")
                name = cars.fetchall()
                for j in name:
                    for g in j:
                        msg += f"{i.get('idShort')} - {g}\n"
    curr.close()
    return msg


def members_label(username, board_id):
    members = TrelloManager(username).get_board_members(board_id)
    data = []
    for i in members:
        curr = connection.cursor()
        sql = 'insert into members(full_name,trello_username,trello_id)values (%s,%s,%s)' \
              'on conflict (trello_id) do update set full_name = excluded.full_name'
        curr.execute(sql, (i.get('fullName'), i.get('username'), i.get('id')))
        connection.commit()
        with connection.cursor() as m:
            m.execute(f"select full_name,trello_id from members where trello_username ='{i['username']}'")
            s = m.fetchall()
            for row in s:
                data.append({
                    'fullName': row[0],
                    'id': row[1]
                })
    con = connection.cursor()
    sql = 'insert into members_one(cards_id)values (%s) on conflict (cards_id)do nothing '
    con.execute('select id from cards')
    name = con.fetchall()
    for j in name:
        con.execute(sql, (j))
        connection.commit()
    sql = 'insert into members_one(memberes_id)values (%s) on conflict (memberes_id)do update set memberes_id=excluded.memberes_id'
    con.execute('select id from members')
    name = con.fetchall()
    for i in name:
        con.execute(sql, (i))
        connection.commit()
    con.close()
    return data
