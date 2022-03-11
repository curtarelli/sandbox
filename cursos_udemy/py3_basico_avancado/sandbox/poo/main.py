import os
path = r'py3_basico_avancado\sandbox\poo'
os.chdir(os.path.join(os.getcwd(), path))

from py3_basico_avancado.sandbox.poo.classes import *

#p1 = Pessoa()
#p2 = Pessoa()
#p1.nome = r'Luiz'
#print(p1.nome)
#p1.falar()

p1 = Pessoa('Luiz', 15)
p2 = Pessoa('Victor', 31)

p1.comer('maçã')
p1.comer('maçã')
p1.parar_comer()
p1.comer('maçã')
p1.parar_comer()
p1.parar_comer()

print(p1.get_ano_nascimento())

p3 = Pessoa.por_ano_nascimento('Rafael', 1988)
p3.get_ano_nascimento()
print(p3.idade)

p1 = Produto('Camiseta', 50)
p1.desconto(10)
print(p1.preco)

a1 = A()
a1.vc = 321
print(a1.vc)
print(A().vc)
A.vc = 321
print(A().vc)

bd = BancoDeDados()
bd._dados

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
maquina.escrever()
