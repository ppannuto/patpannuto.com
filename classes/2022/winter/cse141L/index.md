<div align="center" markdown="1">
[Pat Pannuto](/)
----------------
</div>

----

CSE 141L: Introduction to Computer Architecture (Lab)
=====================================================

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


## CSE141L - Winter 2022

Meets M/W from 12:00 to 12:50 in CENTR 115.<br/>

[Pat Pannuto](https://patpannuto.com) is the instructor, and their office is CSE 3202 (right in the corner).<br/>
Office hours [TBD], or always available by appointment (please email / chat after class).

---

## Overview

Hands-on digital design projects aiming to familiarize students with state machines, digital logic implementations, design of processor, control, and memory systems.
This is a digital design, simulation, and synthesis project course.

This course is designed to run alongside CSE 141.
We expect that you are enrolled in both.

### Objectives

By the end of this course, students will be able to:

1. Learn correct hardware design practices suitable for FPGA and VLSI digital design.
2. Learn how to write Synthesizable Verilog, and to use the tools to turn it into a circuit.
3. Design, Implement, and Test your own digital circuits, all the way to an FPGA bitstream.
4. Learn about computer architecture in the best way – by doing.
5. Learn how programs and algorithms are implemented in hardware.
6. Work in a team, building a large, complex system using design principles that apply to both software and hardware.
7. Help your classmates and exercise your creativity.

---

[TOC]

---

## Syllabus

> ### DISCLAIMER
>
> Due to our unusual circumstances, the details in this syllabus may change (e.g. schedule, grading policy, assignments, etc.). We will update this syllabus in the event of changes as the course progresses.

### Instructor

 - <a href="https://patpannuto.com">Pat Pannuto</a> - [ppannuto@eng.ucsd.edu](mailto:ppannuto@eng.ucsd.edu)

#### TAs

 - Adithya Anand - ananand@ucsd.edu <!-- Prior 142L -->
 - Link Lin - yul065@ucsd.edu <!-- Prior 141, 142L, 141L, 240A -->
 - Chavisa Thamjarat - cthamjar@ucsd.edu <!-- Prior 142 -->
 - Kanlin Wang - kaw008@ucsd.edu <!-- Prior 141L -->

<!--
### Textbook

`Computer Organization and Design MIPS Edition, The Hardware/Software Interface, Fifth Edition (Patterson & Hennessy)`
<small>(ISBN-13: 978-0124077263, ISBN-10: 0124077269)</small>

The textbook is required for this course.

#### Other recommended reading

 - Hennessy & Patterson, "Computer Architecture: A Quantitative Approach", Morgan Kaufmann
    - A more advanced treatment of many of the same topics in the textbook, as well as a lot more breadth.
 - Synthesis Lectures on Computer Architecture
    -  This contains a number of truly outstanding (and very recent and up-to-date) books on computer architecture, any of which you can download free while in the UCSD domain. In particular, see the books on Processor Microarchitecture (most useful for this class), Performance Evaluation Methods, Memory System, and Multithreading Architectures.
-->

### Schedule

<!-- Official
	Section
		LE 	A00 	M 	12:00p-12:50p 	CENTR 	115 	Pannuto, Patrick William

	66122 	LA 	A01 	W 	12:00p-12:50p 	CENTR 	115 	Pannuto, Patrick William
-->

Lectures are M/W from 12:00 to 12:50 US/Pacific, CENTR 115.<br/>



### Expectations

Course format is two hours of lecture/demo/discussion per week, plus
independent work in the CSE basement labs (B250, B260, B270) or at home on own
computers.  Attendance is strongly recommended, but not required, and all
lectures are podcast.

Discussions, Q&A, peer-to-peer instruction, etc. take place on our [Piazza][piazza]
website. You are encouraged to post questions, help answer other students'
questions, and provide feedback and suggestions to your instruction staff.

What is important to me is that students put forth an honest effort and treat
one another, and the instructors, courteously and honestly. Constructive
criticism is always welcome.

#### Academic Integrity

This is a collaborative course, but students are expected to do their own work
and to refrain from taking credit for the work of others.

#### Accommodations for Students with Disabilities

If you have a disability for which you are or may be requesting accommodations,
please contact
[Office for Students with Disabilities](https://students.ucsd.edu/well-being/disability-services/). You
must have documentation from the Office before accommodations can be granted.


### Assignments

Students shall work in teams of one to three members each.

Each group will work over the course of the quarter to design and implement
a custom processor.

There are four lab reports, due at the starts of weeks 4, 6, and 8, plus the final report.
Reports shall be submitted on [Gradescope][gradescope].

There is no final exam for this course. The complete processor and its final
report are due at the end of the assigned "exam session."
This quarter, that is 2:30pm US/Pacific on Wednesday, March 16.

#### Logistics

Submit lab reports on [Gradescope][gradescope].

We will use [Piazza][piazza] for Q&A.

#### Course Resources

 - [ModelSim](https://www.mentor.com/company/higher_ed/modelsim-student-edition) (download or use on CSE B250/60/70 lab computers)
 - [Quartus Prime Lite](http://fpgasoftware.intel.com/?edition=lite) (download or use on lab computers)


### Grading

Each team shall design a specialized RISC processor.
These will be tested on instructor-provided testbenches, and final course
grades will depend on how well your designs perform against these testbenches
and whether your designs can be synthesized into actual digital gate-level
logic.

#### Milestones

There are intermediate deadlines (Labs 1, 2, and 3).
The primary goal of these is to help you ensure that you are on track.
They will be evaluated by course staff, but this is primarily for feedback to
you for your benefit; generally these will not directly impact your final
grade.

An imperfect milestone is okay, but take it as a very serious warning
sign that you are behind; it will only get harder to catch up as time
progresses.
**It is far better to submit what you have than to submit nothing.**

Each incomplete milestone will lower your course grade by one notch (e.g. , A to A- or A- to B+).

Habitually late submissions may lower your course grade by one notch (e.g. , A to A- or A- to B+).


### Agenda

<!--
Winter Quarter begins           Monday, January 3
Instruction begins	        Monday, January 3
Martin Luther King, Jr. Holiday Monday, January 17
Presidents' Day Holiday         Monday, February 21
Instruction ends	        Friday, March 11
Final Exams                     Saturday – Saturday, March 12–19
Winter Quarter ends             Saturday, March 19
-->

This course meets for one hour twice a week.
Loosely speaking, there will be one traditional lecture per week and one
interactive demo session showcasing how to use tools or implement ideas covered
in lecture.

> **Update:** In accordance with the campus policy, this course will be fully
> remote for the first two weeks of instruction. We will meet on Zoom. See the
> Canvas announcement for more details.

<table class="table table-bordered table-hover">
  <tr class="table-primary">
    <th>Week</th>
    <th>Topic</th>
    <th>Readings & Assignments</th>
  </tr>

  <tr>
    <td>Week 1</td>
    <td>
      <ul>
        <li>M: <a href="WI22_cse141L-intro.pptx">Welcome, Logistics, &amp; Basics</a></li>
        <li>W: SystemVerilog</li>
      </ul>
    </td>
    <td>
      <ul>
        <li>W: SystemVerilog Tutorials</li>
        <li>W: Lab 1 Released</li>
      </ul>
    </td>
  </tr>

  <tr>
    <td>Week 2</td>
    <td>Microprocessor Architecture</td>
    <td>Microprocessor Types</td>
  </tr>

  <tr>
    <td>Week 3</td>
    <td>Microprocessor Implementation</td>
    <td>Assembly Language</td>
  </tr>

  <tr>
    <td>Week 4</td>
    <td>SystemVerilog</td>
    <td>Lab 1 DUE</td>
  </tr>

  <tr>
    <td>Week 5</td>
    <td>SystemVerilog Verification</td>
    <td>SystemVerilog</td>
  </tr>

  <tr>
    <td>Week 6</td>
    <td>Debugging</td>
    <td>Lab 2 DUE</td>
  </tr>

  <tr>
    <td>Week 7</td>
    <td>Debugging</td>
    <td></td>
  </tr>

  <tr>
    <td>Week 8</td>
    <td>General Help</td>
    <td>Lab 3 DUE</td>
  </tr>

  <tr>
    <td>Week 9</td>
    <td>Open Discussions / Q&amp;A</td>
    <td></td>
  </tr>

  <tr>
    <td>Week 10</td>
    <td>[No Lecture] Good luck on projects!</td>
    <td></td>
  </tr>

  <tr>
    <td>Week 11</td>
    <td></td>
    <td>Final Report DUE</td>
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

[gradescope]: https://www.gradescope.com/courses/345130
[piazza]: https://piazza.com/class/kxxzc98qlx778m
