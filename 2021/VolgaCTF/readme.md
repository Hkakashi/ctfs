# writeups
## JWT

Register an account and check the token stored. From the challenge name we know it is JWT. 

Decode at [jwt.io](jwt.io) we can see it has `jku` field which use to locate JSON web key set.

![picture 2](../../images/f864297277934cee05f0e2b800fddec6b3eb033d8bdee1b76cc574234529b661.png)  

We can try to change this field and see if it send request to us. Use [webhook.site](webhook.site) to listen for requests.

And it send a reqest to us. 

Search online, seems the only thing missing is we have to use a algorithm (kty) recogizable by the server.

And after some testing, if we change the kid in the header, it will gave us an error message:

```
JWT processing failed. Additional details: [[17] Unable to process JOSE object (cause: org.jose4j.lang.UnresolvableKeyException: 
Unable to find a suitable verification key for JWS w/ header {"kid":"HS25","alg":"HS256"} from JWKs 
[org.jose4j.jwk.OctetSequenceJsonWebKey{kty=oct, kid=HS256, alg=HS256}] obtained from http://localhost:8080/secret): 
JsonWebSignature{"kid":"HS25","alg":"HS256"}->eyJraWQiOiJIUzI1IiwiYWxnIjoiSFMyNTYifQ.eyJqa3UiOiJodHRwOi8vbG9jYWxob3N0OjgwODAvc2VjcmV0IiwiZXhwIjoxNjE3NjEyNDE4LCJqdGkiOiJuVE84NHI4UklhVU84eU5vTXpiOEV3IiwiaWF0IjoxNjE3MDA3NjE4LCJuYmYiOjE2MTcwMDc0OTgsInN1YiI6ImRlYWxicmVha2VyIn0.nLcsfv12LKrCIgEgIPHAOgfjwgVhXNEsGg18_lbxzdM]
```

which gave us the `kty` field. And the rest is stright forward, we can provide JWKs below:

```
{
"kty":"oct",
"k":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
"alg":"HS256",
"kid":"HS256"
}
```

And sign JWT:

![picture 3](../../images/37fb603a492b739e5bd9ac50ea548c9d54744270c75d9ff2a5505e20faad6421.png)  

Change the token and we are admin.

## Unicorn Networks

[writeup from aszx87410](https://github.com/aszx87410/ctf-writeups/issues/29)

## flask admin

This admin page is not properly protected:
http://172.105.84.156:5000/admin/user/new/

This page can be used to create an admin account.

