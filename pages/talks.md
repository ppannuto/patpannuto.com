<div class="page-header">
  <h1><a href="/" style="color: inherit;">Pat Pannuto</a></h1>
</div>

I am happy to share slides from any presentation I give.
I generally try to post slides from major talks here,
but if something is missing that you are interested in, please reach out and I will add it.

---

2020
====

<div class="row talk" markdown="1">
<div class="col-lg-3 col-md-4 col-sm-5 col-xs-12" markdown="1">
[![Title Slide](/talks/2020-11-16-ENSsysKeynote_thumb.jpg "Towards a Taxonomy of Energy Scavenging Applications, Architectures, and Execution Models")](/talks/2020-11-16-ENSsysKeynote.pdf)
#### _Keynote_
</div>
<div class="col-lg-9 col-md-8 col-sm-7 col-xs-12" markdown="1">

### Towards a Taxonomy of Energy Scavenging Applications, Architectures, and Execution Models, at [ENSsys'20][enssys20]
As energy scavenging systems become more popular, we are developing a growing
diversity of energy income sources, energy storage and management techniques,
energy usage policies, and expectations of systems that all operate in a
(possibly) non-deterministic manner. This talk looks back over the last decade
of platform development to see if we can start to identify common trends among
these platforms and to start a conversation around structuring principles,
expectations, and capabilities of energy scavenging systems.

[enssys20]: http://www.enssys.org/2020/

<a href="/talks/2020-11-16-ENSsysKeynote.pptx">[pptx]</a>
<a href="/talks/2020-11-16-ENSsysKeynote.pdf">[pdf]</a>

</div>
</div>

2019
====

<div class="row talk" markdown="1">
<div class="col-lg-3 col-md-4 col-sm-5 col-xs-12" markdown="1">
[![Title Slide](/talks/pannuto19cpsbench_thumb.jpg "Planes, Trains, Apples, and Oranges: Reproducible Results and Fair Comparisons in Localization Research")](/talks/pannuto19cpsbench.pdf)
#### _Invited Talk_
</div>
<div class="col-lg-9 col-md-8 col-sm-7 col-xs-12" markdown="1">

### Planes, Trains, Apples, and Oranges: Reproducible Results and Fair Comparisons in Localization Research, at [CPS-IoTBench'19][cpsbench19]
Localization remains a continually captivating research problem as so much of
human interaction and reasoning relies on location-based contexts. However,
decades of work have revealed that there is no one-size-fits-all solution to
the bevy of applications that require location information. If every
application sets its own requirements, how then do we measure progress in
localization technology when each technology sets its own benchmarks? How can
we tease apart improvements to underlying physical layer estimates from
enhancements to algorithms that process these data points and measure these
contributions against the development of systems that exploit fusion to realize
better gains than either physical or algorithmic advancements alone? More
questions than answers, this talk aims to lay out the state of the field as it
is today and to invite discussion on what defines fair comparisons and how to
enhance the creation of reproducible artifacts, experimental configurations,
and location traces and datasets.

[cpsbench19]: https://cps-iotbench2019.ethz.ch/

<a href="/talks/pannuto19cpsbench.pptx">[pptx]</a>
<a href="/talks/pannuto19cpsbench.pdf">[pdf]</a>

</div>
</div>


2018
====

<div class="row talk" id="pannuto18slocalization" markdown="1">
<div class="col-lg-3 col-md-4 col-sm-5 col-xs-12" markdown="1">
[![Title Slide](/talks/pannuto18slocalization_thumb.jpg "Slocalization: Sub-μW Ultra Wideband Backscatter Localization")](/talks/pannuto18slocalization.pdf)
</div>
<div class="col-lg-9 col-md-8 col-sm-7 col-xs-12" markdown="1">

### Slocalization: Sub-μW Ultra Wideband Backscatter Localization, at [IPSN'18][ipsn18]
After a lot of work in localization and tracking of motes, drones, and people,
this presentation aims to ask a bigger question: Is it possible to localize
every physical thing in the world? If we do so, how might the way that humans
and computers interact with the world change?

We then introduce Slocalization, a new ultra wideband backscatter localization
system that takes a step towards truly ubiquitous localization. With
Slocalization, we introduce the latency/energy tradeoff to localization
research, demonstrating that we can achieve decimeter-accurate localization of
sub microwatt tags &ndash; at a millihertz update rate. The primary challenge
is recovery of the very low amount of reflected energy afforded by ultra
wideband backscatter.  The key idea is to leverage the stationarity and stable
periodicity of the tag to enable repeated integration of estimates of the
channel to slowly lift the tag signal out of the noise. We empirically validate
Slocalization up to 30 meters in a bi-static configuration
(anchor&rarr;15m&rarr;tag&rarr;15m&rarr;anchor), requiring about fifteen
minutes to realize sub-decimeter accuracy.

[ipsn18]: https://ipsn.acm.org/2018/

<a href="/talks/pannuto18slocalization.pptx">[pptx]</a>
<a href="/talks/pannuto18slocalization.pdf">[pdf]</a>

</div>
</div>


2016
====

<div class="row talk" id="pannuto16mbus-nzero" markdown="1">
<div class="col-lg-3 col-md-4 col-sm-5 col-xs-12" markdown="1">
[![Title Slide](/talks/pannuto16mbus-nzero_thumb.jpg "MBus: A power-aware interconnect for ultra-low power micro-scale system design")](/talks/pannuto16mbus-nzero.pdf)
#### _Invited Talk_
</div>
<div class="col-lg-9 col-md-8 col-sm-7 col-xs-12" markdown="1">

### MBus: A power-aware interconnect for ultra-low power micro-scale system design, at [DARPA N-ZERO Program Review][nzero]
The [DARPA N-ZERO program][nzero] is a really interesting initiative
looking to push the envelope for lowest-power sensors:
<small>
<blockquote>
The Near Zero Power RF and Sensor Operations (N-ZERO) program has the goal of developing the technological foundation for persistent, event-driven sensing capabilities in which the sensor can remain dormant, with near-zero power consumption, until awakened by an external trigger or stimulus.

If successful, the program could extend the lifetime of remotely deployed communications and environmental sensors—also known as unattended ground sensors (UGS)—from weeks or months to years.
</blockquote>
</small>

The N-ZERO program emphasizes the development of novel low-power sensors and
wakeup frontends, initially with the intent of using the frontends to
opportunistically wake traditional sensing and communication systems.

I was invited to the program review to discuss the viability and technical
challenges of integrating [MBus][mbus] frontends with N-ZERO chips, towards
the long-term vision of replacing the high-energy traditional sensing and
compute frontends with ultra-low power systems, such as the [Michigan Micro
Mote][michigan-micro-mote].

[nzero]: https://www.darpa.mil/program/near-zero-rf-and-sensor-operations
[michigan-micro-mote]: https://www.eecs.umich.edu/eecs/about/articles/2015/Worlds-Smallest-Computer-Michigan-Micro-Mote.html

<a href="/talks/pannuto16mbus-nzero.pptx">[pptx]</a>
<a href="/talks/pannuto16mbus-nzero.pdf">[pdf]</a>

</div>
</div>


<div class="row talk" id="pannuto16hotwireless" markdown="1">
<div class="col-lg-3 col-md-4 col-sm-5 col-xs-12" markdown="1">
[![Title Slide](/talks/pannuto16hotwireless_thumb.jpg "Ultra-Wideband and Indoor Localization")](/talks/pannuto16hotwireless.pdf)
#### _Invited Talk_
</div>
<div class="col-lg-9 col-md-8 col-sm-7 col-xs-12" markdown="1">

### Ultra-Wideband and Indoor Localization, at [HotWireless'16][hotwireless16]
[HotWireless](hotwireless16) is one of my favorite workshops, I feel like I
always come away with a few things that I find really interesting coming down
the pipe. This year I was invited to come give a talk on our recent work in
ultra-wideband localization technologies.

This is a particularly fun talk for me as it centers around two systems that
were originally proposed at previous HotWireless workshops. First we discuss
[SurePoint][kempke16surepoint], a refinement of the [PolyPoint][kempke15polypoint]
system presented at HotWireless'15, that realizes a robust, reliable, and
scalable indoor localization system. Then we look at what we can achieve with a
non-COTS UWB system with [Harmonium][kempke16harmonium] a descendent of
[Harmonia][kempke14harmonia] from HotWireless'14, that exploits asymmetry
between the tag and anchor to realize an inexpensive (&lt;$5), lightweight (3g),
and low-power tag (75mW). Finally, we close with some thoughts on open ideas
for UWB research, including backscatter, protocol refinements, and better
utilization of the channel impulse response.

[hotwireless16]: http://hotwireless16.ece.wisc.edu/
[kempke16surepoint]: /pubs/kempke16surepoint.pdf
[kempke16harmonium]: /pubs/kempke16harmonium.pdf
[kempke15polypoint]: /pubs/kempke15polypoint.pdf
[kempke14harmonia]: /pubs/kempke14harmonia.pdf

<a href="/talks/pannuto16hotwireless.pptx">[pptx]</a>
<a href="/talks/pannuto16hotwireless.pdf">[pdf]</a>

</div>
</div>


<div class="row talk" id="pannuto16nextmote" markdown="1">
<div class="col-lg-3 col-md-4 col-sm-5 col-xs-12" markdown="1">
[![Title Slide](/talks/pannuto16nextmote_thumb.jpg "The Recent Past and Distant Future of Micro-Scale Embedded Systems")](/talks/pannuto16nextmote.pdf)
#### _Keynote_
</div>
<div class="col-lg-9 col-md-8 col-sm-7 col-xs-12" markdown="1">

### The Recent Past and Distant Future of [Micro-Scale] Embedded Systems, at [NextMote: Next Generation Platforms for the Cyber-Physical Internet][nextmote16]
NextMote was a new workshop at [EWSN'16][ewsn16]. Inspired by the work we have
been doing in [millimeter-scale system design][mbus], I was invited to come
I was invited to come give the keynote presentation to open the new workshop.

The talk traverses the evolution from yesterday's motes to "next" and
"next-next" generation motes. Along the way we'll face a few harsh realities
that will limit and shape future evolution (a trillion devices cannot demand
replacing a trillion batteries), uncover recent results already pushing
boundaries (including highlights from the design and implementation of the
world's smallest computer), and explore some of the possibilities that emerge
when we rethink designs from the ground up (can we build useful motes that
don't include CPUs?).

[ewsn16]: http://www.iti.tugraz.at/EWSN2016/cms/index.php?id=36
[nextmote16]: http://www.iti.tugraz.at/EWSN2016/cms/index.php?id=12

<a href="/talks/pannuto16nextmote.pptx">[pptx]</a>
<a href="/talks/pannuto16nextmote.pdf">[pdf]</a>

</div>
</div>


<div class="row talk" id="pannuto16msResearchSummit" markdown="1">
<div class="col-lg-3 col-md-4 col-sm-5 col-xs-12" markdown="1">
[![Title Slide](/talks/pannuto16msResearchSummit_thumb.jpg "PolyPoint and the First Steps Towards Ubiquitous Localization")](/talks/pannuto16msResearchSummit.pdf)
</div>
<div class="col-lg-9 col-md-8 col-sm-7 col-xs-12" markdown="1">

### PolyPoint and the First Steps Towards Ubiquitous Localization, at the [Student Summit on Mobility, Systems, and Networking][MSsummit16]
This event mirrored MSR&rsquo;s traditional faculty retreats, only targeted at
senior-level graduate students. This was one of the most enjoyable events I
have had the pleasure of attending. Lots of really bright people working on
really interesting things with great opportunities to converse with peers and
senior members in the field equally. I would highly recommend that anyone given
the opportunity attend (and that faculty actually nominate your students when
asked!).

[MSsummit16]: https://www.microsoft.com/en-us/research/event/student-summit-mobility-systems-networking/

<a href="/talks/pannuto16msResearchSummit.pptx">[pptx]</a>
<a href="/talks/pannuto16msResearchSummit.pdf">[pdf]</a>

</div>
</div>

2015
====

<div class="row talk" id="pannuto15mbus" markdown="1">
<div class="col-lg-3 col-md-4 col-sm-5 col-xs-12" markdown="1">
[![Title Slide](/talks/pannuto15mbus_thumb.jpg "MBus: An Ultra-Low Power Interconnect for Next Generation Nanopower Systems")](/talks/pannuto15mbus.pdf)
</div>
<div class="col-lg-9 col-md-8 col-sm-7 col-xs-12" markdown="1">

### MBus: An Ultra-Low Power Interconnect for Next Generation Nanopower Systems, [42nd International Symposium on Computer Architecture][isca15]
This presentation introduces [MBus][mbus], the missing interconnect technology
that enables the millimeter-scale computing class. From the
[Michigan Micro Mote (M<sup>3</sup>)](http://cubicmm.eecs.umich.edu) project, an
effort develop next-next generation millimeter-scale computers today, we
discovered that the traditional technologies for composing embedded systems,
I<sup>2</sup>C and SPI, cannot scale to millimeter-scale designs. We drafted a
set of fundamental requirements for a millimeter-scale interconnect, and show
that no existing interconnect satisfies these requirements. We then take these
requirements and design a new interconnect, MBus, optimizing for
millimeter-scale systems while providing a superset of features from existing
interconnect technologies. For more information on MBus and the M<sup>3</sup>
project, visit [mbus.io][mbus].

[isca15]: http://www.ece.cmu.edu/calcm/isca2015/

<a href="/talks/pannuto15mbus.pptx">[pptx]</a>
<a href="/talks/pannuto15mbus.pdf">[pdf]</a>
<a href="/publications.html#pannuto15mbus">[paper]</a>

</div>
</div>

<div class="row talk" id="pannuto15making-m3" markdown="1">
<div class="col-lg-3 col-md-4 col-sm-5 col-xs-12" markdown="1">
[![Title Slide](/talks/pannuto15making-m3_thumb.jpg "Lessons from Five Years of Making Michigan Micro Motes")](/talks/pannuto15making-m3.pdf)
</div>
<div class="col-lg-9 col-md-8 col-sm-7 col-xs-12">

### Lessons from Five Years of Making Michigan Micro Motes (M<sup>3</sup>), [6th Workshop on Architectural Research Prototyping][warp15]
[WARP'15][warp15] hearkened the return of a workshop that had been on a
five-year hiatus. The workshop seeks to both motivate the importance and value
of actually building systems in the architecture community as well as to share
lessons and experiences from fabrication. This talk begins by highlighting an
architectural problem, the absence of an interconnect technology that is
appropriate for mm-scale modules, and our solution to that issue: [MBus][mbus].
The talk then covers a breadth of the system, manufacturing, and design issues
that we have solved and are struggling with for the Michigan Micro Mote project.
Finally, the talk closes with an introduction of an emerging issue in low-power
system design, the need for an indirection layer for peripheral control and
semi-automated operations, and our solution to that issue, the MPQ protocol
for MBus.

[warp15]: http://www.csl.cornell.edu/warp2015/
[mbus]: http://mbus.io

<a href="/talks/pannuto15making-m3.pptx">[pptx]</a>
<a href="/talks/pannuto15making-m3.pdf">[pdf]</a>
<a href="/publications.html#pannuto15making-m3">[paper]</a>

</div>
</div>

<div class="row talk" id="techchange15" markdown="1">
<div class="col-lg-3 col-md-4 col-sm-5 col-xs-12" markdown="1">
[![Title Slide](/talks/techchange15_thumb.jpg "Sensor Systems and the Art of Effectively Deploying Sensor Networks")](/talks/techchange15.pdf)
#### _Guest Speaker_
</div>
<div class="col-lg-9 col-md-8 col-sm-7 col-xs-12" markdown="1">

### Sensor Systems and the Art of Effectively Deploying Sensor Networks, [TechChange TC111: Technology for Monitoring and Evaluation][tc111]

[TC111][tc111] was a online course focusing on skills and strategies for
collecting, managing, analyzing, and visualizing Information Communication
Technologies put on by [TechChange][techchange]. I was asked to give a guest
lecture on the capabilities and added value of sensor deployments as well as
the challenges in recovering data from deployments, with a focus on how
non-technical organizations can realize and utilize sensing. This presentation
was in collaboration with [Guillaume Kroll](http://cega.berkeley.edu/staff/)
at the [Center for Effective Global Action (CEGA)](http://cega.berkeley.edu/).

[tc111]: https://docs.google.com/document/d/18FmiR_eUrfM2XlEceVUMaIMFBfU7YOyzoIrblUSf1kU/edit
[techchange]: http://techchange.org/

<a href="/talks/techchange15.pptx">[pptx]</a>
<a href="/talks/techchange15.pdf">[pdf]</a>

</div>
</div>

2014
====

<div class="row talk" id="vlcs14" markdown="1">
<div class="col-lg-3 col-md-4 col-sm-5 col-xs-12" markdown="1">
[![Title Slide](/talks/vlcs14_thumb.jpg "System Architecture Directions for a Software-Defined Lighting Infrastructure")](/talks/vlcs14.pdf)
</div>
<div class="col-lg-9 col-md-8 col-sm-7 col-xs-12" markdown="1">

### System Architecture Directions for a Software-Defined Lighting Infrastructure, [1st ACM Workshop on Visible Light Communication Systems][vlcs14]

[VLCS'14][vlcs14] was a new workshop attached to [MobiCom'14][mobicom14]. This
talk presented our initial research into the design of Software-Defined
Lighting (SDL), in particular looking at the diversity of applications already
created and coming down the pipe and looking at ways of mapping all of these
applications to a single, unified lighting network. A copy of the workshop
[paper](/publications.html#kuo14vlc_arch) is also
available.

[vlcs14]: http://archive.networks.rice.edu/VLCS-2014/index.html
[mobicom14]: http://www.sigmobile.org/mobicom/2014/

<a href="/talks/vlcs14.pptx">[pptx]</a>
<a href="/talks/vlcs14.pdf">[pdf]</a>
<a href="/publications.html#kuo14vlc_arch">[paper]</a>

</div>
</div>

<div class="row talk" id="stanford-IoT14" markdown="1">
<div class="col-lg-3 col-md-4 col-sm-5 col-xs-12" markdown="1">
[![Title Slide](/talks/stanford-IoT14_thumb.jpg "Embedded System Design and the Internet of Things")](/talks/stanford-IoT14.pdf)
#### _Invited Talk_
</div>
<div class="col-lg-9 col-md-8 col-sm-7 col-xs-12" markdown="1">

### Embedded System Design and the Internet of Things, [Stanford Internet of Things Industrial Research Program](http://iot.stanford.edu/workshop14.html)

The workshop was a kickoff for the Stanford Internet of Things Industrial
Research Program. I was asked to describe the state of security for the
Internet of Things, in particular looking from the perspective of an embedded
systems hardware and network developer. The talk gives an overview of some
recent research, some challenges and directions in networking, and a
discussion of the hardware trends, expectations, and requirements for embedded
systems, all with an eye towards security.

<a href="/talks/stanford-IoT14.pptx">[pptx]</a>
<a href="/talks/stanford-IoT14.pdf">[pdf]</a>

</div>
</div>

<div class="row talk" id="dil14-pannuto" markdown="1">
<div class="col-lg-3 col-md-4 col-sm-5 col-xs-12" markdown="1">
[![Title Slide](/talks/dil14-pannuto_thumb.jpg "Sensing Technologies for Data Collection and Monitoring")](/talks/dil14-pannuto.pdf)
#### _Invited Talk_
</div>
<div class="col-lg-9 col-md-8 col-sm-7 col-xs-12" markdown="1">

### Sensing Technologies for Data Collection and Monitoring, [State of the Science](http://dil.berkeley.edu/stateofthescience/)

The State of the Science conference put on by [DIL](http://dil.berkeley.edu/),
[gui2de](http://gui2de.georgetown.edu/), [CEGA](http://cega.berkeley.edu/), and
the [USAID Higher Education Solutions Network](http://www.usaid.gov/hesn).
I was asked to give a presentation on the state of sensors and sensor networks
as they are available today with an emphasis on the challenges of actually
deploying systems. I was also asked to touch on the current state of research in
the area and what kinds of interesting systems are coming down the pipe.

<a href="/talks/dil14-pannuto.pptx">[pptx]</a>
<a href="/talks/dil14-pannuto.pdf">[pdf]</a>
<a href="http://www.youtube.com/watch?v=cDx0_ybpSFE">[youtube]</a>

</div>
</div>


2013
====

<div class="row talk" id="terraswarm13-mbus-trenches" markdown="1">
<div class="col-lg-3 col-md-4 col-sm-5 col-xs-12" markdown="1">
[![Title Slide](/talks/terraswarm13-mbus-trenches_thumb.jpg "Sensing Technologies for Data Collection and Monitoring")](/talks/terraswarm13-mbus-trenches.pdf)
</div>
<div class="col-lg-9 col-md-8 col-sm-7 col-xs-12" markdown="1">

### MBus: Enabling the Next Generation of Sensors and Systems, [TerraSwarm Annual Meeting](http://www.terraswarm.org/conferences/13/annual/index.htm)

The [TerraSwarm Research Center](http://www.terraswarm.org/) holds an annual
meeting for all participating members. During the meeting, I was asked to give
a "from the trenches" talk, describing my current research, which at the time
was focused heavily on [MBus](http://mbus.io/).

<a href="/talks/terraswarm13-mbus-trenches.pptx">[pptx]</a>
<a href="/talks/terraswarm13-mbus-trenches.pdf">[pdf]</a>

</div>
</div>


2012
====

<div class="row talk" id="intro_git" markdown="1">
<div class="col-lg-3 col-md-4 col-sm-5 col-xs-12" markdown="1">
[![Title Slide](/talks/intro_git_thumb.jpg "Introduction to Git by Scott Chacon")](https://github.com/schacon/git-presentations/tree/master/basic_git_talk)
#### _Invited Talk_
</div>
<div class="col-lg-9 col-md-8 col-sm-7 col-xs-12" markdown="1">

### Introduction to Git, [Michigan Hackers](http://michiganhackers.org/)

The Michigan Hackers are a student group at the University of Michigan who
attempt to bring together people interested in building system.
For the last few years, they've thrown [the largest
hackathon](http://mhacks.org/) in the world. In their nascency, I was invited to
give one of the first tech talks. The audience was primarily experienced
hackers, so the goal of the talk was to dive into the internals of
[git](http://git-scm.com/). I presented a slide deck put together by Scott
Chacon, [available here](https://github.com/schacon/git-presentations).

<a href="https://www.youtube.com/watch?v=clsnIPDlMrw">[youtube]</a>
<a href="https://github.com/schacon/git-presentations/tree/master/basic_git_talk">[slides <i class="fa fa-external-link"></i>]</a>

</div>
</div>


2011
====

<div class="row talk" id="pannuto11plc" markdown="1">
<div class="col-lg-3 col-md-4 col-sm-5 col-xs-12" markdown="1">
[![Title Slide](/talks/pannuto11plc_thumb.jpg "Exploring Powerline Networking for the Smart Building")](/talks/pannuto11plc.pdf)
</div>
<div class="col-lg-9 col-md-8 col-sm-7 col-xs-12">

### Exploring Powerline Networking for the Smart Building, [IP+SN 2011](http://hinrg.cs.jhu.edu/ip+sn2011/)

[IP+SN 2011](http://hinrg.cs.jhu.edu/ip+sn2011/) was a workshop attached to
the [IPSN 2011](http://ipsn.acm.org/2011/) conference in downtown Chicago. I
attended this workshop as an undergraduate, presenting some of the first
research I ever worked on. The impetus for the work was trying to reconcile
the cognitive dissonance of using wireless as the medium to connect AC power
meters, devices that are literally wired together already. The result was that
powerline networking is not as trivial as I'd hoped, with a fairly
non-intuitive connectivity graph. The takeaway was that hybrid routing,
leveraging the physically long hops provided by powerline communication and
using wireless to bridge disjoint powerline networks, would likely provide the
most efficient building-wide network.

<a href="/talks/pannuto11plc.odp">[odp]</a>
<a href="/talks/pannuto11plc.pdf">[pdf]</a>
<a href="/publications.html#pannuto11plc">[paper]</a>

</div>
</div>
