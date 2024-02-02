---
title: "Rewriting the Ruby parser"
author: Pito Salas
date: 2023-06-16
tags:
    - explainer
    - parser
    - ruby
    - yarp
---



[ Rewriting the Ruby parser](<https://railsatscale.com/2023-06-12-rewriting-
the-ruby-parser/>) –At Shopify, we have spent the last year writing a new Ruby
parser, which we’ve called YARP (Yet Another Ruby Parser). As of the date of
this post, YARP can parse a semantically equivalent syntax tree to Ruby 3.3 on
every Ruby file in Shopify’s main codebase, GitHub’s main codebase, CRuby, and
the 100 most popular gems downloaded from rubygems.org. We recently got
approval to merge this work into CRuby, and are very excited to share our work
with the community. This post will take you through the motivations behind
this work, the way it was developed, and the path forward.


