import sqlite3

class Create_cursor():
    def __init__(self, db_path):
    #Open Database
        self.db_path = db_path
        self.conn = self.create_connection()
        self.cursor = self.conn.cursor()
    def create_connection(self):
        return sqlite3.connect(self.db_path)

    def create_table(self):
        # Create a SQL Table
        sql_command = '''
                         CREATE TABLE IF NOT EXISTS words(
                             Id INTEGER PRIMARY KEY AUTOINCREMENT, 
                             New_word TEXT, 
                             Translation TEXT,
                             Progress INTEGER, 
                             Time INTEGER
                         )'''

        self.cursor.execute(sql_command)
        print('Base with words successfully open')
        # Commit the changes to the database
        self.conn.commit()

    def print_data(self):
        select_data = 'SELECT * FROM words'
        self.cursor.execute(select_data)
        rows = self.cursor.fetchall()

        for row in rows:
            print(row)

    def write_new_word(self, word):
        insert_data = f"""
                   INSERT INTO words 
                   (New_word, Translation, Progress, Time) 
                   VALUES ( 
                       '{word['New_word']}',
                       '{word['Translation']}',
                       '{word['Progress']}',
                       '{word['Time']}'
                   )
               """
        self.cursor.execute(insert_data)
        # Commit the changes to the database
        self.conn.commit()
        print("Record new word successfully")

    def number_of_elements(self):

        select_data = 'SELECT * FROM words'
        self.cursor.execute(select_data)
        rows = self.cursor.fetchall()
        i = 0
        for row in rows:
            i = i + 1

        # print(i)
        return i

    def data_list(self):

        select_data = 'SELECT * FROM words'
        self.cursor.execute(select_data)
        rows = self.cursor.fetchall()
        all_lists = []
        word_id = []
        learning_words = []
        translated_words = []
        progress_list = []
        sec_time_list = []
        for row in rows:

            word_id.append(row[0])
            learning_words.append(row[1])
            translated_words.append(row[2])
            progress_list.append(row[3])
            sec_time_list.append(row[4])

        all_lists.append(word_id)
        all_lists.append(learning_words)
        all_lists.append(translated_words)
        all_lists.append(progress_list)
        all_lists.append(sec_time_list)

        return all_lists

    def get_record_list(self, row_name):

        select_data = f'SELECT {row_name} FROM words'
        self.cursor.execute(select_data)
        progress_list = self.cursor.fetchall()
        new_progress_list =[]
        for progress in progress_list:
            elem = progress[0]
            new_progress_list.append(elem)
        return new_progress_list

    def get_record_by_id(self, row_name, record_id):
        query = f"SELECT {row_name} FROM words WHERE id = ?"

        self.cursor.execute(query, (record_id,))
        record = self.cursor.fetchone()
        return record[0] if record else None

    def delete_record(self,number):

            # Deleting single record now
            sql_update_query = """DELETE from words where id = ?"""
            self.cursor.execute(sql_update_query, (number,))
            self.conn.commit()
            print("Record deleted successfully ")


    def edit_word_record(self, word, word_id):

        sql_update_query = """Update words set  New_word = ?  where id = ?"""
        data = (word, word_id)

        self.cursor.execute(sql_update_query, data)
        self.conn.commit()

    def edit_translation_record(self, translate, word_id):

        sql_update_query = """Update words set  Translation = ?  where id = ?"""
        data = (translate, word_id)

        self.cursor.execute(sql_update_query, data)
        self.conn.commit()

    def edit_progress_record(self, progress, word_id):

        sql_update_query = """Update words set  Progress = ?  where id = ?"""
        data = (progress, word_id)

        self.cursor.execute(sql_update_query, data)
        self.conn.commit()

    def edit_time_record(self, time, word_id):

        sql_update_query = """Update words set  Time = ?  where id = ?"""
        data = (time, word_id)

        self.cursor.execute(sql_update_query, data)
        self.conn.commit()


    def close_database(self):
        self.conn.close()



