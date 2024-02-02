---
title: "[GEEK] The BIG LIE of certificate checking"
author: Pito Salas
date: 2005-05-02
---


>>

>>
[![](https://i0.wp.com/s3.media.squarespace.com/production/1075723/12829350/weblogs/archives/Screenshot-1.png?resize=250%2C250)](<https://i0.wp.com/s3.media.squarespace.com/production/1075723/12829350/weblogs/archives/Screenshot-1.png>)Maybe
you've read or heard my rants about what has become known as the "Scary Dialog
Box" that users see when the run a Java application without a valid
certificate.

>>

>> And if you have used BlogBridge, you will have seen it and many of you have
asked what the heck it means, and I am sure many more have chosen not to run
BlogBridge because of it.

>>

>> Sun has heard this complaint from many many people and is now trying to fix
the problem, by introducing this new alternative dialog box to report the same
thing. There's a post and a thread about this
[here](<http://weblogs.java.net/blog/stanleyh/archive/2005/04/deployment_good_1.html>).
Here's what you see if your application is signed with a verified certificate:

>>

>>
[![](https://i0.wp.com/weblogs.java.net/blog/stanleyh/archive/goodbye_scary_dialog_box/security_warning_self_signed.jpg?resize=250%2C250)](<https://i0.wp.com/weblogs.java.net/blog/stanleyh/archive/goodbye_scary_dialog_box/security_warning_self_signed.jpg>)

>>

>> Is this an improvement? **Yes**.

>>

>> Is it good enough? **No!**

>>

>> IMHO the whole idea of using certificates to sign applications is fatally
flawed. It provides illusory security.

>>

>> As a small developer, all I have to do to make it go away is to spend some
number of hundreds of dollars to get a certificate from Verisign or one of the
many other CAs. When I do this, the message then becomes this:

>>

>>
[![](https://i0.wp.com/weblogs.java.net/blog/stanleyh/archive/goodbye_scary_dialog_box/security_warning_signed.jpg?resize=250%2C250)](<https://i0.wp.com/weblogs.java.net/blog/stanleyh/archive/goodbye_scary_dialog_box/security_warning_signed.jpg>)

>>

>> How is the user any more secure?

>>

>> Any malware developer could do the same thing. Of course they are smart
enough so their company name wouldn't show up as **" Malware Developer"** and
the application wouldn't be called ** "Big Bad Virus."**

>>

>> How is the user to know?

>>

>> So my problem with this whole signed application certificate thing is that
it gives the user a **very false sense of security.**

>>

>> Technorati Tags: [java](<http://technorati.com/tag/java>),
[security](<http://technorati.com/tag/security>),
[webstart](<http://technorati.com/tag/webstart>)


[[GEEK] The BIG LIE of certificate checking](None)
