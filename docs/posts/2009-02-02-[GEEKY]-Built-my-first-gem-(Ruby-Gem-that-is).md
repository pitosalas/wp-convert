---
title: "[GEEKY] Built my first gem (Ruby Gem that is)"
author: Pito Salas
date: 2009-02-02
tags:
    - api
    - free
    - gov
    - opensource
    - rest
    - ruby
    - sdk
    - sunlight
    - time
---

**Link: [[GEEKY] Built my first gem (Ruby Gem that is)](None):** ""



I've gotten interested in what is going on in the public sector, in particular
in the world of non profits. I've learned a lot, met many people and been
trying to define a project that would at the same time do something to better
the world as be an interesting and fulfilling product challenge (notice,
missing from that list is "make a lot of money")

I want to start posting some of the cool things I am figuring out but so far I
haven't because I can't really figure out how to organize it.

One area that I have immersed myself into is the many diverse groups who are
doing work promoting government openness and transparency by, among many other
things, creating the technical bridges to allow information that is already
being collected to be more easily accessible. There are many of them, and one
of them is the [Sunlight Foundation](<http://www.sunlightfoundation.com/>).
They are doing some really cool work, both themselves, and sponsoring and
granting others who share their goals.

Wow what a long wind-up.

Anyway, in digging deeply into their APIs and datasets I decided to learn by
doing and created a Ruby Gem called
[govsdk](<http://github.com/pitosalas/govsdk/tree/master>) with the following
goals:

  * A simple and consistent sdk to all the various government (federal, state and local) APIs available.

  * Totally hide from the user of the SDK what those APIs are, what the networking and REST pieces are. Instead provide classes which represent the natural domain objects and behind the scenes accesses appropriate datasets and APIs.

  * Identify the 'current' best APIs for the various facts and figures so that the user need not do the work to learn each of the organizations and data models. When new ones come online or change, hide that as well.

  * Provide all this in an open source library, for free, with example code, documentation and test suites.

Version 0.0.1 of the GovSdk GEM (0.0.1 -- get the idea?) is implemented and
available at [GovSdk](<http://github.com/pitosalas/govsdk/tree/master>). Check
it out, but expect it to change because this is still quite embryonic.


