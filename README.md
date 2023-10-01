# quarantelli-Proyecto-YokoCino-Python_Django-master
Proyecto Final de CoderHouse - 

El proyecto es visible y funcional iniciando incluso desde http://127.0.0.1:8000/
Luego de eso puede navegarse normalmente a través de los botones, y desde ellos se accede a todas las funcionalidades
* A excepcion de las que requieren ser un usuario del staff (unicamente la edicion de posts)

1. Existe la ruta about con info corta sobre el proyecto
2. La vista de inicio funciona como cara principal dando una preview de todos los Post que componen el blog
3. Clickear en cada uno trae el detalle, a traves de un slug, para no mostrar un id
4. No hay botones que lleven a una pagina de "No hay paginas aun". Solo existe un mensaje en caso de ingresar una busqueda que no arroje un resultado
5. Como dije anteriormente, unicamente los usuarios del grupo Staff pueden modificar los post, a diferencia de lo que se pide que se relaciona unicamente con las imagenes
6. El modelo post cumple con los requisitos que pide la consigna (titulo, subtitulo, autor, fecha e imagen)
7. Existe la app Accounts para manejar lo referido a los usuarios (login, register, profile)
8. Es posible cargar link y descripcion a un perfil luego de ser creado - solo desde la edicion, no al principio
9. El admin permite manejar la base de ambas apps, donde incluso hay algunas personalizaciones para sumar comodidad (no en todos los modelos, mejorable con mas tiempo)
10. La mensajeria se maneja desde la app Accounts
