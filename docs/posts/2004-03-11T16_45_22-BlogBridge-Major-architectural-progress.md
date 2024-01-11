---
title: "BlogBridge Major architectural progress"
author: Pito Salas
date: 2004-03-11T16:45:22
---


>>

>> We made some major new progress since the last update.

>>

>> **Unread Management.** The persistent RSS layer (Informa) has been updated
to support Unread management. This has been carried through the rest of
BlogBridge, using Bold in the Channel Guide and in the Article list in the
usual way to show read and uread. A set of new commands, Mark Read, Mark All
Read have been added as well. Some of the other variations still need to be
implemented.

>>

>> Refined background processing. The various background processes have been
moved into their own subsystem making it easier to manage them. Also a simple
activity indicator has been added to the status bar so the user can see that
there's background activity. Finally an initial Preferences dialog box has
been implemented allowing control over some of these background processes.

>>

>> **Imrpoved HTML rendering.** With the help of another developer we are
bringing the HTML rendering into the 21st century, slowly. As you can see in
the screenshot RSS images are handled and we will use the opportunity to also
support italics, links and other formats.

>>

>> **Other User Interface Changes.** We've introduced an initial command bar
at the top of the window. It looks like we will be able to do without a menu
bar and tie all the commands either to the command bar or the right click
menu.


