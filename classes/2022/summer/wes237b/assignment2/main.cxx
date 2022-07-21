#include <iostream>
#include <stdio.h>
#include <math.h>

#include <opencv2/opencv.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

using namespace std;
using namespace cv;

int main(int argc, const char * argv[]) {
	Mat image; //, gray, dct_cv, dct_lab;

	// Read in the image and store it in a matrix
	image = imread("image.tif");

	// Display the image
	imshow("Original Color", image);

	// Wait for a key
	waitKey(0);

	return 0;
}
