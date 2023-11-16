from prettytable import PrettyTable
from dbConnection import connect, disconnect

def employer_of_month():
    conn, context = connect()

    context.execute("""
        CREATE OR REPLACE FUNCTION employer_of_month(
            date DATE
        ) RETURNS TABLE (id_emp INT, nome VARCHAR(255))
        AS $$
        BEGIN
            RETURN QUERY
            SELECT sub.id_emp, sub.nome
            FROM
                (
                    SELECT
                    me.id_emp,
                    e.nome,
                    COUNT(me.id_mov) AS countMov,
                    RANK() OVER (ORDER BY COUNT(me.id_mov) DESC) AS rankMov
                FROM
                    movimentacoes_empregados me
                    INNER JOIN empregados e ON e.id_emp = me.id_emp
                    INNER JOIN movimentacoes mo ON mo.id_mov = me.id_mov
                WHERE mo.data BETWEEN
                    TO_DATE(
                    CONCAT(EXTRACT(YEAR FROM date),
                        '-',
                        EXTRACT(MONTH FROM date),
                        '-',
                        '1'),
                    'YYYY-MM-DD'
                    )
                    AND 
                    TO_DATE(
                    CONCAT(EXTRACT(YEAR FROM date),
                        '-',
                        EXTRACT(MONTH FROM date),
                        '-',
                        '30'),
                    'YYYY-MM-DD'
                    )
                
                GROUP BY me.id_emp, e.nome
                ) AS sub
            WHERE
                sub.rankMov = 1;
        END;$$ LANGUAGE plpgsql;

    """)
    conn.commit()

    disconnect(conn, context)

def execute_employer_of_month(date):
    conn, context = connect()

    context.execute("SELECT * FROM employer_of_month(%s)", (date,))
    result = context.fetchone()

    table = PrettyTable(['id_emp', 'nome'])
    table.add_row(result)
    print(table)

    disconnect(conn, context)