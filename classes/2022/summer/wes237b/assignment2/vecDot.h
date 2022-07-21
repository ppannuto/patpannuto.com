// Include guard, one should be in all headers
#ifndef VECMUL_H
#define VECMUL_H

// Include the Eigen pacakge that provides vec classes
#include <Eigen/Core>

// Calculate the dot product between two arbitrary vectors
//  @param     xin First vector
//  @param     yin Second vector
//  @param  length Length of the vectors
//  @return        Dot product of the vectors
float dot_product(Eigen::VectorXf xin, Eigen::VectorXf yin, uint32_t length);

#endif // VECMUL_H
