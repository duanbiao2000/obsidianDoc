---
aliases: 
categories: 
tags:
  - Mindset
  - Creative/Tutorial
  - Mindset/Meta
  - Action/TODO
  - Effective
---

# Prompts for Learning to Code with AI

## Introduction

Use these prompts to get started learning how to code from scratch or simply to have AI (like ChatGPT or Claude Opus) write and modify code for you. Make AI a tool in your toolbox! This set of prompts is relating to practical software engineering problems and concepts.

At the bottom of this doc is a glossary of high-level terms that you may want to plug into the prompts to learn more.

**Important note**: you _**need**_ to use a high-quality model such as **GPT-4 or Claude Opus** to make this work. ==Using GPT-3.5, Llama, or other similar models will only leave you frustrated and stuck. ==High-end models will generate much better code and explain things much more clearly (and correctly!)
<!--SR:!2025-03-25,3,250-->

## Exploring Concepts

- **Starter Prompts**
  - What is [X] / How does [X] work / What does [X] mean? How do I use [X]? `<--- simple but super effective`
  - I am a new developer learning how to code. Please help me create a basic [app idea] web app using the MERN stack
  - I am a new developer learning how to code. Please explain what [X] is and what role it plays in building software.
  - What are the alternatives to [X]? When and why would I use them?
  - I am a new developer interested in understanding the difference between [X] and [Y]. Could you explain?
    - In what scenarios would I choose [X] over [Y]? Please explain and provide examples.
  - Please explain what each line in this code does: `[paste the code]`
  - How do you [accomplish certain task]? Answer with a high level explanation and specific steps.

- **Follow-up Prompts**
  - Please rephrase this in a few simple sentences and include an example that would be really easy to understand.
  - I still don't get it; can you explain it in a simpler or different way
  - How can I use this? / What do I do with this? / Where do I put this?
  - What should I do next? / How can I build on this? / Are there any other ways to do this?
  - Are there any concerns or tradeoffs with this approach?
  - [Open a new Chat and start over] `<--- good when ChatGPT gets stuck rehashing the same ideas`

**Note**: Remember to always give the LLM (AI) the relevant context, whether it is the code you are investigating or your relative understanding and experience working with a certain technology.

## Coding

- **Writing new code**
  - I am building an app using [tech stack] and need some code to [do X]. Please write it for me.
  - I want to implement some new functionality in my [tech stack] app. This new code needs to do [X] and has to do it in a particular way: [Y]. Make sure it doesn't [Z]
    - `Modify this prompt as needed to specify complex requirements and things the AI should avoid. Just write out all the requirements in one initial go.`

- **Modifying code**
  - I have this code: `[code]`. Please modify it to [do X].
  - Please refactor this code so that it is more clean and functionality is properly separated: `[code]`
  - Please add error handling to this code: `[code]`
  - That code doesn't work because it also needs to [do X]. Can you modify it to do that?
  - Ok now that we have that working, we also need it to [do Y]. Can you modify it to do that?
  - I had to make a change to that code so the latest code is: `[code]`. `<--- make sure ChatGPT is staying up to date on your latest version of code`
  - Please state the _full_ code in your response

## Troubleshooting

- I tried to run that but got this error: `[error]` in the `[where you saw the error]`
- It's still not working; what should I check to make sure I am doing this the right way?
- I got this error: `[error]`. Is there a different way we can do this to avoid this error?
- I tried [X, Y, Z] but it is still not working. Any other ideas?
- Can you point me to some resources that would explain how this works?
- Please explain this line by line so I can troubleshoot it.

## Glossary / Terminology

These are various terms that you might not be familiar with but can act as starting points for learning with AI. Ask ChatGPT about these concepts to start building an understanding of how they all fit together. Feel free to incorporate these into your prompts to improve the quality

### Practical Terms (web development)


- **Server:** A physical or virtual machine that runs the backend code and serves the frontend to users. It processes requests, runs the application's backend logic, and manages resources.
- **Environment:** The setup or context in which a web application or development tool runs, often categorized as development, testing, staging, or production environments, each with its configurations and purposes.
- **API (Application Programming Interface):** A set of rules and protocols for building and interacting with software applications, enabling different software entities to communicate with each other.
- **Database:** A structured collection of data stored electronically. It's managed and accessed through a database management system (DBMS), allowing for data retrieval, insertion, update, and deletion.
- **Authentication (Auth):** The process by which an application verifies the identity of a user, typically through login credentials, ensuring that users are who they claim to be.
- **Authorization:** After authentication, it determines what resources and operations the authenticated user has permission to access and perform within an application.
- **Framework:** A comprehensive set of tools and libraries designed to simplify the development process of software projects by providing a structured foundation to build upon.
- **Library:** A collection of pre-written code that developers can use to optimize tasks, such as manipulating data or interfacing with certain hardware or software, without writing code from scratch.
- **Component:** A reusable element in UI design or a modular unit in software architecture, each with its own functionality.
- **Cookies:** Small pieces of data sent from a website and stored on the user's computer by the user's web browser while the user is browsing, used to remember information about the user for their next visit.
- **Sessions:** A way to store information across multiple page requests for a particular user, enabling persistence of state across the web application.
- **Service:** A function or set of functions provided by one part of a software system to others, focusing on accomplishing specific tasks. Typically a specific program running somewhere that can be invoked.
- **Microservice:** An architectural style that structures an application as a collection of small, autonomous services, each focusing on a single function or business capability.
- **Container:** Lightweight, standalone, executable software packages that include everything needed to run a piece of software, including the code, runtime, system tools, libraries, and settings.
- **Serverless:** A cloud computing execution model where the cloud provider dynamically manages the allocation and provisioning of servers. Developers can build and run applications and services without thinking about servers.
- **Cloud:** Computing services offered over the internet (the cloud), including servers, storage, databases, networking, software, analytics, and intelligence, to offer faster innovation, flexible resources, and economies of scale.
- **Network:** A group of interconnected computers, servers, and devices that can exchange data and resources with each other.
- **ETL (Extract, Transform, Load):** A process in data warehousing that involves extracting data from various sources, transforming it into a suitable format, and loading it into a destination database for analysis or reporting.
- **Data Normalization:** The process of organizing the columns (attributes) and tables (relations) of a database to minimize data redundancy and improve data integrity.
- **Logging:** The process of recording activities and events in a software application or system, which is crucial for debugging and monitoring the application's behavior in development and production environments.
- **Localhost:** The standard hostname for the local computer being used, often for testing software locally.
- **Port:** A numerical identifier in networking used to route data to specific programs or services on a computer.

### Computer Science Terms (relevant for practical use)

- **Algorithm:** A step-by-step procedure or set of rules designed to perform a specific task or solve a particular problem.
- **Language:** In the context of programming, a language is a set of syntax rules and structures used to write software programs that computers can execute.
- **Executable:** A type of file that contains a program capable of being executed or run as a program in the computer.
- **Call Stack:** A data structure used by programming languages to keep track of active subroutines or functions in a program's execution, where the last function called is the first to be completed and removed.
- **Stack Trace:** A report showing the sequence of function calls that led to an error or exception, used for debugging.
- **Conditional Statement:** A programming feature that performs different actions based on whether a specified condition evaluates to true or false. (if / else statement)
- **Recursion:** A programming technique where a function calls itself in order to solve a problem.
- **Syntax:** The set of rules that defines the correct combination of symbols that are considered to be a valid part of the language.
- **Queue:** A collection used to manage items in a sequence where items are added and removed according to specific algorithms, with FIFO (First In, First Out) being the most common, but others like LIFO (Last In, First Out) and priority-based removal are also used, depending on the application's requirements.
- **Runtime:** The period during which a program is running, starting from program execution to program termination.
- **Compilation:** The process of translating code written in a high-level programming language into a machine level language that can be executed by the computer.
- **Async vs Sync:** Asynchronous programming allows a program to do more than one thing at a time, while synchronous programming has tasks run in sequence, causing subsequent tasks to wait until the current task finishes.
- **Dependency:** A piece of software or a module that another piece of software relies on to function properly.
- **Error Handling:** The process of responding to and managing errors in a program, often through the use of try-catch blocks or similar constructs.
- **Serialization/Deserialization:** The process of converting an object into a format that can be stored or transmitted (serialization) and the process of converting that format back into an object (deserialization).
- **Multithreading:** A type of execution that allows a single process to have multiple threads of execution running concurrently.


### Technologies



- **Express:** A minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications, making it easy to build single-page, multi-page, and hybrid web applications.

- **Databases**: (e.g. MongoDB, Postgres) MongoDB is a popular NoSQL database known for its flexibility and scalability, while PostgreSQL is a powerful open-source relational database system. The key difference lies in how they store data: relational databases structure data into predefined tables and rows, whereas nonrelational databases store data without a fixed schema, often making them more flexible and scalable for certain types of applications.

- **Docker:** A platform as a service (PaaS) that uses OS-level virtualization to deliver software in packages called containers, allowing developers to package applications with their dependencies and deploy as one package.

- **Git:** A distributed version-control system for tracking changes in source code during software development, enabling multiple developers to work on a project concurrently.

- **Cloud Providers:** (e.g. AWS, Azure, GCP) These services offer a wide range of cloud computing resources and services. AWS (Amazon Web Services) is known for its robust, scalable, and affordable cloud solutions. Microsoft Azure offers a wide range of cloud services supporting various operating systems, databases, and developer tools. Google Cloud Platform provides cloud computing services that run on the same infrastructure Google uses internally for its end-user products.

- **Design System:** (e.g. MUI, ShadCN, Chakra, Bootstrap, Tailwind) A set of standards for design and code along with components that unify both practices. These systems help teams develop digital products faster by making design reusable—MUI, ShadCN, Chakra UI, Bootstrap, and Tailwind CSS are examples of such systems, offering ready-made components that are easy to integrate into web projects.

- **Cache:** (e.g. Redis) An in-memory data structure store, used as a database, cache, and message broker. Redis supports data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs, geospatial indexes with radius queries, and streams.

- **Websocket:** A communication protocol that provides full-duplex communication channels over a single TCP connection, enabling web servers and clients to exchange data more efficiently, facilitating real-time data transfer and interaction in web applications.

- **GraphQL:** A query language for APIs that allows clients to request exactly the data they need, making it possible to aggregate data from multiple sources with a single request.

- **Webpack:** A static module bundler for JavaScript applications, which bundles JavaScript files for usage in a browser, yet it is also capable of transforming, bundling, or packaging just about any resource or asset.

- **Nginx:** A high-performance web server, reverse proxy, and load balancer that provides increased security, scalability, and speed for web applications.


- **CI/CD (Continuous Integration/Continuous Delivery):** Practices in software development that automate the process of integrating code changes from multiple contributors into a single software project, and delivering or deploying code changes to a production environment automatically.

- **Flutter:** An open-source UI software development kit by Google used for building natively compiled applications for mobile, web, and desktop from a single codebase.

- **Postman:** A collaboration platform for API development, which simplifies each step of building an API and streamlines collaboration so you can create better APIs—faster.

- **curl:** A command-line tool used for transferring data with URLs. It supports various protocols including HTTP, HTTPS, FTP, and more, making it a versatile tool for testing, downloading files, and making API requests directly from the terminal.

- **Terminal:** A text-based interface to the system, allowing for the execution of commands, scripts, and programs. It provides direct access to the underlying operating system through a command-line interface (CLI), essential for software development, system administration, and troubleshooting.
