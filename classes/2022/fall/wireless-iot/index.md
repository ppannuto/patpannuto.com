<div align="center">
<h1><a href="/">Pat Pannuto</a></h1>
</div>

----

<h1>Wireless and Communication in the Internet of Things</h1>

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

<h2>CSE190(C00) / CSE291(C00) - Fall 2022</h2>

This course is a "mezzanine" class, i.e. it is open to both undergraduate and
graduate students, but you must register for 190 or 291 as-appropriate.

Meets M/W/F from 13:00 to 13:50.
Lectures are in 2154&nbsp;CSE.
Labs are in 3219&nbsp;CSE.

[Pat Pannuto](https://patpannuto.com) is the instructor, and their office is CSE 3202 (right in the corner).<br/>
Office hours TBA.

[Nishant Bhaskar](https://cseweb.ucsd.edu/~nibhaska/) is the TA.
Office hours, location TBA.

&rarr; [Click here for the UCSD Embedded Seminar](https://sites.google.com/eng.ucsd.edu/embeddedlunch/) (Thr 12:30-1:30) &ndash; All are welcome!

---

[TOC]

---

## Overview

Internet of Things (IoT) devices are often battery-powered, or sometimes even
energy-harvesting and battery-free. For most applications, 80% or more of
power goes to communication, i.e.\ sending data between the IoT device and the
internet at large. These two realities mean that many IoT devices use custom
communication technologies, or common ones in different ways (e.g. why does my
Fitbit scale make my home WiFi go literally 100x slower when it's on?).

This class will focus on how an IoT system designer should choose and use the
wide array of wireless technologies. Specifically, we will look at WiFi,
Classic Bluetooth, Bluetooth Low Energy, IEEE 802.15.4, 2g/3g/4g/5g cellular,
LTE-M, NB-IoT, LoRa, SigFox, and some time with more esoteric choices, such
as Visible Light Communication (VLC), Infrared Communication (IR), Ultrasonic,
and boutique RF such as wake-up radios and backscatter. Persons finishing this
course should be well-suited for work in real-world IoT systems upon
completion.


### Target Audience

The intended audience of this course is technically-oriented makers.
People who want to build (non-wall-powered) interesting stuff that will
eventually need to talk to the world.
This class looks at the (low-power) options and tries to give some basic
experience in each of them.

**This is an advanced course.** Labs will have instructions of _what_ you
are supposed to do, but not step-by-step instructions of _how_ you are
supposed to do things. _You_ are expected to use resources (Google,
Stack&nbsp;Overflow, course staff, classmates, etc.) to figure out how
to get things done.


### Learning Goals of this Course

At the end of this class, students should be able to:

1. Understand tradeoffs in wireless protocol design and how those tradeoffs influence suitability for application goals.
1. Make or support communication technology design decisions with respect to application requirements, device capabilities, and infrastructure requirements.
1. Explain the basic operating principles and performance of:
    - Bluetooth Low Energy
    - 802.15.4 and Thread
    - WiFi
    - LoRa
    - Basic Cellular Data
1. Explain what "{B,P,L,W}AN", "star", "mesh", and "cell" mean in wireless networking, and how topology influences system design and performance.
1. Estimate performance—in throughput, latency, energy use, and reliability—given technical information on a wireless technology.
1. Demonstrate basic self-sufficiency in the compilation, loading, and testing of previously-unseen software on previously-unseen hardware platforms.
    - TODO: Course design Q: How to satisfy this goal with group labs? Maybe pre-lab / homework can help here?


---

## Syllabus

> _Note: This is a new course, and is still experimental._
>
> This syllabus is subject to change as-needed, and we ask that you are
> forgiving of any rough edges.

This class aims to be reasonably self-contained.
The primary responsibilities are to

 1. Come to lectures ready to engage in the material.
 2. Come to the lab days **prepared** and ready to hack.

We will also have a few small homework assignments throughout the quarter.
These are intended to be more fun and educational about the extant
infrastructure in the world around you than a large amount of work.


### Course Staff

[Pat Pannuto](https://patpannuto.com) is the instructor and their office is [CSE 3202](https://cse.ucsd.edu/about/floormaps) (right in the corner).
Their email is [ppannuto@ucsd.edu](mailto:ppannuto@ucsd.edu?Subject=CSE190-CSE291:);
please remember to include `CSE190` or `CSE291` in the subject line for class issues.

##### What should you call me?
Most students call me Professor or Professor Pannuto or Dr. Pannuto.
I also answer happily to &ldquo;Prof[essor] P.&rdquo;

##### What should I call you?
I should call you by your preferred name, with the correct pronunciation and any honorific or pronouns you choose.
Please correct me (in the chat if there is one, out loud in class or in Zoom, or via email/Piazza/etc after the fact – however you are most comfortable) if I ever make a mistake.


#### TA - Nishant Bhaskar

[Nishant Bhaskar](https://cseweb.ucsd.edu/~nibhaska/) is the TA.


### Prerequisites

`CSE 101: Design and Analysis of Algorithms` and `CSE 110: Software Engineering`
(or equivalents) are required prerequisites for this course.

> Transitively, `CSE 30: Computer Organization and Systems Programming` (or
> equivalent) is thus also required.
> **We expect that you are comfortable with C code.**

We expect that you are comfortable with the basics of software engineering,
i.e.,
modular design,
data structures,
physical (in-memory) representation of data structures,
code compilation,
build systems,
version control,
debuggers,
and **TODO: More?**.

`CSE 123: Computer Networks` is not a prerequisite of this course. However, if
you are able to take 123 in advance of this course or concurrently, it is
helpful.


### Textbook & Other Resources

**TODO:**

No textbook Req'd

List of useful resources? (Seshia-Lee book? Tock book?)



### Schedule

This course meets Mon/Wed/Fri from 13:00 to 13:50 US/Pacific.

Generally, we will have lecture on Mondays and Wednesday with a lab section on Friday.
However, this will vary certain weeks, so please plan to pay attention to the course schedule.

Lectures are in ...

Labs are in ...


#### (A?)Sychronous?, Remote?, Recordings?

This course is designed for synchronous, in-person instruction.
That said, life happens, so we will make _best-effort_ attempts to stream the
lectures via Zoom and will make these recordings available in Canvas.

Please be sure to review the [Participation](#15-participation-peer-instruction) section in detail as well.


#### Office Hours

Up-to-date office hours are available in Canvas.


### Grading

A quick reminder: Effective learning comes from **active engagement** and **re-enforcement**.
Activities, assignments, and grading are designed to help with this.

_You get out of class what you put into it._

#### 10%: Minute-Quizzes

Lecture will begin with a "minute-quiz."
These will be (very) short and will cover material from the prior lecture, or possibly pre-lab, lab, post-lab, homework or other assignment.
You should not need to study or worry about these – if you were there and paying attention, you'll be prepared.

Correct quizzes earn 1%/ea, incorrect quizzes earn 0.5%/ea, and missing quizzes are 0%.
Excluding the first day of class, and considering holidays, there are
**`15?? todo-sched`**
quizzes.
Anything earned over 10% counts as half.
e.g., someone who answers all 15 correctly will score 12.5% in this section.
This creates a natural, built-in makeup policy that allows you to miss up to three lectures without penalty.
For this reason, there is no makeup opportunity for missed quizzes.

Quizzes are released at 13:00 and collected at 13:02. No late quizzes are accepted.


#### 10%: Homework

 - Maybe 2 hw's at 5% ea?
    - cellular data worksheets?


> ##### Homework Late Policy
>
> _Homework ever is better than homework never._
>
> The goal of homework is to help you to understand better by working through problems on your own.
> To that end, we will allow for late submission of homework at any point until end of business on the last regular instruction day of the term (17:00, US/Pacific, December 2nd).
> Late homework will receive 50% of earned points.
> Late homework is not eligible for regrades and will be graded and returned at instructor convenience.
> Late homework should take care to add extra details showing how you, personally worked through problems and that your work is your own.
> Late homework that is "just answers" or otherwise does not clearly show your own work will receive no credit.


#### 60%: Labs

This class will have 4 labs.
The breakdown within each lab may vary.

(Nominal: 15% ea, 5% pre-lab, 10% lab and report?)

##### 20%: Pre-Labs

Pre-labs are absolutely essential to your success during the lab session.
You *must* have completed your pre-lab *before* the start of the lab session to make good use of the lab time.

For this reason, your pre-labs are due by the start of lab.
There are no exceptions, and there is no late policy here.
If you have not completed the pre-lab by the start of the lab session you will receive no credit for that pre-lab
(even though you will probably have to do the pre-lab work, during lab..., before you can actually start on the lab).

##### 40%: Post-Labs and Lab Reports

The meat of the lab work and some writeups.


#### 15% Final Exam (Design Assignment)

Take-home 'final', it's an end-to-end pencil-and-paper design task.
Not so far removed from the homeworks, but an exercise of:
"You're an engineer at startup X, who's building Y, with requirements
1,2,3,4. What do you design and why."


#### Final Grades

I believe in mastery learning. My goal is to teach you the material and for
everyone to learn it. I am most successful if everyone in class _earns_ an `A`.
This class will not be curved.

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



<table class="final-grade-table">
<caption>
Final grade <i>estimator</i>.
<small>Disclaimer: I wrote this in an afternoon in ugly javascript.
I use Excel to compute actual final grades.</small>
</caption>
<tr>
<th></th>
<th>Earned %</th>
<th>Nominal Max</th>
<th>Final %</th>
<th>Final Grade</th>
</tr>
<tr class="final-grade-row">
<th>Minute Quizzes</th>
<td><input type="number" value="18" /></td>
<td>10</td>
<td></td>
<td rowspan="2" id="final-grade-percent"></td>
</tr>
<tr class="final-grade-row">
<th>Homework</th>
<td><input type="number" value="15" /></td>
<td>10</td>
<td></td>
</tr>
<tr class="final-grade-row">
<th>Pre-Labs</th>
<td><input type="number" value="24" /></td>
<td>20</td>
<td></td>
<td rowspan="2" id="final-grade-letter"></td>
</tr>
<tr class="final-grade-row">
<th>Labs</th>
<td><input type="number" value="48" /></td>
<td>40</td>
<td></td>
</tr>
<tr class="final-grade-row">
<th>Final Project</th>
<td><input type="number" value="15" /></td>
<td>15</td>
<td></td>
</tr>
</table>

<script>
function computeGrades() {
  const rows = document.getElementsByClassName('final-grade-row');
  let total = 0;

  for (const row of rows) {
    console.assert(row.children.length >= 4, row);
    // row.children[0] = th = category
    const earned = Number(row.children[1].children[0].value);
    const nom_max = Number(row.children[2].innerText);
    const finalp = row.children[3];

    let final;

    if (earned <= nom_max) {
      final = earned;
    } else {
      let overage = earned - nom_max;
      final = nom_max + (overage/2);
    }

    console.log(earned, nom_max, final);

    finalp.innerText = final;

    total += final;
  }

  const totalp = document.getElementById('final-grade-percent');
  const totall = document.getElementById('final-grade-letter');

  totalp.innerText = total.toFixed(1);

  let total_rounded = Number(total.toFixed(1));

  if (total_rounded >= 96.7) {
    totall.innerText = "A+";
  } else if (total_rounded >= 93) {
    totall.innerText = "A";
  } else if (total_rounded >= 90) {
    totall.innerText = "A-";
  } else if (total_rounded >= 86.7) {
    totall.innerText = "B+";
  } else if (total_rounded >= 83.3) {
    totall.innerText = "B";
  } else if (total_rounded >= 80) {
    totall.innerText = "B-";
  } else if (total_rounded >= 76.7) {
    totall.innerText = "C+";
  } else if (total_rounded >= 73.3) {
    totall.innerText = "C";
  } else if (total_rounded >= 70) {
    totall.innerText = "C-";
  } else if (total_rounded >= 60) {
    totall.innerText = "D";
  } else {
    totall.innerText = "F";
  }
}

// Any input change, recompute
const rows = document.getElementsByClassName('final-grade-row');

for (const row of rows) {
  const input = row.children[1].children[0];
  // Only if input exists (i.e. skip title row, which won't have this child)
  if (input) {
    input.addEventListener("input", computeGrades);
  } else {
    console.log('no listener for', row, input);
  }
}

// And do once on load with example grades
computeGrades();
</script>



##### CAPEs Incentive

If, at the end of the term, the
[CAPE response rate](https://cape.ucsd.edu/responses/current.aspx)
is >=90.0%, we will
**TODO: Do something helpful**


### Academic Integrity

**TODO: Think about what the goal is to say here; group-heavy work...**

Old text from 141:
<details markdown="1">
In this course we expect students to adhere to the [UC San Diego Integrity of Scholarship Policy](https://senate.ucsd.edu/Operating-Procedures/Senate-Manual/Appendices/2).
This means that you will complete your work honestly, with integrity, and support an environment of integrity within the class.

Cheating WILL be taken seriously.
It is not fair to honest students to take cheating lightly, nor is it fair to the cheater to let them go on thinking that is a reasonable alternative in life.

The following is not considered cheating:

 - Discussing homework in groups (with the writeup done separately, later).
 - Discussing additional, unassigned problems (e.g. nearby numbers in the back-of-chapter problem lists) in any way, shape, or form.

The following is:

 - Discussing homework with someone who has already completed the problem, or looking at their completed write-up.
 - Using homework solutions from the web, previous versions of the class, or anywhere else.
 - Receiving, providing, or soliciting assistance from another student during a test.

Homework is not intended to be a grade-maker, but to prepare you for the tests, which are the grade-makers.
Cheating on homework just hurts you.
If you are choosing between not turning in an assignment, or using somebody's else work, do yourself a favor and just don't turn it in.
You are facing a permanent mark on your academic record and a certainty of having to explain it to any future employer or school that you apply to.

If you are caught cheating on any assignment, you will first be flagged with an
`X` course grade, which prevents you from withdrawing from the course for any
reason.
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
</details>


---


## Resources for Students

<!-- fold this temporarily -->
<details markdown="1">
### Getting Help
First, try to make sure you help yourself by staying up to date with course material. Nearly half the grade is participation and homeworks, which are not meant to be tricky, simply to give you practice and confidence with the material.
We also encourage forming study groups to discuss 141 material.
In addition to our homework assigments, there are quite a few good problems at
the end of each chapter of the course textbook. Trying extra / similar-looking
problems (especially with your study group) is perfectly acceptable, and you
may discuss extra problems you work on with no limitations.

**Discussion section** is an opportunity for additional explanation and guided
practice with material from each week. Professor Pannuto did not go to any
discussions in their first two years of college becuase discussions were
&ldquo;not required&rdquo; and no one ever really explained what they were or
why they were helpful. Professor Pannuto got dragged to a discussion section
for a theory and cryptography course by a friend to whom they are forever
grateful at the end of sophomore year, realized how insanely helpful
discussions were, and had significantly better grades thereafter.

**Office hours** are the perfect place for one-on-one support and asking specific
questions. Office hours are most useful after you have worked on the problem for
a little while yourself (I usually say that you should struggle with a problem
for fifteen full minutes, but not more than fifteen minutes before seeking help).
You are not interrupting course staff (TAs _or_ the professors) when you come to
office hours. It is _literally_ our job to be available to help you during those
times. Office hours are also not restricted to content from 141. Folks have asked
about research / grad school in CS, how to get jobs in computer architecture,
what other classes to take if they like (or hate!) this stuff, the best coffee
shops for working accessible by light rail, tips for developing fruit-bearing
trees in San Diego, or anything else that you would like to know about.

**The IDEA Engineering Student Center**, located just off the lobby of Jacobs
Hall, is a hub for student engagement, academic enrichment,
personal/professional development, leadership, community involvement, and a
respectful learning environment for all.  The Center offers a variety of
programs, listed in the IDEA Center Facebook page at
http://www.facebook.com/ucsdidea/ and the Center web site at
http://idea.ucsd.edu/.  The IDEA Center programs support both undergraduate
students and graduate students.

### Diversity and Inclusion
We are committed to fostering a learning environment for this course that
supports a diversity of thoughts, perspectives and experiences, and respects
your identities (including race, ethnicity, heritage, gender, sex, class,
sexuality, religion, ability, age, educational background, etc.).  Our goal is
to create a diverse and inclusive learning environment where all students feel
comfortable and can thrive.

Our instructional staff will make a concerted effort to be welcoming and
inclusive to the wide diversity of students in this course.  If there is a way
we can make you feel more included please let one of the course staff know,
either in person, via email/discussion board, or even in a note under the door.
Our learning about diverse perspectives and identities is an ongoing process,
and we welcome your perspectives and input.

We also expect that you, as a student in this course, will honor and respect
your classmates, abiding by the
[UCSD Principles of Community](https://ucsd.edu/about/principles.html).
Please understand that others’ backgrounds, perspectives and experiences may be
different than your own, and help us to build an environment where everyone is
respected and feels comfortable.
If you experience any sort of harassment or discrimination, please contact the
instructor as soon as possible.   If you prefer to speak with someone outside
of the course, please contact the
[Office of Prevention of Harassment and Discrimination](https://ophd.ucsd.edu/).


### Students with Disabilities
We aim to create an environment in which all students can succeed in this course.  If you have a disability, please contact the Office for Students with Disability (OSD), which is located in University Center 202 behind Center Hall, to discuss appropriate accommodations right away.  We will work to provide you with the accommodations you need, but you must first provide a current Authorization for Accommodation (AFA) letter issued by the OSD.  You are required to present their AFA letters to Faculty (please make arrangements to contact me privately) and to the OSD Liaison in the department in advance so that accommodations may be arranged.

### Basic Needs/Food Insecurities
If you are experiencing any basic needs insecurities (food, housing, financial resources), there are resources available on campus to help, including The Hub and the Triton Food Pantry.
Please visit [thehub.ucsd.edu](/http://thehub.ucsd.edu/) for more information.
</details>

---


## Agenda


### Schedule

<!--
<pre>

Major Landmarks:

Fall Quarter begins             Mon, Sep 19
Instruction begins              Thu, Sep 22 <-- First class Fri
CSE Faculty Retreat             Fri, Oct  7 --or-- Fri Oct 14
Indigenous Peoples' Day         Mon, Oct 10
Pat Travel                      Fri, Oct 28
Pat Travel                      Mon, Nov  7 <maybe Wed Nov 9 too>
Veteran's Day                   Fri, Nov 11
Thanksgiving                    Fri, Nov 25
Instruction ends                Fri, Dec  2
Final Exam?                     ..?..
Fall Quarter ends               Sat, Dec 10



F'22 First Draft Schedule

    M                             W                               F
0   -                             -                               LEC     Intro
1   LEC     Networking Basics     LEC      BT PHY/MAC, BLE        LAB     Wireshark?
2   LEC     BLE, BLE adv's        LEC      BLE Conn's             LAB[!P] BLE p1: Basic BLE + BLE adv sniff?
3   ~~hol~~                       LEC      Wrap BLE, 15.4 [trad]  LAB[!P] BLE p2: Advaced BLE stuff?
4   LEC     15.4, Thread          LEC      15.4, Thread           LAB     154 p1: Raw 15.4 Connections?
5   LEC     Zigbee, Routing       LEC      [new] CoAP, MQTT, etc  LAB[!P] 154 p2: Thread Network? CoAP/MQTT??
6   LEC     WiFi [phy]            LEC      WiFi [mac]             LEC     Wide-Area Intro, LoRa start
7   LAB[!P] LoRa p1: Basic LoRa   LEC[!P?] LoRa, SigFox, etc      ~~hol~~
8   LAB     LoRa p2: chat app??   LEC      Intro Cell, 2g         LEC     3g/4g/5g
9   LAB     ??? cell p1 ???       LEC      Cell Wrap-up           ~~hol~~
10  LAB     ??? cell p2 ???       LEC      Misc: Weirder RF       LEC     Misc: non-RF: VLC, IR, UL...
11  Final exam week

^ no WiFi Lab, small Wifi HW?
^ what other HW?

- HW: Background knowledge check HW?

$branden$ It would be really nice to have a basic 15.4 example that you could build on top of yourself.
For example, it's easy to make an app where you provide a raw buffer of bytes as the advertisement payload. So figuring out what those bytes are can be the challenge.
It would similarly be great to have a base 15.4 example that just sent/received raw bytes.
Although maybe Zephyr itself has some?
https://docs.zephyrproject.org/latest/connectivity/networking/api/ieee802154.html



W'22 Schedule as reference:

        M/W                                     F
1       Networking Fundamentals; topolgies      wireshark something
2       2g/3g/4g                                Pick a country, cell phone plan
3       [Holiday] / LTE-M, NB-IoT               Revise for LP-cell
4       LoRa, SigFox, etc                       Revise for LP-ISM [next time: Helium chat]
5       BLE / BLE Adv                           Basic BLE + sniffing
6       BLE Conn / 15.4 [trad]                  BLE Connections
7       15.4 [trad] / Thread                    OpenThread demo
8       [Holiday] / Zigbee,Routing,Flooding     CoAP on OT
9       WiFi [phy] / WiFi [mac]                 _Maybe: revisit LoRa w/ HW?_, o/w more 15.4
10      VLC, IR, Ultrasonic, Boutique RF        [No class; project time]

</pre>
-->


<style>
td.class-week {
  writing-mode: vertical-lr;
  transform: rotate(180deg);
  vertical-align: middle;
  padding: 3px;
}

td.class-subject {
  font-weight: bolder;
  writing-mode: vertical-lr;
  transform: rotate(180deg);
  vertical-align: middle;
  border-style: dotted;
  padding: 3px;
}

.visuallyhidden {
  visibility: hidden;
}

.due {
  color: red;
  font-weight: bolder;
}

.assigned {
  font-weight: bolder;
}

.lab {
  background-color: aliceblue;
}
</style>


<!-- https://alphagov.github.io/table-editor/generic-tables.html -->
<table class="source-tableeditor table table-hover">
<tbody>
<tr>
<th>&nbsp;&nbsp;<!--Subject--></th>
<th>&nbsp;&nbsp;<!--Week--></th>
<th colspan="4">When</th>
<th>Where</th>
<th>What</th>
</tr>
<tr>
<td rowspan="4" class="class-subject">Introduction &amp; Networking Basics</td>
<td class="class-week">Week&nbsp;0</td>
<td>Fri</td>
<td>Sep 23</td>
<td></td>
<td><strong>Assigned:</strong> Pre-Lab 1</td>
<td>2154</td>
<td>
<strong>Welcome &amp; Intro</strong>
<ul>
<li>Course overview</li>
<li>Introduction the IoT</li>
<li>Introduction to wireless communication</li>
</td>
</tr>
<tr>
<td rowspan="3" class="class-week">Week&nbsp;1</td>
<td>Mon</td>
<td>Sep 26</td>
<td></td>
<td></td>
<td>2154</td>
<td>
<strong>Networking Basics</strong>
<ul>
<li>OSI layer model</li>
<li>IP and routing basics</li>
<li>Data link layer</li>
</ul>
</td>
</tr>
<tr>
<td>Wed</td>
<td>Sep 28</td>
<td></td>
<td></td>
<td>2154</td>
<td>
<strong>Wireless basics</strong>
<ul>
<li>PHY layer</li>
<li>How PHY impacts Data impacts Network...</li>
<li>Medium Access Control</li>
</tr>
<tr>
<td>Fri</td>
<td>Sep 30</td>
<td><span class="due">Due: </span>Pre-Lab 1<br /><br /></td>
<td><span class="assigned">Assigned:</span> Post-Lab 1</td>
<td class="lab">3219</td>
<td class="lab">
<strong>Lab: Wireshark</strong><br />
<em>Outcomes&ndash;</em> After this lab you should understand:
<ul>
<li>What is &ldquo;sniffing&rdquo; and how to do it?</li>
<li>How to find specific traffic you generate?</li>
<li>How to identify layers in a captured packet?</li>
<li>How to infer information about unknown traffic?</li>
</ul>
</td>
</tr>
<tr>
<td rowspan="6" class="class-subject">Bluetooth</td>
<td rowspan="3" class="class-week">Week&nbsp;2</td>
<td>Mon</td>
<td>Oct 3</td>
<td></td>
<td><span class="assigned">Assigned: </span>Pre-Lab 2</td>
<td>2154</td>
<td>Bluetooth PHY/MAC, BLE</td>
</tr>
<tr>
<td>Wed</td>
<td>Oct 5</td>
<td></td>
<td></td>
<td>2154</td>
<td>BLE, BLE adv's</td>
</tr>
<tr>
<td>Fri</td>
<td>Oct 7</td>
<td><span class="due">Due: </span>Pre-Lab 2</td>
<td><strong>&nbsp;</strong></td>
<td class="lab">3219</td>
<td class="lab">LAB: BLE Adv's</td>
</tr>
<tr>
<td rowspan="3" class="class-week">Week&nbsp;3</td>
<td>Mon</td>
<td>Oct 10</td>
<td><strong></strong></td>
<td></td>
<td>2154</td>
<td>BLE Conn's</td>
</tr>
<tr>
<td>Wed</td>
<td>Oct 12</td>
<td></td>
<td></td>
<td>2154</td>
<td>Wrap BLE, 15.4 [trad]</td>
</tr>
<tr>
<td>Fri</td>
<td>Oct 14 <span class="visuallyhidden">!P</span></td>
<td></td>
<td><strong>Assigned:</strong> Post-Lab 2</td>
<td class="lab">3219</td>
<td class="lab">LAB: BLE Conn's</td>
</tr>
<tr>
<td rowspan="6" class="class-subject">802.15.4</td>
<td rowspan="3" class="class-week">Week&nbsp;4</td>
<td>Mon</td>
<td>Oct 17</td>
<td><strong></strong></td>
<td><strong>Assigned: </strong>Pre-Lab 3</td>
<td>2154</td>
<td>15.4, Thread</td>
</tr>
<tr>
<td>Wed</td>
<td>Oct 19</td>
<td></td>
<td></td>
<td>2154</td>
<td>15.4, Thread</td>
</tr>
<tr>
<td>Fri</td>
<td>Oct 21</td>
<td><strong>Due: </strong>Pre-Lab 3</td>
<td><strong>&nbsp;</strong></td>
<td class="lab">3219</td>
<td class="lab">LAB: 15.4 Raw Conn's?</td>
</tr>
<tr>
<td rowspan="3" class="class-week">Week&nbsp;5</td>
<td>Mon</td>
<td>Oct 24</td>
<td></td>
<td></td>
<td>2154</td>
<td>Zigbee, Routing</td>
</tr>
<tr>
<td>Wed</td>
<td>Oct 26</td>
<td></td>
<td></td>
<td>2154</td>
<td>CoAP, MQTT, etc</td>
</tr>
<tr>
<td>Fri</td>
<td>Oct 28 <span class="visuallyhidden">!P</span></td>
<td><strong></strong></td>
<td><strong>Assigned: </strong>Post-Lab 3</td>
<td class="lab">3219</td>
<td class="lab">LAB: 15.4 Thread? CoAP MQTT?</td>
</tr>
<tr>
<td rowspan="6" class="class-subject">WiFi</td>
<td rowspan="3" class="class-week">Week&nbsp;6</td>
<td>Mon</td>
<td>Oct 31</td>
<td><strong></strong></td>
<td><strong>Assigned: </strong>Pre-Lab 4</td>
<td>2154</td>
<td>WiFi (phy)</td>
</tr>
<tr>
<td>Wed</td>
<td>Nov 2</td>
<td></td>
<td></td>
<td>2154</td>
<td>WiFi (mac)</td>
</tr>
<tr>
<td>Fri</td>
<td>Nov 4</td>
<td></td>
<td></td>
<td>2154</td>
<td>?? more WiFi ?? Energy Analysis / Performance ??</td>
</tr>
<tr>
<td rowspan="3" class="class-week">Week&nbsp;7</td>
<td>Mon</td>
<td>Nov 7 <span class="visuallyhidden">!P</span></td>
<td><strong>Due: </strong>Pre-Lab 4</td>
<td><strong>&nbsp;</strong></td>
<td class="lab">3219</td>
<td class="lab">LAB: WiFi (??)</td>
</tr>
<tr>
<td>Wed</td>
<td>Nov 9 <span class="visuallyhidden">?P</span></td>
<td><strong></strong></td>
<td><strong>Assigned: </strong>Post-Lab 4</td>
<td class="lab">3219</td>
<td class="lab">LAB: WiFi (??)</td>
</tr>
<tr>
<td>Fri</td>
<td>Nov 11</td>
<td></td>
<td></td>
<td colspan="2">~holiday~</td>
</tr>
<tr>
<td rowspan="4" class="class-subject">LP-WANs</td>
<td rowspan="3" class="class-week">Week&nbsp;8</td>
<td>Mon</td>
<td>Nov 14</td>
<td><strong></strong></td>
<td><strong>Assigned: </strong>Pre-Lab 5</td>
<td>2154</td>
<td>Wide-Area Intro</td>
</tr>
<tr>
<td>Wed</td>
<td>Nov 16</td>
<td></td>
<td></td>
<td>2154</td>
<td>LoRa, SigFox, etc</td>
</tr>
<tr>
<td>Fri</td>
<td>Nov 18</td>
<td><strong>Due: </strong>Pre-Lab 5</td>
<td><strong>&nbsp;</strong></td>
<td class="lab">3219</td>
<td class="lab">LAB: LoRa (Basic LoRa?)</td>
</tr>
<tr>
<td rowspan="3" class="class-week">Week&nbsp;9</td>
<td>Mon</td>
<td>Nov 21</td>
<td><strong></strong></td>
<td><strong>Assigned: </strong>Post-Lab 5</td>
<td class="lab">3219</td>
<td class="lab">LAB: LoRa (chat app?)</td>
</tr>
<tr>
<td rowspan="4" class="class-subject">Cellular</td>
<td>Wed</td>
<td>Nov 23</td>
<td><strong></strong></td>
<td><strong>Assigned: </strong>HW-Cell</td>
<td>2154</td>
<td>Intro cell, 2g [expect low attendance]</td>
</tr>
<tr>
<td>Fri</td>
<td>Nov 25</td>
<td></td>
<td></td>
<td colspan="2">~holiday~</td>
</tr>
<tr>
<td rowspan="3" class="class-week">Week&nbsp;10</td>
<td>Mon</td>
<td>Nov 28</td>
<td><strong></strong></td>
<td></td>
<td>2154</td>
<td>3g/4g/5g</td>
</tr>
<tr>
<td>Wed</td>
<td>Nov 30</td>
<td></td>
<td></td>
<td>2154</td>
<td>Cell Wrap-Up</td>
</tr>
<tr>
<td class="class-subject">Grab Bag</td>
<td>Fri</td>
<td>Dec 1</td>
<td><strong>Due: </strong>HW-Cell</td>
<td><strong>&nbsp;</strong></td>
<td>2154</td>
<td>Misc: werider RF, non-RF stuff</td>
</tr>
<tr>
<td></td>
<td class="class-week">Week&nbsp;11</td>
<td>EXAM TBD</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Old full table:
<details>

<table class="table table-bordered table-hover">
  <tr class="table-primary">
    <th>Date</th>
    <th>Topic</th>
    <th>Assignment / Additional Materials</th>
  </tr>

  <tr class="table-info">
    <td colspan="4">Week 0: Introduction, Motivation, and Background</td>
  </tr>
  <tr>
    <td>Jan&nbsp;3<br/><a href="#">[slides]</a><a href="#">[pdf]</a></td>
    <td>
    <ul>
      <li>What's IoT?</li>
      <li>What's &ldquo;low-power&rdquo;?</li>
    </ul>
    </td>
    <td></td>
  </tr>

  <tr class="table-info">
    <td colspan="4">Week 0: Introduction, Motivation, and Background</td>
  </tr>
  <tr>
    <td>Jan&nbsp;5<br/><a href="WI22_cse291-02-networking.pptx">[slides]</a><a href="WI22_cse291-02-networking.pdf">[pdf]</a></td>
    <td>
    <ul>
      <li>Fundamentals of Networking</li>
      <li>(Aka CSE123 in an hour flat :D)</li>
    </ul>
    </td>
    <td></td>
  </tr>
  <tr class="table-warning">
    <td>Jan&nbsp;7</td>
    <td>
    <ul>
      <li>Learning to look at networks</li>
    </ul>
    </td>
    <td>
    <ul>
      <li>Wireshark local network</li>
      <li>Identify and report on (a) traffic you made and can find, (b) traffic you didn't know you were making, (c) something you can't identify.</li>
      <li><a href="WI22_Lab1_Wireshark.docx">Lab Worksheet [docx]</a> <a href="WI22_Lab1_Wireshark.pdf">[pdf]</a></li>
    </ul>
    </td>
  </tr>

  <tr class="table-info">
    <td colspan="4">Long-Range Technologies</td>
  </tr>
  <tr>
    <td>Jan&nbsp;10<br/><a href="WI22_cse291-03-og-cell.pptx">[slides]</a><a href="WI22_cse291-03-og-cell.pdf">[pdf]</a></td>
    <td>
    Mobile Networking Origins
    <ul>
      <li>Fundamentals of ceullar technology</li>
      <li>Relevance of &ldquo;old&rdquo; cell technology to today&rsquo;s IoT</li>
    </ul>
    </td>
    <td>
    <b>Optional</b> Reading
    <ul>
      <li><a href="https://patpannuto.com/pubs/jagtap2021centuryinfra.pdf">Century-Scale Smart Infrastructure; HotOS'21</a> &mdash; Some thoughts on sunset issues in wireless technologies, how they will affect the IoT, and what we might do about it.</li>
    </ul>
    </td>
  </tr>
  <tr>
    <td>Jan&nbsp;12<br/><a href="WI22_cse291-04-moreGs-cell.pptx">[slides]</a><a href="WI22_cse291-04-moreGs-cell.pdf">[pdf]</a></td>
    <td>
    Evolution of Cellular
    <ul>
      <li>3G, 4G, and 5G</li>
    </ul>
    </td>
    <td>
    </td>
  </tr>
  <tr class="table-warning">
    <td>Jan&nbsp;14</td>
    <td>
    Emprical, Global Perspective of Cellular
    </td>
    <td>
    <ul>
      <li>Estimate cellular cost and performance for an IoT deployment.</li>
      <li><a href="WI22_Lab2_CellGlobalPerspective.docx">Lab Worksheet [docx]</a> <a href="WI22_Lab2_CellGlobalPerspective.pdf">[pdf]</a></li>
    </ul>
    </td>
  </tr>
  <tr>
    <td>Jan&nbsp;17</td>
    <td colspan="2"><i>No class, MLK Holiday</i></td>
  </tr>
  <tr>
    <td>Jan&nbsp;19<br/><a href="WI22_cse291-05-cell-for-IoT.pptx">[slides]</a><a href="WI22_cse291-05-cell-for-IoT.pdf">[pdf]</a></td>
    <td>
    Upcoming Cellular IoT Technologies
    <ul>
      <li>LTE Cat-M</li>
      <li>NB-IoT</li>
    </ul>
    </td>
    <td>
    </td>
  </tr>
  <tr class="table-warning">
    <td>Jan&nbsp;21</td>
    <td>
    Design Decisions I
    </td>
    <td>
    <ul>
      <li>Radio technology and device lifetime</li>
      <li>Find a cellular radio and figure out how much energy it will need.</li>
      <li><a href="WI22_Lab3_CellIoTPower.docx">Lab Worksheet [docx]</a> <a href="WI22_Lab3_CellIoTPower.pdf">[pdf]</a></li>
    </ul>
    </td>
  </tr>
  <tr>
    <td>Jan&nbsp;24 &amp; 26<br/><a href="WI22_cse291-06_07-LPWANs.pptx">[slides]</a><a href="WI22_cse291-06_07-LPWANs.pdf">[pdf]</a></td>
    <td>
    LPWANs
    <ul>
      <li>LPWAN Design</li>
      <li>Unlicensed LPWANs</li>
      <li>LPWAN Challenges</li>
    </ul>
    </td>
    <td>
    Papers referenced for those interested in more details:
    <small>
    <ul>
      <li>Abusayeed Saifullah, et al. <i>SNOW: Sensor Network over White Spaces.</i> SenSys, 2016.</li>
      <li>Xianjin Xia, et al. <i>FTrack: Parallel decoding for LoRa transmissions.</i> SenSys, 2017.</li>
      <li>Shuai Tong, et al. <i>Combating packet collisions using non-stationary signal scaling in LPWANs.</i> MobiSys, 2020.</li>
      <li>Shuai Tong, et al. <i>CoLoRa: Enabling multipacket reception in LoRa.</i> INFOCOM, 2020.</li>
      <li>Muhammad Osama Shahid, et al. <i>Concurrent interference cancellation: Decoding multi-packet collisions in LoRa.</i>, SIGCOMM, 2021.</li>
    </ul>
    </small>
    </td>
  </tr>
  <tr class="table-warning">
    <td>Jan&nbsp;28</td>
    <td>
    Design Decisions II
    </td>
    <td>
    <ul>
      <li><a href="WI22_Lab4_LPWAN-Full-Circle.docx">Lab Worksheet [docx]</a> <a href="WI22_Lab4_LPWAN-Full-Circle.pdf">[pdf]</a></li>
    </ul>
    </td>
  </tr>

  <tr class="table-info">
    <td colspan="4">RF in the Small: PANs and WANs</td>
  </tr>
  <tr>
    <td>Jan&nbsp;31<br/><a href="WI22_cse291-08-BLE.pptx">[slides]</a><a href="WI22_cse291-08-BLE.pdf">[pdf]</a></td>
    <td>
    Bluetooth Low Energy
    </td>
    <td>
    Yes, <a href="https://www.snopes.com/fact-check/bluetooth-etymology/">Bluetooth really is named after a Viking king, and the symbol is his initials</a>.
    </td>
  </tr>
  <tr>
    <td>Feb&nbsp;2<br/><a href="WI22_cse291-09-BLE-adv.pptx">[slides]</a><a href="WI22_cse291-09-BLE-adv.pdf">[pdf]</a></td>
    <td>
    BLE Advertisements
    <ul>
      <li>Advertisement Detail</li>
      <li>Advertisement-based Networking?</li>
    </ul>
    </td>
    <td>
    Papers referenced for those interested in more details:
    <small>
    <ul>
      <li>Martin, Jeremy, et al. <i>Handoff all your privacy–a review of apple’s bluetooth low energy continuity protocol.</i> PETS, 2019</li>
      <li>DeBruin, Samuel, et al. <i>Powerblade: A low-profile, true-power, plug-through energy meter.</i>SenSys, 2015.</li>
      <li>Schrader, Raphael, et al. <i>Advertising power consumption of bluetooth low energy systems.</i> IDAACS-SWS, 2016.</li>
      <li>Jeon, Wha Sook, et al. <i>Performance analysis of neighbor discovery process in bluetooth low-energy networks.</i> IEEE TVT, 2016.</li>
      <li>Perez-Diaz de Cerio, David, et al. <i>Analytical and experimental performance evaluation of BLE neighbor discovery process including non-idealities of real chipsets.</i> Sensors, 2017.</li>
      <li>Ghena, Branden. <i>Investigating Low Energy Wireless Networks for the Internet of Things.</i> PhD Thesis, 2020.</li>
      <li>Kravets, Robin, et al. <i>Beacon trains: Blazing a trail through dense BLE environments.</i> Workshop on Challenged Networks, 2016.</li>
    </ul>
    </small>
    </td>
  </tr>
  <tr class="table-warning">
    <td>Feb&nbsp;4</td>
    <td>
    Real-World BLE
    </td>
    <td>
    <ul>
      <li><a href="WI22_Lab5_IntroBLE.docx">Lab Worksheet [docx]</a> <a href="WI22_Lab5_IntroBLE.pdf">[pdf]</a></li>
    </ul>
    </td>
  </tr>
  <tr>
    <td>Feb&nbsp;7<br/><a href="WI22_cse291-10-BLE-conn.pptx">[slides]</a><a href="WI22_cse291-10-BLE-conn.pdf">[pdf]</a></td>
    <td>
    BLE Connections
    </td>
    <td></td>
  </tr>
  <tr>
    <td>Feb&nbsp;9<br/><a href="WI22_cse291-11-ieee802154.pptx">[slides]</a><a href="WI22_cse291-11-ieee802154.pdf">[pdf]</a></td>
    <td>
    [Project Check-in]<br />
    Intro to 802.15.4
    </td>
    <td></td>
  </tr>
  <tr class="table-warning">
    <td>Feb&nbsp;11</td>
    <td>
    BLE Connections
    </td>
    <td>
    <ul>
      <li><a href="WI22_Lab6_BLEConnections.docx">Lab Worksheet [docx]</a> <a href="WI22_Lab6_BLEConnections.pdf">[pdf]</a></li>
    </ul>
    </td>
  </tr>
  <tr>
    <td>Feb&nbsp;14<br/><a href="WI22_cse291-12-ieee802154_Thread.pptx">[slides]</a><a href="WI22_cse291-12-ieee802154_Thread.pdf">[pdf]</a></td>
    <td>
    Finish 802.15.4<br />
    Intro to Thread
    </td>
    <td>
    Papers referenced for those interested in more details:
    <small>
    <ul>
      <li>Hui, Jonathan W., et al. <a href="https://patpannuto.com/papers/hui2008ipdead.pdf"><i>IP is Dead, Long Live IP for Wireless Sensor Networks.</i></a> SenSys, 2008</li>
    </ul>
    </small>
    </td>
  </tr>
  <tr>
    <td>Feb&nbsp;16<br/><a href="WI22_cse291-13-Thread.pptx">[slides]</a><a href="WI22_cse291-13-Thread.pdf">[pdf]</a></td>
    <td>
    Thread
    </td>
    <td>
    Additional Resources:
    <small>
    <ul>
      <li>Geoff Mulligan and the 6LoWPAN WG. <a href="https://dl.acm.org/doi/10.1145/1278972.1278992"><i>The 6LoWPAN architecture.</i></a> EmNets, 2007.</li>
      <li>Thread Group. <a href="https://www.threadgroup.org/Portals/0/documents/support/6LoWPANUsage_632_2.pdf"><i>Thread Usage of 6LoWPAN.</i></a> White Paper, 2015.</li>
      <li>Thread Group. <a href="https://www.threadgroup.org/Portals/0/documents/support/Thread%20Network%20Fundamentals_v3.pdf"><i>Thread Network Fundamentals.</i></a> White Paper, 2020.</li>
    </ul>
    </small>
    </td>
  </tr>
  <tr class="table-warning">
    <td>Feb&nbsp;18</td>
    <td>
    Trying out Thread
    </td>
    <td>
    <p>
    For today, we are going to try to follow the <a href="https://openthread.io/codelabs/openthread-hardware#0">official OpenThread lab</a>.
    </p>
    <p><small>
    Work in groups of (at least) three to see if you can get a Thread network running across your devices.
    It's quite possible that we will end up with one large Thread network at the end of the lab, that
    would be a success too :).
    Nothing to write-up or turn in today, but do want to have Thread basics working so that we can use
    your Thread network(s) to communicate higher-level application data next week.
    </small></p>
    </td>
  </tr>
  <tr>
    <td>Feb&nbsp;21</td>
    <td colspan="2"><i>No class, Presidents' Day Holiday</i></td>
  </tr>
  <tr>
    <td>Feb&nbsp;23<br/><a href="WI22_cse291-14-Zigbee_Routing_Flooding.pptx">[slides]</a><a href="WI22_cse291-14-Zigbee_Routing_Flooding.pdf">[pdf]</a></td>
    <td>
    Zigbee<br/>
    Mesh Routing<br/>
    Mesh Flooding
    </td>
    <td>
    Additional Resources:
    <small>
    <ul>
      <li>Kim, Hyung-Sin, et al. <a href="https://rise.cs.berkeley.edu/wp-content/uploads/2019/06/KIM_LAYOUT.pdf"><i>Thread/OpenThread: A Compromise in Low-Power Wireless Multihop Network Architecture for the Internet of Things.</i></a> IEEE Communications 2019.</li>
      <li>Dutta, Prabal, et al. <a href="https://web.eecs.umich.edu/~prabal/pubs/papers/dutta12amac.pdf"><i>A-MAC: A Versatile and Efficient Receiver-Initiated Link Layer for Low-Power Wireless.</i></a> TOSN 2012.</li>
      <li>Ferrai, Federico, et al. <a href="https://ieeexplore.ieee.org/abstract/document/5779066"><i>Efficient network flooding and time synchronization with Glossy.</i></a> IPSN 2011.</li>
      <li>Ferrai, Federico, et al. <a href="https://dl.acm.org/doi/abs/10.1145/2426656.2426658"><i>Low-power wireless bus.</i></a> SenSys 2012.</li>
    </small>
    </td>
  </tr>
  <tr class="table-warning">
    <td>Feb&nbsp;25</td>
    <td>
    CoAP and End-to-End Operation
    </td>
    <td>
    <ul>
      <li><a href="WI22_Lab8_BigHappyThreadFamily.docx">Lab Worksheet [docx]</a> <a href="WI22_Lab8_BigHappyThreadFamily.pdf">[pdf]</a></li>
    </ul>
    </td>
  </tr>
  <tr>
    <td>Feb&nbsp;28<br/><a href="WI22_cse291-15-PrettyPHYForAWiFi.pptx">[slides]</a><a href="WI22_cse291-15-PrettyPHYForAWiFi.pdf">[pdf]</a></td>
    <td>WiFi [PHY]</td>
  </tr>
  <tr>
    <td>Mar&nbsp;2<br/><a href="WI22_cse291-16-WiFiReturnOfTheMAC.pptx">[slides]</a><a href="WI22_cse291-16-WiFiReturnOfTheMAC.pdf">[pdf]</a></td>
    <td>WiFi [MAC]</td>
  </tr>
  <tr class="table-warning">
    <td>Mar&nbsp;4</td>
    <td>
    <small><del>Cancelled due to weather.</del></small>
    </td>
    <td>
    </td>
  </tr>
  <tr>
    <td>Mar&nbsp;7<br/><a href="WI22_cse291-17-WeirderRFStuff.pptx">[slides]</a><a href="WI22_cse291-17-WeirderRFStuff.pdf">[pdf]</a></td>
    <td>Boutique RF: Backscatter, Wakeup Radios</td>
    <td>
    Additional Resources:
    <small>
    <ul>
      <li>Buettner, Michael et al. <a href="https://dl.acm.org/doi/abs/10.1145/1460412.1460468"><i>RFID Sensor Networks with the Intel WISP.</i></a> SenSys 2008.</li>
      <li>Zhang, Hong et al. <a href="https://web.cs.umass.edu/publication/details.php?id=2114"><i>Moo: A Batteryless Computational RFID and Sensing Platform.</i></a> UMass Tech Report, 2011.</li>
      <li>Van Huynh, Nguyen et al. <a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8368232"><i>Ambient Backscatter Communications: A Contemporary Survey.</i></a> IEEE Communications Surveys &amp; Tutorials 2018.</li>
      <li>Liu, Vincent et al. <a href="https://dl.acm.org/doi/abs/10.1145/2534169.2486015"><i>Ambient Backscatter: Wireless Communication out of Thin Air.</i></a> SIGCOMM 2013.</li>
      <li>Iyer, Vikram et al. <a href="https://dl.acm.org/doi/abs/10.1145/2934872.2934894"><i>Inter-Technology Backscatter: Towards Internet Connectivity for Implanted Devices.</i></a> SIGCOMM 2016.</li>
      <li>Pannuto, Pat et al. <a href="https://ieeexplore.ieee.org/abstract/document/8480075"><i>Slocalization: Sub-µW Ultra Wideband Backscatter Localization.</i></a> IPSN 2018.</li>
    </small>
    </td>
  </tr>
  <tr>
    <td>Mar&nbsp;9</td>
    <td>VLC, IR, Ultrasonic</td>
  </tr>
  <tr class="table-warning">
    <td>Mar&nbsp;11</td>
    <td colspan="2"><i>No lab, finish your class projects!</i></td>
  </tr>
  <tr class="table-success">
    <td colspan="4">Finals Week</td>
  </tr>
  <tr>
    <td>
    <p>Mar&nbsp;14</p>
    <p><em>3&ndash;6&nbsp;PM</em></p>
    </td>
    <td>Final Presentations</td>
    <td>
    <p>See presentation details below.</p>
    </td>
  </tr>

</table>
</details>


---


<div class="row flex-nowrap">
<div class="col-lg-2">
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />
</div>
<div class="col-lg-10">
<p>
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>. Copyright <a href="https://patpannuto.com/">Pat Pannuto</a>, 2022.
</p>
</div>
</div>
