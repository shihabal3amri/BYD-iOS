# BYD iOS traducido · Beta pública

La aplicación china de BYD para iPhone con inglés, árabe, ruso, español y chino simplificado. Incluye actualizaciones de traducciones, pestañas personalizables, widgets y desbloqueo por proximidad opcional. El español sigue en revisión.

[Descargar IPA · 351 MB](https://shihabal3amri.github.io/BYD-iOS/es/) · [Notas y sumas de verificación](https://github.com/shihabal3amri/BYD-iOS/releases/tag/v9.16.0-r6)

## Novedades de la Revisión 6: idiomas y traducciones

Añade español y chino simplificado, descargas firmadas de traducciones y correcciones en ajustes, diálogos y títulos de accesos rápidos. En **Ajustes → Traducciones** puedes actualizar manualmente; las actualizaciones automáticas están desactivadas por defecto. Cierra completamente BYD y vuelve a abrirla para aplicar los cambios.

Selecciona **Keep App Extensions** al instalar. Abre BYD unos 30 segundos después de actualizar y añade los widgets desde la galería. Los widgets siguen el idioma elegido, pero sus traducciones siguen incluidas en el IPA.

BYD incluye cuatro extensiones: en total usa cinco identificadores de aplicación. Revisa los disponibles en AltStore → My Apps → View App IDs. [Más información sobre el límite.](https://faq.altstore.io/altstore-classic/app-ids)

## 1. Configura AltStore Classic

Si ya tienes AltStore Classic, continúa al siguiente paso. Si no, instala **AltServer en tu ordenador** y úsalo para instalar **AltStore Classic en el iPhone**. Usa tu propia cuenta de Apple; no necesitas una suscripción de desarrollador de pago. Activa el modo de desarrollador en iOS 16 o posterior.

[Guía para macOS](https://faq.altstore.io/altstore-classic/how-to-install-altstore-macos) · [Guía para Windows](https://faq.altstore.io/altstore-classic/how-to-install-altstore-windows)

## 2. Instala o actualiza BYD

1. Toca **Añadir a AltStore Classic** y confirma que deseas añadir la fuente.
2. Busca **BYD Localized** en AltStore, revisa los permisos e instala con tu cuenta de Apple. Cuando se te pregunte, selecciona **Keep App Extensions** para conservar las extensiones.
3. Abre BYD e inicia sesión con tu cuenta. En **Yo → Ajustes** puedes elegir el idioma y las pestañas inferiores.

**¿Ya está instalada?** Actualiza la fuente de AltStore y selecciona **Update** en **My Apps**. Busca **9.16.0 · Revisión 6**. Conserva la aplicación y usa la misma cuenta de Apple para mantener los datos locales.

Mantén AltServer abierto y accesible por la misma red Wi-Fi o por USB al instalar, actualizar o renovar la firma. Con una cuenta gratuita, renueva AltStore y BYD antes de que caduque la firma de siete días. La descarga ocupa unos 351 MB; la velocidad depende de tu conexión con GitHub.

Si el botón no abre AltStore, añade esta dirección en **Browse → Sources → +**:

`https://raw.githubusercontent.com/shihabal3amri/BYD-iOS/main/source.json`

## Instalación con Impactor

Importa el IPA en [Impactor](https://github.com/claration/Impactor), mantén **BYD** como nombre y conserva todas las extensiones de widgets. Firma e instala con tu propia cuenta de Apple.

Si aparece **Developer API error 35** relacionado con **appIdName**, establece BYD como nombre y vuelve a intentarlo con el mismo IPA. Mantén la gestión predeterminada del identificador y de los grupos. Descargar el IPA no lo instala.

## Desbloqueo por proximidad · Beta opcional

Abre **Yo → Ajustes → Desbloqueo por proximidad**. Usa tu llave Bluetooth BYD ya activada para desbloquear al acercarte y, opcionalmente, bloquear al alejarte. Las acciones automáticas, ubicación, movimiento y registros están **desactivados por defecto para usuarios nuevos**. Se conservan los ajustes guardados de quienes ya lo probaban.

1. Comprueba primero el bloqueo y desbloqueo Bluetooth normales. Abre **Elegir distancias**, mide ambas posiciones llevando el teléfono como de costumbre y guarda. Las acciones automáticas se pausan durante la calibración.
2. Activa **Desbloqueo por proximidad** y, si quieres, **Bloquear al alejarse**. Empieza lejos, acércate, aléjate y comprueba la respuesta real del coche. Calibra cada teléfono por separado.
3. Para usarlo con la pantalla bloqueada, abre **Detección en segundo plano → Soporte de ubicación**, sigue los permisos y permite la ubicación en segundo plano cuando se ofrezca. Las **pistas de movimiento** son opcionales y requieren permiso de actividad física. Abre BYD de nuevo tras reiniciar el teléfono o forzar el cierre.

El soporte en segundo plano puede aumentar el consumo de batería; no se garantiza funcionamiento continuo ni durante toda la noche. Esta función procesa la ubicación en el teléfono sin guardar ni subir coordenadas. Otras funciones de ubicación de BYD tienen sus propios ajustes.

**Problema conocido en un XS:** se observaron señales inconsistentes y se informó de un desbloqueo involuntario desde el interior de un edificio. Persistió tras actualizar a iOS 18.7.10. La causa no está resuelta y no se ha demostrado un fallo de hardware. Si las lecturas se solapan o hay acciones involuntarias, desactiva la función e informa del problema.

Para enviar comentarios, activa los registros antes de probar, marca los momentos relevantes y exporta al terminar. Incluye teléfono/iOS, modelo de coche, umbrales, estado de pantalla y respuesta real. Revisa los registros antes de compartirlos.

## Beta pública · Revisión 6

Las actualizaciones firmadas se probaron en iPhone X y Android. El adaptador de accesos rápidos superó 145 comprobaciones con objetos UIKit reales y los controles de regresión existentes pasaron. La instalación de este paquete de producción concreto en un iPhone sin jailbreak aún no está verificada.

Requiere iOS 15 o posterior. El español sigue en revisión. Algunos contenidos e imágenes permanecen en chino. Las traducciones de widgets se distribuyen con la aplicación. El problema de proximidad observado en un XS sigue sin resolverse; el perfil puede aparecer en blanco.

## Notas y sumas de verificación

`BYD-iOS_9.16.0_r6.ipa`

SHA-256: `9264280e225c61d1a115211433aa10e9b37aec5d4f94bc6fd7ae446aab36ec04`

## Recibe novedades

Suscríbete a nuestro canal de Telegram y activa las notificaciones para enterarte de nuevas versiones.

[Suscribirse en Telegram](https://t.me/byd_localized)

Proyecto no oficial, sin afiliación ni respaldo de BYD. La aplicación y los recursos originales pertenecen a sus propietarios. No se garantizan funciones restringidas por Apple como llaves Wallet, notificaciones push o integración con Siri. Esta es una fuente de AltStore Classic, no de AltStore PAL.
