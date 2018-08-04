# Import module to generate hashes
import hashlib

# Hashing functions


def _hash_bytestr_iter(bytesiter, hasher, ashexstr=False):
    for block in bytesiter:
        hasher.update(block)
    return (hasher.hexdigest() if ashexstr else hasher.digest())


def _file_as_blockiter(afile, blocksize=65536):
    with afile:
        block = afile.read(blocksize)
        while len(block) > 0:
            yield block
            block = afile.read(blocksize)


# Function to get the hash


def gethash(fname):
    return [(fname,
             _hash_bytestr_iter(
                 _file_as_blockiter(open(fname, 'rb')), hashlib.sha256()))
            for fname in fnamelst]
