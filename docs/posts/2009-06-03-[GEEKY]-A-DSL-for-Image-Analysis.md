---
title: "[GEEKY] A DSL for Image Analysis"
author: Pito Salas
date: 2009-06-03
---
# [[GEEKY] A DSL for Image Analysis](None)




I have been working quite a lot on **Election Reform**   over the last few
weeks, at least from the technology side.

To be honest there is just so much I could be blogging about in this narrow
specialized space that [my cup
overfloweth](<http://wiki.trustthevote.org/index.php/Main_Page>), but also it
has been an impediment, not knowing where to start. There's so much background
and new new learning (for me anyway) that it's been daunting.

Herewith the start of my attempts to further document what I am up to.

One task I've taken on is prototyping a "[post election
audit](<http://www.sos.ca.gov/elections/elections_peas.htm>)" system (more on
this soon.) Basically at the heart of that beast is a bit of code to analyze
an image of a ballot and figure out what the vote was.

**For now** my programming language of choice is **Ruby** , although image
processing with Ruby **may still turn out to be impractical**. I've been
studying up on the task, reading books (see [Practical Algorithms for Image
Analysis](<http://www.amazon.com/gp/product/052188411X?ie=UTF8&tag=blogbridge-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=052188411X>)![](http://www.assoc-
amazon.com/e/ir?t=blogbridge-20&l=as2&o=1&a=052188411X), for example) and
studying techniques and image processing code libraries that seem appropriate.

Two of the biggies I have come across are
[RMagick/ImageMagick](<http://rmagick.rubyforge.org/>) and
[OpenCV](<http://opencv.willowgarage.com/wiki/>). Both have a lot of history
and dynamic communities. **I don 't know yet** which is the best one to use.
The investigation **continues**.

But one idea I have started to implement which is quite fruitful on many
levels is a "[Domain Specific
Language](<http://www.oreillynet.com/ruby/blog/2005/12/what_is_a_dsl.html>)"
for Image Analysis. There is a lot of literature on creating DSLs, and in
particular DSLs hosted on Ruby. They are easy to do and in this particular
domain, add a lot to my productivity and ability to frame and comprehend what
the heck I am doing.

I won't go into hairy technical detail here but I would be glad to share my
approach and my code with anyone who asks. Here's what one of my earliest test
programs look like as written in this home-brew DSL:

`  
open_image :one, "432Leon200dpibw431.tif"  
open_image :target, "target2.tif"  
open_image :t3, "target3.tif"  
#  
binarize :one  
binarize :target  
#  
find_similar_regions :one, :target, :points  
print :points  
#  
relativize_points :points, :outpoints  
print :outpoints  
#  
deskew :one  
write_image :one, "432Deskewed.tif"  
find_first_nonwhite_row :one, :nonwhite_row  
print :nonwhite_row  
`

See how it talks in very high level primitives about image processing? Also
see how the choice between OpenCV and RMagick is totally hidden? I can change
my mind later and not break anything Is it kind of readable?

I will build out this DSL just in the direction and to the extent needed for
my particular task, Ballot analysis. But you can see that it can go pretty
far. How'd'you like it?

Technorati Tags: [dsl](<http://technorati.com/tag/dsl>),
[ruby](<http://technorati.com/tag/ruby>),
[opencv](<http://technorati.com/tag/opencv>),
[imagemagick](<http://technorati.com/tag/imagemagick>),
[ballots](<http://technorati.com/tag/ballots>)


