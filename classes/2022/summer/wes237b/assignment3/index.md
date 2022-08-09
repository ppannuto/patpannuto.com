<h1>Assignment 3 - Due date: Aug 21, 2022</h1>

_Is all this parallel HW actually worth it?_

[TOC]

---

## Lab: Optimizations, Hardware, and Software

Today, we'll be comparing how performance varies based on software
optimization, hardware acceleration, and hardware platform selection.


### First, some class tools for the Jetson

It should hopefully make life easier to have a familiar, consistent environment
across the two platforms.

#### Install Jupyter Notebook

> Note: Jupyter might already be set up from prior users of the board.

`ssh` into your jetson by `ssh -L 8888:localhost:8888 wes-237b@192.168.55.1` and do the following:

 1. Install Jupyter
     1. `sudo apt-get update`
     1. `sudo apt-get install python3-pip`
     1. `pip3 install --upgrade pip`
     1. `pip3 install jupyter`
     1. `pip3 install jupyterlab`
     1. `pip3 install notebook`
 1. Set up your Jupyter install
     1. `~/.local/bin/jupyter-notebook --generate-config`
     1. Place `jupyter_notebook_config.py` in `~/.jupyter/` directory
 1. Create a working directory
     1. `cd ~/Desktop`
     2. `mkdir jupyter`
     3. `cd jupyter`
 1. Start jupyter notebook
     1. `~/.local/bin/jupyter-notebook`
 1. Navigate to the URL with the token specified in the terminal.  This should be in the form of `http://localhost:8888/?token=<token>`.

#### Install `perf`

> Note: `perf` might already be set up from prior users of the board.

If it isn't, you should be able to just do:

 1. `wget https://developer.nvidia.com/embedded/l4t/r32_release_v7.1/sources/t186/public_sources.tbz2` This may need to be updated depending on the release of Jetpack installed on your board.
 1. `tar -xjf public_sources.tbz2`
 1. `tar -xjf Linux_for_Tegra/source/public/kernel_src.tbz2`
 1. `cd kernel/kernel-4.9/tools/perf`
 1. `make`
 1. `sudo make install`
 1. `perf --version` You may need to disconnect `ssh` and reconnect.


### Background and Resources

Here are some [slides to follow along with][slides] for today's lab.

Work through the slides up through "Compile Neon".


### Getting started with NEON

**Note:**

 - ARMv7 (PYNQ) requires `-mfpu=neon` and `-O1 -ftree-vectorize`
 - ARMv8 (Jetson) requires `-O1 -ftree-vectorize`

Download and complete [`neon.c`](neon.c)

 1. Compile it with: `gcc -mfpu=neon neon.c -o neon`
 1. Run: `./neon`
 1. Modify the code to add `250` to _data_ instead of `3`

Make sure that you can compile and run the NEON code on both platforms.

If you're having difficulty figuring out the right functions to call,
here is my [neon_final.c](neon_final.c). Do try to figure things out on
your own for a bit first, however.

_There is no deliverable for this section._

### Implementing an FIR filter

[Finite Impulse Response (FIR) filters](https://en.wikipedia.org/wiki/Finite_impulse_response)
are one of the most common software filter implementations. This is largely because their
operation aligns really well with hardware parallelism. Basically, a signal comes in over
time, which is shifted along a vector. The filter is a set of (carefully designed) coefficients
in another vector. Each time step, the FIR performs a multiply-accumulate operation (which
in practice is convolution).

The next section in the [lab slides][slides] go over FIR filter operation, or there is also
a video explanation in the [Additional Resources](#additional-resources).

We've set up some starter code for you:

 1. Download [lab3_pynq.zip](lab3_pynq.zip)
 1. Upload `lab3_pynq.zip` to pynq board and unzip it
    1. `unzip lab3_pynq.zip`

You should be able to compile and run the example:

    $ make && ./lab3_fir
    c++ -O0 -std=c++11 -mfpu=neon -Iinclude   src/fir.cpp src/main.cpp -o lab3_fir -lc
    RMSE_naive: 170.16
    RMSE_opt:   170.16
    RMSE_neon:  170.16

The template includes both an `input.txt` input signal and an
already-filtered `golden_output.txt` output signal.
The [Root Mean Square Error (RMSE)](https://en.wikipedia.org/wiki/Root-mean-square_deviation)
estimates how close your filtered signal is to the output.
You will get the RMSE of each implementation down to `0.00`.


#### A naive implementation: `fir()`

Fill out the body of the `fir()` method in `src/fir.cpp`.

Recall that FIR is just a multiply-accumulate operation (a loop) 'slid' across
the input sample (another loop).
This will be short (i.e. my solution is seven lines of code), but the loop
bounds can be a bit tricky: my outer loop is:

    for (int n = 0; n < length-filterLength; n++) {

RMSE_naive should be `0.00` when `fir()` is implemented correctly.


#### Loop Unrolling: `fir_opt()`

Next, we will 'unroll' the inner loop. Recall that loop unrolling is an
optimization that reduces control flow overhead. If a loop will be
executed 4<em>n</em> times, then the inner body of the loop can be replaced
by four copies of itself (careful with the indexes..) and the loop executed
only <em>n</em> times.

Compilers will add extra code to handle the case where a loop is executed
an odd number of times. For simplicity, our `main.cpp` simply ensures that
the loop execution count is divisible by 4 before calling `fir_opt()`.

Implement `fir_opt()`:

 - Manually duplicate the loop body.
 - Increment the inner loop variable by 4 instead of 1.

RMSE_opt should be `0.00` when `fir_opt()` is implemented correctly.


#### Vectorization: `fir_neon()`

Lastly, we will vectorize the inner loop, using NEON intrinsics to compute four
operations in parallel.

[ARM Developer has a nice intrinsics lookup page][intrinsics]. Take advantage
of the filters to help find what you need.

There's a few steps to vectorizing, your loop will now:

 - Load the input data into vector registers.
 - Prepare an output register.
 - Do the actual computation (should be one step!).
 - Extract the result from the vector register.

RMSE_neon should be `0.00` when `fir_neon()` is implemented correctly.


#### Profiling with `gprof`

We are also going to look at a different profiling tool: `gprof`.
Did you notice the `-pg` flag we added to the compile command?
Or have you been wondering where that `gmon.out` file came from?
That is `gprof` in action.

Unlike `perf` or other external tools, `gprof` _modifies the actual
program_. When compiled with `-pg`, the compiler adds instrumentation
to the actual program binary which tracks metrics such as when and how often
functions are called. When your program finishes running (assuming it
doesn't crash..), it writes out the results to a `gmon.out` file.
This means that _there is no separate profiling tool to run for `gprof`_.
This often trips people up. Your (instrumented) program _is_ the profiling
tool!

Now, there is an actual `gprof` program, however all this does is _parse_ the
`gmon.out` file and display the already-collected profiling data in a
human-readable format. Play around with some of the `gprof` options (some
examples are in the [lab slides][slides]; there are many more online).
Can you get a sense of the performance difference across the `fir_XXX()`
implementations? Could you have gleaned this information from `perf`?

> **Caution:** Be sure to delete the `gmon.out` file whenever you change
> configurations.
>
> By default, the file is appended to, such that you could execute a program
> multiple times (or with a suite of inputs) and see performance over the
> average of all of them – not what we want to do here!


### Lab Report Deliverables

 1. On either the PYNQ or Jetson:
   Try compiling with `-O0`, `-O1`, `-O2`, `-O3`, and `-Ofast` (see a description
   of what optimizations these map to in the [gcc documentation][gcc-opts] if you
   are interested). Pick at least three of these optimization levels and use
   `gprof` information to make a table that compares the performance of the
   three `fir_` implementations for each optimization level.

 1. Profiling itself has overhead! Your program is doing more work now...  Try
 compiling with and without the `-pg` flag (any optimization level; your
 choice). Are you able to measure a performance change of the whole `lab3_fir`
 program with profiling on/off?
 Why/why not?
 Think about where profiling overhead comes from given what `gprof` is doing.
 (You can try using `time` for this, `perf` might give more detail)?

 1. Does platform matter? Using the same optimization level, measure and report
 the performance on the other platform.


---


## Assignment: Sobel Filters

In this assignment, you will learn how to implement a
[Sobel filter](https://en.wikipedia.org/wiki/Sobel_operator),
and optimize convolution on an ARM processor.

We have provided you with template starter code:

 - [sobel.zip](sobel.zip)

If you prefer working via Jupyter, you may also find this
display notebook helpful:

 - [display_output.ipynb](display_output.ipynb)

### Part 1: Basic Sobel Algorithm

You have to implement a Sobel filter without using OpenCV functions. We don't
provide an error function for your baseline Sobel implementation, however your
Sobel filter should produce similar visual result compared to the OpenCV Sobel
function.


### Part 2: Optimizations

In the lab component, you learned how to optimize a FIR filter by loop
unrolling and using NEON instructions.  For this part, you have to optimize
your Sobel implementation using similar techniques.

Implement the following optimizations for your Sobel function:

 1. **Loop unrolling:** Your Sobel function, unlike the FIR from the lab, is a convolution on 2D signals.
 The principle of loop unrolling is similar for both functions, and you can use a similar approach
 as from lab here.
 2. **ARM NEON:** Use appropriate ARM NEON instructions to speed up your Sobel code.
 You are free to use any NEON instruction for this task.


### Report Deliverables

 1. Explain (very) briefly how you used NEON intrinsics in your optimized Sobel.

 1. Use your non-optimized basic Sobel algorithm as your baseline.
 Following the same techniques from the lab, provide a comparison between your
 baseline, loop-unrolled, and NEON implementations.  You only need to report
 performance on one platform and one optimization configuration (but tell us
 which one!).

 1. Also compare the performance of your optimized Sobel versus OpenCV's Sobel.

#### Extra Credit

Try a different profiling tool.
Two ideas (you are welcome to find others):

 - [pinpoint](https://github.com/osmhpi/pinpoint) is an _energy_ profiler,
   what can you learn about your implementations' energy efficiency?
 - [`gcov`][gcov-opt] enables finer-grained, line-by-line profiling.
   What extra information can you learn about where overhead sits in your
   implementation?

---

## Mini-Assignment: Introduction to CUDA – Vector Add

This last piece is completely separate, it's just starting to look ahead a bit.

Follow the first two introductory CUDA tutorials:

 - [Tutorial 01](https://cuda-tutorial.readthedocs.io/en/latest/tutorials/tutorial01/)
 - [Tutorial 02](https://cuda-tutorial.readthedocs.io/en/latest/tutorials/tutorial02/)


### Report Deliverables

Answer the following questions in 1 or 2 sentences:

 1. What does the __global__ flag mean?
 2. Explain the following line of code in terms of threads, blocks, and grids:

        foo<<4,32>>(out, in1, in2)



---

## What to Submit

Prepare a report document with answers for each of the `Report Deliverables` above.

In addition, create zipfiles with your code from each part of this assignment.
All code should compile if we simply run `make`.


---

## Additional Resources

 - [Video explaining how FIR operates as a filter.](https://www.youtube.com/watch?v=NvRKtdrssFA)
   This lightly covers some of the signal theory at the beginning and end; if you just want the
   explainer of what calculations the filter needs to do, jump to the 3:00-minute mark.

[slides]: wes237b-su22-LAB-03-parallel_FIR_perf.pdf
[intrinsics]: https://developer.arm.com/architectures/instruction-sets/intrinsics/#f:@navigationhierarchiessimdisa=[Neon]&f:@navigationhierarchiesreturnbasetype=[float]&f:@navigationhierarchieselementbitsize=[32]
[gcc-opts]: https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html
[gcov-opt]: https://gcc.gnu.org/onlinedocs/gcc/Gcov-and-Optimization.html#Gcov-and-Optimization
