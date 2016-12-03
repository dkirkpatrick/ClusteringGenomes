/*
*	Part of the ClusteringGenomes Project by Douglas Kirkpatrick
*	Copyright (c) 2016, all rights reserved
*/

#ifndef MBDistance_H_
#define MBDistance_H_

#include "DistanceMetric.h"
#include <vector> 
#include <algorithm> 

class MBDistance : public DistanceMetric {
public:
	MBDistance(double genomeFactor, double phenotypeFactor); 
	double getDistance(std::vector<std::string>& row1, std::vector<std::string>& row2);
private: 
	double m_genomeFactor;
	double m_phenotypeFactor; 
};

#endif