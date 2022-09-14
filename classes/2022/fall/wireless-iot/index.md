<div style="text-align:center">

<h1>Wireless and Communication in the Internet of Things</h1>

<h2 style="font-family:monospace">
Home |
<a href="syllabus.html">Syllabus</a> |
<a href="agenda.html">Agenda</a> |
<a href="labs.html">Labs</a> |
</h2>

</div>

---

<p>
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
</p>

<div style="text-align:center" markdown="1">
## CSE190(C00) / CSE291(C00) - Fall 2022
</div>

This course is a "mezzanine" class, i.e. it is open to both undergraduate and
graduate students, but you must register for 190 or 291 as-appropriate.

Meets M/W/F from 13:00 to 13:50.
Lectures are in 2154&nbsp;CSE.
Labs are in 3219&nbsp;CSE.

[Pat Pannuto](https://patpannuto.com) is the instructor, and their office is CSE 3202 (right in the corner).
[Office hours](syllabus.html#getting-help) are Wednesdays, 15:00-15:50.

[Nishant Bhaskar](https://cseweb.ucsd.edu/~nibhaska/) is the TA.
Office hours, location TBA.

&rarr; [Click here for the UCSD Embedded Seminar](https://sites.google.com/eng.ucsd.edu/embeddedlunch/) (Thr 12:30-1:30) &ndash; All are welcome!

---

<h2>Overview</h2>

Internet of Things (IoT) devices are often battery-powered, or sometimes even
energy-harvesting and battery-free. For most applications, 80% or more of
power goes to communication, i.e. sending data between the IoT device and the
internet at large. These two realities mean that many IoT devices use custom
communication technologies, or common ones in different ways (e.g. why does my
old Fitbit scale make my home WiFi go literally 100x slower when it's on?).

This class will focus on how an IoT system designer should choose and use the
wide array of wireless technologies. Specifically, we will look at WiFi,
Classic Bluetooth, Bluetooth Low Energy, IEEE 802.15.4, 2g/3g/4g/5g cellular,
LTE-M, NB-IoT, LoRa, SigFox, and some time with more esoteric choices, such
as Visible Light Communication (VLC), Infrared Communication (IR), Ultrasonic,
and boutique RF such as wake-up radios and backscatter. Persons finishing this
course should be well-suited for work in real-world IoT systems upon
completion.


<h3>Target Audience</h3>

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

<div class="prep" markdown="1">
<tt markdown="1">

> https://www.celt.iastate.edu/instructional-strategies/effective-teaching-practices/revised-blooms-taxonomy/
>
> |               |  K1: | Factual     |  K2: | Conceptual     | K3: | Procedural     | K4: | Metacognitive
> |---------------|------|-------------|------|----------------|-----|----------------|-----|--------------
> |B1: Remember   |      | List        |      | Recognize      |     | Recall         |     | Identify
> |B2: Understand |      | Summarize   |      | Classify       |     | Clarify        |     | Predict
> |B3: Apply      |      | Respond     |      | Provide        |     | Carry Out      |     | Use
> |B4: Analyze    |      | Select      |      | Differentiate  |     | Integrate      |     | Deconstruct
> |B5: Evaluate   |      | Check       |      | Determine      |     | Judge          |     | Reflect
> |B6: Create     |      | Generate    |      | Assemble       |     | Design         |     | Create

</tt>
</div>

1. <span class="prep" markdown="1">**B4: K2,K4**</span> Analyze a new wireless technology or protocol to extract key technical features and limitations.
    - Specifically: infrastructure requirements, energy use, processing and timing demands, latency, throughput, goodput, and how network scale and density affects each of these factors.
1. <span class="prep" markdown="1">**B4-5: K1,K2**</span> Assess how physical-world constraints of an application scenario map to the capabilities of communication technologies.
    - Specifically: deployment area, device density, energy availability, spectrum access, and form factor.
1. <span class="prep" markdown="1">**B2: K1**</span> Explain the basic operating principles and performance most-used technologies in mobile computing:
    - Bluetooth Low Energy
    - 802.15.4 and Thread
    - WiFi
    - LoRa
    - Basic Cellular Data
1. <span class="prep" markdown="1">**B2-3: K1**</span> Explain what "{B,P,L,W}AN", "star", "mesh", and "cell" mean in wireless networking, and how topology influences system design and performance.
1. <span class="prep" markdown="1">**B3? 'unseen'?: K3**</span> Demonstrate basic self-sufficiency in the compilation, loading, and testing of previously-unseen software on previously-unseen hardware platforms.
1. <span class="prep" markdown="1">**B6: K3**</span> Design a system architecture and estimate its performance given an application scenario.

<!-- OLD
1. Make or support communication technology design decisions with respect to application requirements, device capabilities, and infrastructure requirements.
1. Explain what "{B,P,L,W}AN", "star", "mesh", and "cell" mean in wireless networking, and how topology influences system design and performance.
1. Estimate performance—in throughput, latency, energy use, and reliability—given technical information on a wireless technology.
1. Demonstrate basic self-sufficiency in the compilation, loading, and testing of previously-unseen software on previously-unseen hardware platforms.
    - TODO: Course design Q: How to satisfy this goal with group labs? Maybe pre-lab / homework can help here?


1. Understand tradeoffs in wireless protocol design and how those tradeoffs influence suitability for application goals.
1. Extract and distill application requirements and deployment constraints that inform the design and selection of wireless communication.
-->

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
