from lib import pypinterest
mc = pypinterest.Client('email_address', 'username', 'password')
c = mc.getfollowing('username')
for i in c:
	print i
