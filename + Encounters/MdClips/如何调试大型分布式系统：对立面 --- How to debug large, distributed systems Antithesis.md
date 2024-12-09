---
title: 如何调试大型分布式系统：对立面 --- How to debug large, distributed systems: Antithesis
categories: []
date: 2024-11-17T13:19:43 (UTC +08:00)
tags: []
source: https://newsletter.pragmaticengineer.com/p/antithesis?utm_source=%2Finbox&utm_medium=reader2
author: Gergely Orosz, Elin Nilsson
---


# 如何调试大型分布式系统：对立面 --- How to debug large, distributed systems: Antithesis

> ## Excerpt
> A brief history of debugging, why debugging large systems is different, and how the “multiverse debugger” built by Antithesis attempts to take on this challenging problem space

---
<!--more-->

Debugging is one of those things all engineers do, but little has changed in _how_ we debug for decades. For example, debugging by printing to the console output or by logging is still pretty common, even though there’s decent debuggers that can be used across IDEs.  
调试是所有工程师都会做的事情之一，但几十年来我们的调试_方式_几乎没有改变。例如，通过打印到控制台输出或通过日志记录进行调试仍然很常见，尽管有可以跨 IDE 使用的不错的调试器。

Believe it or not, some debugging tools today are actually _less_ advanced than in the old days. Steve Yegge, head of engineering at Sourcegraph – [said](https://newsletter.pragmaticengineer.com/p/steve-yegge) last year:  
不管你相信与否，今天的一些调试工具实际上_不如_以前先进。 Sourcegraph 工程主管 Steve Yegge去年[表示](https://newsletter.pragmaticengineer.com/p/steve-yegge)：

> “I saw the best debugger I’ve ever used at GeoWorks, in 1990. To this day, I’ve yet to see a debugger do what theirs did back then: path choice on the fly, undo on the spot, or step an instruction backwards.”  
> “1990 年，我在 GeoWorks 上看到了我用过的最好的调试器。直到今天，我还没有看到调试器能完成他们当时所做的事情：即时路径选择、当场撤消或单步执行指令倒退。”

This stagnant rate of progress makes it very interesting that there’s a small engineering team working today on building a _much better_ debugging tool, which specifically focuses on debugging large and distributed systems. It’s called Antithesis, and is the focus of this article.   
这种停滞不前的进展速度使得今天有一个小型工程团队正在致力于构建一个_更好的_调试工具，该工具专门专注于调试大型分布式系统，这非常有趣。它称为对立，也是本文的重点。

Today, we cover: 今天，我们介绍：

1.  Brief history of debugging  
    调试简史
    
2.  Antithesis’ “multiverse debugger”  
    Antithesis 的“多元宇宙调试器”
    
3.  Q&A with Antithesis co-founder, Will Wilson  
    与 Antithesis 联合创始人 Will Wilson 的问答
    
4.  Tech stack 技术栈
    
5.  Engineering team and culture  
    工程团队和文化
    
6.  Advanced testing tools for better bug management  
    先进的测试工具可实现更好的错误管理
    
7.  Better bug management with advanced testing tools  
    使用先进的测试工具更好地管理错误
    
8.  Tradeoffs of complexity 复杂性的权衡
    

_As always with these deep dives about a vendor, this publication has no affiliation with Antithesis, and was not paid for this article. Check out [our ethics policy.](https://blog.pragmaticengineer.com/ethics-statement/)  
与往常一样，对供应商进行深入研究，本出版物与 Antithesis 没有任何关系，并且没有为本文付费。查看[我们的道德政策。](https://blog.pragmaticengineer.com/ethics-statement/)_

## 1\. Brief history of debugging  
1\. 调试简史

Debugging and software development have gone hand in hand since the earliest days of computing. But why do we call it ‘debugging’? The etymology is a bit obscure, but it could include a real-life insect.  
从计算机诞生之初起，调试和软件开发就一直齐头并进。但为什么我们称其为“调试”呢？词源有点晦涩，但它可能包括现实生活中的昆虫。

#### First “debugged” computer  
第一台“调试”计算机

In 1947, a team of scientists at Harvard University including computer science pioneer, [Grace Hopper](https://en.wikipedia.org/wiki/Grace_Hopper), found a moth trapped in a relay of the Mark II mainframe computer which was causing it to malfunction. The fault was documented, and the moth itself was added to a hand-written record, reading: “...first actual case of bug being found.”  
1947 年，哈佛大学的一个科学家团队（包括计算机科学先驱[Grace Hopper](https://en.wikipedia.org/wiki/Grace_Hopper) ）发现一只飞蛾被困在 Mark II 大型计算机的继电器中，导致其发生故障。该错误被记录下来，飞蛾本身也被添加到手写记录中，上面写着：“……发现错误的第一个实际案例。”

Faults were called “bugs” before this incident, but the serendipitous episode may have helped cement the term “debugging” in the lexicon. Several computer science papers from the 1950s mention “debugging” in passing, which suggests the word was in use and its meaning was common knowledge among professionals. It also appears in the 1963 manual of the first time-sharing operating system, the Compatible Time-Sharing System ([CTSS](https://en.wikipedia.org/wiki/Compatible_Time-Sharing_System).)  
在此事件之前，故障被称为“bug”，但这次偶然的事件可能有助于巩固“调试”一词在词典中的地位。 20 世纪 50 年代的几篇计算机科学论文顺便提到了“调试”，这表明这个词已经被使用，而且它的含义是专业人士的常识。它也出现在 1963 年第一个分时操作系统兼容分时系统（ [CTSS](https://en.wikipedia.org/wiki/Compatible_Time-Sharing_System) ）的手册中。

#### Evolution of debugging tools  
调试工具的演变

Programmers have always built tools to make their lives easier, and debuggers are a case in point. Here’s how the toolset evolved from the 1960s.  
程序员总是构建工具来让他们的生活更轻松，调试器就是一个很好的例子。以下是该工具集自 20 世纪 60 年代以来的演变过程。

**1960s: punch card era.** The earliest debugging tools:  
**20世纪60年代：打卡时代。**最早的调试工具：

-   **Typewriter debugging:** [DEC Debugging Tape](https://www.computerhistory.org/pdp-1/189cc577e7b13aafbb0efab4c547d262/) (DDT): a debugger program that worked on a typewriter! It allowed the modifying of a program or its data on the mainframe, while it was running. (DEC stands for “Digital Equipment Corporation”, which was a major computer hardware company of the time.) This was an era when the typewriter served as the command line interface. See the [full manual for commands](https://www.computerhistory.org/pdp-1/_media/pdf/DEC.pdp_1.1964.102650078.pdf).   
    **打字机调试：** [DEC 调试磁带](https://www.computerhistory.org/pdp-1/189cc577e7b13aafbb0efab4c547d262/)(DDT)：在打字机上运行的调试程序！它允许在主机运行时修改程序或其数据。 （DEC 代表“数字设备公司”，是当时一家主要的计算机硬件公司。）这是一个以打字机作为命令行界面的时代。请参阅[命令的完整手册](https://www.computerhistory.org/pdp-1/_media/pdf/DEC.pdp_1.1964.102650078.pdf)。
    
-   **Online Debugging Tool** ([ODT](https://en.wikipedia.org/wiki/On-line_Debugging_Tool)): a family of debugger programs that allowed the accessing of memory using [octal addresses](https://en.wikipedia.org/wiki/Octal) while software ran. Also produced by the Digital Equipment Corporation.  
    **在线调试工具**（ [ODT](https://en.wikipedia.org/wiki/On-line_Debugging_Tool) ）：一系列调试器程序，允许在软件运行时使用[八进制地址](https://en.wikipedia.org/wiki/Octal)访问内存。也由数字设备公司生产。
    

**1970s: (symbolic) debuggers.** New, powerful programming languages like [C](https://en.wikipedia.org/wiki/C_(programming_language)), [FORTRAN](https://en.wikipedia.org/wiki/Fortran) and [COBOL](https://en.wikipedia.org/wiki/COBOL) were developed in the ‘70s, which allowed fetching of symbol maps that showed the memory addresses of variables. Symbol maps were used for more efficient debugging, as they made it unnecessary to manually track memory addresses. The tools in use today are symbolic debuggers.  
**20 世纪 70 年代：（象征性的）调试器。**新的、强大的编程语言，如[C](https://en.wikipedia.org/wiki/C_(programming_language)) 、 [FORTRAN](https://en.wikipedia.org/wiki/Fortran)和[COBOL](https://en.wikipedia.org/wiki/COBOL)是在 70 年代开发的，它们允许获取显示变量内存地址的符号映射。符号映射用于更有效的调试，因为它们使得无需手动跟踪内存地址。目前使用的工具是符号调试器。

**Late 1970s: breakpoints.** With the ability to inspect the memory of a running program and to get a memory dump, the next debugging task is to halt program execution on a given condition, like a variable reaching a certain value. [Breakpoints](https://en.wikipedia.org/wiki/Breakpoint) allow for precisely that.   
**20 世纪 70 年代末：断点。**有了检查正在运行的程序的内存并获取内存转储的能力，下一个调试任务就是在给定条件下停止程序执行，例如变量达到某个值。[断点](https://en.wikipedia.org/wiki/Breakpoint)正是可以实现这一点。

The core functionality of halting program execution emerged in the 1940s, with involved approaches like removing cables, deliberately causing program crashes, and via hardware switches. Over time, the utility and usability of breakpoints evolved, and by the end of the ‘70s, they were in symbolic debuggers in ways recognisable today. More advanced tools added the option of allowing a program to advance one step forward (step forward) and the more complex functionality of going back (step back.)  
停止程序执行的核心功能出现于 20 世纪 40 年代，涉及的方法包括移除电缆、故意导致程序崩溃以及通过硬件开关。随着时间的推移，断点的实用性和可用性不断发展，到 70 年代末，它们以今天可识别的方式出现在符号调试器中。更高级的工具添加了允许程序前进一步（前进）的选项和更复杂的后退功能（后退）。

**Mid-1980s: “modern debugging.”** From the 1980s, the software development experience continued to evolve with better terminals, more interactivity, and ever-tighter feedback loops. Debugging improvements followed a similar pattern. For example, in 1983 Turbo Pascal introduced its IDE with built-in debugging capabilities – which might have been the first “mainstream” IDE with debugging enabled.   
**20 世纪 80 年代中期：“现代调试。”**从 20 世纪 80 年代开始，软件开发体验不断发展，终端越来越好，交互性越来越强，反馈循环也越来越紧。调试改进遵循类似的模式。例如，1983 年 Turbo Pascal 推出了具有内置调试功能的 IDE，这可能是第一个启用调试功能的“主流”IDE。

Graphic debugging tools with visual breakpoints and output were innovations of this time. Remote debugging – debugging programs running over networks – became possible with the spread of the internet.  
具有可视断点和输出的图形调试工具是当时的创新。随着互联网的普及，远程调试（调试通过网络运行的程序）成为可能。

**Today’s modern debugging tools have modern features,** such as:  
**当今的现代调试工具具有现代功能，**例如：

-   **Time-travel debugging.** Also known as “reverse debugging”, this is most common within functional programming and in deterministic environments. It allows recreating issues, and to “step backwards” to figure out root causes. _Today’s deep dive is on one such tool, Antithesis._  
    **时间旅行调试。**也称为“反向调试”，这在函数式编程和确定性环境中最常见。它允许重现问题，并“后退一步”找出根本原因。_今天的深入探讨就是这样一个工具：Antithesis。_
    
-   **Record and replay debugging**. The application state is recorded in each step of the process and can be replayed. Recordings tend to include memory state, memory interactions, inputs, and system resource status markers, among others. [ReDevBug](https://revdebug.com/) does this.  
    **记录并回放调试**。应用程序状态记录在流程的每个步骤中，并且可以重播。记录往往包括内存状态、内存交互、输入和系统资源状态标记等。 [ReDevBug](https://revdebug.com/)就是这样做的。
    
-   **Automatic debugging.** Tools that can automatically locate and sometimes fix bugs in code. These debuggers are usually ML or AI-driven.  
    **自动调试。**可以自动定位并有时修复代码中的错误的工具。这些调试器通常是机器学习或人工智能驱动的。
    
-   **AI-assisted debugging.** The latest wave of debugging uses GenAI to predict and locate bugs in a more efficient manner. It’s early days, but we can expect more solutions like this.  
    **AI辅助调试。**最新一波调试使用 GenAI 以更有效的方式预测和定位错误。现在还处于早期阶段，但我们可以期待更多这样的解决方案。
    

## 2\. Antithesis’s ‘multiverse debugger’  
2.Antithesis的“多元宇宙调试器”

[Antithesis](https://antithesis.com/) was founded in 2018 with the vision of a better way to test systems, and it has raised an impressive $47M (!!) in seed funding. The business model is usage-based pricing, based on the number of CPUs used for testing activities; a good analogy is Amazon renting out its EC2 servers. Today, Antithesis sells cores on an annually-reserved basis, with a minimum for getting started with, and hopes to offer more flexibility in the future, I’m told.  
[Antithesis](https://antithesis.com/)成立于 2018 年，其愿景是提供更好的系统测试方法，并已筹集了令人印象深刻的 4700 万美元（！！）种子资金。商业模式是基于使用量的定价，基于用于测试活动的 CPU 数量；一个很好的类比是亚马逊出租其 EC2 服务器。据我所知，如今，Antithesis 以每年预留的方式销售核心，并提供最低入门价格，并希望在未来提供更大的灵活性。

Time-travel debugging tools are usually limited to functional languages where state management is simple, or to deterministic environments; like in well-defined sandboxes. For most real-world programs, no time travel option is available for debugging, so when a backend service crashes non-deterministically, there’s no good way to turn back time and investigate it; the best option is usually to add more logging to help explain future crashes.  
时间旅行调试工具通常仅限于状态管理简单的函数式语言或确定性环境；就像在明确定义的沙箱中一样。对于大多数现实世界的程序来说，没有时间旅行选项可用于调试，因此当后端服务非确定性崩溃时，没有好的方法可以回溯时间并进行调查；最好的选择通常是添加更多日志记录以帮助解释未来的崩溃。

#### Building a time machine 建造一台时间机器

The Antithesis team spent several years building a system that acts like a time machine. It wraps your current system, and lets you rewind your steps. Within the “wrapper”, to rewind the state of the system to 5 seconds earlier, you type:   
Antithesis 团队花了几年时间构建了一个像时间机器一样的系统。它包含您当前的系统，并让您倒回您的步骤。在“包装器”中，要将系统状态倒回到 5 秒前，请键入：

branch = branch.end.rewind(5).branch   
分支=branch.end.rewind(5).branch

Files deleted within the last five seconds come back, including if deleted permanently without being put in deleted file storage. Any changes made in files since are also undone.  
过去五秒内删除的文件将恢复，包括永久删除但未放入已删除文件存储的情况。此后对文件所做的任何更改也将被撤消。

**Creating the time machine means creating a deterministic simulation,** which can progress from its starting point to the future, arbitrarily. It can go back in time, too, which raises interesting possibilities. For example, if your server crashed: wouldn’t it be great to “rewind” time and attach a debugger? In a simulated system, you can do this: simulate the system to the point where the process will crash, then add a debugger or export a memory dump. Similarly, if a user reports that their session was slow: it’s now possible to go “back in time” by recreating their session, and attaching a debugger.  
**创建时间机器意味着创建确定性模拟，**它可以任意地从起点发展到未来。它也可以回到过去，这带来了有趣的可能性。例如，如果您的服务器崩溃了：“倒带”时间并附加调试器不是很好吗？在模拟系统中，您可以这样做：将系统模拟到进程将崩溃的程度，然后添加调试器或导出内存转储。同样，如果用户报告其会话速度很慢：现在可以通过重新创建会话并附加调试器来“回到过去”。

**Having a deterministic simulator creates previously hard-to-achieve scenarios**, such as:  
**拥有确定性模拟器会创建以前难以实现的场景**，例如：

-   Jump into the future; for example, by fast-forwarding a system 10 hours in the future, to inspect how memory usage and CPU usage will trend at that time. This is not a prediction, but it allows _actually_ inspecting the future state of the system!  
    跳向未来；例如，通过快进未来10个小时的系统，以检查当时的内存使用率和CPU使用率的趋势。这不是预测，但它允许_实际_检查系统的未来状态！
    
-   Generate more logs to work with. When a suspicious event is identified in the present, you can go back in time and add more logging to where this event may have originated from. You could also enable detailed logging across the system for a few minutes or seconds before an event occurs.  
    生成更多日志以供使用。当当前发现可疑事件时，您可以及时返回并在该事件可能的来源位置添加更多日志记录。您还可以在事件发生之前在系统中启用几分钟或几秒钟的详细日志记录。
    
-   Change the past. Go back to before a crash happened, and change the code executing.  
    改变过去。返回到崩溃发生之前，并更改正在执行的代码。
    

#### What Antithesis does 对立题有什么作用

Antithesis is not only a time-traveling debugger, though. A good way to describe it is as **“Deterministic Simulation Testing** (DST) as a service.”  
不过，Antithesis 不仅仅是一个时间旅行调试器。描述它的一个好方法是**“确定性模拟测试**(DST) 即服务”。

Deterministic Simulation Testing (DST) is a technique of building a simulation in which software can run in a single thread, and where you’re in control of all variables like time, randomness, etc., in order to achieve determinism during testing.  
确定性模拟测试 (DST)是一种构建模拟的技术，其中软件可以在单线程中运行，并且您可以控制时间、随机性等所有变量，以便在测试期间实现确定性。

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff92726d-9ccc-4933-93bb-8554c605970e_1600x1008.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff92726d-9ccc-4933-93bb-8554c605970e_1600x1008.png)

What is DST? One explanation  
什么是夏令时？一种解释

DST is a combination of:  
DST 是以下各项的组合：

-   **Fuzzing**: also referred to as “[fuzz testing](https://en.wikipedia.org/wiki/Fuzzing),” this is automated testing that inputs invalid, unexpected, or random inputs to a program.  
    **模糊测试**：也称为“[模糊测试](https://en.wikipedia.org/wiki/Fuzzing)”，这是一种向程序输入无效、意外或随机输入的自动化测试。
    
-   **Assertions:** making logical statements that should always be true or false, and breaking the program when an assertion fails; e.g.; asserting that an integer variable’s value is always greater than zero, so the program breaks when this condition fails.  
    **断言：**做出应该始终为真或假的逻辑语句，并在断言失败时中断程序；例如;断言整数变量的值始终大于零，因此当此条件失败时程序将中断。
    
-   **Shotgun debugging:** making random changes to software and seeing if it fixes the bug.   
    **Shotgun 调试：**对软件进行随机更改并查看是否修复了错误。
    
-   **Time travel debugging:** the ability to “step backward and forward in time,” within the state of the program.  
    **时间旅行调试：**在程序状态内“及时向后和向前步进”的能力。
    

Doing Deterministic Simulation Testing is really hard for any system because you have to build _everything_ from scratch. No existing frameworks and libraries without support for all time-traveling, debugging, fuzzing, etc, can be used. One of the first “proper” usages of DST was within the distributed database, [FoundationDB](https://www.foundationdb.org/), one of whose creators is Antithesis cofounder, Will Wilson.  
对于任何系统来说，进行确定性模拟测试都非常困难，因为您必须从头开始构建_一切_。不支持所有时间旅行、调试、模糊测试等的现有框架和库都不能使用。 DST 的第一个“正确”用法是在分布式数据库[FoundationDB](https://www.foundationdb.org/)中，其创建者之一是 Antithesis 联合创始人 Will Wilson。

Because implementing DST is so difficult, Antithesis made the c_omputer/hypervisor_ deterministic, instead. This means anything that runs on this Antithesis computer/hypervisor can be tested with DST, without doing everything yourself.  
由于实施 DST 非常困难，因此 Antithesis 使计算机_/管理程序_具有确定性。这意味着在此 Antithesis 计算机/虚拟机管理程序上运行的任何内容都可以使用 DST 进行测试，而无需亲自执行所有操作。

And thanks to running a fully deterministic environment, Antithesis can manipulate it into weird states on purpose, which allows developers to inspect weird states and bugs to find out their causes. _[Read more on how Antithesis works](https://antithesis.com/product/how_does_antithesis_work/)._  
由于运行完全确定性的环境，Antithesis 可以故意将其操纵到奇怪的状态，这使得开发人员可以检查奇怪的状态和错误以找出其原因。_[详细了解 Antithesis 的工作原理](https://antithesis.com/product/how_does_antithesis_work/)。_

## 3\. Q&A with Antithesis co-founder, Will Wilson  
3\. 与 Antithesis 联合创始人 Will Wilson 的问答

The company’s CEO took some questions from us, and in this section the questions are _italicized_, with Will’s responses in normal text.  
该公司的首席执行官回答了我们的一些问题，在本节中，问题以_斜体字_显示，威尔的回答则为普通文本。

#### How debugging large systems is different  
调试大型系统有何不同

_The Antithesis tool was built to debug large and complex systems, but how are these systems different from common ones like single services, apps, and single-threaded websites?  
Antithesis 工具旨在调试大型且复杂的系统，但这些系统与单一服务、应用程序和单线程网站等常见系统有何不同？_

‘A few things make large systems different:  
“有几件事使大型系统与众不同：

-   **Bizarre failures are a certainty**. If your software runs on one computer, things like bitflips in memory, or corruption on disk are exceptionally uncommon. If your software runs on a cluster with tens of thousands of machines, you’d better have a plan for it.  
    **离奇的失败是必然的**。如果您的软件在一台计算机上运行，那么内存中的位翻转或磁盘损坏之类的情况就非常罕见。如果你的软件运行在拥有数万台机器的集群上，你最好有一个计划。
    
-   **Expectations are usually higher.** If your software runs on one computer, and it crashes, there’s not a lot your software can do to improve the situation, except not losing any durable state. But if your software runs on a large cluster, people probably expect it to function if one or two machines die.  
    **期望通常更高。**如果您的软件在一台计算机上运行并且崩溃了，那么除了不丢失任何持久状态之外，您的软件无法做太多事情来改善这种情况。但是，如果您的软件在大型集群上运行，人们可能希望在一两台机器死机时它仍能正常运行。
    
-   **Concurrency plays a bigger role.** You can get in trouble with multi-threaded systems on a single machine, but with many machines and unreliable/noisy networks between them, it gets so much worse.  
    **并发发挥着更大的作用。**您可能会在单台机器上使用多线程系统时遇到麻烦，但是对于许多机器以及它们之间不可靠/嘈杂的网络，情况会变得更糟。
    
-   **Timestamps are meaningless.** Unless you’re Google and have atomic clocks in your datacenters, you need to assume that clocks on different machines are not perfectly synchronized, which can make reading logs very confusing. You may literally not know whether an event started on system A or system B!  
    **时间戳毫无意义。**除非您是 Google 并且数据中心内有原子钟，否则您需要假设不同机器上的时钟不完全同步，这可能会使读取日志变得非常混乱。您实际上可能不知道事件是在系统 A 还是系统 B 上启动的！
    
-   **Large systems probably don’t “fit inside the head” of any person,** which can make reasoning through the state machine the old fashioned way, much harder. Also, the sheer length of time and numbers of people it takes to build these systems, means there are many opportunities to lose institutional knowledge, or memories to fade.’  
    **大型系统可能不适合任何人的“头脑”，**这可能会使通过状态机以老式方式进行推理变得更加困难。此外，建立这些系统所需的时间和人员数量，意味着有很多机会失去机构知识或记忆褪色。
    

‘All of the above make testing and debugging large systems much harder, especially the first three points. Many failure modes of large-scale systems are “external” or environmental, and to do with hardware faults, network messages getting delayed, or weird pauses on a thread. These are harder to reason about in advance, and they’re _monumentally_ harder to test for and debug, as they may depend on highly specific conditions or timings that are almost impossible to reproduce on demand.  
“以上所有因素都使得测试和调试大型系统变得更加困难，尤其是前三点。大型系统的许多故障模式都是“外部”或环境性的，与硬件故障、网络消息延迟或线程上奇怪的暂停有关。这些很难提前推理，而且测试和调试也_非常_困难，因为它们可能依赖于高度特定的条件或时序，而这些条件或时序几乎不可能按需重现。

**‘The paradox of distributed systems is that a one-in-a-million bug can be a huge urgent problem** because you’re processing millions of requests all the time, so the bug will occur frequently. But, it’s still a one-in-a-million bug, so a test probably won’t reproduce it!’  
**“分布式系统的悖论在于，百万分之一的错误可能是一个巨大的紧急问题**，因为您一直在处理数百万个请求，因此错误会频繁发生。但是，它仍然是百万分之一的错误，因此测试可能无法重现它！”

#### How Antithesis is used 如何使用对偶

_Where does Antithesis fit into customers’ software delivery and process timelines?  
Antithesis 在哪里适合客户的软件交付和流程时间表？_

‘We see customers using Antithesis in very different ways. There are teams who run short tests on almost every PR, or who run long tests overnight or weekends, and some teams only pull it out when trying to track down a really crazy bug.   
“我们看到客户以非常不同的方式使用 Antithesis。有些团队几乎对每个 PR 都进行短期测试，或者在夜间或周末进行长时间测试，而有些团队只有在试图追踪真正疯狂的 bug 时才将其拉出来。

‘We don’t tell our customers they should eliminate any of their existing tests because it’s probably inexpensive to keep them, and we don’t want to be the cause of any outage or emergency. That said, many customers stop investing as much in non-Antithesis tests, and instead try to find ways to use our platform for as much testing as possible.  
“我们不会告诉客户他们应该取消任何现有的测试，因为保留它们可能成本不高，而且我们不想成为任何停电或紧急情况的原因。也就是说，许多客户停止在非对立测试上投入尽可能多的资金，而是尝试寻找方法使用我们的平台进行尽可能多的测试。

‘Some customers have come up with really creative ways to use our platform. For example, who said this tool can _only_ be used for hunting bugs? It’s a general platform for looking for _any_ behavior in software systems. For example it can help answer questions like:  
“一些客户想出了非常有创意的方式来使用我们的平台。例如，谁说这个工具只能_用来_寻找bug？它是一个用于查找软件系统中_任何_行为的通用平台。例如，它可以帮助回答以下问题：

> “Can function A _ever_ run before function B? Or does this function _ever_ get called with a negative parameter?”  
> “函数 A 可以在函数 B 之前运行_吗_？或者这个函数是否_曾经_被使用负参数调用过？”

‘**Most of what Antithesis “replaces” is human effort of the really annoying, unpleasant kind,** like adding logging, then waiting for it to happen again in production. Or designing weird, ad-hoc fault injection systems in end-to-end tests. Or writing a script to run an integration test dozens of times to chase down an intermittent problem that only occurs once every ten runs. Basically, the stuff no programmer enjoys doing.’  
Antithesis“取代”的大部分内容**都是非常烦人、不愉快的人类工作，**比如添加日志记录，然后等待它在生产中再次发生。或者在端到端测试中设计奇怪的临时故障注入系统。或者编写一个脚本来运行集成测试数十次，以追踪每十次运行才发生一次的间歇性问题。基本上，这是程序员不喜欢做的事情。”

## 4\. Tech stack 4.技术栈

_What is the tech stack behind Antithesis? DST is hard to do with existing libraries, so which frameworks you might use instead of writing a bespoke one?  
Antithesis 背后的技术堆栈是什么？ DST 很难用现有的库来实现，那么您可以使用哪些框架而不是编写定制的框架？_

‘We have a pretty bad case of “not-invented here” syndrome. Basically, compared to most companies, we see a larger cost to adopting lots of third-party dependencies. So we bias towards building tools in house that do _exactly_ what we need, which means our tech stack is very “home-grown”.  
“我们有一个非常糟糕的“非这里发明”综合症。基本上，与大多数公司相比，我们发现采用大量第三方依赖项的成本更大。因此，我们倾向于在内部构建_完全_满足我们需要的工具，这意味着我们的技术堆栈是非常“本土化”的。

**‘Languages** we use often:  
'我们经常使用的**语言**：

-   [C](https://en.wikipedia.org/wiki/C_(programming_language)) and [C++](https://en.wikipedia.org/wiki/C%2B%2B): languages with low-level memory manipulation, helpful for high-performance scenarios and necessary for kernel-mode code  
    [C](https://en.wikipedia.org/wiki/C_(programming_language))和[C++](https://en.wikipedia.org/wiki/C%2B%2B) ：具有低级内存操作的语言，有助于高性能场景，并且是内核模式代码所必需的
    

-   [Rust](https://www.rust-lang.org/): a modern programming language emphasizing performance, type safety and concurrency  
    [Rust](https://www.rust-lang.org/) ：一种强调性能、类型安全和并发性的现代编程语言
    
-   [Typescript](https://www.typescriptlang.org/): a language adding static typing for JavaScript. Popular across backend and frontend domains  
    [Typescript](https://www.typescriptlang.org/) ：一种为 JavaScript 添加静态类型的语言。在后端和前端领域很受欢迎
    
-   [Nix](https://nix.dev/manual/nix/2.18/language/index.html): a language to create derivations (precise descriptions of how contents of existing files are used to derive new files)  
    [Nix](https://nix.dev/manual/nix/2.18/language/index.html) ：一种创建派生的语言（精确描述如何使用现有文件的内容派生新文件）
    

‘Our major dependencies: '我们的主要依赖：

-   [Nix/NixOS](https://nixos.org/): a tool for package management and system configuration  
    [Nix/NixOS](https://nixos.org/) ：包管理和系统配置工具
    
-   [BigQuery](https://cloud.google.com/bigquery): a managed serverless data warehouse product by Google  
    [BigQuery](https://cloud.google.com/bigquery) ：Google 的托管无服务器数据仓库产品
    
-   Hypervisor: we use a fork/rewrite of the FreeBSD kernel hypervisor, [bhyve](https://en.wikipedia.org/wiki/Bhyve).  
    虚拟机管理程序：我们使用 FreeBSD 内核虚拟机管理程序的分叉/重写， [bhyve](https://en.wikipedia.org/wiki/Bhyve) 。
    

**‘Our homegrown stack** is surprisingly large!  
**“我们的本土堆栈**出奇地大！”

-   **Hypervisor**: custom-built for our needs; [more details here.](https://antithesis.com/blog/deterministic_hypervisor/)  
    **Hypervisor** ：根据我们的需求定制；[更多详细信息请参见此处。](https://antithesis.com/blog/deterministic_hypervisor/)
    
-   **A fully-reactive browser-based Javascript notebook**. It has sophisticated dependency tracking. We currently use it to deliver the multiverse [debugging experience](https://antithesis.com/blog/multiverse_debugging/)  
    **完全响应式的基于浏览器的 Javascript 笔记本**。它具有复杂的依赖性跟踪。我们目前使用它来提供多元宇宙[调试体验](https://antithesis.com/blog/multiverse_debugging/)
    
-   **Fuzzer**: optimized for [exploring the state space](https://antithesis.com/blog/sdtalk/) of interactive programs (read [more about fuzzing](https://en.wikipedia.org/wiki/Fuzzing))  
    **Fuzzer** ：针对探索交互式程序的[状态空间](https://antithesis.com/blog/sdtalk/)进行了优化（阅读[有关模糊测试的更多信息](https://en.wikipedia.org/wiki/Fuzzing)）
    
-   **Fault injector:** a testing tool to deliberately introduce failures, errors or problematic conditions  
    **故障注入器：**故意引入故障、错误或有问题情况的测试工具
    
-   **Binary instrumentation** for customer software: inserting additional code (instrumentation code) into a customer’s compiled program to analyze its behavior during runtime.  
    客户软件的**二进制检测**：将附加代码（检测代码）插入客户编译的程序中，以分析其在运行时的行为。
    
-   **Customizable Linux environment**: what customers’ software run in  
    **可定制的Linux环境**：客户的软件运行在什么环境中
    
-   **Build system:** based on [Nix](https://en.wikipedia.org/wiki/Nix), which glues our systems together  
    **构建系统：**基于[Nix](https://en.wikipedia.org/wiki/Nix) ，它将我们的系统粘合在一起
    
-   **Infrastructure and security mechanisms**, built to ensure we run a [trusted computing base](https://antithesis.com/security/manifesto/)  
    **基础设施和安全机制**，旨在确保我们运行一个[值得信赖的计算基础](https://antithesis.com/security/manifesto/)
    

‘Our homegrown stack is huge! One of the coolest things about working at Antithesis as an engineer is that if there’s any computer science topic you’re interested in, there’s a good chance we do it, at least a little.  
“我们的本土堆栈非常庞大！作为一名工程师，在 Antithesis 工作最酷的事情之一是，如果您对任何计算机科学主题感兴趣，我们很有可能会这样做，至少有一点。

#### Building a database 建立数据库

‘We started using BigQuery very early because the pricing model is unbeatable for a tiny startup with bursty workloads. But the data model did not make much sense for us.   
“我们很早就开始使用 BigQuery，因为对于具有突发工作负载的小型初创公司来说，定价模型是无与伦比的。但数据模型对我们来说没有多大意义。

‘Our use case is to analyze ordered streams of events: logs, code coverage events, etc. But because we have a deterministic multiverse which can fork, the stream of events form a _tree_ structure rather than a single linear history! But BigQuery is not well set up to handle trees of events, and neither is any other SQL database.   
“我们的用例是分析有序的事件流：日志、代码覆盖事件等。但是因为我们有一个可以分叉的确定性多元宇宙，所以事件流形成一个_树_结构而不是单个线性历史！但 BigQuery 并没有很好地设置来处理事件树，任何其他 SQL 数据库也是如此。

‘We managed to putter along for a while with crazy hacks. For instance, we built a new data structure called a "skip tree", inspired by the [skip list](https://en.wikipedia.org/wiki/Skip_list) which we implemented in SQL. This data type greatly improved the asymptotic performance of our queries (the performance characteristics at scale). However, we eventually got to the point of regularly crashing BigQuery's [planner](https://cloud.google.com/bigquery/docs/query-plan-explanation); at which point we knew we had to move to something else.   
“我们设法通过疯狂的黑客行为度过了一段时间。例如，受我们在 SQL 中实现的[跳跃列表](https://en.wikipedia.org/wiki/Skip_list)的启发，我们构建了一种称为“跳跃树”的新数据结构。这种数据类型极大地提高了我们查询的渐近性能（大规模的性能特征）。然而，我们最终达到了定期使 BigQuery 的[规划器](https://cloud.google.com/bigquery/docs/query-plan-explanation)崩溃的地步；那时我们知道我们必须转向其他事情。

‘We evaluated Snowflake, and its Recursive CTE feature, and also evaluated a large number of other SQL and NoSQL databases, but nothing fundamentally fixed the problem.  
“我们评估了 Snowflake 及其递归 CTE 功能，还评估了大量其他 SQL 和 NoSQL 数据库，但没有从根本上解决问题。

‘**We were hesitant to build our own database for ages, until a company hackathon** where a team tried writing a proof-of-concept analytic database for [folding](https://en.wikipedia.org/wiki/Fold_%28higher-order_function%29) Javascript functions up and down petabyte-scale trees, thrown together in a week using Amazon [S3](https://aws.amazon.com/s3/) and [Lambda](https://aws.amazon.com/lambda/). It actually worked!   
多年来，**我们一直在犹豫是否要建立自己的数据库，直到一次公司黑客马拉松**，其中一个团队尝试编写一个概念验证分析数据库，用于在 PB 级树上[折叠](https://en.wikipedia.org/wiki/Fold_%28higher-order_function%29)Javascript 函数，并使用 Amazon [S3](https://aws.amazon.com/s3/)和Amazon S3在一周内拼凑在一起。[拉姆达](https://aws.amazon.com/lambda/)。它确实有效！

‘We're cautious, and a lot of people on our team have built databases before. We know that the hardest part of building a database is not getting started, but towards the end of the project with testing and operationalizing. But we do have this really great technology for testing distributed systems!   
“我们很谨慎，我们团队中的很多人以前都建立过数据库。我们知道，构建数据库最困难的部分不是开始，而是在项目结束时进行测试和操作。但我们确实拥有这项非常出色的技术来测试分布式系统！

‘**We decided to write a custom database for** _**our**_ **needs, 100% tested with Antithesis.** We would have no other test plan except for running it with Antithesis! We are now nearing the end of the project, and so far, it’s going well!  
'我们决定根据_**我们的**_需求**编写一个自定义数据库****，并使用 Antithesis 进行 100% 测试。**除了使用对偶运行之外，我们没有其他测试计划！我们现在该项目已接近尾声，到目前为止，一切进展顺利！

‘If we succeed, it would solve a huge number of production issues with BigQuery, and enable us to launch some amazing new features. Plus, this project gives us the ultimate empathy with customers.   
“如果我们成功，它将解决 BigQuery 的大量生产问题，并使我们能够推出一些令人惊叹的新功能。另外，这个项目让我们对客户产生了终极的同理心。

## 5\. Engineering team and culture  
5\. 工程团队和文化

_Tell us about the engineering team’s values and practices.  
告诉我们工程团队的价值观和实践。_
