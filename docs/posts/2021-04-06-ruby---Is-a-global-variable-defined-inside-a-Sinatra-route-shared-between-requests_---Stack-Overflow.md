---
title: "ruby - Is a global variable defined inside a Sinatra route shared between requests? - Stack Overflow"
author: Pito Salas
url: "https://stackoverflow.com/questions/14388263/is-a-global-variable-defined-inside-a-sinatra-route-shared-between-requests" 
cover: "https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon@2.png?v=73d79a89bded" 
date: 2021-04-06
tags:
    - sinatra-tips-ruby-stackoverflow-state-variables-global
---
<img src=https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon@2.png?v=73d79a89bded width="500">



(**Web site except:** Say I've got: get '/' do $random = Random.rand() response.body = $random end If I have thousands of requests per second coming to /, will the $random be shared and 'leak' outside the context or...) 
