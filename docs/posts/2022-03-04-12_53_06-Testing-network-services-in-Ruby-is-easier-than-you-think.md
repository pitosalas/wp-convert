---
title: "Testing network services in Ruby is easier than you think"
author: Pito Salas
date: 2022-03-04 12:53:06
tags:
    - testing, doubles, ruby, network, soa, cosi105
---

(**Web site except:** You’ve started a new project and it’s time for your code to depend on a third-party service. It could be something like ElasticSearch, Resque, a billing provider, or just an arbitrary HTTP API. You’re a good developer, so you want this code to be well tested. But how do you test code that fires off requests to a service that’s totally out of your control?) 
