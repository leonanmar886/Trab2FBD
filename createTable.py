from dbConnection import get_db_connection


def create_all_tables():
    conn = get_db_connection()

    with conn.cursor() as context:
        context.execute("""
                        DROP TABLE IF EXISTS Embarcacoes CASCADE;
                        CREATE TABLE Embarcacoes (
                            id_emb SERIAL PRIMARY KEY,
                            nome VARCHAR(255) NOT NULL,
                            tipo VARCHAR(255) NOT NULL
                        );

                        DROP TABLE IF EXISTS Tripulantes CASCADE;
                        CREATE TABLE Tripulantes (
                            id_trp SERIAL PRIMARY KEY,
                            nome VARCHAR(255) NOT NULL,
                            data_nasc DATE NOT NULL,
                            funcao VARCHAR(255) NOT NULL,
                            id_emb INTEGER REFERENCES Embarcacoes
                        );

                        DROP TABLE IF EXISTS Empregados CASCADE;
                        CREATE TABLE Empregados (
                            id_emp SERIAL PRIMARY KEY,
                            nome VARCHAR(255) NOT NULL,
                            data_nasc DATE NOT NULL,
                            funcao VARCHAR(255) NOT NULL
                        );

                        DROP TABLE IF EXISTS Movimentacoes CASCADE;
                        CREATE TABLE Movimentacoes (
                            id_mov SERIAL PRIMARY KEY,
                            data DATE NOT NULL,
                            tipo VARCHAR(255) NOT NULL,
                            id_emb INTEGER REFERENCES Embarcacoes
                        );

                        DROP TABLE IF EXISTS Movimentacoes_Empregados CASCADE;
                        CREATE TABLE Movimentacoes_Empregados (
                            id_mov INTEGER REFERENCES Movimentacoes ON DELETE CASCADE,
                            id_emp INTEGER REFERENCES Empregados ON DELETE CASCADE,
                            PRIMARY KEY(id_mov, id_emp)
                        );

                        """)
        conn.commit()
        context.close()
        conn.close()