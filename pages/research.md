Research
========

The high-level theme of my research is "embedded systems". In particular,
I focus on enabling technology for low-power, pervasive systems with an emphasis
on the deployability and maintenance of large, long-term networks.

Raw data is included in the `source` tarballs for each project. If
you have further questions or need assistance, please do not hesitate to
<a href="/index.html">contact me</a>.

M<sup>3</sup>
-------------

The goal of the Michigan Micro Mote (M<sup>3</sup>) project is to finally
realize the Smart Dust vision: networks of integrated, autonomous,
energy-harvesting nodes that can sense the environment and deliver their data
over a wireless mesh network.  The concrete goal of the project is to: (1)
create sensor nodes that are cubic-mm in size, (2) draw ~10 nW, and (3) deliver
data every few minutes over a multihop network. This requires advances in every
layer of the system stack &ndash; circuits to memory to processor to timers to radios
to interconnects to packaging to software to protocols to programming models. If
successful, this represents a 1,000-10,000 fold improvement over the
state-of-the-art in size and power.
<p style="text-align: right; font-size:75%; padding: 0px; margin: 0px;"><i>Abstract lifted from 
	<a href="http://web.eecs.umich.edu/~prabal/">Prabal Dutta</a></i></p>
</p>

M<sup>3</sup> is an ambitious project, composed of a team of four faculty (
<a href="http://eecs.umich.edu/~dennis/">Dennis Sylvester</a>,
<a href="http://blaauw.eecs.umich.edu/people.php?u=professor&sid=ad661190b78e093e994bbcc8bc5d6b87">David Blaauw</a>,
<a href="http://eecs.umich.edu/~wentzlof/">David Wentzloff</a>,
and <a href="http://eecs.umich.edu/~prabal/">Prabal Dutta</a>
) and over a dozen graduate students. My primary contribution is the software
development environment for the M<sup>3</sup> system. This includes a
hardware/software emulation system and a supporting software library for this
M<sup>3</sup>. I also work on system architecture design.

### M-ulator

A highly extensible {ARM} {e,si}mulator. It is capable of both
simple simulation of various ARM cores (currently M0, M3) or in-circuit
emulation (currently the Michigan Micro Mote platform)

In addition, this project is used as a teaching tool for embedded systems
courses (currently at University of Michigan and University of Utah), both to
understand internal core design and higher-level MCU usage.

<p style="padding-left: 1em;">
<a href="https://github.com/ppannuto/M-ulator"><i>Available on github</i></a>
</p>

Low-Power I2C
-------------

An I2C variant designed by
<a href="https://sites.google.com/site/yoonmyunglee/">Yoonmyung Lee</a> for the
M<sup>3</sup>, this demo paper briefly explores the ultra-low power bus design
space. Its focus is on the design challenges of interfacing conventional
commercial systems with hyper-power concious systems, and the tradeoffs made to
achieve nano-Watt power budgets.

This work was presented at IPSN'12 in Beijing

<p style="font-size: 75%;"><b>Pat Pannuto</b>, Yoonmyung Lee, Ben Kempke, Dennis Sylvester, David
Blaauw, and Prabal Dutta.  Ultra-constrained sensor platform interfacing.  In
<i>Proceedings of the 11th international conference on Information Processing in
	Sensor Networks</i>, IPSN &#8217;12, pages 147&#8211;148, New York, NY, USA, 2012. ACM</p>

<p style="padding-left: 1em;">
<tt>
<a href="/research/ipsn12-i2c-paper.pdf">paper</a>
<a href="/research/ipsn12-i2c-poster.pdf">poster</a>
<a href="/research/cubicmm-demo.tar.gz">source</a>
</tt>
</p>


&#181;SDR
---------

Collaborative work with <a href="http://eecs.umich.edu/~samkuo/">Ye-Sheng Kuo</a>,
supporting the final steps of his &#181;SDR platform. &#181;SDR is a 10x
improvement in the price, power, and portability of SDR platforms. It trades the
modularity of the RF frontends and some amount of processing power for these
advantages. Several low-power protocols (A-MAC, Glossy) have been implemented in
&#181;SDR already.

For up-to-date information on &#181;SDR, please
<a href="http://energy.eecs.umich.edu/wiki/doku.php?id=proj:sdr:home">visit the
	project website</a>.

<p style="font-size: 75%;">
Ye-Sheng Kuo, <b>Pat Pannuto</b>, Thomas Schmid, and Prabal Dutta. Reconfiguring
the software radio to improve power, price, and portability.  In <i> Proceedings
of the 10th ACM Conference on Embedded Networked Sensor Systems</i>,
SenSys &#8217;12, New York, NY, USA, 2012. ACM
</p>

<p style="padding-left: 1em;">
<tt>
<a href="/research/sensys12-sdr.pdf">paper</a>
<a href="/research/sdr2.tar.gz">source</a>
</tt>
</p>

### Powerline Communications (PLC)

My introduction to research as an undergraduate, this work sought to explore the
feasibility of using Powerline Communications (PLC) in a commercial building. In
a home, a PLC deployment is easy as the same line and neutral wires run to every
outlet. This is untrue in a commercial building, which is parcelled off into
electrically isolated regions by transformers.

The work was an exploration of the connectivity graph of the Computer Science
building at the University of Michigan, seeking to characterize it and then
attempt an explanation of the observed characteristics.

<p style="font-size: 75%;">
<b>Pat Pannuto</b> and Prabal Dutta. Exploring powerline networking for the
smart building. In <i>Extending the Internet to Low power and Lossy Networks</i>,
IP+SN &#8217;11, April 2011
</p>

<p style="padding-left: 1em;">
<tt>
<a href="research/ipsn11-plc.pdf">paper</a>
<a href="research/ipsn11-plc-pres.pdf">presentation</a>
<a href="research/paper_ip_sn.tar.gz">source</a>
</tt>
