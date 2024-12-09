---
title: 发货/展示/询问 --- Ship / Show / Ask
categories: []
date: 2024-11-21T13:23:14 (UTC +08:00)
tags: []
source: https://martinfowler.com/articles/ship-show-ask.html
author: Rouan Wilsenach 鲁安·威尔森纳赫
---


# 发货/展示/询问 --- Ship / Show / Ask

> ## Excerpt
> Ship/Show/Ask is a branching strategy that helps teams wait less and ship more, without losing out on feedback.

---
<!--more-->

## How do you do Continuous Integration with Pull Requests?  
如何与拉取请求进行持续集成？

[Pull Requests](https://martinfowler.com/bliki/PullRequest.html) have been widely adopted by many software teams. Some people love them, and some people long for the days of [Continuous Integration](https://martinfowler.com/articles/continuousIntegration.html) – where you never created branches and your team put their changes together all the time.  
[Pull Request](https://martinfowler.com/bliki/PullRequest.html)已被许多软件团队广泛采用。有些人喜欢它们，有些人则渴望[持续集成](https://martinfowler.com/articles/continuousIntegration.html)的日子——在这种日子里，你从未创建分支，而你的团队一直将他们的更改放在一起。

In some ways, Pull Requests are a game changer. Code hosting tools offer fantastic code review functionality. There are loads of SaaS providers offering services that can run on your pull requests – from running your tests and checking code quality to deploying fully-fledged preview environments.  
在某些方面，拉取请求改变了游戏规则。代码托管工具提供了出色的代码审查功能。有大量 SaaS 提供商提供可以根据您的拉取请求运行的服务 - 从运行测试和检查代码质量到部署成熟的预览环境。

But the adoption of Pull Requests as the primary way of contributing code has created problems. We’ve lost some of the “Ready to Ship” mentality we had when we did Continuous Integration. Features-in-progress stay out of the way by delaying integration, and so we fall into the [pitfalls of low-frequency integration](https://martinfowler.com/articles/branching-patterns.html#Low-frequencyIntegration) that Continuous Integration sought to address.  
但采用拉取请求作为贡献代码的主要方式已经产生了问题。当我们进行持续集成时，我们已经失去了一些“准备交付”的心态。正在进行的功能会延迟集成，因此我们陷入了持续集成试图解决[的低频集成陷阱](https://martinfowler.com/articles/branching-patterns.html#Low-frequencyIntegration)。

Sometimes Pull Requests sit around and get stale, or we’re not sure what to work on while we wait for review. Sometimes they become bloated as we think “well, I may as well do this while I’m here.”  
有时拉取请求会闲置并变得陈旧，或者我们不确定在等待审核时要做什么。有时，当我们想“好吧，我还可以在这儿的时候做这件事”时，它们就会变得臃肿。

We also get tired of the number of Pull Requests we have to review, so we don't talk about the code anymore. We stop paying attention and we just click “Approve” or say “Looks good to me”.  
我们也厌倦了必须审查的 Pull Request 数量，因此我们不再谈论代码。我们不再关注，只是点击“批准”或说“我觉得不错”。

## Introducing Ship / Show / Ask  
船舶介绍/展示/询问

There’s an approach to software branching I’ve used with my teams. It’s worked really well, so I’d like to share it with you.  
我在我的团队中使用过一种软件分支方法。它的效果非常好，所以我想与大家分享。

Every time you make a change, you choose one of three options: Ship, Show or Ask.  
每次进行更改时，您都可以选择以下三个选项之一：发货、展示或询问。

### Ship 船

![](https://martinfowler.com/articles/ship-show-ask/Ship.png)

Figure 1: Change goes straight on mainline  
图 1：更改直接在主线上进行

This feels the most like Continuous Integration. You want to make a change, so you make it directly on your [mainline](https://martinfowler.com/articles/branching-patterns.html#mainline). When you do this, you’re not waiting for anyone to take your change to production. You’re not asking for a code review. No fuss – just make the change, with all the usual Continuous Integration techniques to make it safe.  
这感觉最像持续集成。您想要进行更改，因此您可以直接在[主线](https://martinfowler.com/articles/branching-patterns.html#mainline)上进行更改。当您这样做时，您不需要等待任何人将您的更改投入生产。您并不是要求进行代码审查。不用大惊小怪——只需进行更改即可，使用所有常用的持续集成技术来确保安全。

Works great when: 在以下情况下效果很好：

-   I added a feature using an established pattern  
    我使用既定模式添加了一个功能
-   I fixed an unremarkable bug  
    我修复了一个不起眼的错误
-   I updated documentation 我更新了文档
-   I improved my code based on your feedback  
    我根据您的反馈改进了我的代码

### Show 展示

![](https://martinfowler.com/articles/ship-show-ask/Show.png)

Figure 2: Open a PR for feedback, but merge it straight away  
图 2：打开 PR 寻求反馈，但立即合并

This is where we take the Continuous Integration mindset and still make use of all the goodness Pull Requests can give us. You make your change on a branch, you open a Pull Request, then you merge it without waiting for anyone. You’ll want to wait for your automated checks (tests, code coverage, preview environments, etc.), but you don’t wait for anyone’s feedback to proceed with taking your change live.  
这就是我们采取持续集成思维方式的地方，并且仍然利用拉取请求可以给我们带来的所有好处。您在分支上进行更改，打开拉取请求，然后将其合并，而无需等待任何人。您需要等待自动检查（测试、代码覆盖率、预览环境等），但您不会等待任何人的反馈来继续实施您的更改。

In doing so, you’ve taken your change live quickly while still creating a space for feedback and conversation. Your team should get notified of your pull request and they can then review what you’ve done. They can provide you with feedback on your approach or code. They can ask you questions. They can learn from what you’ve done.  
通过这样做，您可以快速实施更改，同时仍然为反馈和对话创造空间。您的团队应该收到有关您的拉取请求的通知，然后他们可以审查您所做的事情。他们可以为您提供有关您的方法或代码的反馈。他们可以问你问题。他们可以从你所做的事情中学习。

Works great when: 在以下情况下效果很好：

-   I would love your feedback on how this code could be better  
    我希望得到您关于如何改进此代码的反馈
-   Look at this new approach or pattern I used  
    看看我使用的这个新方法或模式
-   I refactored X so now it looks like this  
    我重构了 X 所以现在看起来像这样
-   What an interesting bug! Look how I fixed it.  
    多么有趣的错误啊！看看我是怎么修好的。

### Ask 问

![](https://martinfowler.com/articles/ship-show-ask/Ask.png)

Figure 3: Open a PR for feedback and wait before merging  
图 3：打开 PR 寻求反馈并等待合并

Here we pause. We make our changes on a branch, we open a Pull Request, and we wait for feedback before merging. Maybe we’re not sure we’ve taken the right approach. Maybe there’s some code we’re not quite happy with but we’re unsure how to improve it. Maybe you’ve done an experiment and want to see what people think.  
在这里我们暂停一下。我们在分支上进行更改，打开拉取请求，并在合并之前等待反馈。也许我们不确定我们是否采取了正确的方法。也许有些代码我们不太满意，但我们不确定如何改进它。也许您已经做了一个实验并想看看人们的想法。

Modern code review tools offer a great space for this kind of conversation and you can even get a whole team together to look at a Pull Request and discuss it.  
现代代码审查工具为这种对话提供了很大的空间，您甚至可以让整个团队聚集在一起查看拉取请求并进行讨论。

Works great when: 在以下情况下效果很好：

-   Will this work? 这行得通吗？
-   How do we feel about this new approach?  
    我们对这种新方法有何看法？
-   I need help to make this better please  
    我需要帮助来改善这个问题
-   I'm done for today, will merge tomorrow  
    今天就完成了，明天合并

## The rules 规则

-   Code review, or “Approval”, should not be a requirement for a Pull Request to be merged.  
    代码审查或“批准”不应成为合并拉取请求的要求。
-   People get to merge their own Pull Requests. This way they’re in control of whether their change is a “Show” or an “Ask”, and they can decide when it goes live.  
    人们可以合并自己的 Pull 请求。通过这种方式，他们可以控制更改是“显示”还是“询问”，并且可以决定更改何时上线。
-   We’ve got to use all the great Continuous Integration and [Continuous Delivery](https://martinfowler.com/bliki/ContinuousDelivery.html) techniques that help keep the mainline releasable. Take [Feature Toggles](https://martinfowler.com/bliki/FeatureToggle.html) as one example.
-   Our branches should not live long, and we should rebase them on the mainline often.

## The conversation

While Pull Requests can be a useful way of talking about changes, they have some pitfalls. The most alluring [Anti Pattern](https://martinfowler.com/bliki/AntiPattern.html) is the idea that they can replace other ways of having a conversation.

One common problem with branching is that folks decide on an approach without discussing it. By the time a Pull Request is opened, time has been invested in a solution that may be sub-optimal. Reviewers are influenced by the selected solution and find it harder to suggest alternative approaches. The bigger the change-sets and the longer-living the branches, the worse this problem becomes. Talk to your team before you start, so you can get better ideas and avoid rework.

Remember that Pull Requests are not the only way to Show or Ask. Hop on a call or walk over to someone's desk. Show your work early and often. Ask for help and feedback early and often. Work on tasks together.

Not opening a Pull Request is also not a reason to avoid a conversation about the code. It’s important that your team still has a good feedback culture and talk to each other about what you think and learn.

## The balance

Now there are three options – which one should I be choosing more often?

It depends. I think each team will have their own balance at any given time.

When you’re delivering features in an established pattern, you’ll be doing more “Shipping”. When you’ve got a high degree of trust in the team and folks share the same quality standards, you’ll be doing more “Shipping” too.

But if you’re still getting to know each other or you’re all doing something new, then there’s a bigger need for conversation and so you’ll do more “Showing” and “Asking”. A junior engineer might often “Show” and “Ask”. A senior engineer might “Ship” a lot but occasionally “Show” a new technique or a refactoring everyone should try.

Some teams won't have much flexibility. Certain industries are highly regulated and an approval or review process will be required for every change. There are a variety of ways to implement this – whether you branch or not – which I won't go into here.

## Should my team adopt this approach?

You already have.

Think about how your team works and you’ll notice you’re doing some balance of Ship/Show/Ask. Most teams I’ve seen fall into one of two brackets: “Mostly Ship” or “Mostly Ask”.

### If you mostly ship

If you rarely branch and all commits go straight to the mainline, you're “Mostly Shipping”. If this is you, think about whether doing some “Showing” might help you.

A big part of why Pull Request models have become so popular is that they support remote-first and asynchronous teams. Explicitly “Showing” the interesting parts of your work to others can help them learn and feel included in the conversation, especially when they work remotely or different hours.

I’ve also found (especially in teams that don’t talk enough 1), always committing to mainline can mean problematic changes are only noticed weeks after they’re made. By this time it’s difficult to have a useful conversation about them because the details have gone fuzzy. Encouraging team members to use the “Show” approach means you can have more conversations about the code as you go.

### If you mostly ask

If your team is opening Pull Requests for most changes, you’re “Mostly Asking”. While Pull Requests are a useful tool for quality and feedback, they have a scaling problem. The unavoidable thing about waiting for approval is that it takes time. If too many changes are in the queue for feedback, either the quality of the feedback goes down or progress slows down. Try “Showing” more so you can get the best of both worlds.

The reason you’re reliant on a lot of “Asking” might be that you have trust issue. “All changes must be approved” or “Every pull request needs 2 reviewers” are common policies, but they show a lack of trust in the development team.

This is problematic, because an approval step is only a band-aid – it won’t fix your underlying trust issues. Do a bit more “Showing”, so you can release some of the pressure in your development pipeline. Then focus your efforts on activities that build trust, such as training, team discussions, or ensemble programming. Every time a developer “Shows” rather than “Asks” is an opportunity for them to build trust with their team.

Another reason you’re relying on lots of “Asking” might be that you don’t have a safe way to put changes on the mainline. In this case, you’ll need to be learning about and implementing techniques to keep your mainline releasable. In the meantime, more “Showing” can be a way to reduce the barrier to taking safe changes to production. The reduced barrier will then also act as an incentive to team members – if you can find a way to make your change safe, it can go live sooner.

## Conclusion

So what is Ship/Show/Ask? Fundamentally, it’s two things:

First – a trick to help you get the best of both worlds – merge your own pull request without waiting for feedback, then pay attention to the feedback when it comes.

Second – a more inclusive, dynamic way of viewing branching strategies. Ship/Show/Ask reminds us that each team’s approach sits on a continuum somewhere between “Always Ship” and “Always Ask”. It encourages us to think about each change independently and ask ourselves – should I Ship, Show or Ask?

___
