class Documento:
    def __init__(self, tipo, num_paginas, editable, contenido):
        self.tipo = tipo
        self.num_paginas= num_paginas
        self.editable= editable
        self.contenido= contenido

    def editar_documento(self, nuevo_contenido):
        if (self.editable == False):
            print('el archivo no puede ser modificado')
        else:
            self.contenido = nuevo_contenido
            print('El archivo fue modificado')

mi_curriculum = Documento(tipo='pdf',num_paginas=80,editable=False,contenido='Soy developer')
proforma_pagina_web = Documento(tipo='WORD',num_paginas=3,editable=True,contenido='La pagina web vale 2500 soles')

mi_curriculum.editar_documento(nuevo_contenido='Ahora soy diseñador')
proforma_pagina_web.editar_documento(nuevo_contenido='La pagina web vale 4000 soles')



        
