---
title: "[GEEKY] REST and the PATCH verb"
author: Pito Salas
date: 2011-05-23
tags:
    - GEEKY
    - http
    - patch
    - post
    - put
---

**Link: [[GEEKY] REST and the PATCH verb](None):** ""



Last year when teaching [REST](<http://www.packetizer.com/ws/rest.html>)
concepts at Brandeis University I proved the truism that there's no better way
to learn about something than to try and teach it. We (all) wrapped ourselves
around the axle trying to understand HTTP "PUT" versus HTTP "POST" and learned
new english words like Idempotency. I won't go into the whole story because
it's kind of long.

**< gross simplification>** But one of the keys ideas that is tricky to
understand is the difference between PUT and POST in REST as it is implemented
using HTTP. PUT replaces a specific resource (think of it as a record for a
specific key) while POST creates a new resource. **< /gross simplification>**

So I was interested to see that there's a move afoot (no idea how serious this
will turn out to be) to add a new verb to HTTP/REST, to change an existing
resource - not replace it like PUT does, or add a whole new one like POST
does, but change one or more parts of it. In effect, it "Patches" it. Seems
like a useful idea

[Here's the draft RFC change](<http://greenbytes.de/tech/webdav/draft-
dusseault-http-patch-11.html#rfc.section.2.1>)


