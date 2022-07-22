#include "vecDot.h"

float dot_product(Eigen::VectorXf vec1, Eigen::VectorXf vec2, uint32_t length) {
	// Note: This function does not use Eigen; it simply uses the Eigen
	// vector type to keep this example simple. A STL vector would work the
	// same for the implementation approach.

	float result = 0.0;

	for (int i=0; i<length; i++) {
		result += vec1[i] * vec2[i];
	}

	return result;
}
