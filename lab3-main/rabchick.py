def solve(nhead,nleg):
    rab=(nleg-2*nhead)/2
    chick=nhead-rab
    return int(rab),int(chick)
'''решил систему через х-число кроликов и у-число куриц; получилось два уравнения 4*х+2у=ноги х+у=головы '''
nhead=35
nleg=94
chick,rab=solve(nhead,nleg)
print(chick,rab)