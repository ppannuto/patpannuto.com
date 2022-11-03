<div style="text-align:center">

<h1>Wireless and Communication in the Internet of Things</h1>

<h2 style="font-family:monospace">
<a href="index.html">Home</a> |
<a href="syllabus.html">Syllabus</a> |
Agenda |
<a href="labs.html">Labs</a>
</h2>

</div>

<!--
<pre>

Major Landmarks:

Fall Quarter begins             Mon, Sep 19
Instruction begins              Thu, Sep 22 <-- First class Fri
CSE Faculty Retreat             Fri, Oct  7 --or-- Fri Oct 14
Indigenous Peoples' Day         Mon, Oct 10
Pat Travel                      Fri, Oct 28
Pat Travel                      Mon, Nov  7 <maybe Wed Nov 9 too>
Veteran's Day                   Fri, Nov 11
Thanksgiving                    Fri, Nov 25
Instruction ends                Fri, Dec  2
Final Exam?                     ..?..
Fall Quarter ends               Sat, Dec 10



F'22 First Draft Schedule

    M                             W                               F
0   -                             -                               LEC     Intro
1   LEC     Networking Basics     LEC      BT PHY/MAC, BLE        LAB     Wireshark?
2   LEC     BLE, BLE adv's        LEC      BLE Conn's             LAB[!P] BLE p1: Basic BLE + BLE adv sniff?
3   ~~hol~~                       LEC      Wrap BLE, 15.4 [trad]  LAB[!P] BLE p2: Advaced BLE stuff?
4   LEC     15.4, Thread          LEC      15.4, Thread           LAB     154 p1: Raw 15.4 Connections?
5   LEC     Zigbee, Routing       LEC      [new] CoAP, MQTT, etc  LAB[!P] 154 p2: Thread Network? CoAP/MQTT??
6   LEC     WiFi [phy]            LEC      WiFi [mac]             LEC     Wide-Area Intro, LoRa start
7   LAB[!P] LoRa p1: Basic LoRa   LEC[!P?] LoRa, SigFox, etc      ~~hol~~
8   LAB     LoRa p2: chat app??   LEC      Intro Cell, 2g         LEC     3g/4g/5g
9   LAB     ??? cell p1 ???       LEC      Cell Wrap-up           ~~hol~~
10  LAB     ??? cell p2 ???       LEC      Misc: Weirder RF       LEC     Misc: non-RF: VLC, IR, UL...
11  Final exam week

^ no WiFi Lab, small Wifi HW?
^ what other HW?

- HW: Background knowledge check HW?

$branden$ It would be really nice to have a basic 15.4 example that you could build on top of yourself.
For example, it's easy to make an app where you provide a raw buffer of bytes as the advertisement payload. So figuring out what those bytes are can be the challenge.
It would similarly be great to have a base 15.4 example that just sent/received raw bytes.
Although maybe Zephyr itself has some?
https://docs.zephyrproject.org/latest/connectivity/networking/api/ieee802154.html



W'22 Schedule as reference:

        M/W                                     F
1       Networking Fundamentals; topolgies      wireshark something
2       2g/3g/4g                                Pick a country, cell phone plan
3       [Holiday] / LTE-M, NB-IoT               Revise for LP-cell
4       LoRa, SigFox, etc                       Revise for LP-ISM [next time: Helium chat]
5       BLE / BLE Adv                           Basic BLE + sniffing
6       BLE Conn / 15.4 [trad]                  BLE Connections
7       15.4 [trad] / Thread                    OpenThread demo
8       [Holiday] / Zigbee,Routing,Flooding     CoAP on OT
9       WiFi [phy] / WiFi [mac]                 _Maybe: revisit LoRa w/ HW?_, o/w more 15.4
10      VLC, IR, Ultrasonic, Boutique RF        [No class; project time]

</pre>
-->

<script>
/* There is an 11-year-old (!) bug in Webkit where they don't support
 * vertical languages in tables. That's some remarkable hostility to
 * i18n support right there. Just hide the topic column on webkit :/
 *
 * https://bugs.webkit.org/show_bug.cgi?id=65917
 */

document.addEventListener("DOMContentLoaded", function(e) {
  // Get the user-agent string
  let userAgentString = navigator.userAgent;
  // Detect Chrome
  let chromeAgent = userAgentString.indexOf("Chrome") > -1;
  // Detect Safari
  let safariAgent = userAgentString.indexOf("Safari") > -1;
  // Discard Safari since it also matches Chrome
  if ((chromeAgent) && (safariAgent)) safariAgent = false;

  if (safariAgent) {
    console.log("Someone tell Apple to fix i18n bugs");
    let subjs = document.getElementsByClassName("class-subject");
    let subjsStatic = Array.prototype.slice.call(subjs, 0);
    for (let subj of subjsStatic) {
      //subj.style.visibility = "hidden";
      subj.remove();
    }
    let weeks = document.getElementsByClassName("class-week");
    let weeksStatic = Array.prototype.slice.call(weeks, 0);
    for (let week of weeksStatic) {
      //week.style.visibility = "hidden";
      week.remove();
    }
  }
});
</script>

<style>
td.class-week {
  writing-mode: vertical-lr;
  transform: rotate(180deg);
  vertical-align: middle;
  padding: 3px;
}

td.class-subject {
  font-weight: bolder;
  writing-mode: vertical-lr;
  transform: rotate(180deg);
  vertical-align: middle;
  border-style: dotted;
  padding: 3px;
}

.visuallyhidden {
  visibility: hidden;
}

.due {
  color: red;
  font-weight: bolder;
}

.assigned {
  font-weight: bolder;
}

.in-flight {
  font-size: smaller;
  color: grey;
}

.even {
  background-color: #efe;
}
.odd {
  background-color: #cfc;
}

.lab {
  background-color: aliceblue;
}
</style>


<!-- https://alphagov.github.io/table-editor/generic-tables.html -->
<table class="source-tableeditor table table-hover">
<tbody>
<tr>
<th class="class-subject">&nbsp;&nbsp;<!--Subject--></th>
<th class="class-week">&nbsp;&nbsp;<!--Week--></th>
<th colspan="3">When</th>
<th>Where</th>
<th>What</th>
</tr>
<tr>
<td rowspan="4" class="class-subject">Introduction &amp; Networking Basics</td>
<td class="class-week even">Week&nbsp;0</td>
<td>F</td>
<td>Sep 23</td>
<td>
<strong>Assigned:</strong> Homework&nbsp;1
<a href="homework/FA22_WxIoT-HW1.docx">[docx]</a>
<a href="homework/FA22_WxIoT-HW1.pdf">[pdf]</a>
</td>
<td>2154</td>
<td>
<strong>Welcome &amp; Intro</strong>
<a href="lectures/FA22_WxIoT-01-intro.pptx">[pptx]</a>
<a href="lectures/FA22_WxIoT-01-intro.pdf">[pdf]</a>
<ul>
<li>Course overview</li>
<li>Introduction the IoT</li>
<li>Introduction to wireless communication</li>
</ul>
</td>
</tr>
<tr>
<td rowspan="3" class="class-week odd">Week&nbsp;1</td>
<td>M</td>
<td>Sep 26</td>
<td>
<strong>Assigned:</strong> Pre-Lab&nbsp;1
<br/>
<br/>
<span class="in-flight">
Still Active:
<ul>
<li>Homework&nbsp;1</li>
</ul>
</span>
</td>
<td>2154</td>
<td>
<strong>Networking Basics</strong>
<a href="lectures/FA22_WxIoT-02_03-networking_wireless.pptx">[pptx]</a>
<a href="lectures/FA22_WxIoT-02_03-networking_wireless.pdf">[pdf]</a>
<ul>
<li>OSI layer model</li>
<li>IP and routing basics</li>
<li>Data link layer</li>
</ul>
</td>
</tr>
<tr>
<td>W</td>
<td>Sep 28</td>
<td>
<span class="in-flight">
Still Active:
<ul>
<li>Homework&nbsp;1</li>
<li>Pre-Lab&nbsp;1</li>
</ul>
</span>
</td>
<td>2154</td>
<td>
<strong>Wireless basics</strong>
<a href="lectures/FA22_WxIoT-02_03-networking_wireless.pptx">[pptx]</a>
<a href="lectures/FA22_WxIoT-02_03-networking_wireless.pdf">[pdf]</a>
<ul>
<li>PHY layer</li>
<li>How PHY impacts Data impacts Network impacts...</li>
<li>Medium Access Control</li>
</ul>
</tr>
<tr>
<td>F</td>
<td>Sep 30</td>
<td>
<span class="due">Due: </span>Homework&nbsp;1
<br/>
<span class="due">Due: </span>Pre-Lab&nbsp;1
<br/>
<br/>
<span class="assigned">Assigned:</span> Post-Lab&nbsp;1
</td>
<td class="lab">3219</td>
<td class="lab">
<strong>Lab: Wireshark</strong><br />
<em>Outcomes&ndash;</em> After this lab you should understand:
<ul>
<li>What is &ldquo;sniffing&rdquo; and how to do it?</li>
<li>How to find specific traffic you generate?</li>
<li>How to identify layers in a captured packet?</li>
<li>How to infer information about unknown traffic?</li>
</ul>
</td>
</tr>
<tr>
<td rowspan="6" class="class-subject">Bluetooth</td>
<td rowspan="3" class="class-week even">Week&nbsp;2</td>
<td>M</td>
<td>Oct 3</td>
<td>
<span class="assigned">Assigned: </span>Pre-Lab&nbsp;2
<br />
<br />
<span class="in-flight">
Still Active:
<ul>
<li>Post-Lab&nbsp;1</li>
</ul>
</span>
</td>
<td>2154</td>
<td>
<strong>Bluetooth/BLE, PHY, MAC</strong>
<a href="lectures/FA22_WxIoT-04-BLE.pptx">[pptx]</a>
<a href="lectures/FA22_WxIoT-04-BLE.pdf">[pdf]</a>
<ul>
<li>BLE Background</li>
<li>BLE Layers</li>
<ul>
<li>Physical Layer</li>
<li>Link Layer</li>
</ul>
<li>BLE Roles</li>
<ul>
<li>Advertising</li>
<li>Scanning</li>
</ul>
</ul>
</td>
</tr>
<tr>
<td>W</td>
<td>Oct 5</td>
<td>
<span class="in-flight">
Still Active:
<ul>
<li>Post-Lab&nbsp;1</li>
<li>Pre-Lab&nbsp;2</li>
</ul>
</span>
</td>
<td>2154</td>
<td>
<strong>BLE, BLE adv's</strong>
<a href="lectures/FA22_WxIoT-05-BLE-adv.pptx">[pptx]</a>
<a href="lectures/FA22_WxIoT-05-BLE-adv.pdf">[pdf]</a>
<ul>
<li>Communicating with Advertisements</li>
<ul>
<li>Advertisement Use Cases</li>
<li>Energy Use</li>
<li>Packet Collisions</li>
</ul>
</td>
</tr>
<tr>
<td>F</td>
<td>Oct 7</td>
<td>
<span class="due">Due: </span>Post-Lab&nbsp;1
<br />
<span class="due">Due: </span>Pre-Lab&nbsp;2
</td>
<td class="lab">3219</td>
<td class="lab">
<strong>Lab: BLE Advertisements</strong><br />
<em>Outcomes&ndash;</em> After this lab you should understand:
<ul>
<li>How to generate and control contents of advertisement packets?</li>
<li>How to deconstruct a captured advertisement packet?</li>
<li>How the capabilities of different BLE sniffers vary, and the significance of those limitations?</li>
<li>How much BLE traffic is in your environment, and how to figure out what (some of it at least..) is?</li>
</ul>
</td>
</tr>
<tr>
<td rowspan="3" class="class-week odd">Week&nbsp;3</td>
<td>M</td>
<td>Oct 10</td>
<td></td>
<td>2154</td>
<td>
<strong>BLE Connections</strong>
<a href="lectures/FA22_WxIoT-06-BLE-connections.pptx">[pptx]</a>
<a href="lectures/FA22_WxIoT-06-BLE-connections.pdf">[pdf]</a>
<ul>
<li>Connection PHY and Link Layer</li>
<li>Connections as Networks</li>
<li>GATT</li>
<li>BLE 5</li>
</ul>
</td>
</tr>
<tr>
<td>W</td>
<td>Oct 12</td>
<td></td>
<td>2154</td>
<td>
<strong>Wrapup BLE</strong><br/>
<br/>
(Start 15.4 if leftover time)
</td>
</tr>
<tr>
<td>F</td>
<td>Oct 14 <span class="visuallyhidden">!P</span></td>
<td><strong>Assigned:</strong> Post-Lab&nbsp;2</td>
<td class="lab">3219</td>
<td class="lab">
<strong>Lab: BLE Connections</strong><br />
<em>Outcomes&ndash;</em> After this lab you should understand:
<ul>
<li>What are GATT Profiles and how do they &ldquo;define&rdquo; devices?</li>
<li>What does pairing actually do, and what differs between various paring modes?</li>
<li>Why is sniffing connections harder than advertisements?</li>
</ul>
</td>
</tr>
<tr>
<td rowspan="6" class="class-subject">802.15.4</td>
<td rowspan="3" class="class-week even">Week&nbsp;4</td>
<td>M</td>
<td>Oct 17</td>
<td>
<strong>Assigned: </strong>Pre-Lab&nbsp;3
<br/>
<span class="in-flight">
Still Active:
<ul>
<li>Post-Lab&nbsp;2</li>
</ul>
</span>
</td>
<td>2154</td>
<td>
<strong>IEEE 802.15.4</strong>
<a href="lectures/FA22_WxIoT-08-ieee802154.pptx">[pptx]</a>
<a href="lectures/FA22_WxIoT-08-ieee802154.pdf">[pdf]</a>
<ul>
<li>Overview</li>
<li>Physical Layer</li>
<li>(Maybe): Link Layer</li>
</ul>
</td>
</tr>
<tr>
<td>W</td>
<td>Oct 19</td>
<td>
<span class="in-flight">
Still Active:
<ul>
<li>Post-Lab&nbsp;2</li>
<li>Pre-Lab&nbsp;3</li>
</ul>
</span>
</td>
<td>2154</td>
<td>
<strong>IEEE 802.15.4</strong>
<a href="lectures/FA22_WxIoT-08-ieee802154.pptx">[pptx]</a>
<a href="lectures/FA22_WxIoT-08-ieee802154.pdf">[pdf]</a>
<ul>
<li>Link Layer</li>
<li>Packet Structure</li>
<li>(Maybe): Intro Thread</li>
</ul>
</td>
</tr>
<tr>
<td>F</td>
<td>Oct 21</td>
<td>
<span class="due">Due: </span>Post-Lab&nbsp;2
<br />
<span class="due">Due: </span>Pre-Lab&nbsp;3
</td>
<td class="lab">3219</td>
<td class="lab">Lab: 15.4 <!--Raw Conn's?--></td>
</tr>
<tr>
<td rowspan="3" class="class-week odd">Week&nbsp;5</td>
<td>M</td>
<td>Oct 24</td>
<td></td>
<td>2154</td>
<td>
<strong>Thread</strong>
<a href="lectures/FA22_WxIoT-10-Thread.pptx">[pptx]</a>
<a href="lectures/FA22_WxIoT-10-Thread.pdf">[pdf]</a>
<ul>
<li>Mesh Refresher</li>
<li>Thread</li>
<ul>
<li>Overview</li>
<li>Addressing</li>
<li>Runtime Behavior</li>
</ul>
</ul>
</td>
</tr>
<tr>
<td>W</td>
<td>Oct 26</td>
<td></td>
<td>2154</td>
<td>
<ul>
<li>(Finish Thread)</li>
<ul>
<li>Last bit of Addressing</li>
<li>Runtime Behavior</li>
</ul>
</ul>
<strong>Routing</strong>
<a href="lectures/FA22_WxIoT-11-RoutingFlooding_BonusZigbee.pptx">[pptx]</a>
<a href="lectures/FA22_WxIoT-11-RoutingFlooding_BonusZigbee.pdf">[pdf]</a>
<ul>
<li>WSN Routing</li>
<ul>
<li>Simple Routing</li>
<li>Mesh Routing</li>
<li>Efficient Flooding (Synchronous Transmissions)</li>
</ul>
<li>Bonus Slides on Zigbee (Not Presented)</li>
<ul>
<li>Overview</li>
<li>PHY/MAC</li>
<li>Application Layer</li>
<li>Interoperability</li>
</ul>
</ul>
</td>
</tr>
<tr>
<td>F</td>
<td>Oct 28 <span class="visuallyhidden">!P</span></td>
<td><strong>Assigned: </strong>Post-Lab&nbsp;3</td>
<td class="lab">3219</td>
<td class="lab">Lab: 15.4 <!--Thread? CoAP MQTT?--></td>
</tr>
<tr>
<td rowspan="6" class="class-subject">WiFi</td>
<td rowspan="3" class="class-week even">Week&nbsp;6</td>
<td>M</td>
<td>Oct 31</td>
<td>
<strong>Assigned: </strong>Pre-Lab&nbsp;4
<br/>
<br/>
<span class="in-flight">
Still Active:
<ul>
<li>Post-Lab&nbsp;3</li>
</ul>
</span>
</td>
<td>2154</td>
<td>
<strong>WiFi (PHY)</strong>
<a href="lectures/FA22_WxIoT-12-PrettyPHYForAWiFi.pptx">[pptx]</a>
<a href="lectures/FA22_WxIoT-12-PrettyPHYForAWiFi.pdf">[pdf]</a>
<ul>
<li>WiFi Overview</li>
<li>WiFi PHY</li>
<ul>
<li>802.11/802.11b</li>
<li>802.11a/802.11g</li>
<li>802.11n/802.11ac</li>
<li>“WiFi 6” (ax)</li>
<li>“WiFi 7” (be?)</li>
<li>Read-World WiFi</li>
</ul>
</ul>
</td>
</tr>
<tr>
<td>W</td>
<td>Nov 2</td>
<td>
<span class="in-flight">
Still Active:
<ul>
<li>Post-Lab&nbsp;3</li>
<li>Pre-Lab&nbsp;4</li>
</ul>
</span>
</td>
<td>2154</td>
<td>
<ul>
<li>(finish):</li>
<ul>
<li>“WiFi 6” (ax)</li>
<li>“WiFi 7” (be?)</li>
<li>Read-World WiFi</li>
</ul>
</ul>
<strong>WiFi (MAC)</strong>
<a href="lectures/FA22_WxIoT-13-WiFiReturnOfTheMAC.pptx">[pptx]</a>
<a href="lectures/FA22_WxIoT-13-WiFiReturnOfTheMAC.pdf">[pdf]</a>
<ul>
<li>802.11 Access Control</li>
<li>802.11 Frame Format</li>
<li>802.11e Improvements</li>
<li>Microcontrollers &amp; WiFi</li>
</ul>
</td>
</tr>
<tr>
<td>F</td>
<td>Nov 4</td>
<td>
<span class="due">Due: </span>Post-Lab&nbsp;3
<br/>
<br/>
<span class="in-flight">
Still Active:
<ul>
<li>Pre-Lab&nbsp;4</li>
</ul>
</span>
</td>
<td>2154</td>
<td>
<!--
Advanced WiFi
more WiFi ?? Energy Analysis / Performance -->
<strong>(Catchup Day)</strong>
<ul>
<li>Finish WiFi</li>
<ul>
<li>802.11e Improvements</li>
<li>Microcontrollers &amp; WiFi</li>
</ul>
<li>(Back to Week 5...)</li>
<ul>
<li>Synchronous Transmissions</li>
</ul>
</ul>
</td>
</tr>
<tr>
<td rowspan="3" class="class-week odd">Week&nbsp;7</td>
<td>M</td>
<td>Nov 7 <span class="visuallyhidden">!P</span></td>
<td>
<span class="due">Due: </span>Pre-Lab&nbsp;4
</td>
<td class="lab">3219</td>
<td class="lab">Lab: WiFi</td>
</tr>
<tr>
<td>W</td>
<td>Nov 9 <span class="visuallyhidden">?P</span></td>
<td><strong>Assigned: </strong>Post-Lab&nbsp;4</td>
<td class="lab">3219</td>
<td class="lab">Lab: WiFi</td>
</tr>
<tr>
<td>F</td>
<td>Nov 11</td>
<td>
<span class="in-flight">
Still Active:
<ul>
<li>Post-Lab&nbsp;4</li>
</ul>
</span>
</td>
<td colspan="2">~holiday~</td>
</tr>
<tr>
<td rowspan="4" class="class-subject">LP-WANs</td>
<td rowspan="3" class="class-week even">Week&nbsp;8</td>
<td>M</td>
<td>Nov 14</td>
<td>
<strong>Assigned: </strong>Pre-Lab&nbsp;5
<br/>
<br/>
<span class="in-flight">
Still Active:
<ul>
<li>Post-Lab&nbsp;4</li>
</ul>
</span>
</td>
<td>2154</td>
<td>Wide-Area Intro</td>
</tr>
<tr>
<td>W</td>
<td>Nov 16</td>
<td>
<span class="in-flight">
Still Active:
<ul>
<!-- Give slightly extra Lab 4 writeup time b/c holiday -->
<li>Post-Lab&nbsp;4</li>
<li>Pre-Lab&nbsp;5</li>
</ul>
</span>
</td>
<td>2154</td>
<td>LoRa, SigFox, etc</td>
</tr>
<tr>
<td>F</td>
<td>Nov 18</td>
<td>
<span class="due">Due: </span>Post-Lab&nbsp;4
<br/>
<span class="due">Due: </span>Pre-Lab&nbsp;5
</td>
<td class="lab">3219</td>
<td class="lab">Lab: LoRa <!--(Basic LoRa?)--></td>
</tr>
<tr>
<td rowspan="3" class="class-week odd">Week&nbsp;9</td>
<td>M</td>
<td>Nov 21</td>
<td>
<strong>Assigned: </strong>Post-Lab 5
</td>
<td class="lab">3219</td>
<td class="lab">Lab: LoRa <!--(chat app?)--></td>
</tr>
<tr>
<td rowspan="4" class="class-subject">Cellular</td>
<td>W</td>
<td>Nov 23</td>
<td>
<strong>Assigned: </strong>Homework&nbsp;2
<br/>
<br/>
<span class="in-flight">
Still Active:
<ul>
<li>Post-Lab&nbsp;5</li>
</ul>
</span>
</td>
<td>2154</td>
<td>Intro cell, 2g <!--[expect low attendance]--></td>
</tr>
<tr>
<td>F</td>
<td>Nov 25</td>
<td>
<span class="in-flight">
Still Active:
<ul>
<li>Post-Lab&nbsp;5</li>
<li>Homework&nbsp;2</li>
</ul>
</span>
</td>
<td colspan="2">~holiday~</td>
</tr>
<tr>
<td rowspan="3" class="class-week even">Week&nbsp;10</td>
<td>M</td>
<td>Nov 28</td>
<td>
<span class="due">Due: </span>Post-Lab&nbsp;5
<br/>
<br/>
<span class="in-flight">
Still Active:
<ul>
<li>Homework&nbsp;2</li>
</ul>
</span>
</td>
<td>2154</td>
<td>3g/4g/5g</td>
</tr>
<tr>
<td>W</td>
<td>Nov 30</td>
<td>
<span class="due">Due: </span>Homework&nbsp;2
<br/>
<br/>
<!--<strong>Assigned: </strong>Final Design Project-->
</td>
<td>2154</td>
<td>Cell Wrap-Up</td>
</tr>
<tr>
<td class="class-subject">Grab Bag</td>
<td>F</td>
<td>Dec 1</td>
<td>
<!--
<span class="in-flight">
Still Active:
<ul>
<li>Final Design Project</li>
</ul>
</span>
-->
</td>
<td>2154</td>
<td>Misc: werider RF, non-RF stuff</td>
</tr>
<!--
<tr>
<td class="class-subject">Final</td>
<td class="class-week odd">Week&nbsp;11</td>
<td colspan="2"><i>Final Exam Week</i></td>
<td colspan="3">
<span class="due">Due: </span>Final Design Project
<ul>
<li>Preferred Deadline: 14:30 US/Pacific (2:30PM) on Monday, Dec 5</li>
<li><span class="due">Hard Deadline:</span> <strong>20:00 US/Pacific (8PM) on Wednesday, Dec 7</strong></li>
</ul>

<p>
The registrar has assigned this course a final exam period of Monday, December 5 from 11:30-14:30.
We will not have an in-person final, rather we encourage you to use this time to complete your
final design project.
</p>

<p>
As we recognize that everyone has a unique and different exam schedule, we
will allow you through Wednesday evening to submit with no late penalty.
</p>

<p>
These deadlines aim to balance flexibility for you and sufficient time to grade
for us.
</p>

<p>
No late submissions will be accepted after the Hard Deadline.
</p>
<br/><br/>
</td>
</tr>
-->
</tbody>
</table>

<!-- FI 	12/05/2022 	M 	11:30a-2:29p 	TBA 	TBA 	-->


<!--
<table class="table table-bordered table-hover">
  <tr class="table-primary">
    <th>Date</th>
    <th>Topic</th>
    <th>Assignment / Additional Materials</th>
  </tr>

  <tr class="table-info">
    <td colspan="4">Week 0: Introduction, Motivation, and Background</td>
  </tr>
  <tr>
    <td>Jan&nbsp;3<br/><a href="#">[slides]</a><a href="#">[pdf]</a></td>
    <td>
    <ul>
      <li>What's IoT?</li>
      <li>What's &ldquo;low-power&rdquo;?</li>
    </ul>
    </td>
    <td></td>
  </tr>

  <tr class="table-info">
    <td colspan="4">Week 0: Introduction, Motivation, and Background</td>
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
    <td>Jan&nbsp;17</td>
    <td colspan="2"><i>No class, MLK Holiday</i></td>
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
  <tr class="table-warning">
    <td>Feb&nbsp;18</td>
    <td>
    Trying out Thread
    </td>
    <td>
    <p>
    For today, we are going to try to follow the <a href="https://openthread.io/codelabs/openthread-hardware#0">official OpenThread lab</a>.
    </p>
    <p><small>
    Work in groups of (at least) three to see if you can get a Thread network running across your devices.
    It's quite possible that we will end up with one large Thread network at the end of the lab, that
    would be a success too :).
    Nothing to write-up or turn in today, but do want to have Thread basics working so that we can use
    your Thread network(s) to communicate higher-level application data next week.
    </small></p>
    </td>
  </tr>
  <tr>
    <td>Feb&nbsp;21</td>
    <td colspan="2"><i>No class, Presidents' Day Holiday</i></td>
  </tr>
  <tr>
    <td>Feb&nbsp;23<br/><a href="WI22_cse291-14-Zigbee_Routing_Flooding.pptx">[slides]</a><a href="WI22_cse291-14-Zigbee_Routing_Flooding.pdf">[pdf]</a></td>
    <td>
    Zigbee<br/>
    Mesh Routing<br/>
    Mesh Flooding
    </td>
    <td>
    Additional Resources:
    <small>
    <ul>
      <li>Kim, Hyung-Sin, et al. <a href="https://rise.cs.berkeley.edu/wp-content/uploads/2019/06/KIM_LAYOUT.pdf"><i>Thread/OpenThread: A Compromise in Low-Power Wireless Multihop Network Architecture for the Internet of Things.</i></a> IEEE Communications 2019.</li>
      <li>Dutta, Prabal, et al. <a href="https://web.eecs.umich.edu/~prabal/pubs/papers/dutta12amac.pdf"><i>A-MAC: A Versatile and Efficient Receiver-Initiated Link Layer for Low-Power Wireless.</i></a> TOSN 2012.</li>
      <li>Ferrai, Federico, et al. <a href="https://ieeexplore.ieee.org/abstract/document/5779066"><i>Efficient network flooding and time synchronization with Glossy.</i></a> IPSN 2011.</li>
      <li>Ferrai, Federico, et al. <a href="https://dl.acm.org/doi/abs/10.1145/2426656.2426658"><i>Low-power wireless bus.</i></a> SenSys 2012.</li>
    </small>
    </td>
  </tr>
  <tr class="table-warning">
    <td>Feb&nbsp;25</td>
    <td>
    CoAP and End-to-End Operation
    </td>
    <td>
    <ul>
      <li><a href="WI22_Lab8_BigHappyThreadFamily.docx">Lab Worksheet [docx]</a> <a href="WI22_Lab8_BigHappyThreadFamily.pdf">[pdf]</a></li>
    </ul>
    </td>
  </tr>
  <tr>
    <td>Feb&nbsp;28<br/><a href="WI22_cse291-15-PrettyPHYForAWiFi.pptx">[slides]</a><a href="WI22_cse291-15-PrettyPHYForAWiFi.pdf">[pdf]</a></td>
    <td>WiFi [PHY]</td>
  </tr>
  <tr>
    <td>Mar&nbsp;2<br/><a href="WI22_cse291-16-WiFiReturnOfTheMAC.pptx">[slides]</a><a href="WI22_cse291-16-WiFiReturnOfTheMAC.pdf">[pdf]</a></td>
    <td>WiFi [MAC]</td>
  </tr>
  <tr class="table-warning">
    <td>Mar&nbsp;4</td>
    <td>
    <small><del>Cancelled due to weather.</del></small>
    </td>
    <td>
    </td>
  </tr>
  <tr>
    <td>Mar&nbsp;7<br/><a href="WI22_cse291-17-WeirderRFStuff.pptx">[slides]</a><a href="WI22_cse291-17-WeirderRFStuff.pdf">[pdf]</a></td>
    <td>Boutique RF: Backscatter, Wakeup Radios</td>
    <td>
    Additional Resources:
    <small>
    <ul>
      <li>Buettner, Michael et al. <a href="https://dl.acm.org/doi/abs/10.1145/1460412.1460468"><i>RFID Sensor Networks with the Intel WISP.</i></a> SenSys 2008.</li>
      <li>Zhang, Hong et al. <a href="https://web.cs.umass.edu/publication/details.php?id=2114"><i>Moo: A Batteryless Computational RFID and Sensing Platform.</i></a> UMass Tech Report, 2011.</li>
      <li>Van Huynh, Nguyen et al. <a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8368232"><i>Ambient Backscatter Communications: A Contemporary Survey.</i></a> IEEE Communications Surveys &amp; Tutorials 2018.</li>
      <li>Liu, Vincent et al. <a href="https://dl.acm.org/doi/abs/10.1145/2534169.2486015"><i>Ambient Backscatter: Wireless Communication out of Thin Air.</i></a> SIGCOMM 2013.</li>
      <li>Iyer, Vikram et al. <a href="https://dl.acm.org/doi/abs/10.1145/2934872.2934894"><i>Inter-Technology Backscatter: Towards Internet Connectivity for Implanted Devices.</i></a> SIGCOMM 2016.</li>
      <li>Pannuto, Pat et al. <a href="https://ieeexplore.ieee.org/abstract/document/8480075"><i>Slocalization: Sub-µW Ultra Wideband Backscatter Localization.</i></a> IPSN 2018.</li>
    </small>
    </td>
  </tr>
  <tr>
    <td>Mar&nbsp;9</td>
    <td>VLC, IR, Ultrasonic</td>
  </tr>
  <tr class="table-warning">
    <td>Mar&nbsp;11</td>
    <td colspan="2"><i>No lab, finish your class projects!</i></td>
  </tr>
  <tr class="table-success">
    <td colspan="4">Finals Week</td>
  </tr>
  <tr>
    <td>
    <p>Mar&nbsp;14</p>
    <p><em>3&ndash;6&nbsp;PM</em></p>
    </td>
    <td>Final Presentations</td>
    <td>
    <p>See presentation details below.</p>
    </td>
  </tr>

</table>
-->
