from bitcoin.rpc import RawProxy
import hashlib
import binascii

def transactionOrBlock(choice):
    if choice == "1":
        checkTrans()
    elif choice == "2":
        checkBlock()

def checkTrans():
    transValue = 0

    transId = raw_input("Enter transaction Id: ")

    p = RawProxy()

    trans = p.decoderawtransaction(p.getrawtransaction(transId))

    for outputTrans in trans['vin']:

        transIdLocal = outputTrans['txid']
        vout = outputTrans['vout']
        transLocal = p.decoderawtransaction(p.getrawtransaction(transIdLocal))

        for outputTransLocal in transLocal['vout']:

            if outputTransLocal['n'] == vout:
                transValue = transValue + outputTransLocal['value']

    for output in trans['vout']:
        transValue = transValue - output['value']

    print(transValue)

def checkBlock():
    hexcoding = 'hex_codec'

    p = RawProxy()
    blockId = raw_input("Enter Block Id: ")

    blockhash = p.getblockhash(int(blockId))

    block = p.getblock(blockhash)

    version = block['versionHex']
    hashPrevBlock = block['previousblockhash']
    hashMerkleRoot = block['merkleroot']
    time = block['time']
    bits = block['bits']
    nonce = block['nonce']

    nonce = hex(int(0x100000000) + int(nonce))[-8:]
    time = hex(int(0x100000000) + int(time))[-8:]

    version         = (version.decode(hexcoding))[::-1].encode(hexcoding)
    hashPrevBlock   = (hashPrevBlock.decode(hexcoding))[::-1].encode(hexcoding)
    hashMerkleRoot  = (hashMerkleRoot.decode(hexcoding))[::-1].encode(hexcoding)
    time            = (time.decode(hexcoding))[::-1].encode(hexcoding)
    bits            = (bits.decode(hexcoding))[::-1].encode(hexcoding)
    nonce           = (nonce.decode(hexcoding))[::-1].encode(hexcoding)

    header_hex = (  version +
                    hashPrevBlock +
                    hashMerkleRoot +
                    time +
                    bits +
                    nonce)

    header_bin = header_hex.decode('hex')
    hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()

    print("Calculated hash:")
    print(hash[::-1].encode(hexcoding))
    print("First hash:")
    print(blockhash)
