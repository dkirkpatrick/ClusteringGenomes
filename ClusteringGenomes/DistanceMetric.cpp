/*
*	Part of the ClusteringGenomes Project by Douglas Kirkpatrick
*	Copyright (c) 2016, all rights reserved
*/

#include "DistanceMetric.h"
#include <iostream>
#include <math.h>
#include <string>
double EuclideanDistance::getDistance(std::vector<std::string>& row1, std::vector<std::string>& row2) {
	if (row1.size() != row2.size()) {
		std::cout << "ERROR: Sizes of rows must be equal!!" << std::endl;
		return 0.0; 
	}
	double distance = 0.0;
	for (int i = 0; i < row1.size(); i++) {
		distance += pow((std::stod(row1[i]) - std::stod(row2[i])), 2);
	}

	return sqrt(distance);
}

double TaxicabDistance::getDistance(std::vector<std::string>& row1, std::vector<std::string>& row2) {
	if (row1.size() != row2.size()) {
		std::cout << "ERROR: Sizes of rows must be equal!!" << std::endl;
		return 0.0;
	}

	double distance = 0.0; 
	for (int i = 0; i < row1.size(); i++) {
		distance += abs(std::stod(row1[i]) - std::stod(row2[i]));
	}

	return distance;
}

double CorrelationDistance::getDistance(std::vector<std::string>& row1, std::vector<std::string>& row2) {
	if (row1.size() != row2.size()) {
		std::cout << "ERROR: Sizes of rows must be equal!!" << std::endl;
		return 0.0;
	}
	double sumX = 0.0, sumY = 0.0, sumXsq = 0.0, sumYsq = 0.0, sumXY = 0.0, r;

	for (int i = 0; i < row1.size(); i++) {
		double xI = std::stod(row1[i]); 
		double yI = std::stod(row2[i]); 
		sumX += xI; 
		sumY += yI;
		sumXY += xI * yI;
		sumXsq += xI * xI;
		sumYsq += yI * yI;
	}
	double n = (double) row1.size(); 
	r = (n*sumXY - (sumX*sumY)) / (sqrt(n*sumXsq - (sumX*sumX)) * sqrt(n*sumYsq - (sumY*sumY)));

	return r*r;
}

double InfNormDistance::getDistance(std::vector<std::string>& row1, std::vector<std::string>& row2) {
	if (row1.size() != row2.size()) {
		std::cout << "ERROR: Sizes of rows must be equal!!" << std::endl;
		return 0.0;
	}

	double distance = abs(std::stod(row1[0]) - std::stod(row2[0]));
	for (int i = 1; i < row1.size(); i++) {
		double temp = abs(std::stod(row1[i]) - std::stod(row2[i])); 
		if (temp > distance) {
			distance = temp; 
		}
	}

	return distance;
}