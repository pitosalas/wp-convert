---
title: "Preserving global state in a flask application"
author: Pito Salas
url: "https://stackoverflow.com/questions/19277280/preserving-global-state-in-a-flask-application?answertab=votes#tab-top" 
cover: "https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon@2.png?v=73d79a89bded" 
date: 2021-07-29
tags:
    - python-tag-flask-bugs-session-tags
---
<img src=https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon@2.png?v=73d79a89bded width="500">



(**Web site except:** I am trying to save a cache dictionary in my flask application.

As far as I understand it, the Application Context, in particular the flask.g object should be used for this.
Setup:

import flask ...) 
