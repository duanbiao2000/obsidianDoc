---
aliases: 如何快速有效地阅读别人的代码 – 自学程序员 --- How to quickly and effectively read other people’s code – Self-Taught Coders
categories: []
createdAt: 2024-11-21T13:31:19 (UTC +08:00)
tags: []
source: https://selftaughtcoders.com/how-to-quickly-and-effectively-read-other-peoples-code/
author: by Alex Coleman  |  Learning, Web Development作者：亚历克斯·科尔曼|学习,网页 开发
---


# 如何快速有效地阅读别人的代码 – 自学程序员 --- How to quickly and effectively read other people’s code – Self-Taught Coders

> ## Excerpt
> Just the other day, a fellow STCer (Self-Taught Coder) asked me the following question: “How do you go about understanding someone else’s code? I am starting to feel more comfortable with my own code, but whenever I try to look at something someone else wrote I feel totally lost. I know some of this is

---
<!--more-->

Just the other day, a fellow STCer (Self-Taught Coder) asked me the following question:  
就在前几天，一位 STCer（自学程序员）同事问了我以下问题：

> “How do you go about understanding someone else’s code? I am starting to feel more comfortable with my own code, but whenever I try to look at something someone else wrote I feel totally lost. I know some of this is unavoidable, especially if the code is poorly (or not at all) documented, but right now I have no strategy at all. Any tips would be greatly appreciated!”  
> “你如何理解别人的代码？我开始对自己的代码感到更加自在，但每当我尝试查看别人写的东西时，我都会感到完全迷失。我知道其中一些是不可避免的，特别是如果代码记录很差（或根本没有），但现在我根本没有策略。任何提示将不胜感激！”

I love this question for a few reasons:  
我喜欢这个问题有几个原因：

1.  The method I’ll recommend for reading and understanding someone else’s code will also help you: 1) better understand _your own_ code; and 2) help you increase the speed and ease with which you understand _all_ new pieces of code you approach.  
    我推荐的阅读和理解别人代码的方法也将帮助您：1）更好地理解_您自己的_代码； 2) 帮助您提高理解_所有_新代码的速度和轻松度。
2.  It sheds light on one of the most important aspects of learning a new skill, like programming: exposure to high quantity, high quality examples of expertise.  
    它揭示了学习编程等新技能最重要的方面之一：接触大量、高质量的专业知识示例。

There are a lot of wins here. Let’s start at the beginning.  
这里有很多胜利。让我们从头开始吧。

## What’s the best way to read and understand someone else’s code?  
阅读和理解别人代码的最佳方法是什么？

The best way I’ve ever discovered to read and understand someone else’s code is to:  
我发现阅读和理解别人代码的最好方法是：

### 1\. Find one thing you know the code does, and trace those actions backward, starting at the end.  
1\. 找到一件您知道代码所做的事情，并从末尾开始向后追踪这些操作。

Say, for example, you know that the code you’re viewing ultimately creates a file with a list of movie titles. Figure out where in the code — the _specific, few lines_ — it generates that file.  
例如，您知道您正在查看的代码最终会创建一个包含电影标题列表的文件。找出代码中的位置（_具体的几行_）生成该文件。

Then, move one step backward and figure out how it places the info in the file.  
然后，向后退一步，弄清楚它如何将信息放入文件中。

Then, move another step backward and figure out where the info came from.  
然后，再向后退一步，找出信息的来源。

And so on… 等等…

**Let’s call those connected pieces of code a “chain of actions**.”
**我们将这些相互连接的代码片段称为“动作链**”。
<!--SR:!2025-03-20,3,250!2000-01-01,1,250-->

Inevitably, using this approach will lead you through a bunch of different areas of the code. And that will probably give you a good deal of insight into things such as:  
不可避免地，使用这种方法将引导您完成代码的许多不同区域。这可能会让您对以下事情有深入的了解：

-   how the body of code is organized (where variables are defined, where different types of functions are located, etc.)  
    代码主体是如何组织的（变量定义在哪里，不同类型的函数位于哪里等）
-   the person’s style of coding  
    人的编码风格
-   how the person who wrote the code thinks and problem solves (this is harder to describe, but it comes intuitively the more examples you see)  
    编写代码的人如何思考和解决问题（这很难描述，但你看到的示例越多，它就越直观）

And by doing that, **you’ll gradually begin to understand more and more of that full body of code**. So where you started with:
通过这样做，**您将逐渐开始理解越来越多的完整代码**。那么你从哪里开始：
<!--SR:!2000-01-01,1,250!2025-03-21,4,270-->

\[ a big file of code that doesn’t really mean much at all to you \]  
\[一个大文件的代码对你来说根本没有多大意义\]

you’ll now be looking at:  
您现在将看到：

\[ still a big file of code, but where you now understand a few specific sections \]  
\[仍然是一个很大的代码文件，但是您现在了解了一些特定的部分\]

It’s almost as if you were originally standing in a room that was pitch-black, and, one at a time, different lights throughout the room were turned on to gradually reveal more details of the room’s appearance.  
就好像你原本站在一个漆黑的房间里，房间里的不同灯光被一盏一盏地打开，逐渐显露出房间外观的更多细节。

![Using "chains of actions" to gradually understand a never-before-seen piece of code](https://selftaughtcoders.com/wp-content/uploads/2015/05/using-paths-of-actions-to-understand-pieces-of-code.png)

Using “chains of actions” to gradually understand a never-before-seen piece of code  
使用“动作链”逐渐理解一段前所未见的代码

### 2\. Rinse and repeat. 2\. 冲洗并重复。

Repeat that process multiple times, and you’ll rapidly increase your understanding of more and more pieces of the overall codebase.  
多次重复该过程，您将快速加深对整个代码库越来越多部分的理解。

Just as parts of the pitch-black room are gradually illuminated, parts of the code gradually “light up” for you, as you understand how they function.  
正如漆黑的房间的某些部分逐渐被照亮一样，当您了解它们的功能时，部分代码也会逐渐为您“照亮”。

The reason that works well is that, in all cases, **a body of code is designed to tackle one (or more) complex problems**. So you’ll always have those “chains of actions” throughout.
效果良好的原因是，在所有情况下，**代码体都是为了解决一个（或多个）复杂问题而设计的**。因此，您将始终拥有这些“行动链”。
<!--SR:!2025-03-20,3,250!2000-01-01,1,250-->

And **the more you can gain an understanding of how different parts of the code are connected, the more you’ll develop an understanding of the entire codebase, as a whole**.
**您对代码不同部分如何连接的了解越多，您对整个代码库的整体理解就越深入**。
<!--SR:!2000-01-01,1,250!2025-03-20,3,250-->

And, over time, **the more (good) code you see, the easier it becomes to read and understand _all_ code, and the faster you can do so.**
而且，随着时间的推移，**您看到的（好）代码越多，阅读和理解_所有_代码就越容易，而且速度也就越快。**
<!--SR:!2000-01-01,1,250!2025-03-20,3,250-->

..which leads directly into the second reason I love this question: it highlights the importance of exposure to high quantity, high quality examples of expertise.  
..这直接引出了我喜欢这个问题的第二个原因：它强调了接触大量、高质量的专业知识示例的重要性。

In programming, **“high quality examples of expertise” = good code** that other programmers wrote.
在编程中， **“专业知识的高质量示例”=其他程序员编写的优秀代码**。
<!--SR:!2025-03-20,3,250!2000-01-01,1,250-->

## The importance of exposing yourself to high quantity, high quality examples of expertise  
让自己接触大量、高质量的专业知识示例的重要性

In her incredibly poignant new book, _[Badass: Making Users Awesome](http://www.amazon.com/gp/product/1491919019/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1491919019&linkCode=as2&tag=alepcol-20&linkId=THNHYVSS752ZYNNU)_, Kathy Sierra states that **exposure to high quantity, high quality examples of expertise is one of the two main factors that dictate how quickly and effectively people learn new skills**. (The other is deliberate practice.)
凯西·塞拉 (Kathy Sierra) 在她令人难以置信的辛酸新书_[《Badass: Making Users Awesome](http://www.amazon.com/gp/product/1491919019/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1491919019&linkCode=as2&tag=alepcol-20&linkId=THNHYVSS752ZYNNU)_ 》中指出，**接触大量、高质量的专业知识示例是决定人们学习新技能的速度和效率的两个主要因素之一**。 （另一个是刻意练习。）
<!--SR:!2000-01-01,1,250!2025-03-20,3,250-->

> “The more you watch (or listen) to expert examples, the better you can become. The _less_ exposure you have to experts or results of expert work, the less likely you are to develop expert skills.”  
> “你看（或听）专家例子越多，你就能变得越好。你接触专家或专家工作成果的机会_越少_，你培养专业技能的可能性就越小。”

Let’s take a look at the first example that clearly pops into everyone’s mind: chicken sexing. Kidding. But it is, in fact, a great demonstration of this concept.  
让我们看一下每个人脑海中清晰浮现的第一个例子：鸡的性别鉴定。开玩笑。但事实上，它很好地体现了这一概念。

### Learning from chicken sexing (yeah, you read that right)  
从鸡性别鉴定中学习（是的，你没看错）

What is chicken sexing? And what does it have to do with exposure to high quantity/quality examples of expertise? Kathy explains:  
什么是鸡的性别鉴定？它与接触大量/高质量的专业知识示例有什么关系？凯西解释说：

> “Determining the gender of a newborn chick is notoriously tough, but for large commercial chicken farms, the sooner the females are separated from the males, the sooner they can be on the feeding-for-egg-production path. In the early 1900s, the Japanese developed a particular method for chick sexing and a few experts (reliable, accurate chick-sexers) emerged.  
> “确定新生雏鸡的性别是出了名的困难，但对于大型商业养鸡场来说，雌性越早与雄性分开，它们就能越早走上产蛋之路。 1900 年代初，日本人开发了一种特殊的小鸡性别鉴定方法，并出现了一些专家（可靠、准确的小鸡性别鉴定师）。  
> Great, we’ll have those experts teach others, right? Just one problem: when questioned, the chick-sexing experts didn’t know exactly _how_ they did it. ‘I just knew.’”  
> 太好了，我们会让这些专家教别人，对吗？只有一个问题：当被问及小鸡性别鉴定专家时，他们并不确切知道他们_是如何_做到的。 “我刚刚知道。”

So how do they even go about the training? Well, assume you’re one of the new chick-sexer recruits. You’re are placed in front of a bin full of baby chicks. Problem is: they all look _exactly_ the same to you. But you’re told to just pick one up and make a guess as to its sex. As far as you’re concerned, your guesses are _completely random_. But Sierra continues:  
那么他们如何进行培训呢？好吧，假设您是新招募的小鸡性别鉴定师之一。你被放置在一个装满小鸡的箱子前面。问题是：它们在你看来都_一模一样_。但你被告知只需拿起一个并猜测它的性别。就你而言，你的猜测_完全是随机的_。但塞拉继续说道：

> “After each wild, random, totally made-up guess, the master chick-sexer gives you _feedback_. Yes, no, no, yes. You still have no idea how the expert “knows,” but you just keep doing this, over and over.  
> “在每次疯狂、随机、完全虚构的猜测之后，小鸡性别鉴定大师都会给你_反馈_。是的，不，不，是的。你仍然不知道专家是如何“知道”的，但你只是不断地重复这样做。  
> And then, eventually, something happens. You begin scoring better than random. You get better. Over time, _much_ better. _But you don’t know why._ For all you know, you’re _still_ just guessing, but now it’s as if some “mysterious” force is guiding your hand toward the correct bin.  
> 然后，最终，有些事情发生了。你开始比随机得分更好。你会好起来的。随着时间的推移，_好多_了。_但你不知道为什么。_就您所知，您_仍然_只是猜测，但现在好像有某种“神秘”的力量正在引导您的手走向正确的垃圾箱。

How does all this “magic” work? Sierra brings it on home:  
所有这些“魔法”是如何发挥作用的？塞拉把它带回家：

> “After enough exposure with feedback, your brain \[begins\] detecting patterns and underlying structures, without your conscious awareness. With _more_ exposure, your brain \[fine-tunes\] its perception and eventually \[figures\] out what _really_ \[matters\]. Your brain \[is\] making finer distinctions and sorting signal from noise even if _you_ \[can’t\] explain how.  
> “在充分接触反馈后，你的大脑\[开始\]在你无意识的情况下检测模式和底层结构。随着接触的次数_增多_，你的大脑会\[微调\]其感知并最终\[找出\]_真正_\[重要\]的东西。你的大脑正在做出更精细的区分，并将信号与噪音分类，即使_你_\[无法\]解释如何做到这一点。  
> _Perceptual knowledge_ includes what we think of as expert _intuition_. The ability to instantly know _which_ chess move to make. Or that _this_ painting is a _forgery_. Or that _this_ house fire will _explode_. Or that there’s _something_ wrong with that code, even though you can’t always articulate _how_ you know.”  
> _感性知识_包括我们所认为的专家_直觉_。能够立即知道要走_哪_一步棋。或者说_这_幅画是_赝品_。或者说_这个_房子会_发生火灾_。或者该代码有_问题_，即使你不能总是清楚地表达你_是如何_知道的。”

![How experts use unconscious perceptual knowledge](https://selftaughtcoders.com/wp-content/uploads/2015/05/experts-perceptual-knowledge-kathy-sierra.jpg)

How experts use unconscious perceptual knowledge  
专家如何利用无意识的感性知识  
_from pp. 134 of Kathy Sierra’s book, “Badass: Making Users Awesome”  
摘自凯西·塞拉 (Kathy Sierra) 著作《Badass: Making Users Awesome》第 134 页_

## How does that play out in programming?  
这在编程中是如何发挥作用的？

Most importantly, know that **the longer you’re programming — and thus the more code samples you see, of all different kinds — the easier it gets to understand other people’s code. And the faster you’re able to do it.**
最重要的是，要知道**您编程的时间越长（因此您看到的各种不同类型的代码示例越多）就越容易理解其他人的代码。而且你能做到的速度越快。**
<!--SR:!2000-01-01,1,250!2025-03-20,3,250-->

It’s a wonderfully self-perpetuating cycle: you read more code; you gain the ability to understand it quicker and more effectively; so you are able to consume even _more_ code; and so on.  
这是一个奇妙的自我延续循环：你阅读更多代码；您能够更快、更有效地理解它；这样您就可以使用_更多_代码；等等。

And it doesn’t stop there: you’ll also see huge positive gains in _your own_ coding. How so?  
而且它并不止于此：您还将在_自己的_编码中看到巨大的积极收益。为何如此？

1.  You’ll be able to more quickly understand code samples and examples you inevitably reference during your own programming (e.g. something from an online course; or a snippet from a StackOverflow post).  
    您将能够更快地理解在自己的编程过程中不可避免地引用的代码示例和示例（例如，在线课程中的内容；或 StackOverflow 帖子中的片段）。
2.  You’ll be able to understand past code you’ve written at a glance. (And, inevitably, down the road, you’ll be working with a lot of different pieces of code all together, so this ability pays off big time.)

Ultimately, that translates to:

1.  Less pauses
2.  More progress

which = **more fun and more enjoyable**. Win!
<!--SR:!2025-03-20,3,250-->

And you better believe that…

## I’ve incorporated all of this into my online course,  
From Idea To Launch

[From Idea To Launch](https://selftaughtcoders.com/from-idea-to-launch/) walks you through building your very own Laravel PHP web application – step by step – based on _your own_ idea. And the course:

1.  **includes plenty of real-world, expert code examples alongside each lesson**, to ensure you’re consistently exposed to high quality examples of code.
2.  **helps you connect with other programmers**, furthering your exposure to examples of others’ code, techniques, and thought processes.
<!--SR:!2000-01-01,1,250!2025-03-20,3,250-->

I always aim to practice what I preach. Be sure to [read more about the course](https://selftaughtcoders.com/from-idea-to-launch/) if you’re interested in building and launching your own web app.

___

**Shoutout:** Thanks to Carol, one of our own, for the inspiration for this post! It’s the best when I get to write about things that come from directly within our group.
<!--SR:!2025-03-20,3,250-->

___

Alex Coleman helps others learn to build web applications with Laravel. His articles and courses have helped over 10,000 developers level-up their PHP web development skills and learn to build and launch their own web applications to the world. If you enjoyed this article, then [join his free newsletter](https://selftaughtcoders.com/newsletter).

___
