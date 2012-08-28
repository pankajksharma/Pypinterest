import MySQLdb

def getusers(client,username,db,cursor):
	c = client.getfollowers(username)
	for i in c:
		if checkuser(i['username'],cursor) == 1:
			print i
			cursor.execute('insert into users(username,followers,name) value(\''+i['username']+'\','+str(i['followers'])+',\''+i['name']+'\')')
			db.commit()
	for i in c:
		getusers(client,i['username'],db,cursor)

def checkuser(username,cursor):
	if cursor.execute('select id from users where username=\''+username+'\'') == 0l:
		return 1
	else:
		return 0

from lib import pypinterest
mc = pypinterest.Client('email_address', 'username', 'password')
db = MySQLdb.connect('localhost','root','root','pinterest')
cursor = db.cursor()
getusers(mc,'steveandkenz',db,cursor)
