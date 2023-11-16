import createTable
import insertItems
import selectItems
import transactions
import storedProcedures
import triggers

#2.2 Criação de Tabelas
createTable.createTable()

#2.3 Inserção de Dados
insertItems.insert_items()

# 2.4 Consulta
selectItems.select_boats_and_crew()
selectItems.select_employes()
selectItems.select_boats()

# 2.5 Transações
transactions.insert_move()
transactions.insert_move_employe()
transactions.select_qtd_moves()

#2.6 Procedimentos Armazenados
storedProcedures.employer_of_month()
storedProcedures.execute_employer_of_month('2023-10-21')

#2.7 Gatilhos
triggers.create_capitain_trigger()
triggers.create_move_trigger()
triggers.test_capitan_trigger()
triggers.test_move_trigger()