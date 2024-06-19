---
title: "Calculated file paths"
author: Pito Salas
url: "https://www.mostlypython.com/calculated-file-paths/?ref=mostly-python-newsletter" 
link: "https://www.mostlypython.com/calculated-file-paths/?ref=mostly-python-newsletter" 
cover: "https://static.ghost.org/v5.0.0/images/publication-cover.jpgcontent/images/size/w1200" 
date: 2024-03-14
tags:
    - python
    - patths
    - relative-path
    - Path
---
<img class="cover" src=https://static.ghost.org/v5.0.0/images/publication-cover.jpgcontent/images/size/w1200>

**Link: [Calculated file paths](https://www.mostlypython.com/calculated-file-paths/?ref=mostly-python-newsletter):** "MP 87: What are they, and why should you use them?

Note: I've been working on the styling of code blocks in technical posts. They should look better than they did previously, and be more aligned with what's discussed in the text. There's still some work to do; if they're"

Nice little article. The biggest thing I learned and was surprised by was this line:

`path = Path(__file__).parent / "coffees.txt"`

What's the story with that slash? 
