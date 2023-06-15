from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Paquete para mejorar los prints'
LONG_DESCRIPTION = 'Paquete para mejorar los prints'

# Configurando
setup(
        # el nombre debe coincidir con el nombre de la carpeta 	  
        #'modulomuysimple'
        name="colors", 
        version=VERSION,
        author="José Huerto",
        author_email="jhuertom@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # añade cualquier paquete adicional que debe ser
        #instalado junto con tu paquete. Ej: 'caer'
        
        keywords=['python', 'colors'],
        classifiers= [
            "Programming Language :: Python :: 3"
        ]
)