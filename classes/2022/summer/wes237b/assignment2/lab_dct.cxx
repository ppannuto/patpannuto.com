#include <iostream>
#include <stdio.h>
#include <math.h>

#include <opencv2/opencv.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

// Note! You need to write this one :)
#include "lab_dct.h"

using namespace cv;

// Helper function to avoid calculating 1/sqrt(2)
float sf(int in) {
	if (in == 0) {
		return 0.70710678118; // 1 / sqrt(2)
	}
	return 1.;
}

Mat lab_dct_naive(Mat input) {
	const int HEIGHT = input.rows;
	const int WIDTH = input.cols;

	float scale = 2./sqrt(HEIGHT*WIDTH);

	// Create the result matrix of the correct datatype
	Mat result = Mat(HEIGHT, WIDTH, CV_32FC1);

	float* result_ptr = result.ptr<float>();
	float* input_ptr = input.ptr<float>();

	//Naive implementation. Lots of nested loops
	for(int x = 0; x < HEIGHT; x++) {
		for(int y = 0; y < WIDTH; y++) {
			float value = 0.f;

			for(int i = 0; i < HEIGHT; i++) {
				for(int j = 0; j < WIDTH; j++) {
					// Take a few minutes to complete this
					// line here given the definition of
					// the DCT
					value +=
				}
			}

			value = scale * sf(x) * sf(y) * value;
			result_ptr[x * WIDTH + y] = value;
		}
	}
	return result;
}

/*****************
  * Ignore this at first!
  *
Mat lab_dct_opt(Mat input){
	const int HEIGHT = input.rows;
	const int WIDTH = input.cols;

	float scale = 2./sqrt(HEIGHT*WIDTH);

	// Create the result matrix of the correct datatype
	Mat result = Mat(HEIGHT, WIDTH, CV_32FC1);
	Mat result_row = Mat(HEIGHT, WIDTH, CV_32FC1);

	float* result_ptr = result.ptr<float>();
	float* input_ptr = input.ptr<float>();

	// Less naive implementation.
	// Perform 2 1D DCTs, one for the rows and one for the columns
	float value;
	for(int k=0; k<HEIGHT; k++) {
		for(int i=0; i<WIDTH; i++) {
			value = 0.0;
			for(int j=0; j<WIDTH; j++) {
				value += input.at<float>(k, j) * cos(M_PI/((float)WIDTH)*(j+1./2.)*(float)i);
			}
			result_row.at<float>(k,i) = value * sf(i);
		}
	}

	// Now perform the column transformation
	for(int k=0; k<WIDTH; k++) {
		for(int i=0; i<HEIGHT; i++) {
			value = 0.0;
			for (int j=0; j<HEIGHT; j++) {
				value += result_row.at<float>(j,k) * cos(M_PI/((float)HEIGHT)*(j+1./2.)*(float)i);
			}

			result.at<float>(i, k) = value*sf(i)*scale;
		}
	}

	return result;
}
*************/
