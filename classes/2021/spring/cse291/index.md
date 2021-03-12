Topics in Embedded Systems & The Internet of Things
===================================================

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
## CSE291 A00 - Spring 2021

Meets Tu/Thr from 15:30 to 16:50 in WARR WEST (tent on the Warren mall!).<br/>
[Pat Pannuto](https://patpannuto.com) is the instructor, and their office is CSE 3202 (right in the corner).<br/>
[Nishant Bhaskar](http://cseweb.ucsd.edu/~nibhaska/) is the TA for the course.

Office hours are TBA.<br/>
Times always available by appointment, generally afternoons are preferred.

Quick Links:
[Paper Reviews](#paper-reviews) |
[Participation](#participation) |
[Class Project](#class-project) |
[Schedule](#schedule) |
[Final Exam / Presentations](#final-exam--presentations)

---

## Overview

Researchers, policy makers, citizen scientists, and curious individuals have
an innumerable array of questions about the world around them.  How does
physical proximity affect disease transmission?  What changes would have the
greatest impact on the carbon footprint of an urban environment?  What is the
historical air quality like for asthmatics in the neighborhoods where I am
shopping for houses? This course is about the design and implementation of
platforms and systems capable of capturing the data to answer such questions.

Formally, this is the study of embedded systems and wireless sensor networks.
These are computing systems that are deployed widely in the physical world,
which creates unique constraints in their physical size, deployment,
management, communication, energy availability, and operation. We will begin
with a history of impactful deployments, then study each of the pieces in
turn, both traditional sensor architectures and more exotic designs such as
energy harvesting systems, synchronous wirelss communication, and how to do
machine learning with less than 1 MB of memory.

### Target Audience

The intended audience of this course is PhD students or masters students who
are interested in pursuing a PhD in the future.
This is a research-oriented class. It's designed to bring people up to speed on
the history as well as the state of the art in mobile computing and to gain
experience with the design, early implementation, and evaluation of a research
idea.



<!--
### Prerequisites

Experience equivalent of an undergraduate degree in any of Electrical
Engineering, Computer Engineering, Computer Science, Data Science, Information
Science, or related areas.  This is a vertical slice through the computing
stack, and we will touch on topics from programming languages and distributed
systems down to circuits and wireless. An enthusiasm and willingness to learn a
little about a lot of new things is far more important than any one specific
background.

The goal is to have a fairly diverse course with folks from different and
complimentary backgrounds. We'll cover topics in each of these areas, but you
are **not** expected to be familiar with all of them.

If you are comfortable with **just one** of these, and are interested in
learning a little about the rest, welcome!

 - Operating Systems
 - Programming Languages (especially systems-oriented ones)
 - Networking
 - Wireless Communication
 - Architecture
-->


## Syllabus

This class is made of three co-equal components: pre-class reviews, in-class
participation, and a quarter-long project.

### Paper Reviews

Before each class you must read each paper and then write a short review.
This should be more than a simple summary of the paper. Here are some questions
to consider while reading and writing your reviews to help guide you:

 - What is the problem this paper addresses, and why is it important?
 - What is the hypothesis of this paper?
 - How was this hypothesis evaluated? What supported it, what refuted it?
 - What are the limits of this system (when does it fail)?
 - What is this most similar to that you are already familiar with; how does it compare, differ?
 - At what point did you decide you liked &ndash; or didn't like &ndash; the paper, **why?**


#### Submitting Reviews

We will use the [HotCRP review system](https://ucsd-cse291-a00-s20.hotcrp.com)
&ndash; the same tool used by many conferences to review papers.

Reviews are due the day before class.
HotCRP will automatically cut off submissions at 12:01am on the morning of class.
We will create accounts for all enrolled students during the first week of classes.
If you need an account or have other issues, please
<a href="mailto:ppannuto@ucsd.edu?subject=CSE291-K00-W20%20HotCRP%20Issue">e-mail me</a>.

### Participation

We will rotate through class members to lead discussion each session. Leads
should be prepared to give an overview of the paper's key ideas and to guide a
discussion about the strengths and weaknesses of the paper, how it relates to
prior and/or subsequent work, and what the core takeaway(s) of the paper may
be.

When not the lead, everyone else is expected to have read the papers and to
actively participate in the class discussions.

### Class Project

This class will feature a quarter long project of your own choosing. Project
scope should be commensurate with group size &ndash; an individual project is
acceptable, though advised against. A core goal of the project is to
demonstrate mastery of the scientific method: namely to clearly articulate a
hypothesis and to design and implement experiments that (in)validate the
hypothesis (note: a project with a negative result may still be a highly
successful project!). The goal of the project is to learn how to propose a
research idea, to then collect preliminary data to probe the viability of that
idea, and finally to practice communicating this process in writing.

The project will have three milestones:

<dl>
  <dt>Week 3</dt>
  <dd>Monday, April 12: One to two page proposal writeup that includes your hypothesis, motivation, and at least one experiment you intend to run.</dd>
  <dt>Week 6</dt>
  <dd>Monday, May 3: Three to four page draft that includes a literature review ("Related Work"), proposed experiments, and their expected outcomes.</dd>
  <dt>Week 10</dt>
  <dd>Tuesday, June 1: Final five to six page paper that includes outcome of small-scale experiments / prototype / etc. This should resemble an early-to-mature draft of an academic workshop paper.</dd>
</dl>



<!--
    What is the problem this paper addresses, and why is it important?
    What is the hypothesis of this paper?
    What are two key assumptions that this paper makes?
    What are the two main strengths of this paper?
    What are the two main weaknesses of this paper?
    Which figure or experiment was most compelling in support of the hypothesis, and why?

    What is the problem the paper addresses?
    Why is the problem important?
    What is the proposed solution?
    What were the challenges that the authors faced?
    How did the authors evaluate their solution?
    What falls outside the scope of this paper?
-->




### Schedule

<table class="table table-bordered table-hover">
  <tr class="table-primary">
    <th>Date</th>
    <th>Topic</th>
    <th>Lead</th>
    <th>Pre-Class Assignment</th>
  </tr>

  <tr class="table-info">
    <td colspan="4">Week 1: Introduction, Motivation, Potential, and Pitfalls</td>
  </tr>
  <tr>
    <td>Mar&nbsp;30</td>
    <td><a href="2021-03-06-cse291-intro.pptx">Introduction</a></td>
    <td>Pannuto</td>
    <td></td>
  </tr>
  <tr>
    <td>Apr&nbsp;1</td>
    <td><a href="#">Ubiquitous Computing</a></td>
    <td>Pannuto</td>
    <td>
      No paper reviews this week, just read and think about these:
      <ul>
        <li><a href="/papers/weiser1991Computer21stCentury.pdf">The Computer for the 21st Century</a></li>
        <li><a href="/papers/weiser1993ubiquitous.pdf">Some Computer Science Issues in Ubiquitous Computing</a></li>
        <li><a href="/papers/pister1999NextCentury.pdf">Next Century Challenges: Mobile Networking for &ldquo;Smart Dust&rdquo;</a></li>
      </ul>
    </td>
  </tr>

  <tr class="table-info">
    <td colspan="4">Week 2: Great Deployments Past</td>
  </tr>
  <tr class="table-warning">
    <td>Apr 5</td>
    <td colspan="2">Project Group Formation Deadline</td>
    <td>Work with Nishant to register your project group.</td>
  </tr>
  <tr>
    <td>Apr&nbsp;6</td>
    <td>
    <a href="#">Early Lessons</a>
    <hr />
    Pre-reading questions:
    <ul>
      <li>What kinds of things are &ldquo;obvious today,&rdquo; but were new then?</li>
      <li>Why do we (as researchers) bother doing deployments? (They're expensive, hard, require many-person hours...)</li>
    </ul>
    </td>
    <td>Pannuto</td>
    <td>
      <a href="https://github.com/ppannuto/patpannuto.com/blob/master/classes/2021/spring/cse291/index.md">Sign up for to lead discussion by submitting a pull request.</a> <small>Conflicts resolved by timestamp (first come, first serve).</small>
      <hr />
      Read and review:
      <ul>
        <li><a href="/papers/juang2002zebranet.pdf">Energy-Efficient Computing for Wildlife Tracking: Design Tradeoffs and Early Experiences with ZebraNet</a></li>
        <li><a href="/papers/mottola2010tunnels.pdf">Not all Wireless Sensor Networks are Created Equal: A Comparative Study on Tunnels</a></li>
      </ul>
      <hr />
      For those wanting more...
      <ul>
        <li><a href="/papers/szewczyk2004greatduckisland.pdf">An Analysis of a Large Scale Habitat Monitoring Application (The Great Duck Island paper)</a></li>
        <li><a href="/papers/balaji2013sentinel.pdf">Sentinel: Occupancy Based HVAC Actuation using Existing WiFi Infrastructure within Commercial Buildings</a></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>Apr&nbsp;8</td>
    <td>
    <a href="#"><strong>Scale</strong></a>
    <hr />
    Pre-reading questions:
    <ul>
      <li>Where do you place the line between what work &ldquo;belongs to&rdquo; research and industry?</li>
      <li>Why do we (as researchers) bother doing big deployments? (They're even more expensive, hard, require many-person hours...)</li>
    </ul>
    </td>
    <td>Pannuto</td>
    <td>
      Read and review:
      <ul>
        <li>TBD: One of the GreenOrbs papers</li>
        <li><a href="/papers/balaji2016brick.pdf">Brick: Towards a Unified Metadata Schema For Buildings</a></li>
      </ul>
      <hr />
      For those wanting more...
      <ul>
        <li><a href="/papers/catlett2017aot.pdf">Array of Things: A Scientific Research Instrument in the Public Way</a></li>
        <li><a href="https://wp.nyu.edu/sonyc/">Sounds of New York City (SONYC)</a></li>
        <li><a href="/pubs/klugman19scale.pdf">Hardware, Apps, and Surveys at Scale: Insights from Measuring Grid Reliability in Accra, Ghana</a></li>
        <li><a href="/pubs/adkins18signpost.pdf">The Signpost Platform for City-Scale Sensing</a></li>
      </ul>
    </td>
    <!--
    ### Human Sensing
     - WRENSys? Opo? iBadge?
    -->
  </tr>

  <tr class="table-info">
    <td colspan="4">Week 3: Everything is an Energy Problem</td>
  </tr>
  <tr class="table-warning">
    <td>Apr 12</td>
    <td>Project Milestone 1 Deadline</td>
    <td colspan="2">One page proposal writeup that includes your hypothesis, motivation, and at least one experiment you intend to run.</td>
  </tr>
  <tr>
    <td>Apr&nbsp;13</td>
    <td>
    <a href="#">Early Insights in Low Power Systems</a>
    <hr />
    Pre-reading questions:
    <ul>
      <li>What's duty cycling? Why didn't we always do this?</li>
      <li>Why is there a gap between the power performance hardware is capable of and what it actually achieves?</li>
    </ul>
    </td>
    <td><i>Your Name Here!</i></td>
    <td>
    <i>Presenter: Choose two for folks to read</i>
    <ul>
      <li><a href="http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.162.943&rep=rep1&type=pdf">Versatile Low Power Media Accessfor Wireless Sensor Networks (B-MAC)</a></li>
      <li><a href="/papers/cao2008virtualbattery.pdf">Virtual Battery: An Energy Reserve Abstraction for Embedded Sensor Networks</a></li>
      <li>...</li>
      <li>...</li>
    </ul>
    <!--
    Read and review:
    <ul>
    </ul>
    <hr />
    For those wanting more...
    <ul>
    </ul>
    -->
    </td>
  </tr>
  <tr>
    <td>Apr&nbsp;15</td>
    <td>
    <a href="#">Energy Harvesting</a>
    <hr />
    Pre-reading questions:
    <ul>
      <li>What's the relation between power source and reliability? How do other system components affect this?</li>
      <li>Is this actually new? What energy harvesting, embedded systems are common, established, and well-older than Pat? What's different now?</li>
      <li>What's the definition of intermittent computing?</li>
    </ul>
    </td>
    <td><i>Your Name Here!</i></td>
    <td>
    <i>Presenter: Choose two for folks to read</i>
    <ul>
      <li><a href="/papers/hester2015ufop.pdf">Tragedy of the Coulombs: Federating Energy Storage for Tiny, Intermittently-Powered Sensors</a></li>
      <li><a href="/papers/colin2018capybara.pdf">A Reconfigurable Energy Storage Architecture for Energy-harvesting Devices</a></li>
      <li><a href="/papers/jackson19capacity.pdf">Capacity over Capacitance for Reliable Energy Harvesting Sensors</a></li>
      <li>Geoff's intermittent definition paper?</li>
    </ul>
    <!--
    Read and review:
    <ul>
    </ul>
    <hr />
    For those wanting more...
    <ul>
    </ul>
    -->
    </td>
  </tr>
  <tr class="table-warning">
    <td>Apr 16</td>
    <td>Project Milestone 1 Feedback Deadline</td>
    <td colspan="2">This is a course staff commitment &ndash; we will have feedback on each project proposal back to you by end of day.</td>
  </tr>


  <tr class="table-info">
    <td colspan="4">Week 4: Communication (Part I)</td>
  </tr>
  <tr>
    <td>Apr&nbsp;20</td>
    <td>Project Workshop Day</td>
    <td>Pannuto</td>
    <td>
      Bring printed copies of revised project proposal drafts to class.
    </td>
  </tr>
  <tr>
    <td>Apr&nbsp;22</td>
    <td>
    <a href="#">Great Ideas in Traditional Communication</a>
    <hr />
    Pre-reading questions:
    <ul>
      <li>What is a MAC protocol, and why has there been <i>so</i> much academic research on them?</li>
      <li>What is different (or not!) about WSN nodes versus phones, laptops, etc? What impact does that have on their communication mechanisms?</li>
    </ul>
    </td>
    <td><i>Your Name Here!</i></td>
    <td>
      <i>Presenter: Choose two for folks to read</i>
      <ul>
        <li><a href="/papers/hui2008ipdead.pdf">IP is Dead, Long Live IP for Wireless Sensor Networks</a></li>
        <li><a href="http://coronet2010.stanford.edu/pubs/sing-08-00.pdf">BoX-MAC (Tech report 2008, sender-initiated MAC)</a></li>
        <li><a href="http://soda.swedish-ict.se/5128/1/contikimac-report.pdf">ContikiMAC (Tech report 2011, sender-initiated MAC)</a></li>
        <li><a href="http://dl.acm.org/citation.cfm?id=1460414">RI-MAC (SenSys 2008, receiver-initiated MAC)</a></li>
      </ul>
      <!--
      Read and review:
      <ul>
      </ul>
      <hr />
      For those wanting more...
      <ul>
      </ul>
      -->
    </td>
  </tr>



  <tr class="table-info">
    <td colspan="4">Week 5: Communication (Part 2)</td>
  </tr>
    <td>Apr&nbsp;27</td>
    <td>
      Synchronous communication protocols
      <hr />
      Pre-reading questions:
      <ul>
        <li>What is synchronous communication?</li>
        <li>What is different (or not!) about WSN nodes versus phones, laptops, etc? What impact does that have on their communication mechanisms?</li>
      </ul>
    </td>
    <td><i>Your Name Here!</i></td>
    <td>
      <i>Presenter: Choose two for folks to read</i>
      <ul>
        <li><a href="http://dl.acm.org/citation.cfm?id=1869985">A-MAC (SenSys 2010, receiver-initiated MAC)</a> (more in <a href="http://dl.acm.org/citation.cfm?id=2240119">TOSN 2012 extended version</a>)</li>
        <li><a href="/papers/ferrari2011glossy.pdf">Efficient Network Flooding and Time Synchronization with Glossy</a></li>
        <li><a href="/papers/ferrari2012lwb.pdf">Low-Power Wireless Bus</a></li>
        <li><a href="/papers/iyer2016interscatter.pdf">Inter-Technology Backscatter: Towards Internet Connectivity for Implanted Devices</a></li>
        <li><a href="/papers/varshney2019tunnelscatter.pdf">TunnelScatter: Low Power Communication for SensorTags using Tunnel Diodes</a></li>
      </ul>
      <!--
      Read and review:
      <ul>
      </ul>
      <hr />
      For those wanting more...
      <ul>
      </ul>
      -->
    </td>
  <tr>
    <td>Apr&nbsp;29</td>
    <td>Spectrum</td>
    <td><i>Your Name Here!</i></td>
    <td>
      <i>Presenter: Choose two for folks to read</i>
      <ul>
        <li><a href="/papers/saifullah2016snow.pdf">SNOW: Sensor Network over White Spaces</a></li>
        <li><a href="https://lab11.eecs.umich.edu/content/pubs/ghena19lpwans.pdf">Challenge: Unlicensed LPWANs Are Not Yet the Path to Ubiquitous Connectivity</a></li>
        <li><a href="http://cseweb.ucsd.edu/~schulman/docs/mobisys19-sparsdr.pdf">SparSDR: Sparsity-proportional Backhaul and Compute for SDRs</a></li>
      </ul>
      <!--
      Read and review:
      <ul>
      </ul>
      <hr />
      For those wanting more...
      <ul>
      </ul>
      -->
    </td>
  </tr>

  <tr class="table-info">
    <td colspan="4">Week 6: Platforms</td>
  </tr>
  <tr class="table-warning">
    <td>May 3</td>
    <td>Project Milestone 2 Deadline</td>
    <td colspan="2">Three to four page draft that includes a literature review ("Related Work"), proposed experiments, and their expected outcomes.</td>
  </tr>
  <tr>
    <td>May&nbsp;4</td>
    <td>
      Hardware Platform Design
      <hr />
      Pre-reading questions:
      <ul>
        <li>...</li>
      </ul>
    </td>
    <td><i>Your Name Here!</i></td>
    <td>
      <i>Presenter: Choose two for folks to read</i>
      <ul>
        <li><a href="/papers/dutta2008epic.pdf">A Building Block Approach to Sensornet Systems</a><!--Building block approach for prototype, pilot, and product--></li>
        <li><a href="/papers/kim2018postsoc.pdf">System Architecture Directions for Post-SoC/32-bit Networked Sensors</a></li>
        <li><a href="/papers/campbell2014ehtoolkit.pdf">An Energy-Harvesting Sensor Architecture and Toolkit for Building Monitoring and Event Detection</a></li>
        <li><a href="http://dl.acm.org/citation.cfm?id=1147744">Telos: enabling ultra-low power wireless research</a><!--Integrated approach (everything-on-board)--></li>
        <li><a href="http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7460722">System Design for a Synergistic, Low Power Mote/BLE Embedded Platform (Firestorm)</a><!--High performance and extensible--></li>
      </ul>
      <!--
      Read and review:
      <ul>
      </ul>
      <hr />
      For those wanting more...
      <ul>
      </ul>
      -->
    </td>
  </tr>
  <tr>
    <td>May&nbsp;6</td>
    <td>
    <a href="#">Software Platform Design (aka Embedded OSes)</a>
    <hr />
    Pre-reading questions:
    <ul>
      <li>What are the requirements of multi-processing?</li>
      <li>Why have prior embedded systems been single-task, what is changing?</li>
    </ul>
    </td>
    <td><i>Your Name Here!</i></td>
    <td>
      <i>Presenter: Choose two for folks to read</i>
      <ul>
        <li><a href="/pubs/levy17multiprogramming.pdf">Multiprogramming a 64kB Computer Safely and Efficiently</a></li>
        <li><a href="/papers/hardin2018appiso.pdf">Application Memory Isolation on Ultra-Low-Power MCUs</a></li>
        <li><a href="https://people.eecs.berkeley.edu/~pister/290Q/Papers/levis06tinyos.pdf">TinyOS: An Operating Systemfor Sensor Networks</a></li>
        <li><a href="https://cseweb.ucsd.edu/~schulman/class/cse291_f18/docs/cooprider_tinyos.pdf">Efficient Memory Safety for TinyOS</a></li>
        <li><a href="https://sing.stanford.edu/pubs/tinyos-retrospective-osdi2012.pdf">Experiences from a Decade of TinyOS Development</a></li>
        <li><a href="http://ieeexplore.ieee.org/abstract/document/1367266/">Contiki - A lightweight and flexible operating system for tiny networked sensors</a></li>
        <li><a href="https://dl.acm.org/doi/10.1145/635506.605407">Maté: A tiny virtual machine for sensor networks</a></li>
      </ul>
      <!--
      Read and review:
      <ul>
      </ul>
      <hr />
      For those wanting more...
      <ul>
      </ul>
      -->
    </td>
  </tr>


  <tr class="table-info">
    <td colspan="4">Week 7: Actual, computer-y things</td>
  </tr>
  <tr class="table-warning">
    <td>May 10</td>
    <td>Project Milestone 2 Feedback Deadline</td>
    <td colspan="2">This is a course staff commitment &ndash; we will have feedback on each project proposal back to you by end of day.</td>
  </tr>
  <tr>
    <td>May&nbsp;11</td>
    <td>
    <a href="#">ML at the Very Edge</a>
    <hr />
    Pre-reading questions:
    <ul>
      <li>How to decide between edge, local compute?</li>
      <li>What is, and is not, different about edge compute capabilities?</li>
      <li>How to manage whole ML systems (training, execution, updates)?</li>
    </ul>
    </td>
    <td><i>Your Name Here!</i></td>
    <td>
      <i>Presenter: Choose two for folks to read</i>
      <ul>
        <li><a href="/papers/yao2017deepiot.pdf">DeepIoT: Compressing Deep Neural Network Structures for Sensing Systems with a Compressor-Critic Framework</a></li>
        <li><a href="/papers/radu2017wearableML.pdf">Multimodal Deep Learning for Activity and Context Recognition</a></li>
      </ul>
      <!--
      Read and review:
      <ul>
      </ul>
      <hr />
      For those wanting more...
      <ul>
      </ul>
      -->
    <!--
     Compute/Comm tradeoff bit...
     - Maybe one of Pengyu's (do any of his papers capture his oral argument about closing this gap?)
    -->
    </td>
  </tr>
  <tr>
    <td>May&nbsp;13</td>
  </tr>

  <!--
    <td>
    Distributed Computing and Task Planning
    <hr />
    Pre-reading questions:
    <ul>
      <li>What are the tradeoffs between centralized and decentralized compute models?</li>
      <li>How to express heterogeneity of compute capability? How is the heterogeneity different from prior distributed systems?</li>
    </ul>
    </td>
    <td><i>Your Name Here!</i></td>
    <td>
      <ul>
        <li><a href="/papers/noor2019ddflow.pdf">DDFlow: Visualized Declarative Programming for Heterogeneous IoT Networks</a></li>
        <!-Or maybe the new one: The Case for Robust Adaptation: Autonomic Resource Management is a Vulnerability??->
        <li><a href="/papers/brooks2018accessors.pdf">A Component Architecture for the Internet of Things</a></li>
        <!-Mate?->
      </ul>
      <hr />
      For those wanting more...
      <ul>
        <li><a href="https://ptolemy.berkeley.edu/books/Systems/PtolemyII_DigitalV1_02.pdf">System Design, Modeling, and Simulation</a> (Good summary of models of computation)</li>
      </ul>
    </td>
  -->

  <tr class="table-info">
    <td colspan="4">Week 8: <a href="https://cps-iot-week2021.isis.vanderbilt.edu/">CPS-IoT Week</a></td>
  </tr>
  <tr>
    <td>May&nbsp;18</td>
    <td>Workshop Day</td>
    <td>Custom Signup; TBD</td>
    <td>Pick a workshop to attend; come to class prepared to give highlights of interesting ideas and conversations from the workshop.</td>
  </tr>
  <tr>
    <td>May&nbsp;20</td>
    <td>Conference Day(s)</td>
    <td>Custom Signup; TBD</td>
    <td>Pick one session to attend; come to class prepared to give highlights of interesting ideas and conversations from the session.</td>
  </tr>

  <tr class="table-info">
    <td colspan="4">Week 9: Security</td>
  </tr>
  <tr>
    <td>May&nbsp;25</td>
    <td>
    <a href="#">Individual Device Security</a>
    <hr />
    Pre-reading questions:
    <ul>
      <li>How would you express the trust/threat model of physically deployed sensing systems?</li>
      <li>How do we balance pragmatism and security; in theory, in practice?</li>
      <li>How can we enforce or prove the state of the physical world?</li>
    </ul>
    </td>
    <td><i>Your Name Here!</i></td>
    <td>
      <i>Presenter: Choose two for folks to read</i>
      <ul>
        <li><a href="https://lightcommands.com/20191104-Light-Commands.pdf">Light Commands: Laser-Based Audio Injection Attacks on Voice-Controllable Systems</a></li>
        <li><a href="/papers/hunt2017sevenproperties.pdf">The Seven Properties of Highly Secure Devices (Azure Sphere)</a></li>
        <li>...</li>
      </ul>
      <!--
      Read and review:
      <ul>
      </ul>
      <hr />
      For those wanting more...
      <ul>
      </ul>
      -->
    </td>
  </tr>
  <tr>
    <td>May&nbsp;27</td>
    <td>
    <a href="#">Security for systems of devices</a>
    <hr />
    Pre-reading questions:
    <ul>
      <li>What properties do blockchains actually provide?</li>
      <li>What risks are similar, different between IoT devices and more traditional computers?</li>
    </ul>
    </td>
    <td><i>Your Name Here!</i></td>
    <td>
      <i>Presenter: Choose two for folks to read</i>
      <ul>
        <li><a href="https://www.usenix.org/system/files/conference/usenixsecurity17/sec17-antonakakis.pdf">Understanding the Mirai Botnet</a></li>
        <li><a href="/papers/anderson2019wave.pdf">WAVE: A Decentralized Authorization Framework with Transitive Delegation</a></li>
        <li><a href="/papers/helium2018.pdf">Helium: A Decentralized Wireless Network</a></li>
        <li>...</li>
      </ul>
      <!--
      Read and review:
      <ul>
      </ul>
      <hr />
      For those wanting more...
      <ul>
      </ul>
      -->
    </td>
  </tr>
  <!--
   - Ravel then vs HomeOS (the paper) / Apple Home / Google Home / etc?
   - Maybe some discussion on AllJoyn/etc?
  -->

  <tr class="table-info">
    <td colspan="4">Week 10: Special Topics</td>
    <!--
     - Steven Weber's stuff
     - Revisit Weiser vision with critical eye (write a critique?)
     - mm-wave scanners for electronics
    -->
  </tr>
  <tr>
    <td>Jun&nbsp;1</td>
    <td>Presentation on topic of class interest / or guest lecture</td>
    <td>Pannuto</td>
    <td>
    <p><i>Due by Midnight</i></p>
    <p>Submit a final draft of your project report to HotCRP.</p>
    <p>Reviews will be assigned at this time.</p>
    </td>
  </tr>
  <tr>
    <td>Jun&nbsp;3</td>
    <td>Presentation on topic of class interest / or guest lecture</td>
    <td>Pannuto</td>
    <td>
    <p><i>Due by Midnight</i></p>
    <p>Each person will be assigned to review two other project papers, similar
    to how we have reviewed papers from class. The goal is to provide
    constructive feedback to your peers for their final reports.</p>
    </td>
  </tr>

</table>


### Final Exam / Presentations

Instead of a final exam, we will have a "mini-conference" where each project
will give a conference-style presentation on their research project.

<!--          FI   06/07/21   M   03:00 P  05:59 P                         -->

We will use the final exam slot for presentations.
The class has been assigned a final exam timeslot of 3-6pm, Monday, June 7th.


Some guidelines for your presentation:

 * Length:
    * For 1-person teams, target around 8:00 minutes in length (no shorter than 6:00, no longer than 12:00).
    * For 2-person teams, target around 10:00 minutes in length (no shorter than 8:00, no longer than 15:00).
 * Ideally should include a demo component that highlights the system you have built in operation. Take some time with this (around 2:00)! Show off your hard work and all the cool things it does!
 * Try to tell a story with your presentation. Here is one rough template (you do **not** have to follow this precisely, it is simply an example of how to organize such a presentation):
    * Begin with an introduction that lays out the problem and *why* it is important [about 1:00]
    * Then, succinctly explain *what* you actually built/did [about 0:30]
        * _What is the hypothesis you are exploring in this work?_
    * [Demo opportunity here]
    * Next, look at some of the related work in this problem space, how does your solution differ from what came before? What ideas do you build on? [about 1:00]
    * After that, look at *how* you designed your system. What tradeoffs did you have to consider in your design, what choices did you make in how to build your system and why did your make those choices? [about 2:00]
    * Now, answer the question *does it work*. Talk about how you evaluated your system (and *why* that is a reasonable evaluation); compare this with prior systems if appropriate [about 2:30]
    * [Demo opportunity here]
    * Finally, what is the impact and result of this work? Tie back to your hypothesis. What questions might someone interested in this want to explore further? [about 1:00]
    * [Demo opportunity here]

For those projects who are willing, we'll post final papers and presentations here on the course website.
