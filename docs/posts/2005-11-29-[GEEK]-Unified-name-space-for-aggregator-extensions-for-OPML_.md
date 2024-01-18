---
title: "[GEEK] Unified name space for aggregator extensions for OPML?"
author: Pito Salas
date: 2005-11-29
---


>>

>> There's
[been](<http://nick.typepad.com/blog/2005/11/an_attention_na_1.html>) a
[lot](<http://www.feedblog.org/2005/11/opml_attention_.html>) of
[discussion](<http://blogs.msdn.com/alexbarn/archive/2005/11/23/496170.aspx>)
(follow these links for more links) of late about how to **extend OPML** ,
including [what I
wrote](<http://www.blogbridge.com/archives/2005/11/geek_preliminar.php>) about
some common **aggregation related** OPML attributes. From reading the
discussions and thinking about it, I am thinking that a course correction
might be better. Much of the discussion has been about an [Attention namespace
for OPML](<http://nick.typepad.com/blog/2005/11/an_attention_na_1.html>). I
totally **support** this and will participate in that discussion.

>>

>> **Yet** there are clearly some information that many aggregators need to
store with the OPML, which is not part of the core OPML standard, and also not
really connected to Attention.

>>

>> Faced with this question an aggregator developer can do one of several
things:

>>

>>   * They can just create a product specific namespace (e.g. blogbridge:
xxx)

>>

>>   * Or they can just include regular non namespace attributes in their OPML
(which will in turn cause either the validator or other aggregators to choke.)

>>

>>

>>

>> What if instead we try to define a **general set** of **a** ggregator **r**
elated **e** xtensions (are:xxx) to OPML? We could do an informal canvas and
try to figure out a small set of really obvious attributes to put into this
ARE name space.

>>

>> To start you thinking about this, here is a collection of attributes
derived from what BlogBridge and FeedDemon each store in their OPML. I've
identified two sets of attributes:

>>

>> The following have to do with bookkeeping and the operation of the
aggregator:

>>

>>   * are:autoPurgeMaxitems - number of items that should be stored locally

>>

>>   * are:autoUpdateFrequency - how often this feed polled

>>

>>   * are:numUnread - number of items currently unread

>>

>>   * are:numFlagged - number of items currently flagged

>>

>>   * are:numVisits - How often a user has visited this feed

>>

>>   * are:firstPostDate - Date of the first post

>>

>>

>>

>> And the following have to do with local user overrides of information that
can also be specified in RSS.

>>

>>   * are:userRating - user supplied rating of how 'good' this feed is

>>

>>   * are:userTitle - user supplied override to the title or name of this
feed

>>

>>   * are:userCreator - user supplied override to the creator of this feed

>>

>>   * are:userDescription - user supplied override to the description of this
feed

>>

>>

>>

>> I'm sure these are already too many. My top level question to those of us
responsible for OPML import and export within Aggregators of all kinds, what
do you think? **Shall we try to do this**? Is it a good idea? Or shall we all
just create our little parochial namespaces with different words for the same
thing?

>>

>> Technorati Tags: [blogbridge](<http://www.technorati.com/tag/blogbridge>),
[feeddemon](<http://www.technorati.com/tag/feeddemon>),
[OPML](<http://www.technorati.com/tag/OPML>)


