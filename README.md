#  AutoExec Suite

AutoExec Suite es una **herramienta de automatización de escritorio** diseñada para **simplificar y optimizar los flujos de trabajo repetitivos a través de la automatización de secuencias de acciones** en la interfaz de usuario.

Esta suite permite a los usuarios **crear, editar y ejecutar secuencias de acciones** como clics del ratón, entradas del teclado, y otras interacciones con la interfaz gráfica de usuario, **sin necesidad de escribir código.**

## Propósito

El propósito principal de AutoExec Suite es **proporcionar a los usuarios una manera eficiente y accesible de automatizar tareas rutinarias** en el escritorio, **mejorando la productividad** y reduciendo el potencial de error humano.

Desde la automatización de procesos de software, hasta la gestión de datos y la navegación web, AutoExec Suite está **diseñada para adaptarse a una amplia gama de aplicaciones y flujos de trabajo**, haciendo que la automatización esté al alcance de usuarios con y sin experiencia técnica.

## Funcionalidades

AutoExec Suite ofrece una variedad de características para facilitar la creación de secuencias de automatización personalizadas:


- **Añadir click automático:** permite simular clics del ratón en puntos específicos de la pantalla, útil para interactuar con aplicaciones y sitios web.
- **Añadir click izquierdo/derecho:** ofrece la posibilidad de añadir clics izquierdos o derechos en cualquier pixel que puedas enfocar con el puntero del ratón.
- **Añadir doble click:** simula doble clics para acciones que lo requieran, como abrir archivos o aplicaciones.
- **Añadir pausa:** introduce pausas entre acciones, permitiendo esperar a que carguen aplicaciones, páginas web, menús y submenús, etc.
- **Añadir entrada de teclado:** automatiza la entrada de teclas simples, facilitando la navegación y entrada de datos.
- **Añadir combinación de teclas:** permite ejecutar combinaciones de teclas para acciones como copiar y pegar.
- **Añadir texto:** simula la escritura de cadenas de texto completas, útil para completar formularios, generar documentos o navegación web.
- **Añadir número autoincremental:** genera números secuenciales, ideal para crear series de nombres de archivo o datos.
- **Añadir texto estático con fecha y hora:** crea cadenas de texto que incluyen la fecha y hora actuales, perfecto para nombrar archivos de manera única y organizada.

## Contribuir

Este proyecto se desarrolló como una **solución personal a la necesidad de automatizar tareas repetitivas** en mis sistemas, pero estoy abierto a sugerencias, mejoras y contribuciones que puedan hacer de esta herramienta **aún más útil y robusta.**

Si deseas contribuir al proyecto, por favor lee **CONTRIBUTING.md** para obtener más información sobre cómo hacerlo.

## Licencia

Este proyecto se encuentra bajo la **Licencia GPL3** - ver el archivo LICENSE para más detalles.

## Instalación y uso

Sigue estos pasos para instalar y configurar la aplicación en tu entorno local.

### Prerrequisitos

Asegúrate de tener Python instalado en tu sistema. Esta aplicación ha sido testeada con Python 3.11.2.

### Clonar el Repositorio

Primero, clona el repositorio a tu máquina local utilizando Git:

```bash
git clone https://github.com/dreykdrk7/autoexec-suite.git
cd autoexec-suite
```

### Instalar Dependencias

Luego, instala las dependencias necesarias para ejecutar la aplicación (se recomienda hacerlo en un entorno virtual, pero **_esta guía no está orientada a explicarte sobre entornos virtuales_**):

```bash
pip install -r requirements.txt
```

### Guía de Uso

Para utilizar la aplicación, ejecuta `autoexec.py` desde la terminal. 

```bash
python autoexec.py
-
python3 autoexec.py
```

### Ejecución Directa de Secuencias

Además de la creación de secuencias a través de su interfaz de usuario, AutoExec Suite permite a los usuarios **cargar y ejecutar secuencias predefinidas** directamente desde la línea de comandos, proporcionando una manera rápida y conveniente de automatizar tareas al iniciar la aplicación:

```bash
python autoexec.py --file nombre_del_archivo_de_secuencia --n número_de_iteraciones
```

Donde `nombre_del_archivo_de_secuencia` es el nombre del archivo que contiene tu secuencia y `número_de_iteraciones` es la cantidad de veces que deseas que se repita la secuencia.
