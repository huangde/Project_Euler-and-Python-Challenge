def P2decode(char):
    import string
    decodekey  =string.lowercase
    decodevalue=(string.lowercase+'ab')[2:]
    decode_dict=dict(zip(decodekey,decodevalue))
    if char in decode_dict:
        return decode_dict[char]
    else:
        return char


if __name__ == '__main__':
    in_str='g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

    print ''.join(map(P2decode,in_str))

    pswrd='map'
    print ''.join(map(P2decode,pswrd))
