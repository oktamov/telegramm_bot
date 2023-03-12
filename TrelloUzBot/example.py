# import psycopg2
# from psycopg2.extras import RealDictCursor
#
# from trello import TrelloManager
#
# connection = psycopg2.connect(
#     dbname='trello',
#     user='postgres',
#     password='developer006',
#     host='localhost',
#     port=5432
# )
#
#
# def show_board_name_id(username):
#     doska = []
#     cur = connection.cursor()
#     cur.execute(f"select board_name, trello_id from boards where trello_username='{username}'")
#     name = cur.fetchall()
#     for i in name:
#         doska.append({"name": i[0],
#                       "id": i[1]})
#     return doska
#
#
# def write_board(username):
#     boards = TrelloManager(username).get_boards()
#     cur = connection.cursor()
#
#     for board_index in range(len(boards)):
#         print(boards[board_index].get("id"))
#         # if boards[board_index].get("id") not in show_board_name_id(username)[board_index].values():
#         #     print("Sassas")
#         sql = "insert into boards(board_name, trello_id, trello_username) values (%s,%s,%s) on conflict (trello_id)do update set board_name = EXCLUDED.board_name"
#         values = (boards[board_index].get("name"), boards[board_index].get("id"), username)
#         cur.execute(sql, values)
#         connection.commit()
#     cur.close()
#
#
# def show_lists(board_id):
#     doska = []
#     cur = connection.cursor()
#     cur.execute(f"select list_name, trello_id from lists where board_id='{board_id}'")
#     name = cur.fetchall()
#     for i in name:
#         doska.append({"name": i[0],
#                       "id": i[1]})
#     print(doska)
#     return doska
#
#
# def write_lists(trello_username, board_id):
#     lists = TrelloManager(trello_username).get_lists_on_a_board(board_id)
#     cur = connection.cursor()
#     cur1 = connection.cursor()
#     for list_index in range(len(lists)):
#         sql = "insert into lists(list_name, trello_id, board_id) values (%s,%s, %s)"
#         values = (lists[list_index].get("name"), lists[list_index].get("id"), board_id)
#         cur.execute(sql, values)
#         connection.commit()
#     cur1.close()
#     cur.close()
#
#
# def write_cards(username, list_id):
#     cards = TrelloManager(username).get_cards_on_a_list(list_id)
#     cur = connection.cursor()
#     for card in cards:
#         print(card.get("idMembers"))
#         sql = "insert into cards(card_name, trello_id, url, cards_desc, list_id, members_id) values (%s, %s, %s, %s, %s,%s)"
#         values = (card.get("name"), card.get("id"), card.get("url"), card.get("desc"), list_id, card.get("idMembers"))
#         cur.execute(sql, values)
#         connection.commit()
#     cur.close()
#
#
# def show_cards(members_id):
#     cur = connection.cursor()
#     cur.execute(f"select card_name from cards where members_id like '%{members_id}%'")
#     msg = f"{cur.fetchall()[0][0]}\n"
#     return msg
#
#
# def write_labels(username, board_id):
#     labels = TrelloManager(username).get_label(board_id)
#     for label in labels:
#         print(label)
#
#
# show_cards('63ea226cab04b3d79fb6049e')
