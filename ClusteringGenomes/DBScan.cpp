/*
*	Part of the ClusteringGenomes Project by Douglas Kirkpatrick
*	Copyright (c) 2016, all rights reserved
*/

#include "DBScan.h"

DBScan::DBScan(DistanceMetric* mDistanceMetric, int minPts, double epsilon) : ClusteringAlgorithm(mDistanceMetric), m_minPts(minPts), m_epsilon(epsilon) {}


std::vector<int> DBScan::getClusters(std::vector<std::vector<std::string>>& myRows) {
	std::vector<int> myTypes = std::vector<int>(myRows.size(), 0); //-1 noise, 1 edge, 2 core
	std::vector<int> myClusters = std::vector<int>(myRows.size(), 0);
	std::vector<int> numNeighbors = std::vector<int>(myRows.size(), 0);
	std::vector<int> coreNeighbor = std::vector<int>(myRows.size(), 0);


	//Initial differentation of core, edge, noise points
	for (int i = 0; i < myRows.size(); i++) {
		for (int j = i + 1; j < myRows.size(); j++) {
			if (m_distanceMetric->getDistance(myRows[i], myRows[j]) < m_epsilon) {
				numNeighbors[i]++;
				numNeighbors[j]++;
			}
		}
		if (numNeighbors[i] == 0) {
			myTypes[i] == -1;
		}
		else if (numNeighbors[i] > m_minPts) {
			myTypes[i] == 2;

		} else {
			myTypes[i] == 1;
		}
	}

	//Final seperation of edge vs noise pts
	for (int i = 0; i < myRows.size(); i++) {
		if (myTypes[i] == 1) {
			double minDistance = m_epsilon+1;
			int whichCorePt = -1;
			for (int j = 0; j < myRows.size(); j++) {
				if (myTypes[j] == 2) {
					double potentialDistance = m_distanceMetric->getDistance(myRows[i], myRows[j]);
					if (potentialDistance < minDistance) {
						minDistance = potentialDistance;
						whichCorePt = j;
					}
				}
			}
			if (minDistance < m_epsilon) {
				coreNeighbor[i] = whichCorePt;
			} else {
				myTypes[i] == -1;
			}
		}
	}


	//Find the neighboring core points of each core point
	std::vector<std::vector<int>> neighboringCorePts = std::vector<std::vector<int>>();
	for (int i = 0; i < myRows.size(); i++) {
		if(myTypes[i] == 2){
			neighboringCorePts[i] = std::vector<int>();
			for (int j = i + 1; j < myRows.size(); j++) {
				if (myTypes[j] == 2 && (m_distanceMetric->getDistance(myRows[i], myRows[j]) < m_epsilon)) {
					neighboringCorePts[i].push_back(j);
				}
			}
		}
	}

	//Construct queues to use in cluster assignment
	std::queue<std::pair<int, int>> myAssignments = std::queue<std::pair<int, int>>();
	std::queue<int> myCorePts = std::queue<int>();
	for (int i = 0; i < myRows.size(); i++) {
		if (myTypes[i] == 2) {
			myCorePts.emplace(i);
			if (myAssignments.empty()) {
				myAssignments.emplace(i, 1);
			}
		}
	}

	int clusterCounter = 2;


	//Assign core points to clusters
	while (!myCorePts.empty()) {
		//If all previous assignments made, start on next cluster
		if (myAssignments.empty()) {
			int potentialNext = myCorePts.front();
			while (myClusters[potentialNext] > 0 && myCorePts.size() > 1) {
				myCorePts.pop();
				potentialNext = myCorePts.front();
			}
			if (myClusters[potentialNext] == 0) {
				myAssignments.emplace(potentialNext, clusterCounter);
				clusterCounter++;
			}
			myCorePts.pop();
		}
		//If there assignments to be made, make them, and push new assignments
		if (!myAssignments.empty()) {
			std::pair<int, int> temp = myAssignments.front();
			if (myClusters[temp.first] == 0) {
				myClusters[temp.first] = temp.second;
				for (int i = 0; i < neighboringCorePts[temp.first].size(); i++) {
					//Make assignments to unassigned core points
					if (myClusters[neighboringCorePts[temp.first][i]] == 0) {
						myAssignments.emplace(neighboringCorePts[temp.first][i], temp.second);
					}
				}
			}
			myAssignments.pop();
		}
	}


	//Assign border points to closest core points
	for (int i = 0; i < myRows.size(); i++) {
		if (myTypes[i] == 1) {
			myClusters[i] = myClusters[coreNeighbor[i]];
		}
	}

	return myClusters;
}
