---
title: "[Geeky] RMagick and memory leaks"
author: Pito Salas
date: 2009-06-19
---

**Link: [[Geeky] RMagick and memory leaks](None):** ""

A [recent post talked about creating a "Domain Specific Language" for image
processing of ballots](</2009/06/02/geeky-a-dsl-for-image-analysis/>). I've
made a lot of progress on that project and wanted to give an update.

One [commenter (my pal Aleks) said to 'watch out for RMagick as it has major
memory leaks](</2009/06/02/geeky-a-dsl-for-image-analysis/#comment-59728>). I
talked to him further and he recommended using
[MiniMagick](<http://github.com/probablycorey/mini_magick/tree/master>)
instead. I investigated.

It turns out indeed that my [RMagick](<http://rmagick.rubyforge.org/>) app was
gobbling up tons of memory.

Both [RMagick](<http://rmagick.rubyforge.org/>) and
[MiniMagick](<http://github.com/probablycorey/mini_magick/tree/master>) are
Ruby bindings to [ImageMagick](<http://www.imagemagick.org/script/index.php>)
which is a comprehensive image processing library, written in C I believe. The
differences between [RMagick](<http://rmagick.rubyforge.org/>) and Mini Magick
are:

  1. [RMagick](<http://rmagick.rubyforge.org/>) uses the ImageMagick API and presents a comprehensive 'rubyfication' of the [ImageMagtick](<http://www.imagemagick.org/script/index.php>) api. This is useful but you do find that you jump back and forth between the RMagick doc and the ImageMagick doc to see what methods in one correspond to which ones in the other. [MiniMagick](<http://github.com/probablycorey/mini_magick/tree/master>) on the other hand is a very thin veneer over [ImageMagick](<http://www.imagemagick.org/script/index.php>)'s command line utilities. It generally uses 'method-not-found' to decide to invoke the corresponding C method. This means that the ImageMagick doc is your primary source. The MiniMagick source itself is a single tiny (**but sophisticated**) Ruby script.

  2. [RMagick](<http://rmagick.rubyforge.org/>) creates in memory [ImageMagick](<http://www.imagemagick.org/script/index.php>) ('[malloc](<http://en.wikipedia.org/wiki/Malloc>)') objects and retains pointers to those inside of Ruby structures. Unless those Ruby structures are garbage collected, the ImageMagick objects just hang around and eat memory, hence the memory leak reputation. Because as far as Ruby is concerned, not that much memory has been used yet, natural garbage collections don't occur and your system memory footprint gets bigger and bigger.

  3. [MiniMagick](<http://github.com/probablycorey/mini_magick/tree/master>) works only with files; it never creates the [ImageMagick](<http://www.imagemagick.org/script/index.php>) malloc objects and hence does not suffer from the memory leak. On the other hand, with a complex process like what I am working on, you are creating, saving and reading a lot of files, **which slows things down**.

I did nearly a day of coding comparing the two and while
[MiniMagick](<http://github.com/probablycorey/mini_magick/tree/master>) made
the memory leaks go away, in the end it was slower for my purposes than
RMagick, **probably due to the files** that were constantly being created,
opened and saved. **Note** after a few dozen complicated operations, the
[RMagick](<http://rmagick.rubyforge.org/>) version got super slow and
basically hung because of memory consumption.

That was easily solved with a little research. I[ found a post that explained
how to address the apparent memory leaks in
RMagick](<http://rubyforge.org/forum/forum.php?thread_id=1374&forum_id=1618>):
I added a forced reclamation of the ImageMagick malloc object whenever I am
done with one (Image.destroy! is the call) and the huge leak is gone. Not sure
yet whether there are other ones, but for now,
[RMagick](<http://rmagick.rubyforge.org/>) wins for me!


