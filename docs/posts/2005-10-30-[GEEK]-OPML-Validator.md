---
title: "[GEEK] OPML Validator"
author: Pito Salas
date: 2005-10-30
---

I just came across [Dave Winer's](<http://www.scripting.com/>) new, [beta,
OPML Validator](<http://www.opml.org/2005/10/28#a85>), which is a welcome
development. While there is an [OPML spec](<http://www.opml.org/spec>), having
a validator too is a great, **pragmatic** , **concrete** way to give a big
thumbs up or down to a particular piece of XML From the very start
[BlogBridge](<http://www.blogbridge.com/>) has **supported OPML** for import
and export, as well as for various **internal** representations and
**communications**. We obviously have done our best to write valid OPML, as
best as we understood what that was.  Still, what trumps every theoretical
position on OPML validity are user cries of: "Hey, I can't import your OPML
into XXX", or "Hey, you fail to import my OPML, but YYY has no problem with
it." Our approach to this situation has been to follow what has been called
"Postel's Law" (which I also [learned from Dave Winer, ages
ago](<http://essaysfromexodus.scripting.com/postelsLaw>)): "Be liberal in what
you accept, and conservative in what you send." And this has worked **well**
so far, although there have been some sticky wickets that we've had to deal
with. You end up feeling like you are chasing your tail trying to accommodate
all the odd dialects. So, it's great that Dave has now put forward the OPML
validator. Running our stuff through it, we do quite well. [Click here
to](<http://validator.opml.org/?url=http%3A%2F%2Fwww.blogbridge.com%2Ftest.opml>)
see the results of running the validator against a [pretty big example of our
opml](<http://www.blogbridge.com/test.opml>).  There are just two errors, each
repeated multiple times:

>>

>>   1. _" An <outline> element with more than just a "text" attribute should
have a "type" attribute indicating how the other attributes are to be
interpreted." _

>>   2. _" An <outline> element should only have known attributes." _

>>

__ In each case we have specified **additional** attributes beyond the basic
ones. **Specifically** they are: rating, queryParam, queryType, tags,
tagsDescription, tagsExtended and icon. Some of those probably deserve to
become part of the core set, while others somehow will have to become part of
an extensibility model. We'll participate in the discussions as they develop.
More to come! Technorati Tags:
[blogbridge](<http://www.technorati.com/tag/blogbridge>),
[OPML](<http://www.technorati.com/tag/OPML>)


* **Link to site:** **[[GEEK] OPML Validator](None)**
