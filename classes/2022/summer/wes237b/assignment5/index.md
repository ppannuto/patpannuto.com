<h1>Assignment 5 - Due date: Sep 18, 2022</h1>

<!-- n.b. Grades Due Sep 21 -->
<h3><a href="#revised-deadlines" style="color:red"><strong>Warning: Limited Late Submission Deadline</strong></a></h3>

_Let's learn some stuff with these machines._

[TOC]

---

## Pre-Lab / Motivation

As some quick inspiration, let's check out what machine learning can do and how
easy modern frameworks make things. We'll use tensorflow to do some digit
recognition on the MNIST dataset.

**Note: This section should be turnkey. It should not take more than ten minutes.**

### Setup: Install Tensorflow

First, we'll need to get TensorFlow on the Jetson:

    $ sudo apt-get install libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev liblapack-dev libblas-dev gfortran
    $ sudo apt-get install python3-pip
    $ sudo pip3 install -U pip
    $ sudo pip3 install -U pip testresources setuptools numpy==1.16.1 future==0.17.1 mock==3.0.5 h5py==2.9.0 keras_preprocessing==1.0.5 keras_applications==1.0.8 gast==0.2.2 futures protobuf pybind11

    $ sudo pip3 install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v44 tensorflow==2.3.1+nv20.12

Now, download an example implementation:

 - Tensorflow MNIST example: [`tf_mnist_example.py`](tf_mnist_example.py)

You should be able to simply run this example:

    $ python3 tf_mnist_example.py

Note, you will need network access when this first runs as it will download the mnist dataset.

<details markdown="1">
<summary>[Click to show] Example output on my (desktop) machine:</summary>

    Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz
    11490434/11490434 [==============================] - 1s 0us/step
    2022-08-12 16:06:49.795378: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
    To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
    predictions:
     [[-0.03353167 -0.5992441   0.2775088   0.14995925  0.17868416  0.01251442
       0.4154998   0.60322917 -0.10094208  0.58693767]]
    loss:
     2.4931512
    Epoch 1/5
    1875/1875 [==============================] - 2s 1ms/step - loss: 0.2945 - accuracy: 0.9155
    Epoch 2/5
    1875/1875 [==============================] - 2s 994us/step - loss: 0.1467 - accuracy: 0.9561
    Epoch 3/5
    1875/1875 [==============================] - 2s 1ms/step - loss: 0.1081 - accuracy: 0.9675
    Epoch 4/5
    1875/1875 [==============================] - 2s 1ms/step - loss: 0.0891 - accuracy: 0.9728
    Epoch 5/5
    1875/1875 [==============================] - 2s 1ms/step - loss: 0.0748 - accuracy: 0.9766
    evaluation:
    
    313/313 - 0s - loss: 0.0766 - accuracy: 0.9772 - 329ms/epoch - 1ms/step
    probabilities:
     tf.Tensor(
    [[6.53528831e-09 2.37911912e-08 4.16913781e-06 1.98437585e-04
      7.76625916e-11 7.91134312e-07 3.66218117e-14 9.99787271e-01
      7.81279994e-07 8.51235291e-06]
     [3.38839108e-08 8.20917267e-05 9.99850750e-01 6.63965839e-05
      3.00753109e-15 2.05818758e-08 8.88171758e-09 1.48753731e-13
      7.58559167e-07 5.27852256e-15]
     [3.27495087e-07 9.98672843e-01 4.06497478e-04 4.13860362e-05
      7.93615618e-05 2.90710591e-06 1.48753126e-04 4.13178146e-04
      2.34751133e-04 1.46073873e-07]
     [9.99955297e-01 1.89552551e-09 6.28136468e-06 6.67276296e-08
      2.16106105e-06 1.12490295e-06 2.45637898e-06 1.76818630e-05
      3.60193830e-08 1.50214664e-05]
     [3.01178479e-05 2.94772473e-08 1.41985929e-05 1.06495186e-07
      9.93193209e-01 7.19620357e-06 2.56260387e-06 1.51762669e-03
      1.54244553e-05 5.21953963e-03]], shape=(5, 10), dtype=float32)
</details>

<br />

Take a quick peek inside the <tt>tf_mnist_example.py</tt> file and see if you can get a
sense of what it's doing.

For the rest of lab, we're going to implement a (tiny corner) of what tensorflow
does for you.



## Lab: Learning a Circuit

Today, we'll be looking into how (performant) machine learning is implemented.

A lot of work for a simple network, we are going to teach a computer to learn how to implement an AND gate :).


### Background and Resources

Here are [intro slides for today's lab][slides].

Here is the [lab workbook][workbook].
The beginning of the workbook is an explainer of all of the key concepts to implement Batch gradient descent.
Read through this lightly once, it's a bit dense.
Once you get to the _Implementation_ section, we start filling in code.
You'll probably need to re-read the relevant sections of the workbook once you start trying to implement each function.



### Building a neural network

First, download the starter code:

 - [`lab5.zip`](lab5.zip)

We dropped a fair amount of starter code on you.
Take a moment to read through everything to get a sense of what this code is trying to do.
By the time we're all done, you'll have implemented:

    sigmoid_activation.cu::sigmoidActivationForward()
    sigmoid_activation.cu::sigmoidActivationBackprop()
    mse_cost.cu::meanSquaredErrorCost()
    mse_cost.cu::dMeanSquaredErrorCost()
    linear_layer.cu::linearLayerForward()
    linear_layer.cu::linearLayerBackprop()
    linear_layer.cu::linearLayerUpdateWeights()
    linear_layer.cu::linearLayerUpdateBias()

    main.cu:: // TODO network structure
        nn.addLayer(...);
        nn.addLayer(...);
        nn.addLayer(...);
        nn.addLayer(...);


#### `mse_cost.cu`

The first thing we'll implement is cost functions.
We'll need both the cost and the derivative of the cost.

Both functions will start by computing an `index` into input matrices.
Nothing special here, same index you've been doing for a while with CUDA:

    int index = blockIdx.x * blockDim.x + threadIdx.x;

You also need to handle when input dimensions don't match hardware structure.
That is, sometimes the index will be invalid, so you'll want to wrap everything:

    if (index < size) {
        ...
    }

After that, the functions differ.

For cost, you'll want to first compute the partial cost at this particular `index`.
Then add that (mind the hint in the source!) to the single, shared, global total `cost`.

The derivative is simpler as it's element-wise, with a result in each `eA[index]`.

<details>
<summary>Solution</summary>

<pre>
__global__ void meanSquaredErrorCost(float* predictions, float* target, const int size, float* cost)
{
	int index = blockIdx.x * blockDim.x + threadIdx.x;

	if (index < size) 
	{
		float partial_cost = powf((predictions[index] - target[index]), 2.0f);
		atomicAdd(cost, partial_cost/size);
	}
}

__global__ void dMeanSquaredErrorCost(float* predictions, float* target, float* eA, const int size)
{
	int index = blockIdx.x * blockDim.x + threadIdx.x;

	if (index < size) 
	{
		eA[index] = 2.0f * (predictions[index] - target[index]);
	}
}
</pre>

</details>


#### `sigmoid_activation.cu`

Next up is the activation function.
We'll need this to go both forward (inference) and backwards (training feedback).

The structure of these methods will look a lot like your MSE methods (though, when is `index` valid now?).
The forward path is quite direct, you simply need to compute the `sigmoid` (this function is given already) for each `input`.
Back-propagation requires a bit more work, but can still be a one-liner.

<details>
<summary>Solution</summary>

<pre>
__global__ void sigmoidActivationForward(float* input, float* output, const int input_rows, const int input_cols)
{
	int index = blockIdx.x * blockDim.x + threadIdx.x;

	if (index < input_rows * input_cols)
	{
		output[index] = sigmoid(input[index]);
	}
}

__global__ void sigmoidActivationBackprop(float* input, float* errorFromLayerBelow, float* errorToLayerAbove, const int input_rows, const int input_cols)
{
	int index = blockIdx.x * blockDim.x + threadIdx.x;

	if (index < input_rows * input_cols)
	{
		errorToLayerAbove[index] = errorFromLayerBelow[index] * sigmoid(input[index]) * (1.0f - sigmoid(input[index]));
	}
}
</pre>

</details>


#### `linear_layer.cu`

Here's the most code we'll be writing.
We'll need to implement all the methods that make a linear layer work.

Start by computing the forward path:

- Ultimately, you're multiplying `W` by `input`.
- First, then, you'll need `row` and `col` indices; this will use an approach similar to the `index`es above.
- What are the output dimensions? It's easier to think about what's happening if you have some extra variables:

        // No math needed to compute these.. just some reasoning.
        int output_rows = ... ;
        int output_cols = ... ;

- You'll also need to guard computation based on dimensions.
- Finally, you'll need one loop.

<details>
<summary>Solution</summary>

<pre>
__global__ void linearLayerForward(float *W, float* input, float* output, float* b,
									const int W_rows, const int W_cols,
									const int input_rows, const int input_cols) 
{
	int row = blockIdx.y * blockDim.y + threadIdx.y;
	int col = blockIdx.x * blockDim.x + threadIdx.x;

	//Get dimension of the output 
	int output_rows = W_rows;
	int output_cols = input_cols;

	float output_value = 0.0f;

	if (col < output_cols && row < output_rows)
	{
		for (int i = 0; i < W_cols; i++)
		{
			output_value += W[row * W_cols + i] * input[i * input_cols + col];
	    }

		output[row * output_cols + col] = output_value + b[row];
	}
}
</pre>
</details>

Next, implement backprop – this will look a lot like the forward path.

<details>
<summary>Solution</summary>
<pre>
__global__ void linearLayerBackprop(float *W, float* eB, float* eA,
									const int W_rows, const int W_cols,
									const int eB_rows, const int eB_cols) 
{
	int row = blockIdx.y * blockDim.y + threadIdx.y;
	int col = blockIdx.x * blockDim.x + threadIdx.x;

	//outputet dimension of the output. W is treated as transposed
	int eA_rows = W_cols;
	int eA_cols = eB_cols;

	float eA_value = 0.0f;

	if (row < eA_rows && col < eA_cols)
	{
		for (int i = 0; i < W_rows; i++)
		{
			eA_value += W[i * W_cols + row] * eB[i * eB_cols + col];
	    }
		eA[row * eA_cols + col] = eA_value;
	}
}
</pre>
</details>

Up next is weight updates. Again, the control flow looks pretty similar.


<details>
<summary>Solution</summary>
<pre>
__global__ void linearLayerUpdateWeights(float *eB, float* input, float* W,
									const int eB_rows, const int eB_cols,
									const int input_rows, const int input_cols, float learning_rate)
{
	int row = blockIdx.y * blockDim.y + threadIdx.y;
	int col = blockIdx.x * blockDim.x + threadIdx.x;

	//outputet dimension of the output. input is treated as transposed
	int W_rows = eB_rows;
	int W_cols = input_rows;


	float dW_value = 0.0f;

	if (row < W_rows && col < W_cols)
	{
		for (int i = 0; i < eB_cols; i++)
		{
			dW_value += eB[row * eB_cols + i] * input[col * input_cols + i];
	    }
		W[row * W_cols + col] = W[row * W_cols + col] - learning_rate * (dW_value / input_rows);
	}
}
</pre>
</details>

Last thing to do is update biases.
This one looks a little different, and our old friend `atomicAdd` will probably need to make an appearance.


<details>
<summary>Solution</summary>
<pre>
__global__ void linearLayerUpdateBias(float *eB, float* b,
									const int eB_rows, const int eB_cols,
									const int b_rows, float learning_rate)
{
	int index = blockIdx.x * blockDim.x + threadIdx.x;

	if (index < eB_rows * eB_cols)
	{
		int col = index % eB_cols;
		int row = index / eB_cols;
		atomicAdd(&b[row], -learning_rate * (eB[row * eB_cols + col] / eB_cols));
	}
}
</pre>
</details>


#### `main.cu`

Once everything is implemented, we need to hook it all together!

We'll put together a pretty simple network, two linear layers each with our simple sigmoid activation function.

It's useful to keep references to the linear layers, as we can print their values to debug things.
You'll need two layers. Here's the whole network:

    LinearLayer ll1 = LinearLayer("linear_1", Shape(2, 2));
    nn.addLayer(&ll1);
    nn.addLayer(new SigmoidActivation("sigmoid_1"));
    LinearLayer ll2 = LinearLayer("linear_2", Shape(2, 1));
    nn.addLayer(&ll2);
    nn.addLayer(new SigmoidActivation("sigmoid_2"));

And you're done!

<details>
<summary>Something not working?</summary>
Here's a complete zip of the fininshed lab: [`lab5_solutions.zip`](lab5_solutions.zip)
</details>

### Training

Once you have everything implemented and the network architecutre created.  It's time to run training.

In `dataset.cu` comment out `XNOR_GATE` to create the AND gate dataset and uncomment it to create the XNOR dataset.


### Deliverables

 - Final code

 - Accuracy of your network and the results of the `time` command.

 - `XNOR_GATE` and `AND_GATE` results.

---

## Assignment

Our final assignment is open-ended. We would like for you to go explore a
little bit and try to build something fun of your own interest (that uses a
GPU, of course!)

We have two choices, and you are welcome to do whichever you prefer.


### Option A: Jetson AI Certification

nVidia will certify you as a "Jetson AI Specialist" if you complete a small,
original project using the Jeston. This might be a fun additional certification
to add to your collection if it is something you are interested in.

[The details of the program are here.](https://developer.nvidia.com/embedded/learn/jetson-ai-certification-programs)

For this option, you must submit to us the same materials you will submit to
nVidia for certification (see the "Hands-On, Project-Based Assessment" section
at the bottom of the page).

You won't get your response from nVidia until after the end of the term, so
don't worry about that; we will grade your project independently.


### Option B: Research Replication

Modern machine learning research is rapidly improving its artifact
dissemination and documentation practices since the rise in attention to the
"ML replication crisis". As a result, most interesting new papers have datasets
and processing pipelines available in public repositories.

For this option, pick a recent (say, within the last 10 years) paper and
perform a replication study. That is, you should run their experiments on your
hardware and compare the results. Unless they happened to run on the same TX2
hardware, the absolute performance will likely be different, but the relative
performance and trends should largely hold.

In your writeup, explain briefly the goal of the study that you chose to
reproduce, as well as any obstacles you had to overcome to get their artifact
running in your environment. Discuss how your results compare to the original
results and try to explain when things diverge.


---

## What to Submit

Prepare a report document with answers for each of the `Report Deliverables` above.

### Lab (Neural Network)

 - Final code

 - Accuracy of your network and the results of the `time` command.

 - `XNOR_GATE` and `AND_GATE` results.

### Assignment
#### Option 1
For the Jetson AI Certification, we will be evaluating the same criteria that NVIDIA will be reviewing.  The requirements are produced below for your convience.

 - AI - The project uses deep learning, machine learning, and/or computer vision in a meaningful way, and demonstrates a fundamental understanding of creating applications with AI. Factors include the effectiveness, technical complexity, and performance of your AI solution on Jetson.

 - Impact / Originality - The concept of your project is novel and applies AI to solve or address challenges or issues faced by yourself or society. Also, our ideas and work are either original or derivative in a significant way.

 - Reproducibility - Any plans, code, and resources needed for someone else to build and use the project are included in the repository and are easy to follow.

 - Presentation and Documentation - The video effectively demonstrates and explains various aspects of the project, and there exists a clear, complete readme in the repository that documents any steps needed to build/run the project along with diagrams and images. Note that educators should have an oral presentation component to their video to highlight their teaching abilities.

#### Option 2

 - Citation of the original paper you are basing your reproduction study on.  Why did you choose it?

 - In your writeup, explain briefly the goal of the study that you chose to reproduce, as well as any obstacles you had to overcome to get their artifact running in your environment. Discuss how your results compare to the original results and try to explain when things diverge.


### Revised Deadlines

> **WARNING: Limited late submission window!!**

Final grades are due to the registrar by end-of-business on September 21.

We can accept late submissions up through start-of-business on September 21 _if
you message us before the original deadline to let us know when you will submit._

As an incentive, if you submit before start-of-business on Friday, September 16,
we will add a bonus 3% to your grade.


<!--

---

## Additional Resources

 - [CUDA Basics Presentation][nvidia-basics] from nVidia.

-->

[slides]: wes237b-su22-LAB-05.pptx
[workbook]: WES237B_Introduction_to_ML.pdf
