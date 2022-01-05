<div align="center" markdown="1">
[Pat Pannuto](/)
----------------
</div>

----

Wireless and Communication in the Internet of Things
====================================================

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

## CSE291 (13) - Winter 2022

Meets M/W/F from 14:00 to 14:50 in 2154 CSE.<br/>

[Pat Pannuto](https://patpannuto.com) is the instructor, and their office is CSE 3202 (right in the corner).<br/>
Office hours available by appointment (please email / chat after class).

&rarr; [Click here for the UCSD Embedded Lunch Seminar](https://sites.google.com/eng.ucsd.edu/embeddedlunch/) (Thr 12:30-1:30) &ndash; All are welcome!

---

## Overview

Internet of Things (IoT) devices are often battery-powered, or sometimes even
energy-harvesting and battery-free. For most applications, 80% or more of
power goes to communication, sending data between the IoT device and the
internet at large. These two realities mean that many IoT devices use custom
communication technologies, or common ones in different ways (e.g. why does my
Fitbit scale make my home WiFi go literally 100x slower when it's on?).

This class will focus on how an IoT system designer should choose and use the
wide array of wireless technologies. Specifically, we will look at WiFi,
Classic Bluetooth, Bluetooth Low Energy, IEEE 802.15.4, 2g/3g/4g cellular,
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

---

## Syllabus

This class aims to be reasonably self-contained.
The primary responsibilities are to come to lectures ready to engage in the
material and to come to the lab days (Fridays) ready to hack.
We will also have a few small homework assignments throughout the quarter.
These are intended to be more fun and educational about the extant
infrastructure in the world around you than a terrible amount of work.
We'll end things with a modest project / report, at your choosing.



### Schedule

<!--
Winter Quarter begins           Monday, January 3
Instruction begins	        Monday, January 3
Martin Luther King, Jr. Holiday Monday, January 17
Presidents' Day Holiday         Monday, February 21
Instruction ends	        Friday, March 11
Final Exams                     Saturday – Saturday, March 12–19
Winter Quarter ends             Saturday, March 19
-->

<table class="table table-bordered table-hover">
  <tr class="table-primary">
    <th>Date</th>
    <th>Topic</th>
    <th>Assignment?</th>
  </tr>

  <tr class="table-info">
    <td colspan="4">Week 1: Introduction, Motivation, and Background</td>
  </tr>
  <tr>
    <td>Jan&nbsp;3<br/><a href="WI22_cse291-01-intro.pptx">[slides]</a></td>
    <td>
    <ul>
      <li>What's IoT?</li>
      <li>What's &ldquo;low-power&rdquo;?</li>
    </ul>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>Jan&nbsp;5</td>
    <td>
    <ul>
      <li>Fundamentals of Networking</li>
      <li>(Aka CSE123 in an hour flat :D)</li>
    </ul>
    </td>
    <td></td>
  </tr>
  <tr>
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
    </ul>
    </td>
  </tr>

  <!-- OKAY. Fuck Covid, delete it all, and we will reimagine labs in realtime I guess. -->

<!--
  NEW. PLAN.

	M/W					F
1	Networking Fundamentals; topolgies	wireshark something
2	2g/3g/4g				Pick a country, cell phone plan
3	LoRa, SigFox, etc			Helium chat
4	LTE-M / NB-IoT				[HW?]
5	BLE					adv to phone
6	15.4 [trad]				class mesh
7	15.4 [concurr]				demo any concurr [too hard?]
8	VLC, IR, Ultrasonic			find / record IR in real world
9	Boutique RF [wakeup radio?]		[Maybe just project time?]
10	TBA					[None: Project]
-->

  <!--
  <tr class="table-info">
    <td colspan="4">Finals Week</td>
  </tr>
  <tr>
    <td>
    <p>Jun&nbsp;7</p>
    <p><em>3&ndash;6 PM</em></p>
    </td>
    <td>Final Presentations</td>
    <td>Pannuto</td>
    <td>
    <p>Submit final papers via HotCRP.</p>
    <p>See presentation details below.</p>
    </td>
  </tr>
  -->

</table>


### Class Project / Report

The intent of the project / report is to offer an open-ended opportunity to dig
deeper into a wireless technology of your choosing.
The format is deliberately under-specified here.
You are welcome to implement something interesting, write a short paper, make a
presentation, create a BLE-inspired interpretive dance, make an oil painting of
your local spectrum utilization (seriously)—be creative!
Read some about [Maker Culture](https://en.wikipedia.org/wiki/Maker_culture)
and _make_ something (wireless, please).

At this stage, you all have been doing this school thing for a while, and I trust
you to create something appropriate for a small-to-medium end-of-term project.
Group projects are acceptable, however, please do scale the project appropriately
with the size of the group (bigger group, bigger project).
You are welcome to discuss proposals with me if you wish.

<!-- https://twitter.com/hakeemjefferson/status/1332771319209881600 -->


### Final Exam / Presentations

Instead of a final exam, we will have a "mini-conference" where each project
will present their work.

<!--          03/14/2022 	M 	3:00p-5:59p                 -->

#### Presentation Details

Logistics of this is lightly TBA until we have an understanding of how many
groups will be presenting, and which modalities will be required.

We'll use the final exam slot–Monday, March 14 from 3-6pm–for the "conference."


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
