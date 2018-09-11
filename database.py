import psycopg2

class Database:
    def __init__(self):
        self.conn = psycopg2.connect("dbname=Events user=postgres password=password host=localhost")
        self.conn.autocommit = True
        self.cur = self.conn.cursor()
        print("Connected to the database")

    def add_users(self, first_name, last_name, age, email, password):
        self.cur.execute("INSERT INTO users(first_name, last_name, age, email, password, created_at) VALUES (%s, %s, %s, %s, %s, NOW())", (first_name, last_name, age, email, password))
    
    def get_all_users(self):
        self.cur.execute("SELECT * FROM users")
        print(self.cur.fetchall())

    
    def update_users(self, user_id,first_name, last_name, age, email, password):
        self.cur.execute("UPDATE users SET first_name= %s, last_name=%s, age= %s, email= %s, password= %s WHERE user_id = %s", (first_name, last_name, age, email, password, user_id))

    def add_event(self, event_name, location):
        self.cur.execute("INSERT INTO event(event_name, location) VALUES(%s, %s)",(event_name, location))
        print("Event added")

    def get_event(self):
        self.cur.execute("SELECT * FROM event")
        print(self.cur.fetchall())

    def update_event(self, event_id, event_name, location):
        self.cur.execute("UPDATE event SET event_name = %s, location = %s WHERE event_id = %s", (event_name, location, event_id))
        print("Event updated")

    def add_ticket(self, user_id, event_id, is_valid, verification_code, created_at):
        self.cur.execute("INSERT INTO ticket(user_id, event_id, is_valid, verification_code, created_at) VALUES (%s, %s, %s, %s, NOW())",(user_id, event_id, is_valid, verification_code))
        print("Ticket added")

    def get_tickets(self):
        sELF.CUR.execute("SELECT * FROM ticket")
        print(self.cur.fetchall())

    def update_tickets(self, user_id, event_id, verification_code,is_valid):
        self.cur.execute("UPDATE ticket SET user_id=%s, event_id=%s, is_valid =%s ,verification_code=%s, created_at=NOW() WHERE ticket_id=%s",(user_id, event_id, is_valid, verification_code, ticket_id))
        print("Ticket table updated")



