import random, time
from randcrack import RandCrack
from pwn import *

# random.seed(time.time())

rc = RandCrack()

# for i in range(624):
# 	rc.submit(random.getrandbits(32))

# print("Random result: {}\nCracker result: {}"
# 	.format(random.randrange(0, 4294967295), rc.predict_randrange(0, 4294967295)))





# Global vars
################################################################
host 		= args['RHOST'] or "challenge.nahamcon.com"   # passed as arguments or hardcode
port 		= args['RPORT'] or "31784"        # passed as arguments or hardcode
# user 		= args['USER']  or ''
# password 	= args['PASS']  or ''
# binary		= args['BIN']   or './path/to/binary'

conn = remote(host, port)

for i in range(624):
    print(i)
    conn.sendline('2')
    conn.recvuntil(b'> Rolling the dice... the sum was:\n')
    rc.submit(int(conn.recvline().decode()))
#resp = conn.interactive()               #if you want to manually try things out first
conn.sendline('3')
conn.sendline(str(rc.predict_getrandbits(32)))
conn.interactive()
exit(0)
'''
resp = conn.recvline()
print "Server sent:   " + resp
resp = conn.recvline()                   #Sometimes initial connects send us 2 lines   
print "Server sent:  " + resp

#data2send = "some send stuff"
#print "Sending: " + data2send
#conn.sendline(data2send)

#resp = conn.recvline()
#print "response wuz: " + resp




# Solve that shit here
################################################################################################

data2send = "some data and stuff"
print "Sending: " + data2send
conn.sendline(data2send)

resp = conn.recvline()
print "Server sent: " + resp   #final response   the FLAG!!! 


# Shut it down
################################################################################################


conn.close() #close connection






'''







################################################################################################
################################################################################################
#	Solutions! 
#
#   trying this out, to keep solutions to challs as comments in a big ol script
#	might be better to pull out into its own
################################################################################################
################################################################################################

#solve equations for internetwache
'''
while True:

	data2 = s.recv(size)
	print "The eq: " + data2
	strr = data2.split(':')
	x = Symbol('x')
	y = Symbol('y')
	equation = strr[1].rstrip()  # ' x +1 = 9'
	eq = equation.split('=')
	left = eq[0]
	right = eq[1]
	an = solve(Eq(sympify(left), sympify(right)))
	s.send(str(an[0]))
	data2 = s.recv(size)
	print "is it right? " + data2

s.close()
'''
################################################################################################


################################################################################################


################################################################################################


################################################################################################


################################################################################################


################################################################################################


################################################################################################


################################################################################################


################################################################################################


################################################################################################


################################################################################################


################################################################################################


################################################################################################






























