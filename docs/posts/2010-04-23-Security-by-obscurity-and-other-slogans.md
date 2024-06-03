---
title: "Security by obscurity and other slogans"
author: Pito Salas
date: 2010-04-23
tags:
    - google
    - security
---

If you've been in computing for any time you may have been hit over the head
by the slogan "Security by Obscurity is No Security". As I have understood the
argument it has a few components:

  1. If your security relies on secret tricks, trap doors, and a hope that no one will be able to find out or guess the work around, then you're fooling yourself. Sooner or later someone will be able to guess the trick, see the code, quit your company and take the secret with them.
  2. Allowing your code and methods to be inspected and analyzed by the public (bad guys included) is the only way to learn about weaknesses that you would be blind to and give you a chance to close them. The other slogan which I will tackle some other time is "All bugs are shallow to a thousand eyes" implying that no matter how subtle the weakness, if you allow lots and lots of people to look, they will find them all.

(Actually Wikipedia has a longer and probably more [correct summary of the
Security By Obscurity
concept](<http://en.wikipedia.org/wiki/Security_through_obscurity>).)

In the past I was **usually quickly persuaded** or at least silenced when
confronted with these arguments, although at a gut level it never really sat
right with me. While the arguments are strong, I had an vague sense that
obscurity in fact does help security and often is a useful part of the whole
security story. But who was I to argue?

With that background I was interested to see an article in the New York Times
the other day, "[Cyberattack on Google Said to Hit Password
System](<http://www.nytimes.com/2010/04/20/technology/20google.html>)":

> "[snip…]But a person with direct knowledge of the investigation now says
> that the losses included one of Google’s crown jewels, a password system
> that controls access by millions of users worldwide to almost all of the
> company’s Web services, including e-mail and business applications. The
> program, code named Gaia for the Greek goddess of the earth, was attacked in
> a lightning raid taking less than two days last December, the person said.
> Described publicly only once at a technical conference four years ago, the
> software is intended to enable users and employees to sign in with their
> password just once to operate a range of services.[snip…]" (from **New York
> Times** , "[Cyberattack  
>  on Google Said to Hit Password
> System](<http://www.nytimes.com/2010/04/20/technology/20google.html>)")

This got me thinking, **where is the Security By Obscurity crowd now**? If you
read the whole article you see that there is considerable concern at Google
about the fact that the operation of this single sign-on, security system has
been revealed.

Not that passwords or digital certificates were compromised, but (apparently)
just the operation or algorithm or code for it was compromised. Isn't this
**just** security by obscurity?

It makes perfect sense to me that these are state secrets for Google and that
it's considered a major breach.


* **Link to site:** **[Security by obscurity and other slogans](None)**
