#Brute Force Tool for gpEasy CMS

Este script permite hacer fuerza bruta contra el panel de autenticación del CMS gpEasy (http://gpeasy.com/Demo)
Sin embargo en el momento el script funciona mas como una script para detectar usuarios válidos en el sistema, ya que por omisión el CMS cuenta con un control que bloquea el usuario por 10 minutos cuando hay mas de 5 intentos de ingreso de contraseñas incorrecto.

El script tiene en cuenta el cambio del parámetro "nonce", aunque todos entendemos que el nonce debería calcularse en cada
intento de autenticación, la implementación del CMS lo cambia cada 10 minutos.

###Ejemplo de uso:

```python
> python bfgpEasy.py
[nonce]:b27d72935f
Testing Usuario: admin...
Testing Usuario: Admin...
Testing Usuario: test...
Testing Usuario: user...
Testing Usuario: whatsapp...
Testing Usuario: trytohackme...
Testing Usuario: 4dm1n...
[Usuario existe y esta bloqueado]:4dm1n
Testing Usuario: gpeasy...
Testing Usuario: gpleasy...
Testing Usuario: login...
>
```

Este script se desarrolló durante la solución de un reto propuesto por @4v4t4r en la comunidad Hacklab-Medellín (http://www.hacklabmedellin.org/) - meetup.com/HackLab-Medellin/

Contribuciones bienvenidas.

TODO:

-Bypass el bloqueo por intentos
-Buscar otra forma de autenticar el usuario (hashes?)

