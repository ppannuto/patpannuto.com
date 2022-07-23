#include <iostream>
#include <stdlib.h>

#include <eigen3/Eigen/Dense>
// Or possibly just
// #include <Eigen/Dense>

#include "vecDot.h"
#include "vecMulTest.h"

//using namespace Eigen;

using namespace std;

using Eigen::MatrixXd;
using Eigen::VectorXd;

int main(int argc, const char* argv[]) {
	MatrixXd m = MatrixXd::Random(3,3);
	m = (m * 10);
	cout << "m: " << endl << m << endl;
	VectorXd v(3);
	v << 1, 2, 3 ;
	cout << "m*v: " << endl << m*v << endl;

	/*
		TODO-- Connect!

	// Test the methods
	if (test_dot(x, y, length)) {
		printf("Test passed\n");
		return 0;
	}
	else {
		printf("Test failed\n");
		return 1;
	}
	*/
}
