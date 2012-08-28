'''see sql.sql'''

from lib import pypinterest
import MySQLdb

db = MySQLdb.connect('localhost','root','root','pinterest')
csr = db.cursor()
csr.execute('select id,username from users')
res = csr.fetchall()  

mc = pypinterest.Client('email_address', 'username', 'password')

for user in res:
	print '\n\n'+str(user[1])+':'
	t = mc.getuserinfo(str(user[1]))
	print tuple(t.keys())
	values = tuple(t.values())
	print str(values)
	csr.execute('insert into user_info '+str(tuple(t.keys())).replace('\'','`')+' values '+str(values))
	db.commit()
