#include <iostream>
#include <stdlib.h>

#include "vecDot.h"
#include "vecMulTest.h"

using namespace arma;
using namespace std;

int main(int argc, const char* argv[]) {
	// Set random number generator
	arma_rng::set_seed_random();
	uint32_t length = 10;

	// Generate two random vectors to length
	vec x = randu<vec>(length);
	vec y = randu<vec>(length);

	// Test the methods
	if (test_dot(x, y, length)) {
		printf("Test passed\n");
		return 0;
	}
	else {
		printf("Test failed\n");
		return 1;
	}
}
