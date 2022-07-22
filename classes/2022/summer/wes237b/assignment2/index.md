<h1>Assignment 2 - Due date: Aug 7, 2022</h1>

_Now we're really implementing things..._

[TOC]

---

## Part 1: Welcome to PYNQ

This is the first in-lab component.
The goal of this part is to get familiar developing on the PYNQ platform.

### (if needed) Setup your PYNQ

This should already be set from prior work with the PYNQ, but in case you
need a fresh start, follow the [PYNQ getting started](http://www.pynq.io/board.html) guide.

You should be able to ssh into the PYNQ board using `ssh xilinx@192.168.2.99` with password `xilinx`.


### Install a linear algebra library

We'll use [Eigen][eigen], which provides building blocks for efficient
implementations of interesting numerical types and matrix-like objects.

- Download the newest stable release from [the Eigen website][eigen] (3.4.0 as-of this writing).
- Copy this over to your PYNQ (i.e., `scp eigen-3.4.0.zip xilinx@192.168.2.99:`).
- On the PYNQ, unzip and move the `Eigen/` folder to the board's include directory (`/usr/include`).


### Create a working directory for this lab

For each lab and assignment, you will need to setup a similar directory structure.
Here's the structure for this first example.
> NOTE: No directory or filenames should have whitespaces. Ever. (Fragile tools later)

```
mkdir lab_pynq_basics
cd lab_pynq_basics
mkdir src include build
```

`src` will hold C/CPP files, `include` header files, and `build` built objects.


### Let's do a dot product

We'll start with a simple vector multiply example so you can see some of what
Eigen code looks like.

Copy the following files into your project:

- [`include/vecDot.h`](vecDot.h)
- [`include/vecMulTest.h`](vecMulTest.h)
- [`src/vecDot.cxx`](vecDot.cxx)
- [`src/vecMulTest.cxx`](vecMulTest.cxx)

Look over these files quickly to sure you are comfortable with what they're doing.

#### Compile

In your project directory, run:

```
g++ -Iinclude src/vecMulTest.cxx src/vecDot.cxx src/main.cxx -o vectest -llapack -lblas -larmadillo
```

> _What are all those flags?_
>
> `-Iinclude` This tells the compiler where to look for our .h files. This is relative to where `g++` is invoked. Sometimes external libraries provide a different include directory, and you'll need to add them. We can have multiple include directories by adding another `-I..`
>
> `src/vecMulTest.cxx src/vecDot.cxx src/main.cxx` These are our source files.
>
> `-o vectest` Specifies what is our output file. In this case, we end up with an executable file called vectest. We can run the executable using `./vectest`.
>
> `-llapack -lblas -larmadillo` These are library flags.
> For each external library we wish to use, we need to specify a link flag to the compiler.
> Note that the lowercase `-l` says to look for a library with that name.
> There are built-in paths to look for libraries (e.g. `/usr/lib`).
> A capital `-L` (i.e. `-L/some/path`) adds additional paths to look for libraries.


#### A Build System?

That's a rough command to type all the time. We can use `make` to capture the
commands to run, and also to be more intelligent about when to compile (i.e.,
no need to compile a new binary if none of the source files change).

Delete the old executable you built:

```
rm vectest
```

Copy the following files into your project:

- [`Makefile`](Makefile)

Now, to build, just run `make`.

### Part 1: Check your understanding

Add new files, `vecCross.h` and `vecCross.cxx`, that implement a cross product method.
Then add tests to the existing test program that compares your cross product result
to the Eigen library cross product implementation (note: now you must check the equality
of matrices).

_Optimization:_ In embedded systems, it's often better with larger data
operations to pre-allocate a result object and give the function a pointer to
an object to fill rather than returning the object from the function.
Try this for your cross product function.

### Part 1: Report Deliverables

_None._

---

## Part 2: Welcome to OpenCV

This is the second in-lab component.
The goal of this part is to get familiar with OpenCV.

We will learn how to read an image into a matrix using OpenCV and then how to perform a
[Discrete Cosine Transform (DCT)](https://en.wikipedia.org/wiki/Discrete_cosine_transform).

> If you want to dig deeper into the DCT, the optimizations presented here, and beyond [here is a good textbook chapter](http://people.missouristate.edu/jrebaza/assets/10compression.pdf).
> You **do not** need to study this for this class, it is just a resource if you are interested.

This part starts to elide more steps, to get you comfortable with
doing your own configuration of projects, libraries, etc.


### Getting Started

We'll make a new project folder for this part:

```
mkdir dct
cd dct
mkdir src include build
```

Let's start with:

- [src/main.cxx](main.cxx)

Copy the `Makefile` from Part 1 into this project folder.
_What do you need to update for this to build?_

Pick an interesting image to test with and make sure this first part is working.


### Let's not torture ourselves (yet?)

Color images are more complicated to work with since they have 3 different matrices.
For RGB images, they'll have a separate matrix for red, green, and blue.

After you read the image in `main.cxx`, convert it to gray scale:

```
// Convert the image to grayscale
Mat gray;
cvtColor(image, gray, CV_BGR2GRAY);
```

When we perform the DCT, we don't want to have to wait too long for a large image.
For the sake of this lab and the homework, we're going to resize the image.
For larger images, you'll see much different results from the optimizations.
Add this code to resize the image to 64x64 pixels:

```
resize(gray, gray, Size(64, 64));
```

Now we're ready to call the opencv dct function.
First, we'll need to convert the Matrix datatype:

```
// Convert the data type for use with opencv dct function
gray.convertTo(gray, CV_32FC1, 1.0/255.0);
Mat dct_cv;
dct(gray, dct_cv);
imshow("Open CV DCT", dct_cv);
```

> (How did we know to do this? From [the docs][openCVdct], or if you try to pass the wrong type, OpenCV will throw an error).

The resulting image is small because we resized the original image to 64x64.
Like the FFT, the DCT will output the same size array as the input.


### Writing our own DCT

We'll start with some starter code:

- [src/lab_dct.cxx](lab_dct.cxx)

Read through this, understand what it's doing and what it's missing.

Fill in the missing pieces.

In `main.cxx`, add a call to the new naive DCT and compare it to the OpenCV DCT.
The transforms should look the same.


### Optimize using 1D separability

Let's add a new function `lab_dct_1D(Mat input)` to your `lab_dct.cxx`.
This is an optimized approach that takes advantage of the 1D separability of the DCT.

To save you some copy-paste, the 1D function is already at the bottom of
`lab_dct.cxx` file, simply uncomment it (and add a header entry...).

Try swapping out DCT implementations in the top-level `main`.
How does the performance change?
If you omit the resize step, how much more significant is the performance difference?

### Part 2: Report Deliverables

1. Provide a copy of your

    1. Original image
    1. Resized, greyscale image
    1. OpenCV DCT result
    1. Naive DCT result
    1. 1D DCT result

1. Use the `time` command to report how long each of the OpenCV, Naive, and 1D
approaches take to execute (remember to remove the image display / keypress wait!).

---

## Part 3: Matrix Multiplication and Performance

This makes up the first part of the expected homework component.

Now, we want you to start getting more comfortable going from spec to
implementation, as well as looking up documentation from libraries to
find the methods you need.

For this part, you will implement your own matrix multiplication and compare the performance with a built in function from either the Eigen library or the openCV library.
_You will be building the project from scratch. Feel free to copy files or examples from the lab or part 1._


### Implement naive matrix multiplication

Write a matrix multiplication function with the following specifications:

 - The function must take 2 matrices as parameters and output the result as `Mat1 * Mat2 = Result`.
     - _To simplify this some, you may assume the matrices are all square._
 - The result should be stored into a pointer to an already-allocated result matrix given as a function parameter.
 - To get you started with psuedocode, the header file would look like `matrix(Matrix in1, Matrix in2, Matrix* result)`.
 - Your code structure should be clear and well documented.

Lots of loops are fine / expected here :).


### Use a linear algebra library

For Eigen and OpenCV (and feel free to add additional libraries if you're
feeling bold!), figure out how to use them to multiply matrices.

If necessary, create a wrapper function that exposes the same interface as your naive implementation.


### Part 3: Report Deliverables (Performance)

Compare the performance of your function to library implementation.

Use any benchmarks covered from WES237A (please mention PMU) to clearly
describe in what ways each function is better than the others.


---


## Part 4: 2D DCTs

The bulk of the homework portion, you will implement different optimizations for the 2D Discrete Cosine Transform (DCT).

You are provided with a skeleton code with a naive, four-nested-loop implementation of DCT.
This code includes a testbench that you can use for developing your code.
In addition, this template code provides you with timer code that you can use to measure your code's performance in actual time.
You will need to use `perf` to get cycle count metrics.
You have to use the provided source code to implement three optimization techniques.

- [2D DCT Skeleton Code](2d_dct.zip)


### Look Up Table (LUT)

DCT coefficients are constant for N-size transforms.
Given N, it's more efficient to store all the coefficients of the DCT matrices and recall them as opposed to calculating them every loop cycle.
This is called a Look Up Table (LUT).

1. Report the performance and cycle count for an input size of 64 (default), without optimizations.
2. Complete the code for initializing the LUTs with DCT coefficients.
3. Use the LUTs to replace the `cos()` functions in the nested loops and eliminate redundant calculation of the coefficients in each iteration.
4. Also incorporate the scaling inside your LUT, and remove the scaling line in the code.


### Matrix Multiplication (MM)

Assuming an input of same width and height, the DCT transform can be
implemented with Matrix Multiplication (MM) using the following formula:

<tt>DCT = CXC<sup>T</sup></tt>

Where C is the coefficient matrix, and X is your input matrix.
From the previous section, you already have an implementation of naive matrix multiplication for square matrices.

Use your code, and one of the LUTs to apply the formula above.

Note: You can use OpenCV to get the transpose.
Look at the hints in the source code.


### Block Matrix Multiplication (BMM)

To increase the performance of your code for bigger image sizes,
we have to implement DCT using BMM.

1. Increase the size of your input image to 384 (just pass 384 as command-line argument).
2. Report the performance and cycle count for an input size of 384, with naiveMM.
3. Optimize your MM code using blocks.
4. Find the optimal block size for that input size.
5. Report the performance and cycle count for an input size of 384, with BMM.


### Pulling it all together, and some Quality Assurance

You should have 4 algorithms (Naive, Separable (in-lab / Part 2 optimization), Matrix Multiplication, and Block Matrix Multiplication).

All 4 algorithms must have RMSE lower than 0.001.

All 4 algorithms must be able to chose to use LUT for DCT coefficients and scaling.
Command-line arguments or simply `#ifdef`s are fine.


### Part 4: Report Deliverables

1. For each algorithm (Naive, Separable, Matrix Multiplication, Block Matrix Multiplication) with and without LUTs, use `perf` to report on the cycle count, cache misses, and L1 cache.
    - Extra Credit: Report on at least 2 additional metrics from `perf`.
      Explain what these metrics measure and why they are the same/different for each algorithm.

2. For the Separable, MM, and BMM implementations, experiment with various sizes. No need to do so for the Naive implementation as it will take a significant amount of time.
    - You may need to change the `FRAME_NUMBER` to see a noticeable difference in some of the optimizations. Feel free to experiment.



---

## What to Submit

Prepare a report document with answers for each of the `Report Deliverables` above.

In addition, create zipfiles with your code from each part of this lab.
All code should compile if we simply run `make`.


[eigen]: http://eigen.tuxfamily.org/index.php?title=Main_Page
[openCVdct]: https://docs.opencv.org/4.x/d2/de8/group__core__array.html#ga85aad4d668c01fbd64825f589e3696d4
