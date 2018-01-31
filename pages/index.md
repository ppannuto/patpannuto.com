<div class="row" style="padding-top: 20px;" markdown="1">
<div class="col-lg-8 col-md-8 col-sm-7 col-xs-12">

<div class="lead">
I'm Pat Pannuto, a PhD student at the University of California, Berkeley.
</div>

I am advised by [Prabal Dutta](http://eecs.umich.edu/~prabal) and am the
recipient of the [National Defense Science & Engineering Graduate (NDSEG) Fellowship](https://ndseg.asee.org/) (2013),
the [National Science Foundation Graduate Research Fellowship Program (NSF GRFP) Fellowship](http://www.nsfgrfp.org/) (2013),
and the [Qualcomm Innovation Fellowship (QInF)](https://www.qualcomm.com/invention/research/university-relations/innovation-fellowship) (2013).

My research focuses on solving the "last inch" problem and solving the
challenges that stand between the burgeoning Internet of Things and inevitable
Internet of Everything.
My research vision pushes towards the realization of
ubiquitous and pervasive computing, aiming to understand how our interaction
and utilization of technology will shift as computing becomes omnipresent and
its operation and interaction shifts from conscious action to unconscious
extension of perception and ability.
What advancements will most change how people interact with themselves, the
world, and one another, and what innovations facilitate these paradigm shifts?
My interests span from low-level details---developing new technology to meet
the energy and area demands of next-generation millimeter systems---to
large-scale global considerations---understanding how our network and
infrastructure must scale and adapt to support the trillions of impending
devices.

</div>
<div class="col-lg-4 col-md-4 col-sm-5 hidden-xs">
<div id="gallery-pat-div"></div>
</div>
</div>

<hr />

#### Selected Honors & Awards

 - **[Rackham Graduate School Outstanding Graduate Student Instructor](http://www.rackham.umich.edu/faculty-staff/awards/student-funding/outstanding-graduate-student-instructor-awards#recipients)** (2017)
 - **[Richard & Eleanor Towner Prize for Outstanding Graduate Student Instructors](https://crlte.engin.umich.edu/grants-awards-certificate/towner-prize/towner-prize-winners/)** (2017)
 - **[Qualcomm Innovation Fellowship](https://www.qualcomm.com/invention/research/university-relations/innovation-fellowship)** Honorable Mention (half fellow), joint with [Brad Campbell](http://www.cs.virginia.edu/~bjc8c/) (2013)
 - **[National Defense Science & Engineering Graduate Fellowship](https://ndseg.asee.org/)** Fellow (2013)
 - **[National Science Foundation Graduate Research Fellowship](https://www.nsfgrfp.org/)** Fellow, declined (2013)
 - **[University of Michigan Department of Computer Science First Year Fellowship](http://eecs.umich.edu/)** Fellow (2012)
 - **[CSE Undergraduate Instructor Award](http://www.eecs.umich.edu/eecs/events/GSI-awards-2012.html)** (2012)
<br><br />
 - **[TerraSwarm'17](https://www.terraswarm.org/conferences/17/annual/)** David Wessel Best Demo Award (2017)
 - **[_IEEE Micro_](https://www.computer.org/web/computingnow/micro)** Top Pick (2016)
 - **[INC12](http://incnano.org/)** Outstanding Poster Award (2016)
 - **[HotWireless'15](http://web.cse.ohio-state.edu/~chebo/HotWireless/)** Potential for Test of Time 2025 Award (2015)

<hr />

#### Michigan Micro Mote & MBus
The Michigan Micro Mote, or M<sup>3</sup> project, aims to bring
general-purpose computing and sensing to millimeter-scale devices.
 As part of this effort, we identified the system interconnect as a key
impediment to further scaling the energy and area of embedded computing.
To address this, I led the design of [MBus, a new chip-to-chip
interconnect](http://mbus.io) optimized for energy-conscious designs.

[Cubeworks](http://cubeworks.us/) is commercializing the M<sup>3</sup> technology.

<small markdown="1">
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


#### Localization

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
    <br /><small markdown="1">{
    **IPSN'18** }
    </small>
  - **SurePoint.** In late 2013, DecaWave released the first (and as of 2018
    still only) commercially available ultra wideband transciever. While ultra
    wideband provides the potential for extremely accurate range estimates, in
    practice single range estimates can exhibit variation well over a meter.
    SurePoint explores what's required to build a scalable, high-fidelity, and
    high-reliability (29 cm 50th percentile, 77 cm 99th percentile accuracy of
    raw range estimates) system atop a UWB ranging primitive.
    <br /><small markdown="1">{
    [SenSys'16](/pubs/kempke16surepoint.pdf) |
    [HotWireless'15](/pubs/kempke15polypoint.pdf) }
    </small>
  - **[Harmonium][harmonia].** Ultra wideband tracking (order 1-10 cm) with
    only narrowband components of lightweight (3 g), low power (75 mW or
    3.9 mJ/fix), low cost (< $5 USD), fast-moving (up to 2.4 m/s) tags.
    <br /><small markdown="1">{
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
    <br /><small markdown="1">{
    [MobiCom'14](/pubs/kuo14luxapose.pdf) }
    </small>
  - **[Opo][opo].** An exploration in _relative_ location, a low-power (126
    J/day) wearable badge that provides high fidelity (centimeter-accurate,
    second-level granularity) human interaction information.
    <br /><small markdown="1">{
    [SenSys'14](/pubs/huang14opo.pdf) }
    </small>

[luxapose]: http://lab11.eecs.umich.edu/projects/vlc_localization/ "Luxapose: Indoor Positioning with Mobile Phones and Visible Light"
[harmonia]: http://lab11.eecs.umich.edu/projects/harmonia/ "Harmonia: Wideband Spreading for Accurate Indoor RF Localization"
[opo]: http://lab11.eecs.umich.edu/projects/opo/ "Opo: A Wearable Sensor for Capturing High-Fidelity Face-to-Face Interactions"
[gridwatch]: http://lab11.eecs.umich.edu/projects/gridwatch/ "GridWatch: Mapping Blackouts with Smart Phones"


#### The Tock Operating System

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

<small markdown="1">
{
[SOSP'17](/pubs/levy17multiprogramming.pdf) |
[APSys'17](/pubs/levy17rustkernel.pdf) |
[PLOS'15](/pubs/levy15ownership.pdf)
}
</small>


#### The Signpost City-Scale Sensing Project

City-scale sensing holds the promise of enabling deeper understanding of our
urban environments. However, a city-scale deployment requires physical
installation, power management, and communications—all challenging tasks
standing between a good idea and a realized one.
The Signpost project aims to provide a platform that enables easy deployment
and experimentation for city-scale applications.

[github/lab11/signpost](https://github.com/lab11/signpost)

<small markdown="1">
{
IPSN'18
}
</small>


<hr />

<div class="row">
<div class="col-lg-12 col-xs-12">

<div class="panel">
<div class="panel-heading"> <h3 class="panel-title"><strong>Contact</strong></h3> </div>
<div class="panel-body">
<p><a href="mailto:ppannuto@berkeley.edu">ppannuto@berkeley.edu</a></p>
<p><a href="tel:+12489904548">248.990.4548</a></p>
<p><a href="https://www.google.com/maps/place/Cory+Hall,+Berkeley,+CA+94720/@37.8750406,-122.2595182,17z/data=!3m1!4b1!4m5!3m4!1s0x80857c2399f46b11:0x89fed96de243799c!8m2!3d37.8750364!4d-122.2573242">545W, Cory Hall, Berkeley, CA 94720</a></p>
</div>
</div>
</div>
</div>

<!--
### News
 * <b>2013/05: </b>I am working at <a href="http://swarmlab.eecs.berkeley.edu">Berkeley</a> this summer
 * <b>2013/04: </b><a href="http://bradcampbell.org">Brad Campbell</a> and I won Honorable Mentions and $50,000 from the <a href="http://www.qualcomm.com/about/research/university-relations/innovation-fellowship/2013">Qualcomm Innovation Fellowship</a>
 * <b>2013/04: </b>I won the <a href="http://ndseg.asee.org/">NDSEG</a> Fellowship
 * <b>2013/04: </b>I won the <a href="http://www.nsfgrfp.org/">NSF GRFP</a> Fellowship
-->
