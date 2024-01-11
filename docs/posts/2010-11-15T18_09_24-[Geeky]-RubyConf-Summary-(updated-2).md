---
title: "[Geeky] RubyConf Summary (updated 2)"
author: Pito Salas
date: 2010-11-15T18:09:24
tags:
    - code
    - rails
    - ruby
    - rubycon-tagf
---



RubyConf 2010 was excellent. It was my first and probably not my last. Some
general thoughts and then a master list of links (the real meat.)

  * Unlike most all 'business' type conferences and talks I have gone to, the RubyConf style of presentation (and perhaps the Rails or Ruby community -- I don't know where it stops) is beautifully minimalist. Very few words on slides, large and impactful photographs. Is it because no one uses PowerPoint and few even use Keynote? I don't know. But there were no text heavy, bullet heavy word slides. And also, lots and lots of code (that part is definitely a geek thing.)

Here is a loosely organized set of links to the things that hit me most at
RubyConf this year. It's random and idiosyncratic (same thing?) but it
reflects my real-time notes and feelings. These were all new to me but they
might be old news to you, of course.

These are my top links:

  * [nicksieger's warbler at master - GitHub](<https://github.com/nicksieger/warbler>) - This was one of my top 5 talks. Warbler is a tool to package a Ruby and/or Rails application into a single .jar or .war file to be run on any other computer that has a Java VM installed. If this works as advertised it is a very important bit of technology. I am going to try it out

  * [MacRuby: The Definitive Guide](<http://ofps.oreilly.com/titles/9781449380373/>) - Another one of my favorite talks, about MacRuby, a Mac OS X implementation of Ruby. From what I saw it looks very real, with good integration with all the Mac OS X libraries, and running on top of the Objective C runtime. It wasn't totally clear what Apple's posture is relative to MacRuby, but I hope it is positive.

  * [mattmatt's showoff at master - GitHub](<https://github.com/mattmatt/showoff>) - Showoff is a very neat presentation tool. It's not an app like Keynote its actually a gem which processes a minimalist markup and serves it up in a local Sinatra server. Also easily lets you deploy your presentation to Heroku. Hmm. Is it mattmatt's or [schacon's showoff at master - GitHub](<https://github.com/schacon/showoff>)???

  * [Git Wrangling](<http://git-tips.heroku.com/#1>) - This was an intense and complex talk about Git. There is as we know, so much more in Git than most people use, and this talk touched into it. Also, Scott Chacon had a funny (but I think he was serious about it) interlude about how to be a gentleman. It includes the recommendation that a gentleman will always rise when a lady enters the room. Also check out [these links with further details about the slides (really, they are good!).](<https://gist.github.com/674651>)

  * [Ruby Mendicant University](<http://university.rubymendicant.com/>) - A really inspiring talk by Greg Brown about his vision and mission to teach people about Ruby and programming. But this is not a fly by night little course, Greg has a big vision and is pursuing this in a comprehensive and highly innovative manner. I was very impressed and will follow and support Greg's work. A great guy!

And here are many more really good ones:

  * <https://github.com/sconover/wrong> - And this is the lightening talk that never happened but I saw mentioned in an email. Apparently there was not sufficient time allowed, and some great talks never happened. This one is about a gem called wrong that defines (can you believe it?) yet another way to express expectations (like assert_ and expect_ and etc etc.) But it's really nice and minimalist. I think it's a good addition to the canon!

  * [DNS Simple](<https://dnsimple.com/>) - This looks important to me, and I think I could really use it. Except… I wish I understood better where DNS Simple fits in my scheme of things. Does it mean that I could ditch GoDaddy as the keeper of my own set of domain names? Would it cost less? Would I be able to cloak my personal name and address like I do with GoDaddy? What are the plusses and minusses? (N.B. See the detailed responses to all these points in the comments)

  * [The GO language](<http://golang.org/>) - I hadn't heard of this language, although it's pretty (really) old after all it's only about 1 year old. Worth looking at for its support of co-routines.

  * <http://www.kanbanpad.com/> - A nicely executed very lightweight project planning 'virtual whiteboard', for the new/old [Kanban](<http://www.crisp.se/kanban>) methodology.

  * [Ticketmaster](<http://ticketrb.com/>) - A tool or platform to connect project/ticket tracking systems together. I post to my ticket tracker, and TicketMaster forwards the new ticket to one or more other ticket trackers (e.g. those my client uses.) This is a tricky problem - how do you handle deletes, and do changes to tickets flow both ways? I didn't look how well TicketMaster tries to solve those problems.

  * [Hipster](<http://www.hipsterrunoff.com/>) - A bit of 2010 Culture that I hadn't seen before. Ok. Culture is stretching it.

  * [http://dl.dropbox.com/u/163257/macruby_2010.pdf](<http://www.kanbanpad.com/>) - PDF of the Mac Ruby Presentation

  * [Apigee | Free and Enterprise API Management Products and Infrastructure](<http://apigee.com/>) - This is a super cool tool to test and experiment with web apis. Interestingly this comes from the guy who build Swivel.com.

  * [rabbit | RubyGems.org | your community gem host](<https://rubygems.org/gems/rabbit>) - Another presentation tool, analogous to showoff.

  * [Stop procrastination: Introducing the noprocrast gem - rfw.posterous.com](<http://rfw.posterous.com/33144299>) - Proof that I am not the only one that gets distracted while working. Here a fellow designed a little utility to cut him off from the net while he is trying to focus. This is called self-binding. Check out this other [article which I have pointed to before about the concept of self-binding (it's not as kinky as it sounds.)](<http://www.theatlantic.com/magazine/archive/2008/11/first-person-plural/7055/>)

  * [](<http://www.theatlantic.com/magazine/archive/2008/11/first-person-plural/7055/>)[RubyConf 2010 | SpeakerRate](<http://speakerrate.com/events/664-rubyconf-2010>) - We are a community who loves building tools. Here's a tool that lets listeners at any conference rate speakers. Very cool building block.

  * <http://blog.danieljackoway.com/rubyconf-2010.html> - Daniel presented about Ruboto, a tool allowing us to write Android applications in Ruby. One nice thing that Jack covers, and I saw this in many of the presentation, is a forthright summary of other tools and solutions that one might consider in addition to Ruboto.

  * [Redcar](<http://redcareditor.com/screenshots/>) - An all-ruby programmers editor -- TextMate written in Ruby. This was a very popular talk and it generated a lot of conversation. It is a work in progress but is very promising. The demonstrations of writing custom commands in Ruby on the fly were impressive. For me personally, I still prefer a full IDE especially one with a visual debugger. I am actually surprised that Rubyists as far as I can tell don't use an interactive debugger (see [this survey](<http://quickquestion.wufoo.com/forms/ruby-debugging-question/>))

  * <http://tmm1.net/debugging-ruby-systems.pdf> - A really good presentation. This pdf (after a bunch of photos at the beginning) is chock full of specific utilities and techniques for advanced profiling and analysis of your ruby and Rails code.

  * [ZOMG WHY IS THIS CODE SO SLOW](<http://www.slideshare.net/tenderlove/zomg-why-is-this-code-so-slow>) - A presentation that unfortunately I missed, but so good that the slides stand on their own. Lots of specific tips around Rails and Ruby Performance

  * [bfts's minitest-2.0.0 Documentation](<http://bfts.rubyforge.org/minitest/>) - A small replacement for Test::Unit. I thought I heard that it was part of Ruby 1.9, but I might have misunderstood.

  * [tmm1's perftools.rb at master - GitHub](<https://github.com/tmm1/perftools.rb/>) - An interesting package of performance tools on Git

  * [MIRAH](<http://www.mirah.org/>) - An interesting little language, it looks like Ruby (but it's NOT Ruby). It is statically typed and compiles directly into efficient JVM byte code.

  * [schacon's grit at master - GitHub](<https://github.com/schacon/grit>) - One of several gems to access Git and Github functionality from Ruby

  * [libgit2's ribbit at master - GitHub](<https://github.com/libgit2/ribbit>) Another one of several gems to access Git and Github functionality from Ruby

  * [BusyConf - Making Great Conferences Even Better](<http://busyconf.com/>) - A promising service for conferences. From what you can see so far, there will be a nice and detailed conference schedule. But I can imagine many additional bits of functionality.

  * [Rc2010 refinements](<http://www.slideshare.net/ShugoMaeda/rc2010-refinements>) - A presentation by Shugo Maeda, close confidant of Matz and a Ruby Committer. The presentation contemplates some rather exotic additions to the Ruby language to overcome some problems that are encountered by large systems built in Ruby. Coyly described as features that might be in Ruby 2.0, which is on an unknown schedule.

  * [RabbitMQ - Messaging that just works](<http://www.rabbitmq.com/>) - A highly touted message queueing platform, usable with Ruby and Rails and other systems.

  * [collectiveidea's delayed_job at master - GitHub](<https://github.com/collectiveidea/delayed_job>) - Delayed job is a popular Ruby based background job product.

  * [markbates's dj_remixes at master - GitHub](<https://github.com/markbates/dj_remixes>) - Mark Bates adds some great additional functionality to Delayed Job

  * [slagyr's solari at master - GitHub](<https://github.com/slagyr/solari>) - A very cute Raffling applications used when you have to raffle something to a big crowd. Very cute, looks great, sound effects and so on.

  * [robey's kestrel at master - GitHub](<https://github.com/robey/kestrel>) - Kestrel is the follow on to Starling, which is a message queueing platform, originally from Twitter.

  * [Home — JRuby.org](<http://www.jruby.org/>) - JRuby is JRuby. I haven't tried it yet. But my sense is that it's definitely worth using in many situations. You can access the huge collection of Java libraries, and, because of the highly optimized JVM, you often will have better performance than MRI (the original and still default Ruby VM)

  * [Rails Talk Ruby CSS Parser](<http://railstalk.com/2010/1/5/ruby-css-parser>) - I was thinking back to some of my own projects, and one is to create a CSS simplifier/optimizer. Here's a Ruby based CSS parser.


