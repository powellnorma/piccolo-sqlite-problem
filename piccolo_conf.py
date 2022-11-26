from piccolo.engine.sqlite import SQLiteEngine
from piccolo.table import Table
from piccolo.columns import Varchar

db_f = 'data.db'
DB = SQLiteEngine(db_f, timeout=300)

class MyEntity(Table):
    name = Varchar()

MyEntity.create_table(if_not_exists=True).run_sync()
