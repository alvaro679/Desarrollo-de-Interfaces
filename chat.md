## Arquitectura
* **Cliente (Python):** Utiliza Sockets. PSP (Programación de Servicios y Procesos).
* **Protocolo:** TCP - IP.
* **Servidor (Java):** PSD (Programación de Servicios y Procesos).
* **Características:** SRV Java, Socket, Cripto, Multihilo.



---

## Definición

| Requisitos | Funcionalidades (Capacidades) | No Funcionales (Tecnologías) |
| :--- | :--- | :--- |
| "Briefing" | Enviar mensajes | Srv (Servidor) -> Java |
| Estado del Usuario | Recibir mensajes | Cliente -> Python / QtDesigner / Pyside6 |
| Reenvío de Mensajes | ¿Documentos? 3° | |
| Stickers | Registro horario Mensajes | |
| Responder a Mensajes | ¿Visto mensaje? 3° | |
| Biblioteca de Docs | - Usuarios | |
| | - Grupos 2°/3° | |
| | - Filtro Búsqueda 3° | |

### Requisitos funcionales mínimos
* Encriptados
* Enviar
* Recibir
* Registro horario
* Usuarios

---

## Esquema de Mensaje
* **Formato:** `Timestamp + usuario + "Mensaje"`
* **Timestamp:** `AAAA MM DD HH MM SS`

### Diagrama de flujo
Una entrada de datos que pasa por un bloque de **"Cripto"** y sale como un **"Pay load"**.

---

## Tareas
- [ ] Investigar Cripto.
- [ ] Investigar Sockets Python.
- [ ] Mockup Interfaz.
- [ ] Diagrama de clases (Cliente / Servidor).
- [ ] Interfaz QTDesign.
- [ ] Servidor multihilo.
- [ ] Cliente Python con Sockets.
- [ ] Interfaz señales + slots.
- [ ] Documentación.
