from dbConnection import get_db_connection
from prettytable import PrettyTable

conn = get_db_connection()
context = conn.cursor()


def select_boats_and_crew():
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
        context.close()
        conn.close()