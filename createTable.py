from dbConnection import connect, disconnect

def createTable():
    conn, context = connect()
    context.execute("""
                    DROP TABLE IF EXISTS Embarcacoes CASCADE;
                    CREATE TABLE Embarcacoes (
                        id_emb INTEGER PRIMARY KEY,
                        nome VARCHAR(255) NOT NULL,
                        tipo VARCHAR(255) NOT NULL
                    );

                    DROP TABLE IF EXISTS Tripulantes CASCADE;
                    CREATE TABLE Tripulantes (
                        id_trp INTEGER PRIMARY KEY,
                        nome VARCHAR(255) NOT NULL,
                        data_nasc DATE NOT NULL,
                        funcao VARCHAR(255) NOT NULL,
                        id_emb INTEGER REFERENCES Embarcacoes
                    );

                    DROP TABLE IF EXISTS Empregados CASCADE;
                    CREATE TABLE Empregados (
                        id_emp INTEGER PRIMARY KEY,
                        nome VARCHAR(255) NOT NULL,
                        data_nasc DATE NOT NULL,
                        funcao VARCHAR(255) NOT NULL
                    );

                    DROP TABLE IF EXISTS Movimentacoes CASCADE;
                    CREATE TABLE Movimentacoes (
                        id_mov INTEGER PRIMARY KEY,
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
    disconnect(conn, context)