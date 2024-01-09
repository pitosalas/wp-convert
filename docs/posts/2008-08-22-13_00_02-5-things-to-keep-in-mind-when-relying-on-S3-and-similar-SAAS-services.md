---
title: "5 things to keep in mind when relying on S3 and similar SAAS services"
author: Pito Salas
date: 2008-08-22 13:00:02
---


On a project I worked on recently, I asked myself whether I should make one or
more of Amazon's awesome web services (AWS - Awesome Web Services) a mission
critical part of the infrastructure of the product. I wrote yesterday about
the [considerations that go into deciding to rely on services like Amazon's
web services as key infrastructure components](</2008/02/18/about-amzn-and-
cloud-computing/>).

Of the five I mentioned, these two considerations were especially confusing to
me:

  * What is the comparable reliability?

  * If the whole scheme doesn't work out, how hard is it to switch?

**On the one hand** , the reliability of running a bunch of servers in a data
center is fairly well understood, as well as the contingency plans to deal
with hardware and software failures.

**On the other hand** (using S3, the storage service as an example,) the
expected reliability is more or less unknown - although preliminary data is
highly positive - and S3 is the only service of it's kind, so that there is a
certain unavoidable amount of lock in.

I expressed that as the rhetorical question,

> _" Do I really want to entrust a business critical function to another
> company - if they decide to shut me off, my business is dead in the water."_

Sounds **ominous** , doesn't it?

But **wait** , I entrust running my servers to a hosting service, don't I? If
they shut me off I am kind of dead in the water too, aren't I? What's the
difference?

### Relying on your hosting provider for ping & power has a different risk
profile than relying on a SAAS provider for disk & cpu in the cloud

Here's why I say that:

  1. There are many many hosting providers (ISPs) to providing ping & power. It's a vibrant and competitive space.

  2. We understand them well. We understand their services, their pricing, their terms of service.

  3. They generally rely mostly on a well known and understood set of technologies, interfaces, software and hardware.

  4. It is feasible to switch from one to another.

  5. It is also feasible (and many do) to have parallel relationships with two totally different hosting services so if one shuts down, crashes, goes out of business, or whatever, you can seamlessly switch to the other.

_Originally posted on Feb 19, 2008. Reprinted courtesy of ReRuns plug-in._


