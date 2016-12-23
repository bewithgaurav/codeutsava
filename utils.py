import MySQLdb

def connect():
    db = MySQLdb.connect("mysql.cwpm2yjzxzkk.us-west-2.rds.amazonaws.com","root","12345678","codeutsava")
    cursor = db.cursor()

