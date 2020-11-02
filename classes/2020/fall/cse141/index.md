CSE 141: Introduction to Computer Architecture
=====================================

<div class="row flex-nowrap no-gutters">
<div class="col-lg-2 col-xs-4">
<img src="/images/research/m3-finger-square.jpg" alt="M3 sensor on a finger" />
</div>
<div class="col-lg-2 col-xs-4">
<img src="/images/research/vlc-centers.png" alt="Luxapose image processing pipeline" />
</div>
<div class="col-lg-2 col-xs-4">
<img src="/images/research/signpost-closeup-square.jpg" alt="Signpost platform deployed outside" />
</div>
<div class="col-lg-2 d-none d-sm-block">
<img src="/images/research/tottag-overlay.png" alt="TotTag ranging platform" />
</div>
<div class="col-lg-2 d-none d-sm-block">
<img src="/images/research/opo-tie.png" alt="Opo interaction tracker clipped to a tie" />
</div>
<div class="col-lg-2 d-none d-sm-block">
<img src="/images/research/powerblade.jpg" alt="Powerblade power meter on a plug" />
</div>
</div>


<!--
[Pat Pannuto](https://patpannuto.com) is the instructor and their office is [CSE 3202](https://cse.ucsd.edu/about/floormaps) (right in the corner).
-->

---

## Overview

The course covers the basics of modern processor design and operation.
Topics include instruction set architectures, computer system performance, machine organization, pipelining, branch prediction, memory-hierarchy design, and an introduction to multiprocessor considerations (and possibly security considerations as well).

This course is designed to run alongside CSE 141L.
We expect that you are enrolled in both.

---

[TOC]

---

## Syllabus

This syllabus applies to Section A, taught by [Prof. Pat Pannuto](https://patpannuto.com).

> ### DISCLAIMER
>
> Due to our unusual circumstances, the details in this syllabus may change (e.g. schedule, grading policy, assignments, etc.). We will update this syllabus in the event of changes as the course progresses.

### Instructors

 - <a href="https://patpannuto.com">Pat Pannuto</a> (Section A)
 - <a href="https://cseweb.ucsd.edu/~tullsen/">Dean Tullsen</a> (Section B)

#### TAs

 - Kazem Taram - mtaram@eng.ucsd.edu
 - Nitish Kulshrestha - nikulshr@eng.ucsd.edu
 - Shanti Modi - shmodi@eng.ucsd.edu
 - Sumiran Shubhi - sshubhi@eng.ucsd.edu


<!--
### Prerequisites

CSE 140 and 140L are required prerequisites for this course.
We expect that you are comfortable with the basics of digital logic, including the fundamentals of logic timing and how 1's and 0's can be used for higher-level operations like addition.

We further expect a basic familiarity with C or C-like code, i.e. you should be comfortable understanding what the following code does:

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
-->

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

Lectures are M/W/F from 10:00 to 10:50 US/Pacific, online.<br/>

Section A discussion is Wednesday from 11:00 to 11:50 US/Pacific, online.<br/>
Section B discussion is Tuesday from 14:00 to 14:50 US/Pacific, online.<br/>
<small>You may attend whichever discussion is more convenient for you, however, the lectures may move at slightly different paces, so attending the "home" discussion may be better when possible.</small>

<!--
Pat's office hours are Mon 8:00 to 8:50 and Wed 13:00 to 13:50 US/Pacific, online.<br/>
Other times available by appointment.
-->

Up-to-date office hours are available in Canvas.


### Grading

A quick reminder: Effective learning comes from **active engagement** and **re-enforcement**.
Activities, assignments, and grading are designed to help with this.

_You get out of class what you put into it._

#### 5%: Participation (Mini-Quizzes)

During lectures, we will have interactive question and answer segments (zoom polls).
These are opportunities to check your understanding and for us to go back and help explain concepts more thoroughly that may be confusing folks.
To accommodate asynchronous participants, these in-lecture polls will not be graded for correctness or attendance.

At the end of each week, we will collect all of the poll questions and release a mini-quiz on canvas.
The quiz must be completed by midnight (campus time) the following Tuesday.

_These quizzes are primarily for you, to help you stay on track and to check your own understanding._
Therefore, we **will not grade them for correctness**.
If you complete the quiz, you will earn full points for that week.
However, if your raw score on a quiz is low, _come to discussion sections or office hours and get help!_

> ##### Mini-Quiz Late Policy
>
> As the purpose of these mini-quizzes is to help you keep up with class, there will be no extensions or late submissions.
> However, we also recognize that life does happen, especially now.
> We will release two bonus quizzes during the term that can be used to make-up a missed mini-quiz.
> The current thinking is one before the midterm and one before the final, which you can use to help check your understanding, but this is highly subject to change.
>
> Make-up quizzes will allow for up-to full participation. They will not count for extra credit.

#### 20%: Homework

These are longer form assignments, designed to test your individual understanding.
You are welcome discuss homework problems with other students or in groups, however, you must complete your final writeup alone.

Homework submission will be via the Gradescope module in Canvas.
Regrade requests will also be handled via Gradescope.
The window for regrades will be no more than one week after graded homework is returned.

Generally, homework will be released every Thursday and due the following Thursday, at midnight.
We expect to release a homework assignment every week, with exceptions for the midterm week, final exam week, and possibly holidays, which should result in around 7-8 homework assignments over the quarter.

> ##### Homework Late Policy
>
> _Homework ever is better than homework never._
>
> The goal of homework is to help you to understand better by working through problems on your own.
> To that end, we will allow for late submission of homework at any point during the term (until the final exam).
> Late homework will receive 50% of earned points.
> Late homework is not eligible for regrades and will be graded and returned at instructor convenience.
> Late homework should take care to add extra details showing how you, personally worked through problems and that your work is your own.
> Late homework that is "just answers" or otherwise does not clearly show your own work will receive no credit.

#### 30%: Midterm

This course will have one midterm exam.

We recognize that students may be attending class from all around the world.
For this reason, we plan to offer the midterm as a ninety minute exam to be
completed during a twelve hour window.

As the midterm is joint with section B, we will offer the midterm from 8am&ndash;8pm
on Tuesday, November 10th. We will convert the class period on Monday, November
9th to a review session open to both sections.

#### 45%: Final Exam

The final exam will be cumulative over all of the course content.

The registrar has assigned: `CSE 141 A00 and B00: Common Final, 12/12/20, 11:30 AM - 2:29 PM` as the final exam time slot for this course.

> ##### _Tentative_ plans
>
> Again, we recognize that students may be attending class from all around the world.
> For this reason, the current thinking is to offer a two hour exam to be completed any time in a twelve hour window.
>
> We will update with final plans and times once we are able.

##### The final exam _will be_ on Saturday

We recognize that Saturday can be a challenging day for some people to block off time, however, we also need to respect that folks have exams in other courses and the purpose of a harmonized exam schedule is to not conflict with those exams.

If you absolutely cannot make Saturday work, please contact Pat directly **before November 1**.


### Academic Integrity

Cheating WILL be taken seriously.
It is not fair to honest students to take cheating lightly, nor is it fair to the cheater to let them go on thinking that is a reasonable alternative in life.

_"Don't test me on this one." ~Prof. Dean Tullsen_

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

> ##### Regret Policy
>
> Sometimes, in the heat of the moment, watching the clock tick down to a deadline, we make mistakes that we come to regret the next day.
> This is a place of learning, and we would prefer that people own up to mistakes and learn from them rather than mete out punishments.
>
> If you have committed an Academic Integrity violation, [you have a 24-hour window to self-report the violation using this form](https://docs.google.com/forms/d/e/1FAIpQLSex1VufqLAAgVeYqD6VtQ_rWr_bt8HbycyNDtNT11KygwIaoA/viewform).
> Timely, self-reported violations will most likely result in an automatic zero on the reported assignment, but no further consequences.
> Non-reported violations will face much more severe consequences.


### Agenda

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
    <td rowspan="5">
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
    <!--<p><a href="cse141-fa20-Pipelines_2020-10-23.pdf">[Annotated Slides]</a></p>-->
    </td>
    <td>Read rest of 4.8 (p321-325)</td>
  </tr>

  <tr class="table-info">
    <td><h4 id="part-v">Part V</h4>
    <td colspan="2">
    <h4>Advanced Pipelines</h4>
    <ul>
      <!--
      <li>Slides as <a href="cse141-fa20-AdvancedPipelines.pptx">pptx</a> or <a href="cse141-fa20-AdvancedPipelines.pdf">pdf</a></li>
      -->
    </ul>
    </td>
    <td><small>
    <!--
    <p><i>Where are we?</i></p>
    <p><a href="/images/places/SeoulGwanaksanSadang.jpg">Looking over Seoul from the Sadang trail</a></p>
    -->
    </small></td>
  </tr>
  <tr>
    <td>Nov&nbsp;4</td>
    <td>
    <p>Exceptions and interrupts</p>
    <!--<p><a href="cse141-fa20-Pipelines_2020-10-23.pdf">[Annotated Slides]</a></p>-->
    </td>
    <td>Read 4.9</td>
  </tr>
  <tr>
    <td>Nov&nbsp;6</td>
    <td>
    <p>Advanced pipelines from the real world</p>
    <!--
    <p>(Slack day)</p>
    <p>(finish pipelines if we are behind, or do more advanced pipeline work)</p>
    -->
    <!--<p><a href="cse141-fa20-Pipelines_2020-10-23.pdf">[Annotated Slides]</a></p>-->
    </td>
    <td>(No Reading; skim 4.10 if interested)</td>
  </tr>

  <tr class="table-warning">
    <td colspan="4">
    <h4 id="midterm">Midterm Exam</h4>
    </td>
  </tr>
  <tr>
    <td>Nov&nbsp;9</td>
    <td>Exam Review</td>
    <td></td>
  </tr>
  <tr>
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

  <!--
  <tr class="table-info">
    <td colspan="4">Part VI: Superscalars</td>
  </tr>
  <tr>
    <td>Nov&nbsp;9</td>
    <td></a></td>
    <td></td>
  </tr>
  <tr>
    <td>Nov&nbsp;11</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Nov&nbsp;13</td>
    <td></td>
    <td></td>
  </tr>
  -->

  <!--
  <tr class="table-info">
    <td colspan="4">Part VII: The Memory/Cache Hierarchy</td>
  </tr>
  <tr>
    <td>Nov&nbsp;16</td>
    <td></a></td>
    <td></td>
  </tr>
  <tr>
    <td>Nov&nbsp;18</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Nov&nbsp;20</td>
    <td></td>
    <td></td>
  </tr>
  -->

  <!--
  <tr class="table-info">
    <td colspan="4">Part VIII: Multicores, Multithreading, and Multiprocessors</td>
  </tr>
  <tr>
    <td>Nov&nbsp;23</td>
    <td></a></td>
    <td></td>
  </tr>
  <tr>
    <td>Nov&nbsp;25</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Nov&nbsp;27-28</td>
    <td colspan="2"><i>Holiday Break</i></td>
  </tr>

  <tr class="table-info">
    <td colspan="4">Virtual Memory</td>
  </tr>
  <tr>
    <td>Nov&nbsp;30</td>
    <td></a></td>
    <td></td>
  </tr>
  <tr>
    <td>Dec&nbsp;2</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Dec&nbsp;4</td>
    <td></td>
    <td></td>
  </tr>
  -->

  <!--
  <tr class="table-info">
    <td colspan="4"></td>
  </tr>
  <tr>
    <td>Dec&nbsp;7</td>
    <td></a></td>
    <td></td>
  </tr>
  <tr>
    <td>Dec&nbsp;9</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Dec&nbsp;11</td>
    <td>Final Exam Review</td>
    <td></td>
  </tr>

  <tr class="table-warning">
    <td colspan="4"><strong>Final Exam: December 12</strong></td>
  </tr>
  -->


  <!-- bgcolor disables highlight for this row -->
  <td bgcolor="#FFFFFF" style="text-align: center;" colspan=4>&mldr;</td>

  <tr class="table-warning">
    <td colspan="4">
    <h4 id="midterm">Final Exam</h4>
    </td>
  </tr>
  <tr>
    <td>Dec&nbsp;11</td>
    <td>Exam Review</td>
    <td></td>
  </tr>
  <tr>
    <td>
    <p>Dec&nbsp;12</p>
    <!--
    <p><i>8am&ndash;8pm</i></p>
    -->
    </td>
    <td>Final Exam</td>
    <td colspan="2">
    <ul>
    <li>Joint with Section B</li>
    <li>Details TBA</li>
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
