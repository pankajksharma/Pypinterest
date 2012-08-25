from lib import pypinterest
mc = pypinterest.Client('email_address', 'username', 'password')
c = mc.getfollowers('username')
for i in c:
	print i
