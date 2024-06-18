---
title: "Database Performance Optimization and Scaling in Rails | AppSignal Blog"
author: Pito Salas
url: "https://blog.appsignal.com/2022/12/07/database-performance-optimization-and-scaling-in-rails.html?utm_source=ruby-magic&utm_medium=email&utm_campaign=rss-email&utm_content=button" 
link: "https://blog.appsignal.com/2022/12/07/database-performance-optimization-and-scaling-in-rails.html?utm_source=ruby-magic&utm_medium=email&utm_campaign=rss-email&utm_content=button" 
cover: "https://ondemand.bannerbear.com/signedurl/Mn62mqoVbWvyB5wgQ1/image.jpg?modifications=W3sibmFtZSI6InRpdGxlIiwidGV4dCI6IkRhdGFiYXNlIFBlcmZvcm1hbmNlIE9wdGltaXphdGlvbiBhbmQgU2NhbGluZyBpbiBSYWlscyJ9LHsibmFtZSI6ImltYWdlIiwiaW1hZ2VfdXJsIjoiaHR0cHM6Ly9hcHBzaWduYWwtbmV4dGpzLWJsb2ctNHFmZDhrdHgyLWFwcHNpZ25hbC52ZXJjZWwuYXBwL2ltYWdlcy9ibG9nLzIwMjItMTIvZGF0YWJhc2UtcGVyZm9ybWFuY2UucG5nIn0seyJuYW1lIjoiY2F0ZWdvcnlfbG9nbyIsImltYWdlX3VybCI6Imh0dHBzOi8vYXBwc2lnbmFsLW5leHRqcy1ibG9nLTRxZmQ4a3R4Mi1hcHBzaWduYWwudmVyY2VsLmFwcC9pbWFnZXMvbG9nb3MvcnVieS1sb2dvLnBuZyJ9XQ&s=a1a18242a66408b1cb5b5940fb0c3cbee5489db2c827efe0b6b7f1654e3d73c7" 
date: 2022-12-08
tags:
    - rails
    - scaling
    - ruby
    - sharding
    - howto
    - active-record
    - scale deploy build rails docker howto
---
<img class="cover" src=https://ondemand.bannerbear.com/signedurl/Mn62mqoVbWvyB5wgQ1/image.jpg?modifications=W3sibmFtZSI6InRpdGxlIiwidGV4dCI6IkRhdGFiYXNlIFBlcmZvcm1hbmNlIE9wdGltaXphdGlvbiBhbmQgU2NhbGluZyBpbiBSYWlscyJ9LHsibmFtZSI6ImltYWdlIiwiaW1hZ2VfdXJsIjoiaHR0cHM6Ly9hcHBzaWduYWwtbmV4dGpzLWJsb2ctNHFmZDhrdHgyLWFwcHNpZ25hbC52ZXJjZWwuYXBwL2ltYWdlcy9ibG9nLzIwMjItMTIvZGF0YWJhc2UtcGVyZm9ybWFuY2UucG5nIn0seyJuYW1lIjoiY2F0ZWdvcnlfbG9nbyIsImltYWdlX3VybCI6Imh0dHBzOi8vYXBwc2lnbmFsLW5leHRqcy1ibG9nLTRxZmQ4a3R4Mi1hcHBzaWduYWwudmVyY2VsLmFwcC9pbWFnZXMvbG9nb3MvcnVieS1sb2dvLnBuZyJ9XQ&s=a1a18242a66408b1cb5b5940fb0c3cbee5489db2c827efe0b6b7f1654e3d73c7>



* **Web site excerpt:** A decent introductory article about scaling rails applications. Somewhat rails specific,  but it does introduce the general principles. Heres the authors blurb: “Improve your Rails application's performance by fine-tuning and scaling your database.”

* **Link to site:** **[Database Performance Optimization and Scaling in Rails | AppSignal Blog](https://blog.appsignal.com/2022/12/07/database-performance-optimization-and-scaling-in-rails.html?utm_source=ruby-magic&utm_medium=email&utm_campaign=rss-email&utm_content=button)**
