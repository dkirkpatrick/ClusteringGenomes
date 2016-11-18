/*
*	Part of the ClusteringGenomes Project by Douglas Kirkpatrick
*	Copyright (c) 2016, all rights reserved
*/

#ifndef ClusteringAlgorithm_H_
#define ClusteringAlgorithm_H_

#include <vector> 
#include <algorithm> 
#include "DistanceMetric.h"

class ClusteringAlgorithm {
public:
	ClusteringAlgorithm(DistanceMetric* mDistanceMetric); 
	virtual std::vector<int> getClusters(std::vector<std::vector<std::string>>& myRows) = 0;
protected: 
	DistanceMetric* m_distanceMetric; 
};

class ModKMeans : public ClusteringAlgorithm {
public:

	ModKMeans(DistanceMetric* mDistanceMetric, int k, double percentChange, int maxIterations); 
	std::vector<int> getClusters(std::vector<std::vector<std::string>>& myRows);

private: 
	//Number of clusters k 
	int m_k; 
	//Percent of cluster assignments that need to stay the same to end loop  
	double m_percentChange; 
	int m_maxIterations; 

};

#endif