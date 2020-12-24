N = 14905562257842714057932724129575002825405393502650869767115942606408600343380327866258982402447992564988466588305174271674657844352454543958847568190372446723549627752274442789184236490768272313187410077124234699854724907039770193680822495470532218905083459730998003622926152590597710213127952141056029516116785229504645179830037937222022291571738973603920664929150436463632305664687903244972880062028301085749434688159905768052041207513149370212313943117665914802379158613359049957688563885391972151218676545972118494969247440489763431359679770422939441710783575668679693678435669541781490217731619224470152467768073
e1 = 12886657667389660800780796462970504910193928992888518978200029826975978624718627799215564700096007849924866627154987365059524315097631111242449314835868137
e2 = 12110586673991788415780355139635579057920926864887110308343229256046868242179445444897790171351302575188607117081580121488253540215781625598048021161675697
c1 = 14010729418703228234352465883041270611113735889838753433295478495763409056136734155612156934673988344882629541204985909650433819205298939877837314145082403528055884752079219150739849992921393509593620449489882380176216648401057401569934043087087362272303101549800941212057354903559653373299153430753882035233354304783275982332995766778499425529570008008029401325668301144188970480975565215953953985078281395545902102245755862663621187438677596628109967066418993851632543137353041712721919291521767262678140115188735994447949166616101182806820741928292882642234238450207472914232596747755261325098225968268926580993051
c2 = 14386997138637978860748278986945098648507142864584111124202580365103793165811666987664851210230009375267398957979494066880296418013345006977654742303441030008490816239306394492168516278328851513359596253775965916326353050138738183351643338294802012193721879700283088378587949921991198231956871429805847767716137817313612304833733918657887480468724409753522369325138502059408241232155633806496752350562284794715321835226991147547651155287812485862794935695241612676255374480132722940682140395725089329445356434489384831036205387293760789976615210310436732813848937666608611803196199865435145094486231635966885932646519

#N = p*q
#c1 = (2*p + 3*q)**e1 mod N
#c2 = (5*p + 7*q)**e2 mod N

#a = c1%N = (2*p + 3*q)**e1
#b = c2%N = (5*p + 7*q)**e2

#c1%(q*p) = (2*p + 3*q)**e1
#c2%(q*p) = (5*p + 7*q)**e2

a = c1%N
b = c2%N

a = 14010729418703228234352465883041270611113735889838753433295478495763409056136734155612156934673988344882629541204985909650433819205298939877837314145082403528055884752079219150739849992921393509593620449489882380176216648401057401569934043087087362272303101549800941212057354903559653373299153430753882035233354304783275982332995766778499425529570008008029401325668301144188970480975565215953953985078281395545902102245755862663621187438677596628109967066418993851632543137353041712721919291521767262678140115188735994447949166616101182806820741928292882642234238450207472914232596747755261325098225968268926580993051
b = 14386997138637978860748278986945098648507142864584111124202580365103793165811666987664851210230009375267398957979494066880296418013345006977654742303441030008490816239306394492168516278328851513359596253775965916326353050138738183351643338294802012193721879700283088378587949921991198231956871429805847767716137817313612304833733918657887480468724409753522369325138502059408241232155633806496752350562284794715321835226991147547651155287812485862794935695241612676255374480132722940682140395725089329445356434489384831036205387293760789976615210310436732813848937666608611803196199865435145094486231635966885932646519

##a**1/e1
##b**1/e2


"""
from decimal import Decimal

c = Decimal(1/e1)

d = Decimal(pow(a,c))

print (d)
## d = 1

e = Decimal(1/e2)

f = Decimal(pow(b,e))

print (f)
# f = 1

# 2p + 3q = 5p + 7q
# 4q = -3p
# q = -3/4p
# 1 = 2p + 3q
# 1 = 2p + 3(-3/4p)
# 1 = 2p - 9/4p
# 1 = -1/4p
# p = -4

# 4q = -3p
# 4q = -3(-4)
# 4q = 12
# q = 3


"""
"""
from decimal import Decimal
c = Decimal((1/e1))

d = Decimal(a**c)

e = Decimal(1/e2)

f = Decimal(b**e)

#c1 = (2*p + 3*q)**e1 mod N

# N = p*q
# q = -3/4p
# N = p*(-3/4 p)
# N = (-3/4p)**2
g = Decimal(Decimal(N)*Decimal(.75))
print (g)

# g = p**2

import math
#h = (g**(1/2))
#print (h)

#p
i = Decimal.sqrt(g)
print (i)

#q
j = N/i
print (j)

print (i*j)
"""

#c1 = (2(N/q) + 3q)**e1 mod N
#c2 = (5(N/q) + 7q)**e2 mod N

# a = (2(N/q) + 3q)**e1
"""
from decimal import Decimal

c = Decimal(1/e1)


# c = 2(N/q) + 3q
d = 2*N


# c = 2N/q + 3q
# cq = 2N + 3q**2
# 3q**2 - cq + 2N

# (-b +- squareRoot (b**2 - 4ac)) / 2a
l = (Decimal(c**2))
print (l)

m = Decimal(12*d)
print (m)

#print ((Decimal(c**2) - (Decimal(12*c)**(1/2))))

n = l - m
print (n)

o = n**1/2

p = 3*c

q = p+o
r = p - o

s = q/6
t = r/6

print (s)
print (t)

# q = -2.981112451568542811586544827E+616
# q = 2.981112451568542811586544827E+616

print (N/s)
print (N/t)

# -0.4999999999999999999999999998
# 0.4999999999999999999999999998

# q = -3/4p

u = 2/Decimal(.75)
print (u)
"""

#N = p*q
#c1 = (2*p + 3*q)**e1 mod N
#c2 = (5*p + 7*q)**e2 mod N

# c1 = (2(n/q) + 3q)**e1 mod N

