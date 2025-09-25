import psycopg2

class PostgresDB:
    def __init__(self, host, database, user, password, port=5432):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )
            print("Database connection successful")
        except Exception as e:
            print(f"Error connecting to database: {e}")

    def list_databases(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
            dbs = cursor.fetchall()
            print("Databases:", [db[0] for db in dbs])
            cursor.close()
        except Exception as e:
            print(f"Error listing databases: {e}")

    def list_tables(self, db_name):
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema='public' AND table_catalog='{db_name}';
            """)
            tables = cursor.fetchall()
            print(f"Tables in {db_name}:", [table[0] for table in tables])
            cursor.close()
        except Exception as e:
            print(f"Error listing tables: {e}")

    def close(self):
        if self.conn:
            self.conn.close()
            print("Database connection closed")


from Utils.db_utils import PostgresDB

# DB details
host = "dexlyn-qa-rds.cpwbcx7a5ige.ap-south-1.rds.amazonaws.com"
user = "qa_read_user"
password = "M8gDkYQCZsTge0Qu"

# Connect and list databases
db = PostgresDB(host=host, database="postgres", user=user, password=password)
db.connect()
db.list_databases()
print(db.list_databases)
print(db.list_tables)
# List tables in a specific database
db.list_tables("qa-swap-events")
# db.list_tables("your_database_name_here")

db.close()            