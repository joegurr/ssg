# (s)tatic (s)ite (g)enerator

I am sick of having to type all of the html for blog posts, and decided I'd build a very simple static site generator to meet my needs.

My only goal for this code is to lower the effort required to publish a blog post.

I decided that I would store the content and metadata of a blog post in a text file with the following structure:

```
title-short:
title-long:
date: YYYY-MM-DD
date_human: Month YYYY
quote:
attribution:
content:
```

I'm not an expert in python package managing, nor how to distribute modules, the following is a reminder to myself how this works.

To 'register' this as a program I can run in the shell I need to run
`python3 setup.py develop --user`
Note, doing this enables me to edit the program and not have to 'reregister' it.

I'd really like to learn more about this!
