/*
*	Part of the ClusteringGenomes Project by Douglas Kirkpatrick
*	Copyright (c) 2016, all rights reserved
*/

#include "ClusteringAlgorithm.h"

ClusteringAlgorithm::ClusteringAlgorithm(DistanceMetric * mDistanceMetric) : m_distanceMetric(mDistanceMetric) {}

ModKMeans::ModKMeans(DistanceMetric* mDistanceMetric, int k, double percentChange, int maxIterations) : ClusteringAlgorithm(mDistanceMetric), m_k(k), m_percentChange(percentChange), m_maxIterations(maxIterations) {}


std::vector<int> ModKMeans::getClusters(std::vector<std::vector<std::string>>& myRows) {
	std::vector<int> myClusters = std::vector<int>(myRows.size(), 0);
	//Assignment of centroids from first n  
	//mCentroids is indicies into the array 
	std::vector<int> myCentroids = std::vector<int>(m_k, 0);
	for (int i = 0; i < m_k; i++) {
		myCentroids[i] = i;
		myClusters[i] = i;
	}
	for (int i = m_k; i < myRows.size(); i++) {
		double distance = m_distanceMetric->getDistance(myRows[myCentroids[0]], myRows[i]);
		myClusters[i] = 0;
		for (int j = 1; j < m_k; j++) {
			double newDistance = m_distanceMetric->getDistance(myRows[myCentroids[j]], myRows[i]);
			if (newDistance < distance) {
				distance = newDistance;
				myClusters[i] = j;
			}
		}
	}
	double changedCluster = 0.0;
	int newCluster;
	int clusterChange = 0;
	int iterations = 0; 
	//Loop for clustering assignments 
	while (changedCluster < m_percentChange && iterations < m_maxIterations) {
		std::vector<double> clusterDistance = std::vector<double>(myRows.size(), 0.0);
		for (int i = 0; i < myRows.size(); i++) {
			for (int j = i + 1; j < myRows.size(); j++) {
				if (myClusters[i] == myClusters[j]) {
					double distance = m_distanceMetric->getDistance(myRows[i], myRows[j]);
					clusterDistance[i] += distance;
					clusterDistance[j] += distance;
				}
			}
		}
		for (int i = 0; i < myRows.size(); i++) {
			if (clusterDistance[myCentroids[myClusters[i]]] > clusterDistance[i]) {
				myCentroids[myClusters[i]] = i;
			}
		}
		for (int i = m_k; i < myRows.size(); i++) {
			double distance = m_distanceMetric->getDistance(myRows[myCentroids[0]], myRows[i]);
			newCluster = 0;
			for (int j = 1; j < m_k; j++) {
				double newDistance = m_distanceMetric->getDistance(myRows[myCentroids[j]], myRows[i]);
				if (newDistance < distance) {
					distance = newDistance;
					newCluster = j;
				}
			}
			if (newCluster != myClusters[i]) {
				clusterChange++;
			}
			myClusters[i] = newCluster;
		}
		changedCluster = (double)clusterChange / (double)myRows.size();
		iterations++; 
	}
	return myClusters;
}