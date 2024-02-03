---
title: "[GEEK] Getting URL objects to time out"
author: Pito Salas
date: 2004-06-10
---


>>

>> For some reason, it is not possible to get at the Socket object that the
URL object uses for its network I/O. And so, on the face of it, you can't set
or change the time-out time. However here are two, semi-kludge properties that
Sun has provided us to overcome that deficiency:

>>

>> System.setProperty("sun.net.client.defaultReadTimeout", "10000");  
> System.setProperty("sun.net.client.defaultConnectTimeout", "10000");


* **Link to site:** **[[GEEK] Getting URL objects to time out](None)**
