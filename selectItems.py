from prettytable import PrettyTable


def select_boats_and_crew(context):
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
##---------------------------------------------------------------------------------------

        context.execute("""
            SELECT * AS dadosEmpregados
            FROM Empregados e
            WHERE e.id_emp IN (SELECT me.id_emp FROM Movimentacoes_Empregados me INNER JOIN Movimentacoes m ON m.id_mov=me.id_mov WHERE m.id_mov = 1 )
        """)
        result1 = context.fetchall()

        table1 = PrettyTable(['dadosEmpregados'])
        for row in result1:
            table.add_row(row)

        print(table1)

##---------------------------------------------------------------------------------------
        context.execute("""
                SELECT COUNT(m.id_emb) AS quantEmbarcacoes
                FROM Embarcacoes e INNER JOIN Movimentacao m
                ON m.id_emb = e.id_emb WHERE e.tipo = 'Cargueiro'
            """)
        result2 = context.fetchall()

        table2 = PrettyTable(['quantEmbarcacoes'])
        for row in result2:
            table.add_row(row)

        print(table2)

        context.close()