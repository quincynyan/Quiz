def input_int(text):
    while True:
        try:
            x = int(input(text))
            break
        except:
            pass
    return x        
