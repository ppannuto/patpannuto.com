<div align="center" markdown="1">
[Pat Pannuto](/)
----------------
</div>

----

CSE 141: Introduction to Computer Architecture
=====================================

<div class="row flex-nowrap no-gutters">
<div class="col-lg-2 col-xs-4">
<img class="img-fluid" src="/images/research/m3-finger-square.jpg" alt="M3 sensor on a finger" />
</div>
<div class="col-lg-2 col-xs-4">
<img class="img-fluid" src="/images/research/vlc-centers.png" alt="Luxapose image processing pipeline" />
</div>
<div class="col-lg-2 col-xs-4">
<img class="img-fluid" src="/images/research/signpost-closeup-square.jpg" alt="Signpost platform deployed outside" />
</div>
<div class="col-lg-2 d-none d-sm-block">
<img class="img-fluid" src="/images/research/tottag-overlay.png" alt="TotTag ranging platform" />
</div>
<div class="col-lg-2 d-none d-sm-block">
<img class="img-fluid" src="/images/research/opo-tie.png" alt="Opo interaction tracker clipped to a tie" />
</div>
<div class="col-lg-2 d-none d-sm-block">
<img class="img-fluid" src="/images/research/powerblade.jpg" alt="Powerblade power meter on a plug" />
</div>
</div>

---

## Overview

The course covers the basics of modern processor design and operation.
Topics include instruction set architectures, computer system performance, machine organization, pipelining, branch prediction, memory-hierarchy design, and an introduction to multiprocessor considerations (and possibly security considerations as well).

This course is designed to run alongside CSE 141L.
We expect that you are enrolled in both.

> If you cannot enroll in both because of scheduling, waitlists, etc, it is more important to complete CSE 141 first.
> You can succeed in CSE 141 without the partner lab, you very likely cannot succeed in 141L without having the 141 material.

---

[TOC]

---

## Syllabus

> #### DISCLAIMER
>
> Due to our continued unusual circumstances, the details in this syllabus may change (e.g. schedule, grading policy, assignments, etc.). We will update this syllabus in the event of changes as the course progresses.

### Course Staff

[Pat Pannuto](https://patpannuto.com) is the instructor and their office is [CSE 3202](https://cse.ucsd.edu/about/floormaps) (right in the corner).

#### TAs

 - Adithya Anand – ananand@ucsd.edu
 - Link Lin – yul065@ucsd.edu
 - Wenshan Luo - w1luo@ucsd.edu
 - Rahul Polisetti – rpolisetti@ucsd.edu


### Prerequisites

CSE 140 and 140L are required prerequisites for this course.
We expect that you are comfortable with the basics of digital logic, including the fundamentals of logic timing and how 1's and 0's can be used for higher-level operations like addition.

We further expect a basic familiarity with C or C-like code, i.e. you should be comfortable understanding what the following code does:

<small markdown="1">
```c
int twoDarray[256][256];
int sum = 0;

for (int i=0; i<256; i++) {
  for (int j=0; j<256; j++) {
    sum += twoDarray[i][j];
  }
}

printf("%d\n", sum);
```
</small>

### Textbook

`Computer Organization and Design MIPS Edition, The Hardware/Software Interface, Fifth Edition (Patterson & Hennessy)`
<small>(ISBN-13: 978-0124077263, ISBN-10: 0124077269)</small>

The textbook is required for this course.

#### Other recommended reading

 - Hennessy & Patterson, "Computer Architecture: A Quantitative Approach", Morgan Kaufmann
    - A more advanced treatment of many of the same topics in the textbook, as well as a lot more breadth.
 - Synthesis Lectures on Computer Architecture
    -  This contains a number of truly outstanding (and very recent and up-to-date) books on computer architecture, any of which you can download free while in the UCSD domain. In particular, see the books on Processor Microarchitecture (most useful for this class), Performance Evaluation Methods, Memory System, and Multithreading Architectures.

### Schedule

Lectures are Tue/Thr from 15:30 to 16:50 US/Pacific, in P416 WEST (the tents between Mandeville Ln and the Library Walk).<br/>


#### Office Hours

Up-to-date office hours are available in Canvas.


### Grading

A quick reminder: Effective learning comes from **active engagement** and **re-enforcement**.
Activities, assignments, and grading are designed to help with this.

_You get out of class what you put into it._

#### 15%: Participation (Peer Instruction)

During lectures, we will have interactive question and answer segments.
These are opportunities to check your understanding and for us to go back and help explain concepts more thoroughly that may be confusing folks.
These in-lecture polls will not be graded for correctness, simply for participation.

> ##### Accommodating Missed Lectures via Mini-Quizzes
>
> There's a lot going on lately, and we recognize that this means folks are more
> often going to need to miss a few lectures.
> If you are unable to attend class for any reason, you can complete that classes mini-quiz as a make-up **up to four times during the quarter**.
> You do not need to contact anyone, simply do the quiz and we will replace up to four participation zero's with quiz completions at the end of the term.
> _For exceptional situations that require more than four make-ups, please contact Professor Pannuto directly._
>
> _These quizzes are primarily for you, to help you stay on track and to check your own understanding._
> Therefore, we **will not grade them for correctness**.
> The quiz must be completed by midnight (campus time) the following week.
> If you complete the quiz, you will earn full points.
> However, if your raw score on a quiz is low, _come to discussion sections or office hours and get help!_
>
> Persons who did attend lecture and would just like some extra practice are welcome to complete the quizzes as well.

> ##### Mini-Quiz Late Policy
>
> As the purpose of these mini-quizzes is to help you keep up with class, there will be no extensions or late submissions.

#### 30%: Homework

These are longer form assignments, designed to test your individual understanding.
You are welcome discuss homework problems with other students or in groups, however, you must complete your final writeup alone.

Homework submission will be via the Gradescope module in Canvas.
Regrade requests will also be handled via Gradescope.
The window for regrades will be no more than one week after graded homework is returned.

Generally, homework will be released every Thursday and due the following Thursday, before the start of class (i.e. at 15:30).
We expect to release a homework assignment every week, with exceptions for the midterm week, final exam week, and possibly holidays, which should result in around 7-8 homework assignments over the quarter.

> ##### Homework Late Policy
>
> _Homework ever is better than homework never._
>
> The goal of homework is to help you to understand better by working through problems on your own.
> To that end, we will allow for late submission of homework at any point until the next exam (i.e. once the Midterm starts, you can no longer submit any homework assigned before the Midterm).
> Late homework will receive 50% of earned points.
> Late homework is not eligible for regrades and will be graded and returned at instructor convenience.
> Late homework should take care to add extra details showing how you, personally worked through problems and that your work is your own.
> Late homework that is "just answers" or otherwise does not clearly show your own work will receive no credit.

#### 25%: Midterm

This course will have one midterm exam.

#### 30%: Final Exam

The final exam will be cumulative over all of the course content.

#### Final Grades

I believe in mastery learning. My goal is to teach you the material in 141
and for everyone to learn it. I am most successful if everyone in class
_earns_ an `A`. This class will not be curved.
<small>I reserve the right to curve sub-components, in particular exams.
The last time I taught this course, I curved the Midterm up very slightly,
and did not curve the final.</small>

<div class="table-responsive">
<table class="table grade-table">
  <tr>
    <th>A+<br /><small>&gt;96.7</small></th>
    <th>A<br /><small>[93,96.7)</small></th>
    <th>A-<br /><small>[90,93)</small></th>
    <th>B+<br /><small>[86.7,90)</small></th>
    <th>B<br /><small>[83.3,86.7)</small></th>
    <th>B-<br /><small>[80,83.3)</small></th>
    <th>C+<br /><small>[76.7,80)</small></th>
    <th>C<br /><small>[73.3,76.7)</small></th>
    <th>C-<br /><small>[70,73.3)</small></th>
    <th>D<br /><small>[60,70)</small></th>
    <th>F<br /><small>[0,60)</small></th>
  </tr>
</table>
</div>
<small><em>Range notation [90,93) means 90 is included and 93 is not</em></small>


### Academic Integrity

In this course we expect students to adhere to the [UC San Diego Integrity of Scholarship Policy](https://senate.ucsd.edu/Operating-Procedures/Senate-Manual/Appendices/2).
This means that you will complete your work honestly, with integrity, and support an environment of integrity within the class.

Cheating WILL be taken seriously.
It is not fair to honest students to take cheating lightly, nor is it fair to the cheater to let them go on thinking that is a reasonable alternative in life.

The following is not considered cheating:

 - Discussing homework in groups (with the writeup done separately, later).

The following is:

 - Discussing homework with someone who has already completed the problem, or looking at their completed write-up.
 - Using homework solutions from the web, previous versions of the class, or anywhere else.
 - Receiving, providing, or soliciting assistance from another student during a test.

Homework is not intended to be a grade-maker, but to prepare you for the tests, which are the grade-makers.
Cheating on homework just hurts you.
If you are choosing between not turning in an assignment, or using somebody's else work, do yourself a favor and just don't turn it in.
You are facing a permanent mark on your academic record and a certainty of having to explain it to any future employer or school that you apply to.

If you are caught cheating on any assignment, you will first be flagged with an
`X` course grade, which means you are no longer permitted to withdraw from the course
for any reason.
Any assignment you are caught cheating on will receive a score of negative 100%.
This includes exams.
(Notice: it is not possible to pass the course if you are caught
cheating on an exam.)
You will receive no notice that you have been caught cheating until after this course
is complete.
You will be referred to the Academic Integrity Office, who will contact you after
the end of the quarter to discuss next steps.
There is no flexibility in this policy.

### Outside Tutoring
Individuals are not permitted to approach students to offer services of any kind in exchange for pay, including tutoring services.
This is considered solicitation for business and is strictly prohibited by University policy.


## Resources for Students

### Getting Help
***[Where should students go for help?  What kind of help is available?***

The IDEA Engineering Student Center, located just off the lobby of Jacobs Hall, is a hub for student engagement, academic enrichment, personal/professional development, leadership, community involvement, and a respectful learning environment for all.  The Center offers a variety of programs, listed in the IDEA Center Facebook page at http://www.facebook.com/ucsdidea/ (you are welcome to Like this page!) and the Center web site at http://idea.ucsd.edu/.  The IDEA Center programs support both undergraduate students and graduate students.

### Diversity and Inclusion
We are committed to fostering a learning environment for this course that supports a diversity of thoughts, perspectives and experiences, and respects your identities (including race, ethnicity, heritage, gender, sex, class, sexuality, religion, ability, age, educational background, etc.).  Our goal is to create a diverse and inclusive learning environment where all students feel comfortable and can thrive.

Our instructional staff will make a concerted effort to be welcoming and inclusive to the wide diversity of students in this course.  If there is a way we can make you feel more included please let one of the course staff know, either in person, via email/discussion board, or even in a note under the door.  Our learning about diverse perspectives and identities is an ongoing process, and we welcome your perspectives and input.

We also expect that you, as a student in this course, will honor and respect your classmates, abiding by the UCSD Principles of Community (https://ucsd.edu/about/principles.html).  Please understand that others’ backgrounds, perspectives and experiences may be different than your own, and help us to build an environment where everyone is respected and feels comfortable.
If you experience any sort of harassment or discrimination, please contact the instructor as soon as possible.   If you prefer to speak with someone outside of the course, please contact the Office of Prevention of Harassment and Discrimination: https://ophd.ucsd.edu/


### Students with Disabilities
We aim to create an environment in which all students can succeed in this course.  If you have a disability, please contact the Office for Students with Disability (OSD), which is located in University Center 202 behind Center Hall, to discuss appropriate accommodations right away.  We will work to provide you with the accommodations you need, but you must first provide a current Authorization for Accommodation (AFA) letter issued by the OSD.  You are required to present their AFA letters to Faculty (please make arrangements to contact me privately) and to the OSD Liaison in the department in advance so that accommodations may be arranged.

### Basic Needs/Food Insecurities
If you are experiencing any basic needs insecurities (food, housing, financial resources), there are resources available on campus to help, including The Hub and the Triton Food Pantry.
Please visit http://thehub.ucsd.edu/ for more information.



## Agenda

Reminder: You will get more out of lecture if you have completed the pre-class reading.
We try to be clear about what is okay to skim and what will be helpful to read deeply.

Bonus materials are for those interested in learning more about a topic.
They are **not** required in any way and their content will **not** be tested in quizzes, homework, or exams.

<table class="table table-bordered table-hover">
  <tr class="table-primary">
    <th>Date</th>
    <th>Topic</th>
    <th>Pre-Class Assignment <small><a href="CompOrgMIPSFifth_TOC.jpg">Fifth Ed. Table of Contents</a></small></th>
    <th>Bonus Material</th>
  </tr>

  <tr class="table-info">
    <td><h4 id="part-0">Part 0</h4>
    <td colspan="3">
    <h4>Welcome!</h4>
    <ul>
    <li>Slides as <a href="2020-10-02-cse141-intro.pptx">pptx</a> or <a href="2020-10-02-cse141-intro.pdf">pdf</a></li>
    </ul>
    </td>
  </tr>
  <tr>
    <td>Oct&nbsp;2</td>
    <td>Introduction and Motivation </td>
    <td></td>
    <td></td>
  </tr>

  <tr class="table-info">
    <td><h4 id="part-i">Part I</h4>
    <td colspan="2">
    <h4>Instruction Set Architecture</h4>
    <ul>
      <li>Slides as <a href="cse141-fa20-ISA.pptx">pptx</a> or <a href="cse141-fa20-ISA.pdf">pdf</a></li>
      <li><a href="https://booksite.elsevier.com/9780124077263/downloads/COD_5e_Greencard.pdf">MIPS Green Card</a></li>
      <li><a href="GreenCardOld.pdf">Simpler MIPS Reference</a></li>
    </ul>
    </td>
    <td><small>
    <p><i>Where are we?</i></p>
    <p><a href="/images/places/PointLomaTidePools.jpg">Visiting Point Loma Tide Pools</a></p>
    </small></td>
  </tr>
  <tr>
    <td>Oct&nbsp;5</td>
    <td>
    <p>What computing looks like; intro to ISA design</p>
    <p><a href="cse141-fa20-ISA_2020-10-05.pdf">[Annotated Slides]</a></p>
    </td>
    <td>Skim 1.1, Read 1.2-1.3</td>
    <td rowspan="3">
    <p>
    <ul>
    <li>Video: <a href="video/ISA_branching.webm">Detailed walkthrough of branching</a></li>
    <hr />
    <li>Computers aren't associative? <a href="https://stackoverflow.com/questions/6430448/why-doesnt-gcc-optimize-aaaaaa-to-aaaaaa">When <tt>x*x*x != x*(x*x)</tt></a></li>
    <li><a href="https://www.xorpd.net/pages/xchg_rax/snip_00.html">x86 Assembly Puzzles</a> &ndash; <small>&ldquo;A book of 0x40 short assembly snippets, each built to teach you one concept about assembly, math or life in general.&rdquo;</small></li>
    </ul>
    </p>
    </td>
  </tr>
  <tr>
    <td>Oct&nbsp;7</td>
    <td>
    <p>ISA design, memory, basic op's</p>
    <p><a href="cse141-fa20-ISA_2020-10-07.pdf">[Annotated Slides]</a></p>
    </td>
    <td>Skim 2.1-2.2, Read 2.3-2.5, Skim 2.10</td>
  </tr>
  <tr>
    <td>Oct&nbsp;9</td>
    <td>
    <p>Control flow; RISC vs CISC</p>
    <p><a href="cse141-fa20-ISA_2020-10-09.pdf">[Annotated Slides]</a></p>
    </td>
    <td>Read 2.6-2.8, Skim 2.16-2.18, Read 2.19</td>
  </tr>

  <tr class="table-info">
    <td><h4 id="part-ii">Part II</h4>
    <td colspan="2">
    <h4>Computer System Performance and Performance Metrics</h4>
    <ul>
      <li>Slides as <a href="cse141-fa20-Performance.pptx">pptx</a> or <a href="cse141-fa20-Performance.pdf">pdf</a></li>
    </ul>
    </td>
    <td><small>
    <p><i>Where are we?</i></p>
    <p><a href="/images/places/CowlesMountain.jpg">Summiting Cowles Mountain</a></p>
    </small></td>
  </tr>
  <tr>
    <td>Oct&nbsp;12</td>
    <td colspan="3"><i>Indigenous Peoples' Day</i></td>
  </tr>
  <tr>
    <td>Oct&nbsp;14</td>
    <td>
    <p>Defining performance, time; Amdahl's law</p>
    <p><a href="cse141-fa20-Performance_2020-10-14.pdf">[Annotated Slides]</a></p>
    </td>
    <td>Skim 1.5, Read 1.6, Skim 1.7-1.8 <hr /> Skim 1.9, Read 1.10, Skim 2.13</td>
    <td>
    <ul>
    <li>Blog series
    (<a href="https://tratt.net/laurie/blog/entries/why_arent_more_users_more_happy_with_our_vms_part_1.html">part&nbsp;1</a>,
    <a href="https://tratt.net/laurie/blog/entries/why_arent_more_users_more_happy_with_our_vms_part_2.html">part&nbsp;2</a>)
    on how hard it is to <i>fairly</i> and accurately measure performance on real-world systems.
    <small>Note: "VM" here refers to the <i>software</i> virtual machine that Python or Java or JavaScript run on.</small>
    </li>
    </ul>
    </td>
  </tr>

  <tr class="table-info">
    <td><h4 id="part-iii">Part III</h4>
    <td colspan="2">
    <h4>The Single Cycle Machine</h4>
    <ul>
      <li>Slides as <a href="cse141-fa20-SingleCycleMachine.pptx">pptx</a> or <a href="cse141-fa20-SingleCycleMachine.pdf">pdf</a></li>
    </ul>
    </td>
    <td><small>
    <p><i>Where are we?</i></p>
    <p><a href="/images/places/Napali.jpg">Hiking a spine of the Nā Pali Coast</a></p>
    </small></td>
  </tr>
  <tr>
    <td>Oct&nbsp;16</td>
    <td>
    <p>Execute units (ALUs), building blocks, and introducing organization</p>
    <p><a href="cse141-fa20-SingleCycleMachine_2020-10-16.pdf">[Annotated Slides]</a></p>
    </td>
    <td>Skim 3.1, Read 3.2, Skim 3.3-3.4</td>
    <td rowspan="3">
    <ul>
    <li>Read 3.7-3.9 for real-world designs; performance.</li>
    </ul>
    </td>
  </tr>
  <tr>
    <td>Oct&nbsp;19</td>
    <td>
    <p>Datapaths and control paths</p>
    <p><a href="cse141-fa20-SingleCycleMachine_2020-10-19.pdf">[Annotated Slides]</a></p>
    </td>
    <td>Read 4.1-4.3, Skim 4.4</td>
  </tr>
  <tr>
    <td>Oct&nbsp;21</td>
    <td>
    <p>Completing the machine; multicycle machines</p>
    <p><a href="cse141-fa20-SingleCycleMachine_2020-10-21.pdf">[Annotated Slides]</a></p>
    </td>
    <td>Read 4.4 (read this time! It is long, and hard)</td>
  </tr>

  <tr class="table-info">
    <td><h4 id="part-iv">Part IV</h4>
    <td colspan="2">
    <h4>Pipelines</h4>
    <ul>
      <li>Slides as <a href="cse141-fa20-Pipelines.pptx">pptx</a> or <a href="cse141-fa20-Pipelines.pdf">pdf</a></li>
    </ul>
    </td>
    <td><small>
    <p><i>Where are we?</i></p>
    <p><a href="/images/places/SeoulGwanaksanSadang.jpg">Looking over Seoul from the Sadang trail</a></p>
    </small></td>
  </tr>
  <tr>
    <td>Oct&nbsp;23</td>
    <td>
    <p>Introducing pipelines</p>
    <p><a href="cse141-fa20-Pipelines_2020-10-23.pdf">[Annotated Slides]</a></p>
    </td>
    <td>Read 4.5 until hazards (p272-277); Skim rest of 4.5</td>
    <td rowspan="7">
    <ul>
    </ul>
    </td>
  </tr>
  <tr>
    <td>Oct&nbsp;26</td>
    <td>
    <p>Control in pipelines; Intro hazards</p>
    <p><a href="cse141-fa20-Pipelines_2020-10-26.pdf">[Annotated Slides]</a></p>
    </td>
    <td>Read 4.6</td>
  </tr>
  <tr>
    <td>Oct&nbsp;28</td>
    <td>
    <p>Data Hazards; Stalls; Forwarding</p>
    <p><a href="cse141-fa20-Pipelines_2020-10-28.pdf">[Annotated Slides]</a></p>
    </td>
    <td>Read 4.5 hazards and data hazards (p277-281); Read 4.7</td>
  </tr>
  <tr>
    <td>Oct&nbsp;30</td>
    <td>
    <p>Finish data hazards; Control hazards</p>
    <p><a href="cse141-fa20-Pipelines_2020-10-30.pdf">[Annotated Slides]</a></p>
    </td>
    <td>Read 4.5 control hazards onwards (p281-286); Read 4.8 until prediction (p316-320)</td>
  </tr>
  <tr>
    <td>Nov&nbsp;2</td>
    <td>
    <p>Branch predictors; wrapping up</p>
    <p><a href="cse141-fa20-Pipelines_2020-11-02.pdf">[Annotated Slides]</a></p>
    </td>
    <td>Read rest of 4.8 (p321-325)</td>
  </tr>
  <tr>
    <td>Nov&nbsp;4</td>
    <td>
    <p>Pipeline catch-up day</p>
    <p>(Actual: Control hazards; intro branch predictors)</p>
    <p><a href="cse141-fa20-Pipelines_2020-11-04.pdf">[Annotated Slides]</a></p>
    </td>
    <td>(reading is slightly ahead of lecture)</td>
  </tr>
  <tr>
    <td>Nov&nbsp;6</td>
    <td>
    <p>Pipeline catch-up day</p>
    <p>(Actual: Branch delay slots; branch predictors)</p>
    <p><a href="cse141-fa20-Pipelines_2020-11-06.pdf">[Annotated Slides]</a></p>
    </td>
    <td>(reading is slightly ahead of lecture)</td>
  </tr>

  <tr class="table-warning">
    <td colspan="4">
    <h4 id="midterm">Midterm Exam</h4>
    </td>
  </tr>
  <tr class="table-warning">
    <td>Nov&nbsp;9</td>
    <td>Exam Review</td>
    <td colspan="2"><a href="CSE141_FA20_MidtermReview.pdf">&ldquo;Whiteboard&rdquo; Notes</a></td>
  </tr>
  <tr class="table-warning">
    <td>
    <p>Nov&nbsp;10</p>
    <p><i>8am&ndash;8pm</i></p>
    </td>
    <td>Midterm Exam</td>
    <td colspan="2">
    <ul>
    <li>Joint with Section B</li>
    <li>Administered asychronously via Canvas</li>
    <li>90-minute &ldquo;one-shot&rdquo; timed exam (timer starts when you do)</li>
    </ul>
    </td>
  </tr>

  <tr>
    <td>Nov&nbsp;11</td>
    <td colspan="3"><i>Veterans Day</i></td>
  </tr>

  <tr>
    <td>Nov&nbsp;13</td>
    <td>
    <p>Actual: Advanced branch predictors</p>
    <p><a href="cse141-fa20-Pipelines_2020-11-13.pdf">[Annotated Slides]</a></p>
    </td>
    <td>(reading is slightly ahead of lecture)</td>
  </tr>

  <tr>
    <td>Nov&nbsp;16</td>
    <td>
    <p>Even more advanced branch predictors</p>
    <p><a href="cse141-fa20-Pipelines_2020-11-16.pdf">[Annotated Slides]</a></p>
    </td>
    <td>(reading is slightly ahead of lecture)</td>
  </tr>

  <tr>
    <td>Nov&nbsp;18</td>
    <td>
    <p>Midterm Review &amp; Branch Predictor Examples</p>
    <!--<p><a href="cse141-fa20-BranchPredictorAnimation.pdf">[Annotated Slides]</a></p>-->
    </td>
    <td>(no reading)</td>
  </tr>

  <tr class="table-info">
    <td><h4 id="part-v">Part V</h4>
    <td colspan="2">
    <h4>Advanced Pipelines</h4>
    <ul>
      <li>Slides as <a href="cse141-fa20-AdvancedPipelines.pptx">pptx</a> or <a href="cse141-fa20-AdvancedPipelines.pdf">pdf</a></li>
    </ul>
    </td>
    <td><small>
    <p><i>Where are we?</i></p>
    <p><a href="/images/places/AzrouMonkey.jpg">Hanging with monkeys, hiking outside Azrou, Morocco</a></p>
    </small></td>
  </tr>
  <tr>
    <td>Nov&nbsp;20</td>
    <td>
    <p>Exceptions and interrupts</p>
    <p><a href="cse141-fa20-AdvancedPipelines_2020-11-20.pdf">[Annotated Slides]</a></p>
    </td>
    <td>Read 4.9</td>
  </tr>
  <tr>
    <td>Nov&nbsp;23</td>
    <td>
    <p>Pipelines in Modern Machines</p>
    <p><a href="cse141-fa20-AdvancedPipelines_2020-11-23.pdf">[Annotated Slides]</a></p>
    </td>
    <td>(No reading)</td>
  </tr>
  <tr>
    <td>Nov&nbsp;25</td>
    <td>
    <p>Pipelines in Modern Machines</p>
    <p><a href="cse141-fa20-AdvancedPipelines_2020-11-25.pdf">[Annotated Slides]</a></p>
    </td>
    <td>(No reading)</td>
  </tr>

  <tr class="table-info">
    <td><h4 id="part-vi">Part VI</h4>
    <td colspan="2">
    <h4>Caches and Memory</h4>
    <ul>
      <li>Slides as <a href="cse141-fa20-MemoryAndCaches.pptx">pptx</a> or <a href="cse141-fa20-MemoryAndCaches.pdf">pdf</a></li>
    </ul>
    </td>
    <td><small>
    <p><i>Where are we?</i></p>
    <p><a href="/images/places/UGhanaLegon.jpg">The University of Ghana at Legon</a></p>
    </small></td>
  </tr>
  <tr>
    <td>Nov&nbsp;27</td>
    <td colspan="3"><i>Thanksgiving Break</i></td>
  </tr>
  <tr>
    <td>Nov&nbsp;30</td>
    <td>
    <p>Introducing Caches</p>
    <p><a href="cse141-fa20-MemoryAndCaches_2020-11-30.pdf">[Annotated Slides]</a></p>
    </td>
    <td>Read 5.1; Skim 5.2</td>
  </tr>
  <tr>
    <td>Dec&nbsp;2</td>
    <td>
    <p>Cache designs &amp; tradeoffs</p>
    <p><a href="cse141-fa20-MemoryAndCaches_2020-12-02.pdf">[Annotated Slides]</a></p>
    </td>
    <td>Read 5.3</td>
  </tr>
  <tr>
    <td>Dec&nbsp;4</td>
    <td>
    <p>Cache performance</p>
    <p><a href="cse141-fa20-MemoryAndCaches_2020-12-04.pdf">[Annotated Slides]</a></p>
    </td>
    <td>Read 5.4 (focus more on the first ~half)</td>
  </tr>
  <tr>
    <td>Dec&nbsp;7</td>
    <td>
    <p>Advanced Caches</p>
    <p><a href="cse141-fa20-MemoryAndCaches_2020-12-07.pdf">[Annotated Slides]</a></p>
    </td>
    <td>Read 5.8 (reviews content through here); Skim 5.13 if you are interested</td>
  </tr>
  <tr>
    <td>Dec&nbsp;9</td>
    <td>
    <p>Virtual Memory</p>
    <p><a href="cse141-fa20-MemoryAndCaches_2020-12-09.pdf">[Annotated Slides]</a></p>
    </td>
    <td>Read 5.7 (focus more on the first ~half)</td>
  </tr>


  <!-- bgcolor disables highlight for this row -->
  <!--<td bgcolor="#FFFFFF" style="text-align: center;" colspan=4>&mldr;</td>-->

  <tr class="table-warning">
    <td colspan="4">
    <h4 id="midterm">Final Exam</h4>
    </td>
  </tr>
  <tr class="table-warning">
    <td>Dec&nbsp;11</td>
    <td>Exam Review</td>
    <td></td>
    <td></td>
  </tr>
  <tr class="table-warning">
    <td>
    <p>Dec&nbsp;12</p>
    <p><i>8am&ndash;8pm</i></p>
    </td>
    <td>Final Exam</td>
    <td colspan="2">
    <ul>
    <li>Joint with Section B</li>
    <li>Administered asychronously via Canvas</li>
    <li>180-minute &ldquo;one-shot&rdquo; timed exam (timer starts when you do)</li>
    </ul>
    </td>
  </tr>

</table>

---

<div class="row flex-nowrap">
<div class="col-lg-2">
<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a>
</div>
<div class="col-lg-10">
<p>
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.
</p>
</div>
</div>
