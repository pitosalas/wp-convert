---
title: "An Introduction to Ractors in Ruby | AppSignal Blog"
author: Pito Salas
url: "https://blog.appsignal.com/2022/08/24/an-introduction-to-ractors-in-ruby.html" 
link: "https://blog.appsignal.com/2022/08/24/an-introduction-to-ractors-in-ruby.html" 
cover: "https://ondemand.bannerbear.com/signedurl/Mn62mqoVbWvyB5wgQ1/image.jpg?modifications=W3sibmFtZSI6InRpdGxlIiwidGV4dCI6IkFuIEludHJvZHVjdGlvbiB0byBSYWN0b3JzIGluIFJ1YnkifSx7Im5hbWUiOiJpbWFnZSIsImltYWdlX3VybCI6Imh0dHBzOi8vYXBwc2lnbmFsLW5leHRqcy1ibG9nLTRxZmQ4a3R4Mi1hcHBzaWduYWwudmVyY2VsLmFwcC9pbWFnZXMvYmxvZy8yMDIyLTA4L3J1YnktcmFjdG9ycy5qcGcifSx7Im5hbWUiOiJjYXRlZ29yeV9sb2dvIiwiaW1hZ2VfdXJsIjoiaHR0cHM6Ly9hcHBzaWduYWwtbmV4dGpzLWJsb2ctNHFmZDhrdHgyLWFwcHNpZ25hbC52ZXJjZWwuYXBwL2ltYWdlcy9sb2dvcy9ydWJ5LWxvZ28ucG5nIn1d&s=4e49080839066ef64a220d1b6f09792344b5a076f1d0cdea0b513af566632d9f" 
date: 2022-12-22
tags:
    - ruby
    - threads
    - concurrency
    - ractor
    - explainer
---
# [An Introduction to Ractors in Ruby | AppSignal Blog](https://blog.appsignal.com/2022/08/24/an-introduction-to-ractors-in-ruby.html)

<img src=https://ondemand.bannerbear.com/signedurl/Mn62mqoVbWvyB5wgQ1/image.jpg?modifications=W3sibmFtZSI6InRpdGxlIiwidGV4dCI6IkFuIEludHJvZHVjdGlvbiB0byBSYWN0b3JzIGluIFJ1YnkifSx7Im5hbWUiOiJpbWFnZSIsImltYWdlX3VybCI6Imh0dHBzOi8vYXBwc2lnbmFsLW5leHRqcy1ibG9nLTRxZmQ4a3R4Mi1hcHBzaWduYWwudmVyY2VsLmFwcC9pbWFnZXMvYmxvZy8yMDIyLTA4L3J1YnktcmFjdG9ycy5qcGcifSx7Im5hbWUiOiJjYXRlZ29yeV9sb2dvIiwiaW1hZ2VfdXJsIjoiaHR0cHM6Ly9hcHBzaWduYWwtbmV4dGpzLWJsb2ctNHFmZDhrdHgyLWFwcHNpZ25hbC52ZXJjZWwuYXBwL2ltYWdlcy9sb2dvcy9ydWJ5LWxvZ28ucG5nIn1d&s=4e49080839066ef64a220d1b6f09792344b5a076f1d0cdea0b513af566632d9f width="500">



(**Web site except:** I read and  heard about Ractors in ruby. This article demystifies them. My evaluation: Ractors are a safer alternative to Threads. I’m sure thats a massive oversimplification and even incorrect in a way. But for me I need a simple hook to hang the concept onto! The author says: “Discover when and why you should use ractors, and build a ractor in Ruby.”) 
