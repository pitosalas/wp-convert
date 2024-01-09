---
title: "Preserving global state in a flask application"
author: Pito Salas
date: 2021-07-29 11:11:31
tags:
    - python, flask, bugs, sessions
---

(**Web site except:** I am trying to save a cache dictionary in my flask application.

As far as I understand it, the Application Context, in particular the flask.g object should be used for this.
Setup:

import flask ...) 
