from createTable import conn,context

context.execute("""
                CREATE OR REPLACE FUNCTION valida_tripulante_capitao()
                RETURNS TRIGGER AS $$
                BEGIN
                    IF TG_OP = 'INSERT' THEN
                        IF (SELECT COUNT(*) FROM tripulante WHERE funcao = 'Capitão') > 0 THEN
                            RAISE EXCEPTION 'Já existe um Capitão na tripulação!';
                        END IF;
                    ELSIF TG_OP = 'UPDATE' THEN
                        IF OLD.funcao <> NEW.funcao THEN
                            IF NEW.funcao = 'Capitão' AND (SELECT COUNT(*) FROM tripulante WHERE funcao = 'Capitão') > 1 THEN
                                RAISE EXCEPTION 'Apenas um Tripulante pode ter a função de Capitão!';
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
                BEFORE INSERT ON movimentacao_empregados
                FOR EACH ROW
                EXECUTE FUNCTION restringe_mov();
""")

conn.commit()
context.close()
conn.close()
