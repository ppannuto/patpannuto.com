<div class="row" markdown="1">
<div class="col-md-8">

# Pat Pannuto
<div class="lead">
Assistant Professor, Computer Science Engineering<br />
<!--<a href="https://cse.ucsd.edu/">University of California, San Diego</a><br />-->
University of California, San Diego<br />
<a href="mailto:ppannuto@ucsd.edu">ppannuto@ucsd.edu</a> |
<a href="https://www.google.com/maps/place/Computer+Science+and+Engineering+Building/@32.8818009,-117.2338248,19.71z/data=!4m5!3m4!1s0x80dc06c3409a5d5f:0xa7dc3be7597d4d47!8m2!3d32.8818006!4d-117.2335236">3202 CSE</a> |
<a href="tel:+18588222924">+1&#8239;858&#8239;822&#8239;2924</a>
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

 - [CSE291 - K00: Platforms and Systems to Bridge the Digital and Physical World](/classes/2020/winter/cse291/)

A [history of my teaching prior to joining UCSD](/teaching.html) is also available.

<hr />

#### <a name="m3"></a> Michigan Micro Mote & MBus
The Michigan Micro Mote, or M<sup>3</sup> project, aims to bring
general-purpose computing and sensing to millimeter-scale devices.
 As part of this effort, we identified the system interconnect as a key
impediment to further scaling the energy and area of embedded computing.
To address this, I led the design of [MBus, a new chip-to-chip
interconnect](http://mbus.io) optimized for energy-conscious designs.

[Cubeworks](http://cubeworks.us/) is commercializing the M<sup>3</sup> technology.

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

Tock isolates software faults, provides memory protection, and efficiently
manages memory for dynamic application workloads written in any language. It
achieves this while retaining the dependability requirements of long-running
applications.

[www.tockos.org](https://www.tockos.org/)

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

  - **Slocalization.** For most of modern history, massive effort has gone
    into the careful organization, sorting, and filing of information for
    later retrieval. With the rise of the Information Age, we have
    transitioned from filing information to simply searching for it on demand,
    expecting our computing infrastructure to automatically find exactly what
    we are searching for.  The same is not yet true for the physical world.
    While there are exceptions, the vast majority of things in the physical
    world remain invisible to the computational domain.
    Slocalization takes one small step towards enabling "search not file" for
    the physical world, demonstrating a sub-microwatt tag that can be
    localized with decimeter accuracy in complex, indoor environments using
    ultra wideband backscatter.
    <br /><small>{
    **[IPSN'18](/pubs/pannuto18slocalization.pdf)** }
    </small>
  - **SurePoint.** In late 2013, DecaWave released the first (and as of 2018
    still only) commercially available ultra wideband transceiver. While ultra
    wideband provides the potential for extremely accurate range estimates, in
    practice single range estimates can exhibit variation well over a meter.
    SurePoint explores what's required to build a scalable, high-fidelity, and
    high-reliability (29 cm 50th percentile, 77 cm 99th percentile accuracy of
    raw range estimates) system atop a UWB ranging primitive.
    <br /><small>{
    [SenSys'16](/pubs/kempke16surepoint.pdf) |
    [HotWireless'15](/pubs/kempke15polypoint.pdf) }
    </small>
  - **[Harmonium][harmonia].** Ultra wideband tracking (order 1-10 cm) with
    only narrowband components of lightweight (3 g), low power (75 mW or
    3.9 mJ/fix), low cost (< $5 USD), fast-moving (up to 2.4 m/s) tags.
    <br /><small>{
    **[TOSN'18](/pubs/pannuto18harmonium.pdf)** |
    [IPSN'16](/pubs/kempke16harmonium.pdf) |
    [MC<sup>2</sup>R'15](/pubs/kempke15harmonia.pdf) |
    [HotWireless'14](/pubs/kempke14harmonia.pdf) }
    </small>
  - **[Luxapose][luxapose].** An exploration in using lighting
    infrastructure for astral navigation indoors. Luxapose spawned considerable
    follow-on work (with which I have no affiliation) that is really cool and
    looks at how to do this without requiring intelligent LED lighting
    infrastructure, in particular check out
    [LiTell](http://xyzhang.ucsd.edu/papers/CZhang_MobiCom16_LiTell.pdf)
    and some of [Xinyu's other light-based localization
    work](http://xyzhang.ucsd.edu/publications.html).
    <br /><small>{
    [MobiCom'14](/pubs/kuo14luxapose.pdf) }
    </small>
  - **[Opo][opo].** An exploration in _relative_ location, a low-power (126
    J/day) wearable badge that provides high fidelity (centimeter-accurate,
    second-level granularity) human interaction information.
    <br /><small>{
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

City-scale sensing holds the promise of enabling deeper understanding of our
urban environments. However, a city-scale deployment requires physical
installation, power management, and communications—all challenging tasks
standing between a good idea and a realized one.
The Signpost project aims to provide a platform that enables easy deployment
and experimentation for city-scale applications.

[github/lab11/signpost](https://github.com/lab11/signpost)

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
