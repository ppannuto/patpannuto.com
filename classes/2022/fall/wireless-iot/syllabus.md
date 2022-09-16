<div style="text-align:center">

<h1>Wireless and Communication in the Internet of Things</h1>

<h2 style="font-family:monospace">
<a href="index.html">Home</a> |
Syllabus |
<a href="agenda.html">Agenda</a> |
<a href="labs.html">Labs</a>
</h2>

</div>

---

<h1>Syllabus</h1>

[TOC]

---

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
In lieu of a final exam, this course will feature a final design assignment.


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
and debuggers.

`CSE 123: Computer Networks` is not a prerequisite of this course. However, if
you are able to take 123 in advance of this course or concurrently, it is
helpful.


### Textbook & Other Resources

There is no textbook for this course.

For background and more depth in embedded system design and operation, we recommend
[Lee & Seshia's Introduction to Embedded Systems](https://ptolemy.berkeley.edu/books/leeseshia/).

For debugging and lab support,
[stack overflow](https://stackoverflow.com/),
[electronics stack exchange](https://electronics.stackexchange.com/),
and vendor forums (e.g. [Nordic DevZone](https://devzone.nordicsemi.com/)) are good resources.

For specific topics, additional resources are linked in the course slides.


### Schedule

This course meets Mon/Wed/Fri from 13:00 to 13:50 US/Pacific.

There is a mixture of lecture and lab sessions.
At first, the general pattern will be lecture on Mondays and Wednesday with a lab section on Friday.
However, this will vary later in the term, so please plan to pay attention to the course schedule.

Lectures are in 2154 CSE.  Labs are in 3219 CSE.
[CSE Building Map](https://cse.ucsd.edu/about/floormaps).


#### (A?)Sychronous?, Remote?, Recordings?

This course is designed for synchronous, in-person instruction.
That said, life happens, so we will make _best-effort_ attempts to stream the
lectures via Zoom and will make these recordings available in Canvas.

<!--
#### Office Hours

Up-to-date office hours are available in Canvas.
-->


### Grading

A quick reminder: Effective learning comes from **active engagement** and **re-enforcement**.
Activities, assignments, and grading are designed to help with this.

_You get out of class what you put into it._

#### 10%: Minute-Quizzes

Lecture will begin with a "minute-quiz."
These will be (very) short and will cover material from the prior lecture, or possibly pre-lab, lab, post-lab, homework or other assignment.
You should not need to study or worry about these – if you were there and paying attention, you'll be prepared.

Correct quizzes earn 1%/ea, incorrect quizzes earn 0.5%/ea, and missing quizzes are 0%.
Excluding the first day of class, and considering holidays, there are 19 lectures.
Anything earned over 10% counts as half.

This creates a natural, built-in makeup policy that allows you to miss _many_ quizzes/questions without penalty.
For this reason, there is no makeup opportunity for missed quizzes.

Depending on the needs of the day, some lectures may skip the minute quiz.
There will be a minimum of 12 minute quizzes during the quarter.

Quizzes are released at 13:00 and collected at 13:02. No late quizzes are accepted.


#### 45%: Labs
Lab activities make up the bulk of the work for this course.
Labs are where you will apply the concepts learned in lecture.

There are five total labs in this course.
The first lab is one session in week 1, while the remaining labs all have two in-class lab days.

<tt markdown="1" style="font-size: smaller;">

 - (&nbsp;5%): Lab 1 – Wireshark
 - (10%): Lab 2 – Bluetooth
 - (10%): Lab 3 – 802.15.4
 - (10%): Lab 4 – WiFi
 - (10%): Lab 5 – LoRa

</tt>

##### Pre-Labs
Pre-labs are absolutely essential to your success during the lab session.
You *must* have completed your pre-lab *before* the start of the lab session to make good use of the lab time.

For this reason, your pre-labs are due by the start of lab.
There are no exceptions, and there is no late/makeup policy for pre-labs.
If you have not completed the pre-lab by the start of the lab session you will receive no credit for that pre-lab
(even though you will probably have to do the pre-lab work, during lab..., before you can actually start on the lab).


##### Post-Lab Reports
You will need to complete a post-lab report for each of the labs.

The report is a mixture of documentation of your in-lab activity as well as
post-lab analysis questions or extra experimentation you may have to perform.

Lab reports are generally due at **20:00 US/Pacific (8 PM)** one week after the
final in-class session for that lab.

Late reports will lose 10% every 24 hours. After 10 days, a missing report
will automatically recieve a zero.

#### 15%: Homework
There are only two homework assignments in this course, one at the beginning
of the term (before the first lab) and one at the end of the term (after the
last lab).

Generally, lab reports include homework-like questions and activites. These
homeworks cover topics that do not have associated labs.

<tt markdown="1" style="font-size: smaller;">

 - (&nbsp;5%): HW1 – Background & Refresher
 - (10%): HW2 – Cell

</tt>

Late homeworks will lose 10% every 24 hours. After 10 days, a missing homework
will automatically recieve a zero.


#### 30% Final Exam (Design Assignment)

<!-- FI 	12/05/2022 	M 	11:30a-2:29p 	TBA 	TBA 	-->

Take-home 'final', this is an end-to-end pencil-and-paper design task.

Loosely, this will be an exercise of:
"You're an engineer at startup X, who's building Y, with requirements
1,2,3,4. What do you design and **why**."


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


<!--
Hide this for now; really needs to break it out per-assignment

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
<td><input type="number" value="12" /></td>
<td>10</td>
<td></td>
<td rowspan="2" id="final-grade-percent"></td>
</tr>
<tr class="final-grade-row">
<th>Homework</th>
<td><input type="number" value="15" /></td>
<td>15</td>
<td></td>
</tr>
<tr class="final-grade-row">
<th>Labs</th>
<td><input type="number" value="50" /></td>
<td>45</td>
<td></td>
<td rowspan="2" id="final-grade-letter"></td>
</tr>
<tr class="final-grade-row">
<th>Final Project</th>
<td><input type="number" value="35" /></td>
<td>30</td>
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

-->


##### CAPEs Incentive

If, at the end of the term, the
[CAPE response rate](https://cape.ucsd.edu/responses/current.aspx)
is >=90.0%, we will add 1% to everyone's final grade.

If, at the end of the term, the
TA evaluation response rate
is >=90.0%, we will add (an additional) 1% to everyone's final grade.



<!-- Hide until decide

### Academic Integrity

**TODO: Think about what the goal is to say here; group-heavy work...**


### Outside Tutoring
Individuals are not permitted to approach students to offer services of any kind in exchange for pay, including tutoring services.
This is considered solicitation for business and is strictly prohibited by University policy.

-->

---

## Resources for Students

### Getting Help

First, try to make sure you help yourself by staying up to date with course activites.
Overal half the grade is participation and labs, which are not meant to be tricky, but rather to give you real-world experience, practice, and confidence with the material.

<!--
**Discussion section** is an opportunity for additional explanation and guided
practice with material from each week. Professor Pannuto did not go to any
discussions in their first two years of college becuase discussions were
&ldquo;not required&rdquo; and no one ever really explained what they were or
why they were helpful. Professor Pannuto got dragged to a discussion section
for a theory and cryptography course by a friend to whom they are forever
grateful at the end of sophomore year, realized how insanely helpful
discussions were, and had significantly better grades thereafter.
-->

**Office hours** are the perfect place for one-on-one support and asking specific
questions. Office hours are most useful after you have worked on the problem for
a little while yourself (I usually say that you should struggle with a problem
for fifteen full minutes, but not more than fifteen minutes before seeking help).
You are not interrupting course staff (TAs _or_ the professors) when you come to
office hours. It is _literally_ our job to be available to help you during those
times. Office hours are also not restricted to content from class. Folks have
asked about research / grad school in CS, how to get jobs in computer
architecture, what other classes to take if they like (or hate!) this stuff,
the best coffee shops for working accessible by light rail, tips for developing
fruit-bearing trees in San Diego, or anything else that you would like to know
about.

**The IDEA Engineering Student Center**, located just off the lobby of Jacobs
Hall, is a hub for student engagement, academic enrichment,
personal/professional development, leadership, community involvement, and a
respectful learning environment for all.  The Center offers a variety of
programs, listed in the
[IDEA Center Facebook page](https://www.facebook.com/ucsdidea/)
and
[the Center web site](https://jacobsschool.ucsd.edu/idea/).
The IDEA Center programs support both undergraduate
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

