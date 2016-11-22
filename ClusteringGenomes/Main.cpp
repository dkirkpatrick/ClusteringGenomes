/*
*	Part of the ClusteringGenomes Project by Douglas Kirkpatrick
*	Copyright (c) 2016, all rights reserved
*/

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

#include "ClusteringAlgorithm.h"
#include "DistanceMetric.h"
#include "DBScan.h"


std::pair<std::string, std::vector<std::string>> getNextRow(std::istream& str);  
void normalize(std::vector<std::vector<double>>& myDistances); 

int main(int argv, char* argc[]) {
	std::cout << "Hello World, this is " << argc[0] << std::endl; 

	std::string inputFile;
	std::string outputFile;

	//////////////CHANGE HERE//////////////


	if (argv > 2) {
		inputFile = argc[1];
		outputFile = argc[2];
	}
	else {
		inputFile = "C:\\Source\\CSE881\\hwData.csv";
		outputFile = "C:\\Source\\CSE881\\myClusters.csv";
	}


	std::string outputSeparator = "\n"; 

	DistanceMetric* myMetric = new EuclideanDistance(); 
	ClusteringAlgorithm* myAlgorithm = new DBScan(myMetric, 3, 0.15); 


	//////////////END CHANGE//////////////

	std::ifstream ifile(inputFile);
	std::vector<std::vector<std::string>> myPopulation = std::vector<std::vector<std::string>>();
	std::vector<std::string> myIDs = std::vector<std::string>(); 
	while (ifile.peek() != EOF)
	{
		std::pair<std::string, std::vector<std::string>> temp = getNextRow(ifile); 
		myPopulation.push_back(temp.second); 
		myIDs.push_back(temp.first); 
	}

	std::vector<std::vector<double>> myDistances = std::vector<std::vector<double>>(); 
	for (int i = 0; i < myPopulation.size(); i++) {
		std::vector<double> temp = std::vector<double>(myPopulation.size(), 0.0);
		myDistances.push_back(temp); 
	}

	for (int i = 0; i < myPopulation.size(); i++) {
		for (int j = i+1; j < myPopulation.size(); j++) {
			myDistances[i][j] = myMetric->getDistance(myPopulation[i], myPopulation[j]); 
			myDistances[j][i] = myDistances[i][j]; 
		}
	}

	std::vector<int> myClusterAssignments = myAlgorithm->getClusters(myPopulation, myDistances);
	
	std::ofstream ofile(outputFile);
	for (int i = 0; i < myClusterAssignments.size(); i++) {
		ofile << myIDs[i] << ", " << myClusterAssignments[i] << outputSeparator;
	}
	ofile << std::endl; 
	ofile.close();

	return 0; 
}

std::pair<std::string, std::vector<std::string>> getNextRow(std::istream& str)
{
	std::vector<std::string> result;
	std::string line;
	std::getline(str, line);


	std::stringstream lineStream(line);
	std::string cell;

	std::string label; 
	std::getline(lineStream, label, ',');
	while (std::getline(lineStream, cell, ','))
	{
		result.push_back(cell);
	}
	return std::pair<std::string, std::vector<std::string>>(label, result);
}