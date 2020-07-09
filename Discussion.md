Architecture:
- When would you prefer to develop an Assignment 1 style web application
(Server-side rendering, serving HTML)?

April 13th, 2020

- When would you prefer an Assignment 2 one (REST API & Single Page
Application)?

June 15th, 2020

Version Control:
- What is git and what is it used for?

Git (/ɡɪt/) is a distributed version-control system for tracking changes in source code during software development. 
It is designed for coordinating work among programmers, but it can be used to track changes in any set of files.
- List 3 git commands you’ve learned in this course.

git branch (list all existing branch)
git add -A (combine all the files)
git commit -m (add a commit for new upload files)

- What is GitHub and what is it used for?

GitHub is a Git repository hosting service, but it adds many of its own features. While Git is a command line tool, 
GitHub provides a Web-based graphical interface. It also provides access control and several collaboration features, 
such as a wikis and basic task management tools for every project.

- What is Kanban and what is it used for?

Kanban boards offer a way to visually manage your work. Widely used by IT managers and software development teams, 
Kanban boards are also being adopted by business managers and project teams to work smarter. With Kanban boards, 
you can: Visually see work in progress.

- What is Markdown and what is it used for?

Markdown is a lightweight markup language with plain-text-formatting syntax. 
Markdown is often used to format readme files, for writing messages in online discussion forums, 
and to create rich text using a plain text editor.

Platform vs Infrastructure:
- What are some of the pros and cons of using Platform-as-a-Service (PaaS) providers such as Heroku?

Pros:
1. It makes deployment, environment configuration, and simple manageability extraordinarily simple and easy to do, 
and getting up and going is a wonderfully simple process.
2. The metrics included are excellent as a first resource for diagnosing high level issues.
3. For beginners, Heroku is an excellent tool, making initial deployment and environment configuration 
wonderfully easy and fast.
4. Heroku is absolutely fantastic on the mobile break point (mobile responsiveness). 
As a startup, things still happen on weekends while out at the park or driving out of town, 
and it has been wonderful to be able to troubleshoot or restart servers from the phone.
5. The Heroku CLI provides a wonderful interface for interacting with the cloud environment.
Cons:
1. Heroku does not provide static IP addresses. For most applications this is not a concern, but in particular cases, 
especially around explicitly sensitive data, this makes Heroku prohibitive.
2. For a more senior engineer seeking to SSH onto a server and monitor the machine's performance, 
or extract log files for extensive research, Heroku does not provide a great way to do this.
3. Heroku permissions controls could be more granular. For instance, allowing some users to view environment 
variables while others can not view these.

- What are some of the pros and cons of using Infrastructure-as-a-Service providers such as Amazon?

Pros:
1. Trust – Amazon Web Services is among the most trusted in the industry, having compiled the most compliance 
certifications. Amazon Web Services boasts FIPS 140-2 Level 2.
2. A capacity solution – previously, companies had to purchase a set amount of data storage, 
without knowing if they would or would not use it. Amazon Web Services allows for a scalable solution, 
meaning companies no longer must ‘wait and see’ if they’ll use all that extra space they paid for.
3. Fast and agile – Amazon Web Services provides speed and agility for applications. 
An application can easily be deployed within minutes via a quick set-up process that allows us to reduce 
time and cost and speed up efficiency and agility.
4. Pay as you go – Like it’s counterpart Azure, Amazon Web Services only asks you to pay for the services you use. 
The process is secure and simple and allows for simple automated scaling according to your cloud usage. 
However, customers have experienced bill shock in the past, we’ll explain more below.
Cons:
1. Cloud computing glitches – Cloud-based services do still glitch, and Amazon Web Services is no exception. 
While the service is robust and well-designed, it’s not perfect and still subject to general cloud computing glitches.
2. Insecure Services – It’s important to note that while configuring services so they are insecure is possible with 
Amazon Web Services this is not a problem exclusive to AWS. All service providers face this issue.
3. Data Mining – AWS (or something else) could be mining your data, something potentially worth worrying about.

Web Frameworks:
- What is Django? What are some of its useful features?

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. 
Built by experienced developers, it takes care of much of the hassle of Web development, 
so you can focus on writing your app without needing to reinvent the wheel. It's free and open source.
Features of Django:
Rapid Development
Secure
Scalable
Fully loaded
Versatile
Open Source
Vast and Supported Community

- What is a model?

A model is the single, definitive source of information about your data. 
It contains the essential fields and behaviors of the data you're storing. 
Generally, each model maps to a single database table. 
The basics: Each model is a Python class that subclasses django.

- What is a view?

Django views are a key component of applications built with the framework. At their simplest they are a 
Python function or class that takes a web request and return a web response. Views are used to do things like fetch 
objects from the database, modify those objects if needed, render forms, return HTML, and much more.

- Name two other popular non-Python web frameworks.

Ruby on Rails, CakePHP

- What is WSGI? What is ASGI?

WSGI:
Django's primary deployment platform is WSGI, the Python standard for web servers and applications. 
Django's startproject management command sets up a minimal default WSGI configuration for you, which you can tweak as 
needed for your project, and direct any WSGI-compliant application server to use.
ASGI:
ASGI, or the Asynchronous Server Gateway Interface, is the specification which Channels and Daphne are built upon, 
designed to untie Channels apps from a specific application server and provide a common way to write application and 
middleware code.

- What is celery and what are task queues used for?

A Celery system can consist of multiple workers and brokers, giving way to high availability and horizontal scaling.
Celery is written in Python, but the protocol can be implemented in any language. 
In addition to Python there’s node-celery and node-celery-ts for Node.js, and a PHP client.
Task queues are used as a mechanism to distribute work across threads or machines.
A task queue’s input is a unit of work called a task. Dedicated worker processes constantly monitor task queues for 
new work to perform.
Celery communicates via messages, usually using a broker to mediate between clients and workers. To initiate a task 
the client adds a message to the queue, the broker then delivers that message to a worker.

Databases:
- What is PostgreSQL? Using StackShare, list 3 well-known companies that use PostgreSQL.

PostgreSQL is a powerful, open source object-relational database system that uses and extends the SQL language 
combined with many features that safely store and scale the most complicated data workloads.
Netflix, Instagram, Spotify

- List two other well-known databases.
Oracle, SQLite

- What are some of the pros and cons of using an Object Relational Mapper (ORM)?

Pros:
Models are DRY (don't repeat yourself): You only write your model once, which makes it far easier to update and 
maintain. All your code points to this one reference.
A lot of things are done for you, from handling the underlying database connection(s) to localisation.
SQL injection is a lot more difficult as queries are prepared and sanitised.
It can improve the formation of the underlying SQL. Developers can sometimes be bad at forming SQL.
When you change the underlying database, you do not have to rewrite code.
Models use OOP, which means you an extend and inherit from Models.
If you take the time to learn SQL queries and the theory behind sql, there is nothing a Model cannot do. You can 
write very complex queries which have the same performance if you were to write them directly in sql, however not all 
developers take the time to learn SQL.
Cons:
While many CRUD (create, read, update and delete) queries run without performance issues, more complex queries can 
lead to performance issues if not written properly.
The N+1 issue. Let's say you have a collection of users (from a users table) and each user has at least one related 
table row in the user_roles table. If you were to loop over the user collection and then dynamically fetch the name 
of each role the ORM would query each and every row separately which obviously can slow down your application. 
The way this is bypassed is by 'bringing' the related table with the original table, reducing the calls to the database.
It abstracts the database layer so if you don't have much understanding of the underpinning it can be a hindrance when 
something goes wrong.
You have to spend a bit of time learning how to use the ORM and this can have an initial impact on development. 
However, once you've learnt one they generally follow the same pattern.
Developers don't necessarily learn about SQL, which can be a massive issue if they remain ignorant.

- What is the purpose of database migrations?

Database migration — in the context of enterprise applications — means moving your data from one platform to another. 
The process of database migration can involve multiple phases and iterations, including assessing the current databases 
and future needs of the company, migrating the schema, and normalizing and moving the data. Plus, testing, testing, 
and more testing.

- What is redis and what are two things it can be used for?

Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache and message broker. 
It supports data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, 
hyperloglogs, geospatial indexes with radius queries and streams. Redis has built-in replication, Lua scripting, 
LRU eviction, transactions and different levels of on-disk persistence, and provides high availability via 
Redis Sentinel and automatic partitioning with Redis Cluster.
Session Cache, Full page Cache

- Why do we use caches?

The primary reason for caching is to make access to data less expensive. This can mean either:
Monetary costs, such as paying for bandwidth or volume of data sent, or
Opportunity costs, like processing time that could be used for other purposes.
Fast data access is an absolute necessity and a rising expectation for today's users: 
serving up information to users quickly can literally be the difference between your app being deleted or not.

HTTP & REST:
- Which four HTTP methods does REST use for performing CRUD operations?
POST
GET
PUT
DELETE

- What is Django REST Framework used for?

Django REST framework is a powerful and flexible toolkit for building Web APIs. 
Some reasons you might want to use REST framework: The Web browsable API is a huge usability win for your developers.
- What is serialization and why do we use it?
Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that 
can then be easily rendered into JSON , XML or other content types.
Serializers used to convert the data sent in a HTTP request to a Django object and a Django object to a valid 
response data. It looks a lot like a Django Form, but it is also concerned in defining how the data will be returned 
to the user.

- Which type of object serialization notation is most commonly used on the web?
JSON

- What is Postman and what is it used for?

Postman is a great tool when trying to dissect RESTful APIs made by others or test ones you have made yourself. 
It offers a sleek user interface with which to make HTML requests, without the hassle of writing a bunch of code 
just to test an API's functionality.
- What are websockets and what are they used for?
The WebSocket protocol enables interaction between a web browser (or other client application) and a web server 
with lower overhead than half-duplex alternatives such as HTTP polling, facilitating real-time data transfer from 
and to the server.
When a client needs to react quickly to a change (especially one it cannot predict), a WebSocket may be best. 
Consider a chat application that allows multiple users to chat in real-time. If WebSockets are used, each user can 
both send and receive messages in real-time.

Javascript:
- What is NodeJS and how is it different from in-browser Javascript?

Node.js is an open source server environment.
Node.js is free.
Node.js runs on various platforms (Windows, Linux, Unix, Mac OS X, etc.).
Node.js uses JavaScript on the server.
Javascript is a popular programming language and it runs in any web browser with a good web browser. On the other hand, 
Node. js is an interpreter and environment for the JavaScript with some specific useful libraries which JS programming 
can be used separately.

- What is npm and what is it used for?

npm is the world's largest Software Library (Registry).
npm is also a software Package Manager and Installer.
It is extremely configurable to support a wide variety of use cases. Most commonly, it is used to publish, discover, 
install, and develop node programs.

- What is ES6? List the names of 3 features that ES6 provides.
ES6 stands for ECMAScript 6.
ECMAScript was created to standardize JavaScript, and ES6 is the 6th version of ECMAScript, it was published in 2015, 
and is also known as ECMAScript 2015.
Features:
let 
const
arrow functions

- What is ReactJS and what is it used for?

React JS is a JavaScript library used in web development to build interactive elements on websites. 
This is usually used for single-page applications. It is used to handle all views of an application for any 
web or mobile application. It is also used to reuse UI components. React enables developers to create web applications 
that can change your data without reloading your page. 

- List two popular alternative Javascript libraries to ReactJS.
InfernoJS
Preact

- What is the DOM? What is a virtual DOM?

The Document Object Model (DOM) is the data representation of the objects that comprise the structure and content of a 
document on the web.
The virtual DOM (VDOM) is a programming concept where an ideal, or “virtual”, representation of a UI is kept in memory 
and synced with the “real” DOM by a library such as ReactDOM. This process is called reconciliation.

- What is the difference between sessionStorage and localStorage?

Local storage and Session storage are the web srorage objects. Session storage is destroyed once the user closes the 
browser whereas, Local storage stores data with no expiration date. The sessionStorage object is equal to the 
localStorage object, except that it stores the data for only one session.

- What is a library like Material-UI used for?

Material-UI is the most popular React UI component library. It's inspired by and built with Google's Material Design 
and has a lot of prebuilt React components, which can help you create React apps in no time.

Docker:
- Why do we run apt-get update && apt-get install -y in one command when using

Docker?
- What are Docker containers and what are the pros and cons of using them?
What is the difference between ADD and COPY with Docker?

- What is a .dockerignore file used for?

dockerignore file is similar to gitignore file, used by the git tool. similarly to . gitignore file, it allows you to 
specify a pattern for files and folders that should be ignored by the Docker client when generating a build context.

- What is Kubernetes and why didn’t we use it?

Deployment:
- What is Amazon S3 used for?

Amazon S3 has a simple web services interface that you can use to store and retrieve any amount of data, at any time, 
from anywhere on the web.
Amazon S3 can be used to replace significant existing (static) web-hosting infrastructure with HTTP client 
accessible objects.

- What is Amazon ECS?

Amazon Elastic Container Service (Amazon ECS) is a fully managed container orchestration service. Customers 
such as Duolingo, Samsung, GE, and Cookpad use ECS to run their most sensitive and mission critical applications 
because of its security, reliability, and scalability.

- What is the difference between ECS Fargate and EC2?

These are two major models for how to run containers on AWS. Amazon EC2 manages or deploy your own EC2 instances to run 
applications effectively. With AWS Fargate, you may run containers without any need of EC2 instances. Both are 
wonderful techniques to manage or scale your containers in a reliable fashion but which service should you choose 
is always a tough task. In this section, we will help you in making the right decision by understanding both services 
in depth based on different parameters Pricing and the Use Cases.

- Name 3 other cloud providers.

Alibaba Cloud
Azure
Google Cloud Platform

- What is Sentry and what is it used for?

Sentry empowers developers to quickly triage and resolve issues while reducing everything-is-on-fire stress, chaos, 
and potential financial loss, by providing cross-stack visibility and deep context about errors.
It is used to be notified of errors happening in application.

- What is Cloudflare and what is it used for?

Cloudflare, Inc. is an American web-infrastructure and website-security company, providing content-delivery-network 
services, DDoS mitigation, Internet security, and distributed domain-name-server services.

- What is SendGrid and what is it used for?

SendGrid is a cloud-based SMTP provider that allows you to send email without having to maintain email servers. 
SendGrid manages all of the technical details, from scaling the infrastructure to ISP outreach and reputation monitoring 
to whitelist services and real time analytics.

- What is the difference between a DNS A record and a CNAME record?
The A and CNAME records are the two common ways to map a host name (“name”) to one or more IP addresses. 
There are important differences between these two records.
The A record points a name to a specific IP.
The CNAME record points a name to another name instead of to an IP.

Meta:
- What are some of the mistakes or difficulties you encountered in developing
these 2 assignments?

In assignment 1, when I pushed the web application to HEROKU, an error occurred and it was not properly modified until 
the assignment was due.
In assignment 2, when I try to push the project to Docker, it shows pushed successful but I cannot open the page on 
0.0.0.0:8000.

- What have you learned from this course that you think might be useful in your
career?

In this course, I learned a lot of things that I had not been exposed to before. Writing web pages in Python is much 
clearer and cleaner, and also it's the way that often used these days. Django, REST API, React, AWS, HEROKU, Docker, 
Postman, Git and Github are all involved in the preparation of the web pages. During this process, I had a preliminary 
learning and application of these contents. Everything I learned and applied will be helpful for my future programming 
learning, and I am grateful for every new skill I learned in this course.