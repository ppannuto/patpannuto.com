Platforms & Systems to Bridge the Digital & Physical World
==========================================================
## CSE291 K00 - Winter 2020

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

Meets M/W from 10:30 to 11:50 in CSE 4140.<br/>
[Pat Pannuto](https://patpannuto.com) is the instructor and their office is CSE 3202 (right in the corner).

Office hours are M/W from 14:00 to 14:50 in CSE 3202.<br/>
Other times available by appointment, generally afternoons are preferred.

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
batteryless systems, backscatter communication, and how to do machine learning
with less than 1 MB of memory.

During the last week of the course, we will shift focus a bit from technology
development. Often advances in embedded systems can lead to unexpected leaps
in capability: modern RF techniques can build camera-like structures that
"see-through" walls to capture occupancy, gestures, or even biometrics like
respiration and heart rate; my PhD work helped build energy-harvesting,
wireless (optical) cameras about a cubic millimeter in size and acoustic
recorders small and thin enough to be imperceptibly embedded in thick paper.
We will finish the term with thoughts on the ethical implications of recent
and future advancements, how policy might encode social norms and
expectations, and what technological solutions could enforce these policies.

### Target Audience

The intended audience of this course is PhD students or masters students who
are interested in pursuing a PhD in the future.
This is a research-oriented class. It's designed to bring people up to speed on
the history as well as the state of the art in embedded systems and to gain
experience with the design, early implementation, and evaluation of a research
idea.



### Prerequisites

Experience equivalent of an undergraduate degree in any of Electrical
Engineering, Computer Engineering, Computer Science, Data Science, Information
Science, or related areas.  This is a vertical slice through the computing
stack, and we will touch on topics from programming languages and distributed
systems down to circuits and wireless. An enthusiasm and willingness to learn a
little about a lot of new things is far more important than any one specific
background.

<!--
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
 - At what point did you decide you liked &ndash; or didn't like &ndash; the paper, why?

#### _The One Thing_

Often in academia, people will refer to papers as pointers to a concept or
idea. As an experiment, for each paper we read this quarter, we will try to
crowdsource putting into words that one _thing_ for each paper.

At the end of each review, include a **short**, single sentence or phrase that
you think best captures the essence of the paper.

#### Submitting Reviews

We will use the [HotCRP review system](https://ucsd-cse291-k00-w20.hotcrp.com)
&ndash; the same tool used by many conferences to review papers. Reviews are
due before the start of class. HotCRP will automatically cut off submissions
at 10:15.  Enrolled students should already have accounts. If you need an
account or have other issues, please
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

 - Monday, January 20: One page proposal writeup that includes your hypothesis, motivation, and expected results.
 - Monday, February 17: Three to four page draft that includes a literature review ("Related Work"), proposed experiments, and their expected outcomes.
 - Friday, March 20: Final five to six page paper that includes outcome of small-scale experiments / prototype / etc. This should resemble an early-to-mature draft of an academic workshop paper.



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
    <td>Jan&nbsp;6</td>
    <td><a href="2020-01-06-cse291-intro.pptx">Introduction</a></td>
    <td>Pannuto</td>
    <td></td>
  </tr>
  <tr>
    <td>Jan&nbsp;8</td>
    <td><a href="2020-01-08-cse291-ubiquitous.pptx">Ubiquitous Computing</a></td>
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
  <tr>
    <td>Jan&nbsp;13</td>
    <td><a href="2020-01-13-cse291-deployments1.pptx">Indoors &amp; Outdoors</a></td>
    <td>Pannuto</td>
    <td>
      <ul>
        <li><a href="/papers/szewczyk2004greatduckisland.pdf">An Analysis of a Large Scale Habitat Monitoring Application (The Great Duck Island paper)</a></li>
        <li><a href="/papers/balaji2013sentinel.pdf">Sentinel: Occupancy Based HVAC Actuation using Existing WiFi Infrastructure within Commercial Buildings</a></li>
      </ul>
      <hr />
      For those wanting more...
      <ul>
        <li><a href="/papers/juang2002zebranet.pdf">Energy-Efficient Computing for Wildlife Tracking: Design Tradeoffs and Early Experiences with ZebraNet</a></li>
        <li><a href="/papers/balaji2016brick.pdf">Brick: Towards a Unified Metadata Schema For Buildings</a></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>Jan&nbsp;15</td>
    <td><a href="2020-01-15-cse291-deployments2.pptx">Cities and the People in Them</a></td>
    <td>Pannuto</td>
    <td>
      <a href="https://github.com/ppannuto/patpannuto.com/blob/master/classes/2020/winter/cse291/index.md">Sign up for one discussion to lead by submitting a pull request.</a> <small>Conflicts resolved by pull request timestamp (first come, first serve).</small>
      <hr />
      <ul>
        <li><a href="/papers/catlett2017aot.pdf">Array of Things: A Scientific Research Instrument in the Public Way</a></li>
        <li><a href="/papers/mottola2010tunnels.pdf">Not all Wireless Sensor Networks are Created Equal: A Comparative Study on Tunnels</a></li>
      </ul>
      <hr />
      For those wanting more...
      <ul>
        <li><a href="https://wp.nyu.edu/sonyc/">Sounds of New York City (SONYC)</a></li>
        <li><a href="/pubs/adkins18signpost.pdf">The Signpost Platform for City-Scale Sensing</a></li>
      </ul>
    </td>
    <!--
    ### Human Sensing
     - WRENSys? Opo? iBadge?
    -->
  </tr>

  <tr class="table-info">
    <td colspan="4">Week 3: Building a Platform</td>
  </tr>
  <tr>
    <td>Jan&nbsp;20</td>
    <td colspan="2"><i>MLK Day</i></td>
    <td>Project proposals due. Submit via e-mail to <a href="mailto:ppannuto@ucsd.edu?subject=CSE291-K00-W20%20Project%20Proposal">ppannuto@ucsd.edu</a>.</td>
  </tr>
  <tr>
    <td>Jan&nbsp;22</td>
    <td>Building blocks &amp; Sensor System Architectures</td>
    <td>Pannuto</td>
    <td>
      <ul>
        <li><a href="/papers/dutta2008epic.pdf">A Building Block Approach to Sensornet Systems</a></li>
        <li><a href="/papers/kim2018postsoc.pdf">System Architecture Directions for Post-SoC/32-bit Networked Sensors</a></li>
      </ul>
      No review for the last one, but please do read it:
      <ul>
        <li><a href="/papers/campbell2014ehtoolkit.pdf">An Energy-Harvesting Sensor Architecture and Toolkit for Building Monitoring and Event Detection</a></li>
      </ul>
    </td>
  </tr>

  <tr class="table-info">
    <td colspan="4">Week 4: Joule Rules Everything Around Me</td>
  </tr>
  <tr>
    <td>Jan&nbsp;27</td>
    <td>Energy Harvesting and Fair Sharing</td>
    <td>Xiaofan</td>
    <td>
      <ul>
        <li><a href="/papers/cao2008virtualbattery.pdf">Virtual Battery: An Energy Reserve Abstraction for Embedded Sensor Networks</a></li>
        <li><a href="/papers/hester2015ufop.pdf">Tragedy of the Coulombs: Federating Energy Storage for Tiny, Intermittently-Powered Sensors</a></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>Jan&nbsp;29</td>
    <td>Whither intermittent computing?</td>
    <td></td>
    <td>
      <ul>
        <li><a href="/papers/colin2018capybara.pdf">A Reconfigurable Energy Storage Architecture forEnergy-harvesting Devices</a></li>
        <li><a href="http://lab11.eecs.berkeley.edu/content/pubs/jackson19capacity.pdf">Capacity over Capacitance for Reliable Energy Harvesting Sensors</a></li>
      </ul>
    </td>
  </tr>

  <tr class="table-info">
    <td colspan="4">Week 5: Communication</td>
  </tr>
  <tr>
    <td>Feb&nbsp;3</td>
    <td>Project Workshop Day</td>
    <td>Pannuto</td>
    <td>
      Bring printed copies of initial drafts to class.
    </td>
  </tr>
  <tr>
    <td>Feb&nbsp;5</td>
    <td>Great Ideas in Traditional Communication</td>
    <td>Sushmitha</td>
    <td>
      <ul>
        <li><a href="/papers/hui2008ipdead.pdf">IP is Dead, Long Live IP for Wireless Sensor Networks</a></li>
        <li><a href="/papers/ferrari2011glossy.pdf">Efficient Network Flooding and Time Synchronization with Glossy</a></li>
      </ul>
      <hr />
      For those wanting more...
      <ul>
        <li><a href="/papers/ferrari2012lwb.pdf">Low-Power Wireless Bus</a></li>
      </ul>
    </td>
  </tr>

  <tr class="table-info">
    <td colspan="4">Week 6: Communication is always the hardest part</td>
  </tr>
  <tr>
    <td>Feb&nbsp;10</td>
    <td>Wild Ideas in Non-Traditional Communication</td>
    <td>Renjie</td>
    <td>
      <ul>
        <li><a href="/papers/iyer2016interscatter.pdf">Inter-Technology Backscatter: Towards Internet Connectivity for Implanted Devices</a></li>
        <li><a href="/papers/varshney2019tunnelscatter.pdf">TunnelScatter: Low Power Communication for SensorTags using Tunnel Diodes</a></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>Feb&nbsp;12</td>
    <td>Sharing Spectrum</td>
    <td></td>
    <td>
      <ul>
        <li><a href="/papers/saifullah2016snow.pdf">SNOW: Sensor Network over White Spaces</a></li>
        <li><a href="https://lab11.eecs.umich.edu/content/pubs/ghena19lpwans.pdf">Challenge: Unlicensed LPWANs Are Not Yet the Path to Ubiquitous Connectivity</a></li>
      </ul>
    </td>
  </tr>


  <tr class="table-info">
    <td colspan="4">Week 7: Embedded Operating Systems</td>
  </tr>
  <tr>
    <td>Feb&nbsp;17</td>
    <td colspan="2"><i>President's Day</i></td>
    <td>Project drafts due. Submit via e-mail to <a href="mailto:ppannuto@ucsd.edu?subject=CSE291-K00-W20%20Project%20Draft">ppannuto@ucsd.edu</a>.
  </tr>
  <tr>
    <td>Feb&nbsp;19</td>
    <td>What's an application, an OS, in an embedded context?</td>
    <td>Nagesh</td>
    <td>
      <ul>
        <li>TinyOS</li>
        <!-- Either Regehr's Safe TinyOS , or the full 35 pager from Phil ... -->
        <li><a href="/pubs/levy17multiprogramming.pdf">Multiprogramming a 64kB Computer Safely and Efficiently</a></li>
        <li><a href="/papers/hardin2018appiso.pdf">Application Memory Isolation on Ultra-Low-Power MCUs</a></li>
      </ul>
    </td>
  </tr>


  <tr class="table-info">
    <td colspan="4">Week 8: Sensors as Computational Platforms</td>
  </tr>
  <tr>
    <td>Feb&nbsp;24</td>
    <td>ML at the Very Edge</td>
    <td></td>
    <td>
      <ul>
        <li><a href="/papers/yao2017deepiot.pdf">DeepIoT: Compressing Deep Neural Network Structures for Sensing Systems with a Compressor-Critic Framework</a></li>
        <li><a href="/papers/radu2017wearableML.pdf">Multimodal Deep Learning for Activity and Context Recognition</a></li>
      </ul>
    <!--
     Compute/Comm tradeoff bit...
     - Maybe one of Pengyu's (do any of his papers capture his oral argument about closing this gap?)
    -->
    </td>
  </tr>
  <tr>
    <td>Feb&nbsp;26</td>
    <td>Distributed Computing and Task Planning</td>
    <td>Wenshan</td>
    <td>
      <ul>
        <li>DDFlow</li><!--Or maybe the new one: The Case for Robust Adaptation: Autonomic Resource Management is a Vulnerability??-->
        <li><i>TBD</i></li><!--Mate?-->
      </ul>
    </td>
  </tr>

  <tr class="table-info">
    <td colspan="4">Week 9: Security</td>
  </tr>
  <tr>
    <td>Mar&nbsp;2</td>
    <td>Trusting sensors and data</td>
    <td>Ke Sun</td>
    <td>
      <ul>
        <li>One of the Kevin Fu sensor injection papers  (Light Commands or Pacemakers)</li>
        <li>Azure Sphere</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>Mar&nbsp;4</td>
    <td>Trusting systems</td>
    <td>Eric Weise</td>
    <td>
      <ul>
        <li><a href="/papers/anderson2019wave.pdf">WAVE: A Decentralized Authorization Framework with Transitive Delegation</a></li>
        <li>Deconstructing a startup: The Helium Network</li>
      </ul>
    </td>
    <!--
     - Ravel then vs HomeOS (the paper) / Apple Home / Google Home / etc?
     - Maybe some discussion on AllJoyn/etc?
    -->
  </tr>

  <tr class="table-info">
    <td colspan="4">Week 10: Ethical Considerations & Societal Impact</td>
    <!--
     - Steven Weber's stuff
     - Revisit Weiser vision with critical eye (write a critique?)
     - mm-wave scanners for electronics
    -->
  </tr>
  <tr>
    <td>Mar&nbsp;9</td>
    <td><i>TBA</i></td>
    <td>Pannuto</td>
    <td>
    </td>
  </tr>
  <tr>
    <td>Mar&nbsp;11</td>
    <td><i>TBA</i></td>
    <td>Pannuto</td>
    <td>
    </td>
  </tr>

</table>


### Final Exam / Presentations

Instead of a final exam, we will have a "mini-conference" where each project
will give a conference-style presentation on their research project.

The class was assigned a final exam timeslot of 8-11am, Friday, March 20th.
We'll probably stick with Friday, March 20th as a date, but if it works for
everyone's schedules, we can try to find a not-8am time slot for this as a
group.
