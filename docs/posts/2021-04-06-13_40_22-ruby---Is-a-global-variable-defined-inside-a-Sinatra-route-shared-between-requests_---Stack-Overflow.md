---
title: "ruby - Is a global variable defined inside a Sinatra route shared between requests? - Stack Overflow"
author: Pito Salas
date: 2021-04-06 13:40:22
tags:
    - sinatra
    - tips
    - ruby
    - stackoverflow
    - state
    - variables
    - global
---


(**Web site except:** Say I've got: get '/' do $random = Random.rand() response.body = $random end If I have thousands of requests per second coming to /, will the $random be shared and 'leak' outside the context or...) 
