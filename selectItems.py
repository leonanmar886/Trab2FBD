from prettytable import PrettyTable
from dbConnection import connect, disconnect

def select_boats_and_crew():
    conn, context = connect()
    """
Utilizamos a cláusula LEFT JOIN para incluir todas as embarcações, mesmo aquelas que não têm tripulantes.
"""
    context.execute("""
        SELECT e.nome as nomeEmbarcacao, COUNT(T.id_trp) as qtdTripulantes
        FROM Embarcacoes e
        LEFT JOIN Tripulantes T ON e.id_emb = T.id_emb
        GROUP BY e.nome
    """)
    result = context.fetchall()

    table = PrettyTable(['nomeEmbarcacao', 'qtdTripulantes'])
    for row in result:
        table.add_row(row)

    print(table)
    
    disconnect(conn, context)

def select_employes():
    conn, context = connect()

    context.execute("""
        SELECT * FROM Empregados e
        WHERE e.id_emp IN (SELECT me.id_emp FROM Movimentacoes_Empregados me INNER JOIN Movimentacoes m ON m.id_mov=me.id_mov WHERE m.id_mov = 1 )
    """)
    result1 = context.fetchall()

    table = PrettyTable(['id_emp', 'nome', 'data_nasc', 'funcao'])
    for row in result1:
        table.add_row(row)

    print(table)

    disconnect(conn, context)

def select_boats():
    conn, context = connect()

    context.execute("""
            SELECT COUNT(m.id_emb) AS qtdEmbarcacoes
            FROM Embarcacoes e 
            INNER JOIN Movimentacoes m
            ON m.id_emb = e.id_emb WHERE e.tipo = 'Cargueiro'
        """)
    result2 = context.fetchall()

    table = PrettyTable(['qtdEmbarcacoes'])
    for row in result2:
        table.add_row(row)

    print(table)

    disconnect(conn, context)