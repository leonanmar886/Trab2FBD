from dbConnection import connect, disconnect

def create_capitan_trigger():
    conn, context = connect()

    context.execute("""
                    CREATE OR REPLACE FUNCTION valida_tripulante_capitao()
                    RETURNS TRIGGER AS $$
                    BEGIN
                        IF TG_OP = 'INSERT' THEN
                            IF (SELECT COUNT(*) FROM tripulantes WHERE funcao = 'Capitão' AND id_emb = NEW.id_emb) > 0 THEN
                                RAISE EXCEPTION 'Já existe um Capitão na tripulação desta embarcação!';
                            END IF;
                        ELSIF TG_OP = 'UPDATE' THEN
                            IF OLD.funcao <> NEW.funcao THEN
                                IF NEW.funcao = 'Capitão' AND (SELECT COUNT(*) FROM tripulante WHERE funcao = 'Capitão' AND id_emb = NEW.id_emb) > 1 THEN
                                    RAISE EXCEPTION 'Apenas um Tripulante por embarcação pode ter a função de Capitão!';
                                END IF;
                            END IF;
                        END IF;

                        RETURN NEW;
                    END;
                    $$ LANGUAGE plpgsql;

                    CREATE TRIGGER trigger_valida_tripulante_capitao
                    BEFORE INSERT OR UPDATE ON tripulante
                    FOR EACH ROW
                    EXECUTE FUNCTION valida_tripulante_capitao();""")
    conn.commit()

    disconnect(conn, context)

def create_move_trigger():
    conn, context = connect()

    context.execute("""
                    CREATE OR REPLACE FUNCTION restringe_mov()
                    RETURNS TRIGGER AS $$
                    DECLARE
                        funcao_empregado TEXT;
                        tipo_movimentacao TEXT;
                    BEGIN
                        SELECT e.funcao INTO funcao_empregado
                        FROM Empregados e 
                        WHERE e.id_emp = NEW.id_emp;

                        SELECT mov.tipo INTO tipo_movimentacao
                        FROM Movimentacao mov
                        WHERE mov.id_mov = NEW.id_mov;

                        IF tipo_movimentacao = 'Manutenção' AND funcao_empregado != 'Manutenção' THEN
                        RAISE EXCEPTION 'Somente empregados da manutenção podem ser escolhidos para executar movimentações desse tipo';
                        END IF;
                        RETURN NEW;
                    END;
                    $$ LANGUAGE plpgsql;

                    CREATE TRIGGER restringe_mov_empregados
                    BEFORE INSERT ON movimentacoes_empregados
                    FOR EACH ROW
                    EXECUTE FUNCTION restringe_mov();
    """)

    conn.commit()
    disconnect(conn, context)

def test_move_trigger():
    conn, context = connect()

    context.execute("""
        INSERT INTO Movimentacoes_Empregados VALUES(%s,%s);
        INSERT INTO Movimentacoes_Empregados VALUES(%s,%s);
    """, (5,5,5,2))

    conn.commit()
    disconnect(conn, context)

def test_capitan_trigger():
    conn, context = connect()

    context.execute("""
            INSERT INTO Tripulantes VALUES(%s,%s,%s,%s,%s);
            INSERT INTO Tripulantes VALUES(%s,%s,%s,%s,%s);
                        
            UPDATE Tripulantes SET funcao = %s WHERE id_trp = %s;
        """,
            (7,'Tripulante7','1980-09-04','Capitão',4,
            8,'Tripulante8','1985-03-03','Capitão',2,
            'Capitão', 3))

    conn.commit()
    disconnect(conn, context)