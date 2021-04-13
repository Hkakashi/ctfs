# writeup for backup
## alice
```
┌──(root💀kali)-[/opt/ctf_crypto/RsaCtfTool]
└─# ./RsaCtfTool.py --publickey ~/ctfs/2021/midnightsunctf/backup/alice/.ssh/authorized_keys --private

[*] Testing key /root/ctfs/2021/midnightsunctf/backup/alice/.ssh/authorized_keys.
[*] Performing fibonacci_gcd attack on /root/ctfs/2021/midnightsunctf/backup/alice/.ssh/authorized_keys.
100%|███████████████████████████████████████| 9999/9999 [00:00<00:00, 53975.70it/s]
[*] Performing pastctfprimes attack on /root/ctfs/2021/midnightsunctf/backup/alice/.ssh/authorized_keys.
100%|████████████████████████████████████████| 113/113 [00:00<00:00, 121933.72it/s]
[*] Performing mersenne_primes attack on /root/ctfs/2021/midnightsunctf/backup/alice/.ssh/authorized_keys.
100%|██████████████████████████████████████████████| 51/51 [00:01<00:00, 34.92it/s]
[*] Performing smallq attack on /root/ctfs/2021/midnightsunctf/backup/alice/.ssh/authorized_keys.
[*] Performing factordb attack on /root/ctfs/2021/midnightsunctf/backup/alice/.ssh/authorized_keys.
[*] Attack success with factordb method !

Results for /root/ctfs/2021/midnightsunctf/backup/alice/.ssh/authorized_keys:

Private key :
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEA7/X2AA3UI2OxE0ovuTg8V5jtnCiUbuMy+7OMhhyzF1cpMNz+
z5DzmCdfENEGdpreoWnBNWcNdlJom4IxDVeBj0dBkfvzfzWfLdFbYtIVfkY9zkIo
9P1uETPqYU0ppwPSs+I9uGTDZ0ADJezGjkox0TftUxOKxE0wTKcispWLtNWhmy28
wQQnFvmHmS4QMmBdRaC8l40hMernAxTRPrnfCK0FrbOHedLVhR34nEc7pX7JbqPw
9USLWrAw8eq7WVEgKlpi1sP17k5rxOIJFNR7BovYzJxawFeLMv7PtI1svhh//F+0
NW4H8Zl/R3xlt6pzvynOXhal+ovUcZxmwv2M8QIDAQABAoIBAHk8BFCcq/xBRtqf
FaN3pQ0Ax7Oo0O2BPmXqnem4IEd/kuEMFnUaH+hUo/QkFybfMfHNM39elG+eTRmc
WloKRvvznU47RBeWKNkGOCyiRZept1o5FOZKEE0CtLz6Njwac17MxDAgQJUuwyhr
CxoipC63GeFqMybgdLGVk7M0WQRAHE7J9qR9J0jHSGiiDVGpEiI4EY0GgFBy7K6P
JOb97/Tbu/v8AoTtC49gl8YvOQMp6YtDoik4lbFkkKPdtpKnF3aWqYdBQCbMq8rh
16eD7mvKAN3K1Hi+LByiPOCZO2ExqXMiWBJsRVR/kr7HFpYBZvsgmMctTPxwAdel
B2TxIJECgYEA8+Y6U3uYRRt1Na6FVhZANNurtzFXKLEWpmEzybRjeTa2y3hluN2e
0PBEJsrK+G36xKNIA9jiergWcGZgypGAkIm34EHI2Is0ktjifySV6gn4/BUjjLHi
uAQjl/hXJpBkknluUeumLDfzKdsx5BV2GSLCBOgc7GzAYV2gRtxxCEUCgYEA+921
peoDPNommLEr2tMJPEA4dSaQa3LpEpRRtqjNFeCXo/xqQ1mBnavGFmQtLruiIqzv
GeC2eJ/8Po0FQ2+Xo+zh8GDtDETfNOB7IazrzOaU8dNQzLrdiOJXjYigSiJAh3TT
n5/icPwkWUFR/NvQAYoH3q2SlZyhtGGwKWE0yr0CgYB5lFGM3fZ4tIhH+zgyQqM8
9ifyCOF2wlgVFi03pflUKicS5HBop+kMJEkEwWBOWJyBuxch+9Jh9DQTUaV8NO3O
nygO3Rwefb32WbEGShmE8fWwy2TONLpcmouXrM7cxWus7GVG5t4N+tH3EnIbTWty
ejYXNhF89XUs0/wadrbNtQKBgFJH8enL81bT5bwIVU1dmCzIxijvekq/9YiOT8ue
hbFZ9/AorAZonUGHNmVmQKR9w9AUMuB/Wt05VsyQgWGweReicYV4BLj3XvwFQfSU
a0w7H/mIkWLwwSLQ3s1sDwFpAy+9aM1DDFTg6ncGMeSrYt692yhSCAs8ak9lgoli
Kj75AoGAMSQ4zf4uQkMjJR19EeWZ9748og6rfUFJCZap7mwQhBntBcMfa725MrXU
fyvS8xiiFAwDwEu964CxMAKo0+2r2fLDetdSBnkqWBPI0K0Vdjtd+ZfUX7Hbw31m
dqwk4Flpg9j+yvsPLg/iZJQfyslmtE3zlLGVBjmUU/pag5rYeQ8=
-----END RSA PRIVATE KEY-----
```

## bob
```
┌──(root💀kali)-[/opt/ctf_crypto/RsaCtfTool]
└─# ./RsaCtfTool.py --publickey ~/ctfs/2021/midnightsunctf/backup/bob/.ssh/authorized_keys --private                                                                 

[*] Testing key /root/ctfs/2021/midnightsunctf/backup/bob/.ssh/authorized_keys.
[*] Performing fibonacci_gcd attack on /root/ctfs/2021/midnightsunctf/backup/bob/.ssh/authorized_keys.
100%|███████████████████████████████████████| 9999/9999 [00:00<00:00, 53805.62it/s]
[*] Performing pastctfprimes attack on /root/ctfs/2021/midnightsunctf/backup/bob/.ssh/authorized_keys.
100%|████████████████████████████████████████| 113/113 [00:00<00:00, 116881.96it/s]
[*] Performing mersenne_primes attack on /root/ctfs/2021/midnightsunctf/backup/bob/.ssh/authorized_keys.
100%|██████████████████████████████████████████████| 51/51 [00:01<00:00, 34.86it/s]
[*] Performing smallq attack on /root/ctfs/2021/midnightsunctf/backup/bob/.ssh/authorized_keys.
[*] Attack success with smallq method !

Results for /root/ctfs/2021/midnightsunctf/backup/bob/.ssh/authorized_keys:

Private key :
-----BEGIN RSA PRIVATE KEY-----
MIIFKQIBAAKCAQIjaiTNy87LpSEEofzlVODW7X755+j4nLRMO6ygpgB4Ln23gUFn
DOT3mbq4MvI9X4TCYslJF5JsJ2SwgwzE8vasFN7glEnWAZAMS1LfCRPFQXbQ5AL+
SjV+FOjHPjz9t9f8HXXNf/9P1yLbxS/L5q/Z1GnZjxur8q/n2oWmfkaHdiKc/MdC
2rUhzRNEuFUQ1thXCTr4DPXS8jheor3Qipm8ed8Q669QfAI6CR5whssoC7p0Ugzi
t1ElXTOpkLpkAo41VjBJSWbIcayhX1LcQ6qyHjy3VRyOyMTyDWKT8b08PoIiGGjd
f/GEP2G1BTECWS5XDbFbUu7nHwZFXkoe4EzGHUcCAwEAAQKCAQIPBRZS3EjJLHbr
k94bE/329aF2NKacm+BzffYSSAGjo2j2PX6XRzkwVNeJpiwjtHQD9G7AH2n0CTcJ
ApMT41UpuiAGA+ymOeFh99Cq37RyIFQqVj8GxuYAR/5qgYSNaTMiygAZbgbEqfXS
F/s99jdXLSaB7nCXr+sPrXWkS5bHfbPBdbQN8tloSrfzlT1erQA8l5N8m+PS88rC
PlOwIXwVJkqs3cso5qWYNsJLYQH3PHgRO2v9wIdHDQY4NdEGl50cDPZa9lS+/Y2f
qW4JtICLWICD0JSdyAdHurquUV4FqfnHlzY3BY0r3fttIF8ckwK/QnnR6giAJC6R
hXu3qYFf60ECggEBAOfuUViI4nGP7OF68eMdXTgjyerDulR9dlK5YkcEFF40sR4k
aeK0r3uhntgkSBMFUJ55wKKw78Jh/z7hzqadgCSNsjGwE8z6ZhR/4a+mDCh1CIqn
vdok00JOdGEQhpsTHAPtA1alf5/+b5VNRz5ccyqNuJBCm3yTqE0D9M7C8vcGLlQv
W/A1V4/6Wmzv4o0HtXr0E/SQVGTZqXJLTxaNnZ+ad2O8jE35dO/Is+ggaqCY8P3T
qc6BuwOwYUCC1jmF00P5+E6fwS6GhtpM3uDBeDaZJxkSxBTK1sngzfxPO9e/Laqe
EXxAMt0Qi0uF8rTLFFBEzKOytsmCwcs0uk+rmVECAicXAoIBABt2TIt/KdDoidPp
CtspjvAmzLHPmzCF6ozBBrIB+adt9crr5N3DJ0QsTvKo2R/ncTRSlkytRrZthBue
ASoZXCL35DGd97o9q/iha8ewkZ/4u5ovYnuCAMHJKF6V5lpWWOreFZcc4Y/AQNYc
4GKx77EKNuBeAqstkLAN197jloFJahLtyKUYq9WQf0SG4vxv/T0hyXsb2+JVI4s0
/5hcDF3pnFli6foRn5cE3MiPjhCWC3MCrQiWs94r9Ff/Jf6JqgpSfuRQZj9sDmuq
znkub12HpOmDH1SW7/fXdox5lUxmhrG9JbTgpSUn4FaA9cwSf8VBYDnB34LcyLWW
+LiWSQECAiSJAoIBAEl4ficY6tgFU4GgYmuoWIWrthNQzh9Rd9S5aHnbbkozowO9
w/aD/PR8T7ziR8uyvMCKVrUImEmZjlR9JqB7Drq24EQ8BiuLxXgal+wsq3ccCwup
+GZPDHU+iP6kdTzQtvyCzGJPY84K6gSFtzLJJYfxCDJn1Q6SZC4xWPwk/f58plOd
HGHWarxBPH6au2W/uVKeG1mSpFCNmowRt26fuXCliOZDz9aYsuvYr+Vng/yjxcdw
tuDYLf2WS/w8LB8dhm9656OjWNmasLeogYtFjMsFgw+KYhUrGT3TyWzcCPrYttj0
ZOi1mzPJ1tW+RU/PJ+v+XGcfXPneAUWQfE4KDPU=
-----END RSA PRIVATE KEY-----
```