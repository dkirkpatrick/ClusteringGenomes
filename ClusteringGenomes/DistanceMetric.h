/*
*	Part of the ClusteringGenomes Project by Douglas Kirkpatrick
*	Copyright (c) 2016, all rights reserved
*/

#ifndef DistanceMetric_H_
#define DistanceMetric_H_

#include <vector> 
#include <algorithm> 


class DistanceMetric {
public:
	virtual double getDistance(std::vector<std::string>& row1, std::vector<std::string>& row2) = 0;
};

class EuclideanDistance : public DistanceMetric {
public: 
	double getDistance(std::vector<std::string>& row1, std::vector<std::string>& row2);
};

class TaxicabDistance : public DistanceMetric {
public:
	double getDistance(std::vector<std::string>& row1, std::vector<std::string>& row2);
};

class CorrelationDistance : public DistanceMetric {
public:
	double getDistance(std::vector<std::string>& row1, std::vector<std::string>& row2);
};


class InfNormDistance : public DistanceMetric {
public:
	double getDistance(std::vector<std::string>& row1, std::vector<std::string>& row2);
};

#endif