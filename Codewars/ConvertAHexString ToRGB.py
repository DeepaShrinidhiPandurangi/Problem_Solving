def hex_string_to_RGB(hex_string): 
    # your code here
    hexadecimal = hex_string[1::]
    print(hexadecimal)
    res = {}
    res['r'] = int(hexadecimal[0:2],16)
    res['g'] = int(hexadecimal[2:4],16)
    res['b'] = int(hexadecimal[4:6],16)
    return res
    pass
