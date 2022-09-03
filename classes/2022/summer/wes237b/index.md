<div align="center">
<h1><a href="/">Pat Pannuto</a></h1>
</div>

---

<h2>WES 237B: Introductions to Embedded Systems Design</h2>

<!--
## Overview

### Learning Goals

---
-->

[TOC]

---

### Course Staff

[Pat Pannuto](https://patpannuto.com) is the instructor and their office is [CSE 3202](https://cse.ucsd.edu/about/floormaps) (right in the corner).
Their email is [ppannuto@ucsd.edu](mailto:ppannuto@ucsd.edu?Subject=CSE141:);
please remember to include `WES237B` in the subject line for class issues.

##### What should you call me?
For folks in the MAS program, "Pat" is fine.
I also respond to Professor, Professor Pannuto, Dr. Pannuto, &ldquo;Prof[essor] P.&rdquo;, etc.

##### What should I call you?
I should call you by your preferred name, with the correct pronunciation and any honorific or pronouns you choose.
Please correct me (in the chat if there is one, out loud in class or in Zoom, or via email/chat after the fact – however you are most comfortable) if I make a mistake.


#### TA & Office Hours

 - Chris Crutchfield - ccrutchf@eng.ucsd.edu

**Office Hours:** Tuesday nights (7-8 PM) and every other Saturday (off-weeks; 10AM-Noon), via Zoom (link in Canvas).


---


### _Tentative_ Syllabus

> Due to our continued unusual circumstances, the details in this syllabus may
> change (e.g. schedule, grading policy, assignments, etc.). We will update
> this syllabus in the event of changes as the course progresses.


### Calendar

#### **Saturday, July 9** &ndash; First Class

 - Lecture: Introduction to 237B, embedded hardware platforms, a short software primer, and performance measures
     - Slides [pptx](wes237b-su22-01-Intro_HWandHuffman.pptx)
 - Lab: Introduction to the Jetson TX2 platform
 - Assignment: Refreshing C, Huffman compression **(Due: July 24)**
     - [Lab 1, Assignment 1](assignment1.html)
     - [Assignment Starter Code](wes237b-a1-huffman.zip)

> ##### **Tuesday, July 12** &ndash; Office Hours
>  - Office Hours: 7-8pm
>  - Zoom: https://ucsd.zoom.us/j/96458655520
> ##### **Thursday, July 14** &ndash; Office Hours
>  - Office Hours: 7-9pm
>  - Zoom: https://ucsd.zoom.us/j/96458655520
> ##### **Tuesday, July 19** &ndash; Office Hours
>  - Office Hours: 7-8pm
>  - Zoom: https://ucsd.zoom.us/j/96458655520

#### **Saturday, July 23** &ndash; Second Class

 - Lecture:
     - Performance, Optimizations, µArch, and the Memory Hierachy
         - Slides [pptx](wes237b-su22-02-Performance_Optimization_Jpg.pptx)
     - _Break_
     - Lab Preview: Quie intro to DCT, MM, BMM
         - Slides [pdf](wes237b-su22-02-LabPrimer.pdf)
 - Lab: PYNQ, OpenCV, and basic DCTs
 - Assignment: Matrix math, 2D DCTs, and profiling
     - [Lab 2, Assignment 2](assignment2/)

> ##### **Tuesday, July 26** &ndash; Office Hours
>  - Office Hours: 7-8pm
>  - Zoom: https://ucsd.zoom.us/j/96458655520
> ##### **Saturday, July 30** &ndash; Office Hours
>  - Office Hours: 10am-12pm
>  - Zoom: https://ucsd.zoom.us/j/96458655520
> ##### **Tuesday, August 2** &ndash; Office Hours
>  - Office Hours: 7-8pm
>  - Zoom: https://ucsd.zoom.us/j/96458655520

#### **Saturday, August 6** &ndash; Third Class

 - Lecture:
     - ` 9:00-10:45` Caches, Compiler optimizations
         - Slides [pptx](wes237b-su22-03-Cache_CompilerOptimizations.pptx)
         - [Extra / succinct notes on caches](cache.html)
     - `10:45-11:00` _Break_
     - `11:00-11:50` Student Presentation
         - HeteroCL ([homepage][heterocl-home], [paper][heterocl-pdf]) - [Presentation Slides (pptx)][heterocl-pptx]
     - `11:50-12:00` _Break / Slack_
 - Lab: ARM NEON, PYNQ vs. Jetson, optimizations in practice, `gprof`
 - Assignment: Implementing a Sobel filter, benchmarking Sobel implementations
     - [Lab 3, Assignment 3](assignment3/)

> ##### **Tuesday, August 9** &ndash; Office Hours
>  - Office Hours: 7-8pm
>  - Zoom: https://ucsd.zoom.us/j/96458655520
> ##### **Saturday, August 13** &ndash; Office Hours
>  - Office Hours: 10am-12pm
>  - Zoom: https://ucsd.zoom.us/j/96458655520
> ##### **Tuesday, August 16** &ndash; Office Hours
>  - Office Hours: 7-8pm
>  - Zoom: https://ucsd.zoom.us/j/96458655520



#### **Saturday, August 20** &ndash; Fourth Class

 - Lecture:
     - `9:00-10:45` SIMD, CUDA, CUDA memory & performance
         - Slides [pptx](wes237b-su22-04-SIMD_CUDA.pptx)
     - `10:45-11:00` _Break_
     - `11:00-11:50` Student Presentation
         - SIMD Camera ([SCAMP Homepage][simdcam-home]) - [Presentation Slides (pptx)][simdcam-pptx]
     - `11:50-12:00` _Break / Slack_
 - Lab: CUDA basics, GPU-accelerated image processing with CUDA
 - Assignment: Sobel and BMM with CUDA
     - [Lab 4, Assignment 4](assignment4/)

> ##### Tuesday, August 23 &ndash; Office Hours
>  - Office Hours: 7-8pm
>  - Zoom: https://ucsd.zoom.us/j/96458655520
> ##### Saturday, August 27 &ndash; Office Hours
>  - Office Hours: 10am-12pm
>  - Zoom: https://ucsd.zoom.us/j/96458655520
> ##### Tuesday, August 30 &ndash; Office Hours
>  - Office Hours: 7-8pm
>  - Zoom: https://ucsd.zoom.us/j/96458655520


#### **Saturday, September 3** &ndash; Fifth & Final Class

 - Lecture:
     - `9:00-10:45` Parallel & Streaming Programming Patterns, Deep Learning (Lite)
         - Slides [pptx](wes237b-su22-05-ParallelPatterns_DeepLearning.pptx)
     - `10:45-11:00` _Break_
     - `11:00-11:50` Student Presentation
     - `11:50-12:00` _Break / Slack_
 - Lab: Learning simple circuits
 - Assignment: Machine learning
     - [Lab 5, Assignment 5](assignment5/)

> ##### Tuesday, August 23 &ndash; Office Hours
>  - Office Hours: 7-8pm
>  - Zoom: https://ucsd.zoom.us/j/96458655520
> ##### Saturday, August 27 &ndash; Office Hours
>  - Office Hours: 10am-12pm
>  - Zoom: https://ucsd.zoom.us/j/96458655520
> ##### Tuesday, August 30 &ndash; Office Hours
>  - Office Hours: 7-8pm
>  - Zoom: https://ucsd.zoom.us/j/96458655520


---


### Grading

 - **Student group research and participation: 30%**
    - Class participation: 10%
    - Group research and presentation: 20%
        - Signup: https://docs.google.com/spreadsheets/d/1QPzLh9vVuuy8PDCHZhj1w48fA8xVvfOBb1-CYDEFhr4/edit?usp=sharing
 - **Assignments : 70%**
    - Assignment 1: 10%
    - Assignments 2 to 5: 15% each
        - Generally: 5% lab portion, 5% working final code, 5% writeup

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

Assignments are for groups of up-to 2.
Group presentations are for different groups of 2 — network!

#### Late Policy

Within one week of original deadline: 10% penalty.

Within two weeks of original deadline: 30% penaly.

Submissions are not accepted more than two weeks past the original deadline.
(For exceptional situations, please email Pat, and we'll work something out.)

#### Attendance

Attendance is required for this course. We also recognize that life happens, so please
just be sure to let us know.

No-show (without notice); late: -5% / occurance. (Need to get explicitly permission
each occasion; preferably in advance, but we know life happens.)


[heterocl-home]: https://heterocl.csl.cornell.edu/
[heterocl-pdf]: https://www.csl.cornell.edu/~zhiruz/pdfs/heterocl-fpga2019.pdf
[heterocl-pptx]: wes237b-su22-StudentPresentation-HeteroCL.pptx
[simdcam-home]: https://personalpages.manchester.ac.uk/staff/p.dudek/scamp/default.htm
[simdcam-pptx]: wes237b-su22-StudentPresentation-SIMDCamera.pptx
