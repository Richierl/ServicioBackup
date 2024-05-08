![image](https://github.com/Richierl/ServicioBackup/assets/124211951/4c517a11-c897-41bc-a652-8c0f9bac34ca)

### 👤 Nombre: Rodriguez Ledesma Ricardo
###  ✏️Materia: Patrones de diseño
### 🏫 Escuela: Instituto Tecnólogico de Tijuana
### 💻 Carrera: Ingenieria en Sistemas Computacionales


### 📝 DESCRIPCIÓN DEL PROYECTO:
El proyecto consiste en el desarrollo de un sistema de servicio de backup utilizando Django, un framework web de alto nivel en Python. El sistema permite a los usuarios realizar las siguientes acciones:

  1. **Crear Backups:**
Los usuarios pueden crear nuevos backups proporcionando un nombre descriptivo, una descripción opcional y subiendo un archivo, que puede ser una imagen o un documento en formato PDF.

  2. **Listar Backups:**
Se muestra una lista de los backups existentes en el sistema, incluyendo detalles como el nombre del backup, la descripción (si está disponible) y un enlace para descargar el archivo asociado.

  3. **Eliminar Backups:**
Los usuarios tienen la capacidad de eliminar backups existentes mediante un botón asociado a cada backup en la lista.

El sistema utiliza un modelo de base de datos para almacenar la información de cada backup, incluyendo el nombre, la descripción (opcional), y la ubicación del archivo asociado en el sistema de archivos.

### 🖥️ TECNOLOGÍAS UTILIZADAS:
  - **Django:** Framework web en Python utilizado para el desarrollo del backend del sistema.

  - **HTML/CSS:** Utilizados para la presentación de las interfaces de usuario mediante plantillas HTML.

  - **SQLite** (u otro gestor de base de datos): Utilizado como el motor de base de datos para almacenar la información de los backups.

### ✒️ PATRONES DE DISEÑO UTILIZADOS:
  1. **MVC (Model-View-Controller):**
MVC es un patrón de arquitectura de software que separa una aplicación en tres componentes principales: Model (Modelo), View (Vista) y Controller (Controlador).

     - **Model (Modelo):** Representa la estructura de datos y la lógica de negocio de la aplicación. En Django, los modelos son clases que definen la estructura de la base de datos y encapsulan la lógica relacionada con los datos.

     - **View (Vista):** Es responsable de la presentación de los datos al usuario. En Django, las vistas son funciones o clases que procesan las solicitudes HTTP y devuelven respuestas, generalmente en forma de plantillas HTML.

     - **Controller (Controlador):** Maneja las interacciones entre el modelo y la vista, y responde a las acciones del usuario. En Django, el enrutador y las vistas funcionan juntos como el controlador, enrutando las solicitudes entrantes a las vistas apropiadas para su procesamiento.

  2. **Template-View (TV):**
El patrón Template-View se basa en la separación de la lógica de presentación (HTML) de la lógica de la aplicación (Python).

     - **Template (Plantilla):** Representa la capa de vista en la que se definen las interfaces de usuario utilizando HTML y otras tecnologías de frontend como CSS y JavaScript. En Django, las plantillas permiten incrustar lógica del lado del servidor y datos dinámicos utilizando etiquetas y variables específicas.

     - **View (Vista):** Representa la capa de control en la que se define la lógica de la aplicación utilizando funciones o clases en Python. Las vistas procesan las solicitudes HTTP, interactúan con el modelo (base de datos) y renderizan las respuestas utilizando plantillas.

  3. ORM (Object-Relational Mapping):
ORM es un patrón que permite interactuar con una base de datos relacional utilizando objetos y clases en lugar de escribir consultas SQL directamente.

     - En Django, el ORM se utiliza para definir modelos (clases de Python) que representan tablas en la base de datos. Estos modelos permiten realizar operaciones CRUD (Crear, Leer, Actualizar, Borrar) en la base de datos utilizando métodos de objeto en lugar de sentencias SQL.

     - El ORM de Django traduce automáticamente las operaciones de objetos Python en consultas SQL subyacentes, lo que simplifica el desarrollo y hace que el código sea más legible y mantenible.

Este proyecto proporciona a los usuarios una forma conveniente de realizar copias de seguridad de archivos importantes, almacenarlos de forma segura en la aplicación y acceder a ellos cuando sea necesario. Está diseñado para ser fácil de usar, escalable y mantener.

### 🎥 VIDEO DE LOOM
https://www.loom.com/share/b7d1c617f8a746d694aab6db9a261fbc?sid=2cad5cea-4df6-4e6e-8e5e-1f86437afca7
