---
title: "[GEEKY] Twitter and Ruby on Rails"
author: Pito Salas
date: 2008-05-03
---

TechCrunch:

> "We’re hearing this from multiple sources: After nearly two years of
> [high](<http://www.techcrunch.com/2007/12/20/twitter-downtime-on-the-
> upswing/>) [profile](<http://www.techcrunch.com/2008/01/15/twitter-fails-
> macworld-keynote-test/>) scaling problems,
> [Twitter](<http://www.twitter.com/>) is planning to abandon Ruby on Rails as
> their web framework and start from scratch with PHP or Java (another
> solution is to stick with the Ruby language and move away from the Rails
> framework)." (from
> [TechCrunch](<http://www.techcrunch.com/2008/05/01/twitter-said-to-be-
> abandoning-ruby-on-rails/>))

Well you know I am a Ruby on Rails fan and often when I propose it I am asked
whether 'Rails will Scale'. Here are my quick thoughts:

  1. First of all, is the rumor true? See comment at the bottom of the post referenced above:   

> "**Update:** Regarding Evan Williams’ statement
> [here](<http://twitter.com/ev/statuses/801530348>), all I can say is that
> multiple sources claim that Twitter is telling people they are planning on
> moving away from Ruby on Rails. This is not the first time a company has
> denied something that has turned out to be 100% true."

  2. Twitter is at the extreme end of scalability challenges. It is a huge and incredibly fast growing system, so if anything would break scalability, it would be Twitter.
  3. No system of the scale of Twitter uses a single language of platform. I would be surprised if there's not a grab bag of PHP, Java, C, SQL stored procedures and other technologies in the overall architecture. So the notion of 'abandoning Rails for Java' doesn't really make much sense anyway.
  4. Most important: Designing, building and operating a system to achieve good performance at Twitter scale is really really hard no matter what language or framework you use. Using Java or PHP or C# or whatever you like doesn't change this basic fact. Consequently changing language of framework would not be a likely cure for a scaling problem.


* **Link to site:** **[[GEEKY] Twitter and Ruby on Rails](None)**
