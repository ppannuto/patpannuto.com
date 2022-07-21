#include <cmath>

#include "vecMul.h"

bool test_dot(Eigen::VectorXf vec1, Eigen::VectorXf vec2, uint32_t length) {
	float eigen_result = vec1.dot(vec2);
	float our_result = dot_product(vec1, vec2, length);

	// Only check precision to four decimal places
	// -> Try me! What happens if we don't round? Why?
	eigen_result = floor(eigen_result * pow(10,4) + .5) / pow(10,4);
	our_result = floor(our_result * pow(10,4) + .5) / pow(10,4);

	return eigen_result == our_result;
}
