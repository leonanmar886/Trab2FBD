import createTable
import insertItems
import selectItems
import transactions
import storedProcedures
import triggers

X = input("""
  Digite uma opção: \n
  1. Criar Tabelas \n
  2. Inserir Dados \n
  3. Consultar \n
  4. Transações \n
  5. Procedimentos Armazenados \n
  6. Gatilhos \n
""")

match X:
  case "1":
    createTable.createTable()
 
  case "2":
    insertItems.insert_items()
    
  case "3":
    selectItems.select_boats_and_crew()
    selectItems.select_employes()
    selectItems.select_boats()
   
  case "4":
    transactions.insert_move()
    transactions.insert_move_employe()
    transactions.select_qtd_moves()
   
  case "5":
    storedProcedures.employer_of_month()
    storedProcedures.execute_employer_of_month('2023-10-21')
  
  case "6":
    triggers.create_capitain_trigger()
    triggers.create_move_trigger()
    triggers.test_capitan_trigger()
    triggers.test_move_trigger()
  