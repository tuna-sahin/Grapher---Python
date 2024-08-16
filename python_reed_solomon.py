
from polynomial_class import polynomial

def get_comb(values,c):
    if c == 1:
        return [[i,] for i in values]
    else:
        l = []
        for i in values:
            values2 = values.copy()
            values2.remove(i)
            for j in get_comb(values2,c-1):
                l.append([i,] + list(j))
                
        l2 = []
        for i in l:
            i.sort()
            if i not in l2:
                l2.append(i)
        print(len(l2))
        return(l2)

def lagrange_interpolation(arr):
    g = polynomial("0")
    for i in arr:
        arr2 = arr.copy()
        arr2.remove(i)
        l = polynomial("1")
        for j in arr2:
            if j[0] == 0:
                temp = "x"
            elif j[0] > 0:
                temp = "x-" + str(j[0])
            else:
                temp = "x+" + str(j[0] * -1)
            l = l * polynomial(temp)
        if i[1] == 0:
            l = polynomial(str(i[1]))
        else:
            
            multiplier = i[1]/l(i[0])
            l = l * polynomial(str(multiplier))
        g += l
    return(g)
def rs_encode(values,t):            
    pairs = []
    for i,j in enumerate(values):
        pairs.append((i,j))
    p = lagrange_interpolation(pairs)        
    parity = []
    for k in range(len(values),len(values)+2*t):
        parity.append(p(k))
    return list(values + tuple(parity))
def rs_decode(values,t):
    c = len(values)-2*t
    a = [(i,j) for i,j in enumerate(values)]
    b = get_comb(a,c)
    
    output_dict = {}
    temp = []
    count = 0
    for l in b:

        p = lagrange_interpolation(l)
        #print(p)
        #print(p)
        if p not in output_dict.keys():
            output_dict[p] = 1
        else:
            output_dict[p] += 1
    
    c = (max(output_dict.values()))
    value = [i for i in output_dict if output_dict[i]==c][0]
    output_list = []
    for i in range(len(values) - 2*t):
        output_list.append(value(i))
    return(output_list)
    
if __name__ == "__main__":
    encoded_set = rs_encode((4,7,2,1,0),2)
    encoded_set[1] += 2                     #error generation
    decoded_set = rs_decode(encoded_set,2)
    print([round(i) for i in decoded_set])
