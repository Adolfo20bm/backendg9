from camelcase import CamelCase

instancia = CamelCase()
s = 'Hola estoy usando camelcase'
resultado = instancia.hump(s)
print(resultado)


c = CamelCase('estoy', 'camelcase')
s = 'Hola estoy usando camelcase'
a=  c.hump(s)
# This is a another Sentence, But This One is a little Different
print(a)