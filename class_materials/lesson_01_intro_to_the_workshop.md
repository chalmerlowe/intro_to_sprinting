# DRAFT OUTLINE:

## TODOs:

[ ] add internal links to sections within this doc  
[ ] add external links to sections outside this doc  
[ ] add external links to outside resources  
[ ] rewrite this draft: = )  
[ ] clean up the prerequisites 
[ ] add a link to basic commandline tutorial   

Welcome to the **Introduction to Open Source Workshop**. Participants are expected to walk away with enough knowledge to be able to participate in a typical open source project. The workshop has a mixture of hands-on and lecture/demo, with the focus on hands-on. This introduction document outlines general expectations. It also includes a section for instructors to orient them on running the workshop and a section for students to help them prep for the workshop.

# What to expect

This workshop covers...

* [Lesson 02](./lesson_02_tool_installation.md): installing a basic set of tools often used in open source development
* [Lesson 03](./lesson_03_venv_overview.md): An overview of virtual environments, a tool to keep the code from one project separate from other projects
* [Lesson 04](./lesson_04_github_overview.md): An overview of github, a version control repository
* [Lesson 05](./lesson_05_git_overview.md): An overview of git, a form of version control software
* [Lesson 06](./lesson_06_intro_to_the_project.md): An introduction to the sample project: a way cool calculator
* [Lesson 07](./lesson_07_project_hands_on.md): The sample project: a hands-on project so the students can practice, repeatedly, all of the skills from A to Z of contributing to an open source code base.

# What not to expect
This workshop does *not* cover...

* How to program
* Programming in any specific language

This is not a programming workshop, nor is it a Python workshop. It is intended to prep students to contribute to open source projects, it is not intended to teach students how to program.

The example code in this version of the workshop is written in Python, but this project can be run using an example project in another programming language, if desired. 

# Learning objectives

Participants should expect to achieve the following learning objectives upon completing this workshop:

* Be able to install the following software: conda, git, etc
* Be able to create a virtual environment
* Be able to use git and github to create a copy of an open source project on their own computer
* Upon editing, adding, or deleting content in a project:
  * incorporate any changes to the project, made by others, into their own local copy
  * correct any conflicts between their changes and other's changes
  * successfully issue a request for their contribution to be added to the open source project

# Prerequisites

Not all contributors to open source projects are programmers, so this workshop makes no presumption that participants know how to program. Contributions to open source projects include documentation, design, graphics, user experience, etc. This workshop will enable programmers and non-programmers to contribute. 

Having said that, the following will help with successfully completing this workshop:

* a desire to learn and experiment
* a basic understanding of the operation of a computer
* a basic understanding of command-line tools 

In the hands-on practice session, you will be using command-line tools to contribute to a practice project, namely a calculator. 

# For the Instructor

This section is intended for the workshop instructor. It outlines what the instructor should do to successfully execute this workshop.

## Teaching methods

This workshop is intended to be as 'hands-on' as possible. While some lecture and demonstration is necessary, the focus is on having participants spend the majority of their time working on using the skills demonstrated. As such, the workshop focuses on the following

* Short sections of lecture to elaborate on the what and the why
* Short demos to show participants what to expect
* Hands-on practice labs to enable participants to practice all the skills in a supportive environment
* Side-saddle mentoring and question answering
* Pair programming to enable participants to help each other
* We strongly recommend the teaching practices suggested by Software Carpentry, including: sticky notes, minute cards, one up/one down, using their own machines, collaborative note taking, pair programming, and the peak rule. For details on these, see [this Software Carpentry article](https://swcarpentry.github.io/instructor-training/15-practices/).

## Advance Preparation (prior to the workshop)

##### Fork and clone the repository we will be using for the workshop:

* Log-in to GitHub (create a GitHub account if you don't have one already) and navigate to [seawolf42/rpn-calc-workshop-2017-03-11](https://github.com/seawolf42/rpn-calc-workshop-2017-03-11)
* Click on "Fork" in the upper-right corner (<img src="http://timhettler.github.io/sassconf-2015/slides/assets/svg/fork.svg" width=12>), and follow the instructions to create a copy of the repository in your account
* In the newly-forked copy, click on "Clone or download" about half-way down the page on the right
* In the dialog that pops up, click the "copy to keyboard" icon (<img src="https://clipboardjs.com/assets/images/clippy.svg" width=12>) on the right side
* Open terminal and navigate to your development directory
* Type `git clone <paste the contents of the clipboard here>`

**Note:** If you run into difficulty, read [Fork A Repo](https://help.github.com/articles/fork-a-repo/) and [Cloning a repository](https://help.github.com/articles/cloning-a-repository/) in the GitHub documentation

##### Miscellaneous:

* Secure a location with a projector, tables, chairs, whiteboard, etc.
* Advertise the session and process registrations, waitlist, etc.
* Plan for food and beverages (the workshop is ~four hours in length)
* Set up an online collaboration where participants can share resources, ideas, etc. Etherpad
* Acquire supplies: post-it notes, pencils, markers, etc

## Day-of Preparation

* Set up the projector, tables, chairs
* Pick up any food/beverages
* Distribute post-it notes, pencils to each student


## Post workshop follow-up
[To be added]

# For the Student

This section is intended for the workshop student. It outlines what students should do to get the most out of the workshop.

## Learning methods
The workshop is about four hours and covers a lot of material. Anything you can do to optimize your learning experience will be beneficial. Below are just some suggestions:

* Ask questions. Lots of questions. Take advantage of the fact that you are in a room with mentors to get your questions answered. 
* Participate
* Take notes
* 





## Prep
Each lesson has the lecture content your instructor will cover. It also provides hands-on steps necessary to successfully navigate through the workshop.
