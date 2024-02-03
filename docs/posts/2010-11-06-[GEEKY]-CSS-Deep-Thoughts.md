---
title: "[GEEKY] CSS Deep Thoughts"
author: Pito Salas
date: 2010-11-06
---



I feel that I am finally mastering CSS and in doing so I am seeing some
interesting patterns. It seems to me that it's very easy to get into a
situation where you have too many CSS rules that overlap and override each
other in ways that are more complex than necessary.

It seems like there could and should be a tool to 'simplify' or 'clean up' css
and reduce the rules to the minimum necessary set to accomplish what you want.
Clearly the browser when it applies CSS, no matter how messy and redundant,
figures it out and does the right thing.

Here are some of the cases that I can see:

  * two or more css rules with exactly the same selector in different part of a file

  * two or more css files which are there for historical reasons but could be merged into one

  * two or more css rules which can be 'refactored' into fewer rules by noticing repeating patterns between them and within the context of all the rules.

  * And so on.

So this is not pretty printing or link-like processing, this is more like
'compiling' a set of css files and then emitting a minimal clean and logical
css back out. Is this a legitimate way to think about things and are there
tools to do this, or has this been tried and turned out to be technically
intractable? Seems to me like it should be possible.


* **Link to site:** **[[GEEKY] CSS Deep Thoughts](None)**
