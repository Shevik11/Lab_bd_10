class DAO:
    def __init__(self, db_connection):
        self.connection = db_connection

    def get(self, table_name):
        query = f"SELECT * FROM {table_name}"
        self.connection.cursor.execute(query)
        result = self.connection.cursor.fetchall()
        column_names = [desc[0] for desc in self.connection.cursor.description]
        rows = [dict(zip(column_names, row)) for row in result]
        for row in rows:
            print(row)
        return rows

    def create_record(self, table_name, values):
        columns = ', '.join(values.keys())
        placeholders = ', '.join(['%s'] * len(values))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.connection.cursor.execute(query, tuple(values.values()))
        self.connection.connection.commit()

    def edit_record(self, table_name, table_id, id, new_values):
        set_values = ', '.join([f"{column}=%s" for column in new_values.keys()])
        query = f"UPDATE {table_name} SET {set_values} WHERE {table_id} = {id}"
        self.connection.cursor.execute(query, tuple(new_values.values()))
        self.connection.connection.commit()

    def delete_record(self, table_name, table_id, id):
        query = f"DELETE FROM {table_name} WHERE {table_id} = {id}"
        self.connection.cursor.execute(query)
        self.connection.connection.commit()

    def get_one(self, table_name, table_id, id):
        query = f"SELECT * FROM {table_name} WHERE {table_id} = {id}"
        self.connection.cursor.execute(query)
        result = self.connection.cursor.fetchone()
        column_names = [desc[0] for desc in self.connection.cursor.description]
        row = dict(zip(column_names, result))
        print(row)
        return row