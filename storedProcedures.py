def employer_of_month(conn):
    conn.execute("""
        CREATE OR REPLACE PROCEDURE employer_of_month(
            date DATE
        )
        LANGUAGE PLPGSQL
        AS $$
        BEGIN
            SELECT id_emp, nome
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
                rankMov = 1;
        END;$$

    """)
    conn.commit()