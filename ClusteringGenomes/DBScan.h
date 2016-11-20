/*
*	Part of the ClusteringGenomes Project by Douglas Kirkpatrick
*	Copyright (c) 2016, all rights reserved
*/

#ifndef DBSCAN_H_
#define DBSCAN_H_

#include <vector>
#include <algorithm>
#include <queue>
#include "DistanceMetric.h"
#include "ClusteringAlgorithm.h"

class DBScan : public ClusteringAlgorithm {
public:

	DBScan(DistanceMetric* mDistanceMetric, int minPts, double epsilon);
	std::vector<int> getClusters(std::vector<std::vector<std::string>>& myRows);

private:
	//Number of clusters k
	int m_minPts;
	//Percent of cluster assignments that need to stay the same to end loop
	double m_epsilon;
};

#endif
