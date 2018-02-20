## Comentarios Python TinyDB

Requisitos de software previamente instalado:

+ Python 3.5
+ Python PIP
+ Ruby 2.3.1
+ TinyDB

### Descipción

En caso de usar el servicio en python:

    $ sudo pip install virtualenv
    $ virtualenv -p python3 <<nombre_ambiente>>
    $ cd <<nombre_ambiente>>
    $ source bin/activate
    $ pip install -r requirements.txt
    $ python app.py

## Pruebas de Comportamiento

Ejecutar

    $ cd test/rspec
    $ rspec spec comentario_perfil_criador.rb

### Formato de Dato Grabado : db/criadores.json

    {
        'criador_id':n,
        'comentarios': [
            {
                criador_id: n, 
                momento: datetime, 
                comentario: text
            },...
        ]
    }

### TODO:

+ Verificar el tipo de dato a usar en el grabado de dato de momento de un comentario para que sea compatible con javacript.

### Fuentes:

+ https://bottlepy.org/docs/dev/
+ http://tinydb.readthedocs.io/en/latest/index.html
+ http://tinydb.readthedocs.io/en/latest/usage.html#document-ids
+ https://buxty.com/b/2013/12/jinja2-templates-and-bottle/

Thanks/Credits

    Pepe Valdivia: developer Software Web Perú [http://softweb.pe]