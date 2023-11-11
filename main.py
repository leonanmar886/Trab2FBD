import createTable
import insertItems
import selectItems
import transactions
import storedProcedures

from dbConnection import conn, context

#2.2 Criação de Tabelas
createTable.createTable(conn, context)

#2.3 Inserção de Dados
insertItems.insert_items(conn, context)

#2.4 Consulta
selectItems.select_boats_and_crew(context)
selectItems.select_employes(context)
selectItems.select_boats(context)

#2.5 Transações
transactions.insert_move(conn, context)
transactions.insert_move_employe(conn, context)
transactions.select_qtd_moves(context)

#2.6 Procedimentos Armazenados
storedProcedures.employer_of_month(conn)

context.close()
conn.close()