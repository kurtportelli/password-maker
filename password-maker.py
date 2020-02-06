def make_password(length, flagUpper, flagLower, flagDigit):
    uppers = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    lowers = set('abcdefghijklmnopqrstuvwxyz')
    digits = set('1234567890')
    
    pool = set()
    password = ''
    
    if flagUpper:
        password += uppers.pop()
        pool.update(uppers)
    if flagLower:
        password += lowers.pop()
        pool.update(lowers)
    if flagDigit:
        password += digits.pop()
        pool.update(digits)
        
    for i in range(len(password), length):
        password += pool.pop()
      
    return password
