from prettytable import PrettyTable
from dbConnection import connect, disconnect

def insert_move():
    conn, context = connect()

    context.execute("INSERT INTO Movimentacoes VALUES(%s,%s,%s,%s)",(6,'2023-10-05','Manutenção', 1))
    conn.commit()

    disconnect(conn, context)

def insert_move_employe():
    conn, context = connect()

    context.execute("INSERT INTO Movimentacoes_Empregados VALUES(%s,%s)",(6,1))
    conn.commit()

    disconnect(conn, context)

def select_qtd_moves():
    conn, context = connect()

    context.execute("""
        SELECT COUNT(m.id_emb) AS qtdMovimentacoes
        FROM Embarcacoes e
        INNER JOIN Movimentacoes m ON m.id_emb = e.id_emb
        WHERE e.tipo = 'Cargueiro'
    """)

    result = context.fetchall()
    table = PrettyTable(['qtdMovimentacoes'])
    for row in result:
        table.add_row(row)
    
    print(table)

    disconnect(conn, context)