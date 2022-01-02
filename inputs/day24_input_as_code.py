def run(num):
    w,x,y,z=0,0,0,0

    # //1
    w = num[0]
    x =  (z % 26) + 14 # Always 0
    x = 1*(x!= w) # Always 1
    z *=  25*x +1 # Always 0 since z is zero up to here
    z +=  x*(w +12) # Always num[0]+12

    # //1
    w = num[1]
    x = ((z %  26) + 15) #  z is 13-21 so this is always >26
    x =  1*(w != x) # This is always true so x=1
    z *=  25*x +1 # So we have z*26
    z +=  x*(num[1]+7) # z -> z*26 + (num[1] + 7)

    # //1
    w = num[2]
    x = ((z %  26) + 12)
    x = 1*(w != x) # This is always true so x=1
    z *=  25 * x + 1  # So we have z*26
    z +=  x*(w+1) # z -> z*26 + (num[2] + 1)

    # //1
    w = num[3]
    x = ((z %  26) + 11)
    x = 1*(w != x) # This is always true so x=1
    z *=  (25*x+1) # So we have z*26
    z +=  x*(w+2) # z -> z*26 + (num[3] +2)

    # //26
    w = num[4]
    x =  (z % 26) - 5
    z = z// 26
    x = 1*(x!= w) # Want num[4] == (z % 26)-5 to be num[4]
    z *=  25*x +1
    z +=  x*(w+4) 
    ## This can do either:
    # z -> z//26 (if z%26 is 5)
    # z -> 26*(z//26) + (num[4]+4)
    # We need z to be small so clearly we want the first case
    # i.e. num[4] = (z%26) -5, = (num[3]+2) -5

    # //1
    w = num[5]
    x = (z %  26) + 14
    x = 1*(x!= w)
    z *=  25*x +1
    z +=  x*(w + 15)
    ## New digit is num[5] + 15

    # //1
    w = num[6]
    x =  (z % 26) + 15
    x = 1*(x!= w)
    y =  25*x+1
    z *=  y
    z +=  x*(w +11)
    ## New digit is num[6] + 11

    # //26
    w = num[7]
    x =  (z % 26) - 13
    z = z// 26
    x = 1*(x!= w)
    z *=  25*x +1
    z +=  x*(w + 5)
    ## Last digit -13 must be num[7]

    # //26
    w = num[8]
    x =  (z % 26) - 16
    z = z// 26
    x = 1*(x!= w)
    z *=  25*x +1
    z +=  x*(w+3)

    # //26
    w = num[9]
    x =  (z % 26) -8
    z = z// 26
    x = 1*(x!= w)
    z *=  25*x + 1
    z +=  x*(w+9)

    # //1
    w = num[10]
    x =  (z % 26) + 15
    x = 1*(x!= w)
    z *=  25*x + 1
    z +=  x*(w+2)

    # //26
    w = num[11]
    x = (z % 26) -8
    z = z// 26
    x = 1*(x!= w)
    z *= 25*x +1
    z += x*(w +3)

    # //26
    w = num[12]
    x = (z % 26)+0
    z = z// 26
    x = 1*(x!= w)
    z *=  25*x +1
    z += x*(w +3)

    # //26
    w = num[13]
    x =  (z % 26) -4
    z = z// 26
    x = 1*(x!= w) # Need x=w, so w = previous (z%26) -4
    z *=  25*x +1
    y =  x*(w+11)
    z +=  x*y

    return z