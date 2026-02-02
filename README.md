# termsg_without_cert

**Termsg** es un chat de terminal escrito en Python que funciona sobre TCP.
Esta versión **NO utiliza cifrado**, y se incluye un **sniffer externo** para
demostrar cómo los mensajes pueden ser interceptados en texto plano.

⚠️ **Proyecto con fines educativos**: redes, TCP, sniffing y seguridad.

---

## 🚀 Cómo funciona

- Protocolo: **TCP**
- Puerto por defecto: **8443**
- Cifrado: ❌ Ninguno (texto plano)
- Codificación: UTF-8

Los mensajes viajan directamente por TCP, lo que permite:
- Verlos en Wireshark
- Capturarlos con Scapy
- Analizar riesgos reales de no usar TLS

---

## 🖥️ Requisitos

- Python **3.10+**
- Windows / Linux
- Permisos de administrador para el sniffer

---

## 📦 Dependencias
Solo necesarias para el sniffer:
```
python -m pip install scapy
```

---

## ▶️ Uso
Ejecutar el servidor
```
python server.py
```
Introduce el nombre de la sala cuando se te pida.

Ejecutar un cliente
```
python client.py <ip_server>
```

Ejecutar el sniffer (en otra terminal)
⚠️ Debe ejecutarse como **administrador**
```
python sniffer.py
```
Verás los mensajes del chat en tiempo real:

![image](https://github.com/nestoree/termsg_without_cert/blob/main/images/snif_no_cert.png)

---

## 🧠 ¿Por qué no hay cifrado?
Esta versión está pensada para:

- Aprender cómo viajan los datos realmente
- Entender por qué TLS es importante
- Comparar tráfico cifrado vs texto plano

| Si buscas seguridad, revisa la versión con [TLS](https://github.com/nestoree/termsg).

---

## ⚠️ Aviso legal
Este software es solo para:

- Educación
- Pruebas en redes propias
- Aprendizaje de seguridad

**No** usar para interceptar tráfico sin permiso.

El autor **no** se hace responsable del uso indebido.

---

## 📜 Licencia

MIT License
