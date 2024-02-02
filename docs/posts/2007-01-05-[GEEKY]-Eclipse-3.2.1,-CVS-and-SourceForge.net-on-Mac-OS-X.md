---
title: "[GEEKY] Eclipse 3.2.1, CVS and SourceForge.net on Mac OS X"
author: Pito Salas
date: 2007-01-05
---


>
> If you need this tip, it will save you a lot of time. 99% likely though, you
> don't need it and it will read as complete gibberish. But I feel compelled
> to share it because it's totally obscure and I just spent 2 hours trying to
> figure it out.
>
> Problem:
>
>   * Eclipse 3.2.1 just ceased to be able to grab code from SourceForge.net
> via CVS. It would give an error: "Invalid argument or cannot assign
> requested address"
>
>

>
> Configuration
>
>   * Eclipse for using CVS on SourceForge requires ExtSSH (which means, use
> the Eclipse bundled SSH client, rather than some other utility that you have
> on your computer -- don't ask.)
>   * Mac OS X, 10.4.9, all patches applied
>   * Eclipse: 3.2.1 - brand new download

>
> Solution:
>
>   * In Mac OS X Network settings, TCP/IP, make sure that IPv6 is configured
> and shows an IPv6 Address.
>

>
> Thanks for listening.


[[GEEKY] Eclipse 3.2.1, CVS and SourceForge.net on Mac OS X](None)
