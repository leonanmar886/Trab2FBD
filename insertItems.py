from prettytable import PrettyTable
from createTable import conn, context

context.execute("INSERT INTO Embarcacoes VALUES(%s,%s,%s)",(1,'Navio1','Cargueiro'))
context.execute("INSERT INTO Embarcacoes VALUES(%s,%s,%s)",(2,'Navio2','Passageiro'))
context.execute("INSERT INTO Embarcacoes VALUES(%s,%s,%s)",(3,'Navio3','Petroleiro'))
context.execute("INSERT INTO Embarcacoes VALUES(%s,%s,%s)",(4,'Navio4','Cargueiro'))

context.execute("INSERT INTO Tripulantes VALUES(%s,%s,%s,%s,%s)",(1,'Tripulante1','1990-01-15', 'Oficial de Convés', 1))
context.execute("INSERT INTO Tripulantes VALUES(%s,%s,%s,%s,%s)",(2,'Tripulante2','1992-03-20', 'Engenheiro', 1))
context.execute("INSERT INTO Tripulantes VALUES(%s,%s,%s,%s,%s)",(3,'Tripulante3','1988-11-05', 'Comissário de Bordo', 2))
context.execute("INSERT INTO Tripulantes VALUES(%s,%s,%s,%s,%s)",(4,'Tripulante4','1995-06-30', 'Oficial de Convés', 3))
context.execute("INSERT INTO Tripulantes VALUES(%s,%s,%s,%s,%s)",(5,'Tripulante5','1991-07-10', 'Capitão', 4))
context.execute("INSERT INTO Tripulantes VALUES(%s,%s,%s,%s,%s)",(6,'Tripulante6','1994-09-25', 'Engenheiro', 4))

context.execute("INSERT INTO Movimentacoes VALUES(%s,%s,%s,%s)",(1,'2023-09-01','Carga', '1'))
context.execute("INSERT INTO Movimentacoes VALUES(%s,%s,%s,%s)",(2,'2023-09-02','Embarque de Passageiros', '2'))
context.execute("INSERT INTO Movimentacoes VALUES(%s,%s,%s,%s)",(3,'2023-10-03','Abastecimento', '3'))
context.execute("INSERT INTO Movimentacoes VALUES(%s,%s,%s,%s)",(4,'2023-10-05','Descarga', '1'))
context.execute("INSERT INTO Movimentacoes VALUES(%s,%s,%s,%s)",(5,'2023-10-05','Manutenção', '4'))

context.execute("INSERT INTO Movimentacoes_Empregados VALUES(%s,%s)",(1,1))
context.execute("INSERT INTO Movimentacoes_Empregados VALUES(%s,%s)",(1,3))
context.execute("INSERT INTO Movimentacoes_Empregados VALUES(%s,%s)",(2,2))
context.execute("INSERT INTO Movimentacoes_Empregados VALUES(%s,%s)",(3,1))
context.execute("INSERT INTO Movimentacoes_Empregados VALUES(%s,%s)",(3,4))
context.execute("INSERT INTO Movimentacoes_Empregados VALUES(%s,%s)",(4,1))
context.execute("INSERT INTO Movimentacoes_Empregados VALUES(%s,%s)",(4,3))
context.execute("INSERT INTO Movimentacoes_Empregados VALUES(%s,%s)",(5,1))

conn.commit()
context.close()
conn.close()