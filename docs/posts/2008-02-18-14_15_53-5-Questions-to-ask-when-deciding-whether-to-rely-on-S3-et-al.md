---
title: "5 Questions to ask when deciding whether to rely on S3 et al"
author: Pito Salas
date: 2008-02-18 14:15:53
---


Several products I've worked on recently have relied on Amazon's really
impressive web services. I've written before about how much [I admire services
such as S3 and EC2, solid, commercial quality infrastructure
services](</2008/01/11/rumorville-microsoft-amazon/>).

They address (and? or? solve) a big problem that application builders have:

> "How many servers will I need, how many users will I have, how much storage
> will I need … and in the end, how much will all that cost?".

They solve this by offering key components of infrastructure as a "software as
a service", SAAS. Starting with permanent storage, which is delivered by S3,
followed by [computes or servers, delivered by
EC2](<http://www.amazon.com/b/ref=sc_fe_l_2?ie=UTF8&node=201590011&no=3435361&me=A36L942TSJ2AJA>),
and further followed by a growing variety of other infrastuctural services.

Let's look at what questions to ask when deciding to use any of these
services. For example, when deciding to depend on [Amazon's S3 storage
service](<http://www.amazon.com/S3-AWS-home-page-
Money/b/ref=sc_fe_l_2?ie=UTF8&node=16427261&no=3435361&me=A36L942TSJ2AJA>)
(delivered over the internet, no hardware required) **instead of** buying a
series of file and database servers (hardware) you need to consider the trade-
offs:

  1. Given my expected growth, what is the comparable cost?

  2. What are my options in each case if my growth doesn't actually develop as I expect?

  3. What is the comparable performance?

  4. What is the comparable reliability?

  5. If the whole scheme doesn't work out, how hard is it to switch?

You see that you end up with a fairly tricky decision matrix. More tomorrow on
how I solved this dilemma.


