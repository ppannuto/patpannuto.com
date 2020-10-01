<div class="row" markdown="1">
<div class="col-md-8">

# Pat Pannuto
<div class="lead">
Assistant Professor, Computer Science Engineering<br />
<!--<a href="https://cse.ucsd.edu/">University of California, San Diego</a><br />-->
University of California, San Diego<br />
<small>
<a href="mailto:ppannuto@ucsd.edu">ppannuto@ucsd.edu</a> |
<a href="https://www.google.com/maps/place/Computer+Science+and+Engineering+Building/@32.8818009,-117.2338248,19.71z/data=!4m5!3m4!1s0x80dc06c3409a5d5f:0xa7dc3be7597d4d47!8m2!3d32.8818006!4d-117.2335236">3202 CSE</a> |
<a href="tel:+18588222924">+1&#8239;858&#8239;822&#8239;2924</a> |
<a href="https://calendar.google.com/calendar/embed?src=ppannuto%40eng.ucsd.edu">Calendar</a>
</small>
</div>

[Publications](/publications.html) |
[CV](/cv/pannuto.pdf) |
[Talks](/talks.html) |
[Teaching](#teaching) |
[Fellowships & Awards](/fellowships.html)

</div><!-- col-md-8 -->

<div id="portraits" class="d-none d-md-block col-md-4">
  <a href="/images/pannuto-headshot-hires.jpg"><img src="/images/pannuto-headshot-square.jpg" alt="Headshot photo of Pat" class="col-md-12"/></a>
</div><!-- col-md-4 -->

</div><!-- first row -->

<div class="row" markdown="1">
<div class="col-md-12">

I am interested in the boundary between the digital and physical world. My
research aims to expand the reach of computational infrastructure to sense and
actuate more of the physical world.

My expertise is in the design and implementation of **resource constrained
computing systems**.  These are systems whose deployment in the world
constrains their form factor, connectivity, deployability, and maintainability,
which often must then operate on microwatts of power, with only kilobytes of
memory and effectively kilobit/second lossy communication links &ndash; yet the
systems as a whole must be accurate, timely, and reliable.

I am always excited to learn about new and interesting problems that we may be
able to solve. In the past, this has included efforts to embed computation in
more places with the [world's smallest computer](#m3), to build systems for
[human social interaction tracking](#localization) to support epidemiologists
and psychologists, to design infrastructure to support [city-scale
sensing](#signpost), and to develop technology capable of [country-wide grid
health monitoring](#gridwatch).

</div>
</div>


<hr />

#### Selected Honors & Awards

 - **[Rackham Graduate School Outstanding Graduate Student Instructor](http://www.rackham.umich.edu/faculty-staff/awards/student-funding/outstanding-graduate-student-instructor-awards#recipients)** (2017)
 - **[Richard & Eleanor Towner Prize for Outstanding Graduate Student Instructors](https://crlte.engin.umich.edu/grants-awards-certificate/towner-prize/towner-prize-winners/)** (2017)
 - **[Qualcomm Innovation Fellowship](https://www.qualcomm.com/invention/research/university-relations/innovation-fellowship)** Honorable Mention (½ fellow), with [Brad Campbell](http://www.cs.virginia.edu/~bjc8c/) (2013)
 - **[National Defense Science & Engineering Graduate Fellowship](https://ndseg.asee.org/)** Fellow (2013)
 - **[National Science Foundation Graduate Research Fellowship](https://www.nsfgrfp.org/)** Fellow (2013)
 - **[University of Michigan Department of Computer Science Fellowship](http://eecs.umich.edu/)** Fellow (2012)
 - **[CSE Undergraduate Instructor Award](http://www.eecs.umich.edu/eecs/events/GSI-awards-2012.html)** (2012)
<br /><br />
 - **[IPSN'18](https://ipsn.acm.org/2018/)** Best Paper Finalist (2018)
 - **[TerraSwarm'17](https://www.terraswarm.org/conferences/17/annual/)** David Wessel Best Demo Award (2017)
 - **[_IEEE Micro_](https://www.computer.org/web/computingnow/micro)** Top Pick (2016)
 - **[INC12](http://incnano.org/)** Outstanding Poster Award (2016)
 - **[HotWireless'15](http://web.cse.ohio-state.edu/~chebo/HotWireless/)** Potential for Test of Time 2025 Award (2015)

<hr />

#### <a name="teaching"></a>Teaching

 - [CSE141 - A00: Introduction to Computer Architecture](/classes/2020/fall/cse141/)
 - [CSE291 - K00: Platforms and Systems to Bridge the Digital and Physical World](/classes/2020/winter/cse291/)

A [history of my teaching prior to joining UCSD](/teaching.html) is also available.

<hr />

#### <a name="m3"></a> Michigan Micro Mote & MBus
<div class="row" markdown="1">
<div class="col-md-10">
The Michigan Micro Mote, or M<sup>3</sup> project, aims to bring
general-purpose computing and sensing to millimeter-scale devices.
 As part of this effort, we identified the system interconnect as a key
impediment to further scaling the energy and area of embedded computing.
To address this, I led the design of [MBus, a new chip-to-chip
interconnect](http://mbus.io) optimized for energy-conscious designs.

The Michigan Micro Mote is on display in World's Smallest Computer exhibit the
lobby of the Computer History Musuem in Mountain View.
You can [see the exhibit online here][chm].

[chm]: https://computerhistory.org/blog/the-worlds-smallest-computer/

[Cubeworks](http://cubeworks.us/) is commercializing the M<sup>3</sup> technology.
</div>
<div class="col-md-2">
![M3 node on a finger](/images/research/m3-finger-square.jpg){: .img-fluid }

![M3 node on edge of US nickel coin](/images/research/m3-nickel-square.jpg){: .img-fluid }
</div>
</div>
<small>
{
[JSTS'16](/pubs/lee16mbus.pdf) |
**[Micro Top Picks '16](/pubs/pannuto16mbus-top-picks.pdf)** |
**[ISCA'15](/pubs/pannuto15mbus.pdf)** |
**[WARP'15](/pubs/pannuto15making-m3.pdf)** |
[CICC'14](/pubs/kuo14mbus.pdf) |
[VLSI'14](/pubs/blaauw14iot.pdf) |
[VLSI'14](/pubs/kim14motion.pdf) |
[JSSC'13](/pubs/lee13modular.pdf)
}
</small>


#### <a name="tock"></a> The Tock Operating System
<div class="row" markdown="1">
<div class="col-md-10">
Low-power microcontrollers lack some of the hardware features and memory
resources that traditionally enable multiprogrammable systems.
Accordingly, microcontroller-based operating systems have not provided
important features like fault isolation, dynamic memory allocation, and
flexible concurrency.
However, an emerging class of embedded applications are software platforms,
rather than single purpose devices, and need these multiprogramming features.
Tock, a new operating system for low-power platforms, takes advantage of
limited hardware-protection mechanisms as well as the type-safety features
of the Rust programming language to provide a multiprogramming environment for
microcontrollers.
</div>
<div class="col-md-2">
![Tock Logo](/images/research/tock-logo-square.png){: .img-fluid .d-none .d-md-block }
</div>
<div class="col-md-12">
Tock isolates software faults, provides memory protection, and efficiently
manages memory for dynamic application workloads written in any language. It
achieves this while retaining the dependability requirements of long-running
applications.

[Google recently announced the OpenSK][opensk], a fully open-source hardware
security module, which is built on top of Tock.

[opensk]: https://security.googleblog.com/2020/01/say-hello-to-opensk-fully-open-source.html

[www.tockos.org](https://www.tockos.org/)
</div>
</div>
<small>
{
[SOSP'17](/pubs/levy17multiprogramming.pdf) |
[APSys'17](/pubs/levy17rustkernel.pdf) |
[PLOS'15](/pubs/levy15ownership.pdf)
}
</small>


#### <a name="localization"></a> Localization

Location information is a key aspect of context-aware computing. Making
location a first-class computational resource, like time synchronization or
networking today, is critical to realizing visions of intelligent and reactive
environments.

I have worked on several localization efforts, tackling different
applications:

##### <a name="slocalization"></a> Slocalization
<div class="row" markdown="1">
<div class="col-md-9">
For most of modern history, massive effort has gone into the careful
organization, sorting, and filing of information for later retrieval. With the
rise of the Information Age, we have transitioned from filing information to
simply searching for it on demand, expecting our computing infrastructure to
automatically find exactly what we are searching for.  The same is not yet true
for the physical world.  While there are exceptions, the vast majority of
things in the physical world remain invisible to the computational domain.
Slocalization takes one small step towards enabling "search not file" for the
physical world, demonstrating a sub-microwatt tag that can be localized with
decimeter accuracy in complex, indoor environments using ultra wideband
backscatter.
</div>
<div class="col-md-3">
![Channel impulse response after repeated integrations](/images/research/sloc-cir.png){: .img-fluid }

![Frontside of tag hardware](/images/research/sloc-tag-front-500px.png){: .img-fluid }

![Backside of tag hardware](/images/research/sloc-tag-back-500px.png){: .img-fluid }
</div>
</div>
<small>{
**[IPSN'18](/pubs/pannuto18slocalization.pdf)** }
</small>

##### <a name="surepoint"></a> SurePoint
In late 2013, DecaWave released the first (and as of 2019 still only)
commercially available ultra wideband transceiver. While ultra wideband
provides the potential for extremely accurate range estimates, in practice
single range estimates can exhibit variation well over a meter.  SurePoint
explores what's required to build a scalable, high-fidelity, and
high-reliability (29 cm 50th percentile, 77 cm 99th percentile accuracy of raw
range estimates) system atop a UWB ranging primitive.
<br /><small>{
[SenSys'16](/pubs/kempke16surepoint.pdf) |
[HotWireless'15](/pubs/kempke15polypoint.pdf) }
</small>

##### <a name="harmonium"></a> [Harmonium][harmonia]
<div class="row" markdown="1">
<div class="col-md-9">
Ultra wideband tracking (order 1-10 cm) with only narrowband components of
lightweight (3 g), low power (75 mW or 3.9 mJ/fix), low cost (< $5 USD),
fast-moving (up to 2.4 m/s) tags.
</div>
<div class="col-md-3">
![Harmonium tag mounted on a micro quadrotor](/images/research/harm-quad-with-tag.jpg){: .img-fluid }
</div>
</div>
<small>{
**[TOSN'18](/pubs/pannuto18harmonium.pdf)** |
[IPSN'16](/pubs/kempke16harmonium.pdf) |
[MC<sup>2</sup>R'15](/pubs/kempke15harmonia.pdf) |
[HotWireless'14](/pubs/kempke14harmonia.pdf) }
</small>

##### <a name="luxapose"></a> [Luxapose][luxapose]
<div class="row" markdown="1">
<div class="col-md-10">
An exploration in using lighting infrastructure for astral navigation indoors.
Luxapose spawned considerable follow-on work (with which I have no affiliation)
that is really cool and looks at how to do this without requiring intelligent
LED lighting infrastructure, in particular check out
[LiTell](http://xyzhang.ucsd.edu/papers/CZhang_MobiCom16_LiTell.pdf) and some of
[Xinyu's other light-based localization work](http://xyzhang.ucsd.edu/publications.html).
</div>
<div class="col-md-2">
![Luxapose image processing snapshot](/images/research/vlc-centers.png){: .img-fluid }
</div>
</div>
<small>{
[MobiCom'14](/pubs/kuo14luxapose.pdf) }
</small>

##### <a name="opo"></a> [Opo][opo]
<div class="row" markdown="1">
<div class="col-md-8">
An exploration in _relative_ location, a low-power (126 J/day) wearable badge
that provides high fidelity (centimeter-accurate, second-level granularity)
human interaction information.

Opo was initially developed in partnership with epidemiologists interested in
understanding the impact of interaction time and distance on the spread of flu
in elementary school settings. The platform has since also been adapted to
support handwashing studies in hospital settings.
</div>
<div class="col-md-4">
![Various configurations of people wearing Opo tags](/images/research/opo-quad.png){: .img-fluid }
</div>
</div>
<small>{
[SenSys'14](/pubs/huang14opo.pdf) }
</small>

[luxapose]: http://lab11.eecs.umich.edu/projects/vlc_localization/ "Luxapose: Indoor Positioning with Mobile Phones and Visible Light"
[harmonia]: http://lab11.eecs.umich.edu/projects/harmonia/ "Harmonia: Wideband Spreading for Accurate Indoor RF Localization"
[opo]: http://lab11.eecs.umich.edu/projects/opo/ "Opo: A Wearable Sensor for Capturing High-Fidelity Face-to-Face Interactions"


#### <a name="gridwatch"></a> GridWatch and The Open INcentive Kit

The power grid is one of humanity's most significant engineering undertakings,
and it is essential in developed and developing nations alike. Yet, most grids
have remarkably little introspection into their operation. GridWatch is
inspired by a simple observation, a smartphone stops charging for one of two
reasons: (1) The user unplugged it, (2) The power went out.
Given that we can filter the first case with the phone's accelerometer, can a
critical mass of smartphones act as low-fidelity, high-coverage,
fine-granularity grid monitor that runs independent of local utilities?
Following the promise shown by this initial inspiration, GridWatch has grown to
include a rich suite of power sensing technologies, which includes [custom
hardware][powerwatch] for high-fidelity measurements and ground truth and most
recently ideas for [non-contact voltage monitoring][fancythat] from project
collaborators.

Today, GridWatch has micro deployments in the United States, Venezuela,
Nigeria, and India. The primary deployment, branded DumsorWatch, in Accra,
Ghana serves as one of the principle measurement and evaluation arms for the
$498 million [Ghana Power Compact][mccghana] and has several hundred sensors
deployed and several thousand app-based participants.

Born out of the complex, wide-area study demanded by DumsorWatch,
the [Open INcentive Kit][oink] (OINK) is a new platform for running and
managing incentive-based studies. With OINK, experimenters set up a series of
rules that express when and how study participants should be incentivized. OINK
monitors a study, automatically triggers incentives, and handles disbursements.

<small>
{
[COMPASS'19](/pubs/klugman19scale.pdf) |
[GetMobile'19](/pubs/klugman19oldtricks.pdf) |
[ICTD'19](/pubs/klugman19oink.pdf) |
[MobiCom'18](/pubs/klugman18liberation.pdf) |
[HotMobile'14](/pubs/klugman14gridwatch.pdf)
}
</small>

[gridwatch]: http://lab11.eecs.umich.edu/projects/gridwatch/ "GridWatch: Mapping Blackouts with Smart Phones"
[fancythat]: https://dl.acm.org/citation.cfm?id=3209864
[powerwatch]: https://github.com/lab11/PlugWatch/tree/master/powerwatch
[mccghana]: https://www.mcc.gov/where-we-work/program/ghana-power-compact
[oink]: https://openincentivekit.com


#### <a name="signpost"></a> The Signpost City-Scale Sensing Project
<div class="row" markdown="1">
<div class="col-md-9">
City-scale sensing holds the promise of enabling deeper understanding of our
urban environments. However, a city-scale deployment requires physical
installation, power management, and communications—all challenging tasks
standing between a good idea and a realized one.
The Signpost project aims to provide a platform that enables easy deployment
and experimentation for city-scale applications.

[github/lab11/signpost](https://github.com/lab11/signpost)
</div>
<div class="col-md-3">
![A deployed signpost in the wild](/images/research/signpost-closeup-square.jpg){: .img-fluid }
</div>
</div>
<small>
{
[IPSN'18](/pubs/adkins18signpost.pdf)
}
</small>


<hr />


<div class="row" markdown="1">
<div class="col-lg-12 col-xs-12">

## <a name="misc"></a> Miscellaneous

<a href="http://confsearch.ethz.ch/confsearch/faces/pages/staticresults.jsp?query=usenix%20asplos%20ewsn%20hotnets%20hotos%20ipsn%20isca%20micro%20mobicom%20mobihoc%20mobisys%20nsdi%20osdi%20sensys%20sigcomm%20sosp%20uist&sortMode=1&graphicView=1">These are the conferences I generally follow</a>, courtesy of ConfSearch.

Working on, or reviewing, any empirical work? [Check out the Empirical Evaluation Guidelines checklist](https://www.sigplan.org/Resources/EmpiricalEvaluation/).

I am happy to share slides from any presentation I give.
I generally try to [post slides from major talks](/talks.html),
but if something is missing that you are interested in, please reach out and I will add it.

I have been fortunate to be successful in many fellowship applications.
This is due in no small part to excellent guidance from my colleagues and mentors.
I am happy to share some of that advice and my application materials [here](/fellowships.html).

[Here are my application materials from the faculty market](/appkit). Hopefully they are helpful.

One of my favorite parts of academia is the opportunity it has afforded me to travel the world.
<a href="https://www.amcharts.com/visited_countries/#AT,BE,DK,FR,DE,IN,IT,NL,PT,ES,VA,CA,US,GH,MA,CN,KR">Here's all the countries I've made it to thus far</a>
(also <a href="https://www.amcharts.com/visited_states/#US-AZ,US-CA,US-CT,US-DC,US-DE,US-FL,US-GA,US-HI,US-IL,US-IN,US-KS,US-KY,US-LA,US-MA,US-MD,US-ME,US-MI,US-MO,US-NJ,US-NV,US-NY,US-OH,US-OK,US-OR,US-PA,US-RI,US-TN,US-TX,US-UT,US-VA,US-WA,US-WI">US states I've spent any appreciable time in</a>).

One lesson from travel is that much of the web is inaccessible from areas where
internet access is unreliable or expensive. There is
[a neat tool that estimates the literal cost of loading your webpage](https://whatdoesmysitecost.com/test/190806_DR_5d72d77810bcd05a0b500102039b0530).
I appreciate Dan Luu's metric of aiming to be [smaller than the JavaScript used by Google's AMP](https://danluu.com/web-bloat/#appendix-irony).

I am a proud alumnus of the [Lab11](https://lab11.eecs.berkeley.edu) research
group, headed by [Dr. Prabal Dutta](http://eecs.umich.edu/~prabal).
During graduate school, I was a
[National Defense Science & Engineering Graduate (NDSEG)](https://ndseg.asee.org/)
Fellow (2013),
a [National Science Foundation Graduate Research Fellowship Program (NSF GRFP)](http://www.nsfgrfp.org/)
Fellow (2013),
and a [Qualcomm Innovation Fellowship (QInF)](https://www.qualcomm.com/invention/research/university-relations/innovation-fellowship)
Fellow (2013).
My graduate studies were also generously supported by the [Semiconductor Research Corporation][src]
through both the [TerraSwarm][terraswarm] program (part of [STARnet][starnet]) and the
[CONIX][conix] center (part of [JUMP][jump]).

[terraswarm]: https://ptolemy.berkeley.edu/projects/terraswarm/
[conix]: https://conix.io/
[src]: https://www.src.org
[starnet]: https://www.src.org/program/starnet/about/
[jump]: https://www.src.org/program/jump/

</div>
</div>
