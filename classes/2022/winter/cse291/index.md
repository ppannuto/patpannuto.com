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
    <th>Assignment / Additional Materials</th>
  </tr>

  <tr class="table-info">
    <td colspan="4">Week 1: Introduction, Motivation, and Background</td>
  </tr>
  <tr>
    <td>Jan&nbsp;3<br/><a href="WI22_cse291-01-intro.pptx">[slides]</a><a href="WI22_cse291-01-intro.pdf">[pdf]</a></td>
    <td>
    <ul>
      <li>What's IoT?</li>
      <li>What's &ldquo;low-power&rdquo;?</li>
    </ul>
    </td>
    <td></td>
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
and _make_ something (wireless or wireless-adjacent, please).

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
