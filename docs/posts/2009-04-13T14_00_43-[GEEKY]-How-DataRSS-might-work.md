---
title: "[GEEKY] How DataRSS might work"
author: Pito Salas
date: 2009-04-13T14:00:43
tags:
    - api
    - datarss
    - followthemon-tagey
    - rest
    - sunlightfoundation-tag
    - webservices
---



**Editors Note (that 's me, Pito): I've decided to change the name of this
thing to "Decentralized Data Discovery - DDD" because I learned from more than
one person that calling it Data RSS was misleading and confusing. I need to go
back and update the papers and blog posts.**

I've just finished writing part 3 of my series about DataRSS. [Part 1 gives
the background and justification for the
concept](<http://www.scribd.com/doc/12866121/Data-Rss>), and [Part 2 worked
through a semi-believable scenario where having DataRSS would be a good
thing.](<http://www.scribd.com/doc/13583957/DataRSS-Case-Study>)

In part 3 I try to get into more technical detail. I hope that you take the
time to read it because that's the only way I will get technical feedback on
it. The reason I wrote the first two parts is that realistically I expect to
lose 99.5% of you guys once you open up part 3. That's why this post is
labeled [GEEKY]. Here's some of what I cover in part 3:

> "Data RSS is a simple protocol and a simple data format. It can be
> implemented in any programming language.
>
> Importantly, the Publisher and Accessor software need not know (can not
> know) what language the _counterparties_ software is written in. " (
> **from** [DataRSS: Technical
> Overview](<http://www.scribd.com/doc/14136777/DataRss-Tech-Overview>))

and

> "DataRSS is used between two parties, the **Publisher** , who ‘owns’ some
> data, and the **Accessor** , who wants to use that data. Publisher and
> Accessor are organizations with people in them. The Publisher wants to offer
> a technical means to allow an application program simple and standardized
> access to their data.
>
> The Accessor wants to write an application program that accesses and does
> something useful with data coming from any Publisher. Accessor and Publisher
> don’t know each other. " ( **from** [DataRSS: Technical
> Overview](<http://www.scribd.com/doc/14136777/DataRss-Tech-Overview>))

**Delicious** isn't it? One final tease, I also have worked out some detailed
examples of how DataRSS might work with the [New York Times
API,](<http://open.blogs.nytimes.com/>) with the [Sunlight Foundation
API](<http://www.sunlightfoundation.com/>) and with the [Follow The Money API.
](<http://www.followthemoney.org/>)


