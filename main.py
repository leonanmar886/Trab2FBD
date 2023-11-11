import createTable
import insertItems
import selectItems

from dbConfig import conn, context

createTable.createTable(conn, context)
insertItems.insert_items(conn, context)
selectItems.select_boats_and_crew(context)
selectItems.select_employes(context)
selectItems.select_boats(context)