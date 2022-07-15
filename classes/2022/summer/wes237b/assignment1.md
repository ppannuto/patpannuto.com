# Assignment 1 - Due date: July 24, 2022

_Welcome to WES 237B!_

## Part 1: Welcome to Jetson TX2

This is the in-lab component. The goal of today's lab is to get familiar with the Jetson TX2 platform.

We are going to use [nVidia's official tutorials](https://github.com/dusty-nv/jetson-inference) for this.

The specific, minimum assignment is to get the Object Detection Inference example up and running for
person detection. You may do this either using a prerecorded video file, or if you would like a bit of
a stretch by configuring a remote live stream from your laptop camera to the Jetson board.

If you finish early, try out some of the other examples to get a feel for the capabilities of the Jetson.

**How to Submit:** Demo your object detection for course staff, either live in-lab, or later during
office hours if needed.

## Part 2: Huffman encoder/decoder

Download this [starter code](wes237b-a1-huffman.zip).

Write the functions to do basic Huffman encoder and decoder in `huffman.cpp`.
Use a text file as your input (Note that random input will not benefit from
huffman coding). Your code must work on other text files than the provided
example.

The input of the encoder is the content of the text file, and the output is
Huffman tree and Huffman codes.

The input of the decoder is Huffman tree and Huffman codes from the encoder,
and the output of the decoder is a text file.

The format you choose for the encoder output is not important so long as it is
efficient (compact) and decodes correctly. For example, you can store the
frequency of each character (256 total), or you can store haracter-frequency
pairs (potentially smaller if only compressing text). Provide a brief
explanation of your chosen format in the report.

Modify only the `huffman.cpp` file.
If you really have to modify another file, do minimal modifications and explain
them in your report.


<!--
Work Submission

IMPORTANT: Follow the instructions exactly, and double check your repository, folder, and file names. You may lose points if you do not follow the exact instructions. If you have a doubt or a question, please ask the TAs, preferably on Piazza.

    Each team must have a bitbucket repository, Please make sure your repository follows our policies.
    All of your codes related to assignment 1 must be placed in a folder called Assignment_1 in your repository’s source directory
    You have to submit these:
        A short report named Report.pdf with brief answers to Part 1.1, 1.2, 1.3 and 2.5. This should be at the root of the assignment folder.
        Your Python script from Part 1.4 name convert.py. This should be at the root of the assignment folder.
        The modified iir_filter_ffd file from Part 1.5. This should be at the root of the assignment folder.
        The completed template folder from Part 2. Place the entire folder inside the assignment folder, but remove any generated binary (CODEC, or any files under objs). We must be able to compile and run your code.

Do not submit other files than those listed, unless you have a good reason, and explain so in your report.
-->