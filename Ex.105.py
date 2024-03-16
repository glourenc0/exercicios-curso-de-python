def notas(*num, sit=False):
    print("-"*30)
    r = {}
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['media'] = sum(num)/len(num)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = "Boa"
        elif r['media'] >= 5:
            r['situacao'] = "Razoável"
        else:
            r['situacao'] = "Ruim"
    return r
    

#Programa principal
resp = notas(5.5 , 2.5, 8.5, sit=True)
print(resp)