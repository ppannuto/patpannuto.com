Teaching
========

[ug-award]: http://www.eecs.umich.edu/eecs/events/GSI-awards-2012.html
In my time at Michigan, I have had the opportunity to teach an array of courses,
some for multiple terms. In 2012, I was recognized by the EECS department and won
the [2011-2012 CSE Undergraduate Instructor Award][ug-award].

In Winter 2016, I built a new course from scratch: Computing for Computing Scientists.


### [EECS 398: Computing for Computer Scientists][c4cs] ([W'16][c4cs-w16], [F'16][c4cs-f16])
[c4cs-f16]: https://c4cs.github.io/archive/f16
[c4cs-w16]: https://c4cs.github.io/archive/w16
[c4cs]: https://c4cs.github.io

Towards the end of my undergraduate teaching career I observed a gap in the
skills and knowledge of our students. A remarkable number of students in
senior-level courses did not use build systems, version control, debuggers, or
other common software development practices. While they may have been exposed
to these tools, learning them amongst all the other coursework was lost,
resulting in an achievement gap on projects that was wholly orthogonal to the
comprehension of course material.
With a groundswell of support from undergraduate students who reviewed the
proposed syllabus, I created Computing for Computer Scientists (C4CS) to help
address this, and taught it for the first time in W'16 to over 300 students.

C4CS is a 1-credit course aimed at improving the efficacy of software
engineers. While the course centers around tools, it is not a series of
tutorials. Rather we seek to develop an understanding for why a tool exists
and how you might build such a thing, to build an intuition and lasting
comprehension. One element students appreciate is that the course itself is
very open, all course materials and course development are open source and
available for anyone to explore at [c4cs.github.io](https://c4cs.github.io)
and [github/c4cs](https://github.com/c4cs/c4cs.github.io).
I have received the most positive feedback however, about the lecture
structure, which is a mix of small amounts of traditional lecturing and then
interactive sessions, typing on screen with students following along,
exploring how things work, and&mdash;critically&mdash;making, correcting, and
learning from mistakes in real time.

Beyond pedagogy, one goal of the course is an attempt to eliminate the
super-hacker archetype. We show that command line wizardry is not purely for
the elites, it is simply a different language that has not yet been learned
(and is unfortunately a bit arcane). During the interactive elements student
questions consistently result in "live Googling", because even an "expert"
doesn't know everything. We aim to eliminate the notion that there is a
"right" way to write code; that an elite emacs user is a fundamentally
better programmer than someone using Sublime. Post-course surveys reveal that
we are having success. Students, particularly those who entered college with
little to no prior programming experience, report an increase in their comfort
and confidence in computer science and an improved sense of "belonging" in the
field.


### [EECS 470: Computer Architecture][eecs470] (W'12)
[eecs470]: http://www.eecs.umich.edu/courses/eecs470/
[pulkit]: http://www.linkedin.com/pub/pulkit-gupta/42/777/350

EECS 470 is a Major Design Experience (MDE, the Michigan term for an engineering
capstone course). It has a well-earned reptuation as one of the toughest MDEs at
Michigan and was a very different teaching experience. As I was only taking one
course this semester, I took on double hours supporting this course. We decided
to change the course format and transform early-semester recitation sessions
into labs. The course GSI, [Pulkit Gupta][pulkit], and I developed the labs that
are still in use (as of W'14) today.





### EECS 373: Design of Microprocessor-Based Systems (W'11, [F'11][eecs373-f11])
[eecs373-f11]: http://eecs.umich.edu/~prabal/teaching/eecs373-f11/
I served as a lab instructor, a very different experience from 482.  As a lab
instructor, I spent no time lecturing. Rather, my time was spent helping to
devlop and refine the labs and with a lot of hands-on time with students
helping them through the tasks and challenges presented by the labs.

If F'11, in addition to lab responsibilities, I built a novel simulator project
for the students. The project required students to build an ARM Cortex-M3
simulator, however, instead of the more traditional model of every student
implementing a carbon-copy project, the entire class had to work together on
one shared repository. A novel simulator architecture facilitated
collaborative work. Students "registered" opcode masks with callback functions
that "taught" the simulator core how to execute instructions (that is, the
decode stage would scan all registered handlers and call the student's
implementation of ADD, SUB, etc). In addition, students had to build
(simulated) reset hardware and a software library to run on the simulated
chip. The project was extremely interesting, and students reported it to be
"unlike anything they had ever seen before". Students had to learn the
challenges of developing and debugging their code, when the code of other
engineers on their project is also new and unreliable. In addition, they had
to deal with the challenges of co-operatively developing software and
hardware. In the end, we found the project to be a much more accurate
microcosm of real-world engineering - in particular new hardware development -
and in some cases exposing critical gaps in the skill set of our engineering
students.

[sim-link]: http://eecs.umich.edu/~prabal/teaching/eecs373-f11/homeworks/HW1.pdf
 * Those interested in more information are encouraged to [download a copy of the project spec][sim-link]

Continuing the trend of building a class students had "never seen before",
for the final exam (take-home), I built a reverse-engineering challenge. The
exam should still be live, and those interested in trying it out can use
the UMID 00011000 to try it yourself!

[sim-exam]: http://eecs.umich.edu/~prabal/teaching/eecs373-f11/labs/final/mission.html
 * Those interested in more information are encouraged to [attempt the question themselves][sim-exam]





### EECS 482: Introduction To Operating Systems ([F'10][eecs482-chen], W'11, [F'11][eecs482-chen], W'12)
[eecs482-chen]: http://www.eecs.umich.edu/~pmchen/eecs482
[pmchen]: http://web.eecs.umich.edu/~pmchen/
[flinn]: https://web.eecs.umich.edu/~jflinn/

This was my first teaching experience. At Michigan, undergraduate students are
offered the opportunity to be Instructional Aides (IA's). An IA often covers
discussion (recitation) sections for larger courses.

I was offered the opportunity to teach either 281 (Intro to Algorithms) or 482
(Operating Systems). I have always had a passion for low-level internals, and
the opportunity to teach our OS course aligned best with my interests.

Over the four semester that I taught this course I worked with
[Peter Chen][pmchen] during the fall terms, and [Jason Flinn][flinn] during the
winter terms.  It was interesting to see different perspectives on what is,
nominally, the same course.

As an IA, I led a weekly discussion session covering course material and held
office hours to assist with comprehension of material and challenges with
course projects.
In addition to the prescribed duties, I held exam review sessions for the
midterms and finals.
This course is fairly refined and established (in fact, it's a bit of an
institution at Michigan), and I am proud to be a part of the course's legacy.

