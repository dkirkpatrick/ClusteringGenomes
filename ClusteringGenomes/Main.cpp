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
#include "MBDistance.h"


std::pair<std::string, std::vector<std::string>> getNextRow(std::istream& str);  

int main(int argv, char* argc[]) {
	std::cout << "Hello World, this is " << argc[0] << std::endl; 

	std::string inputFile;
	std::string outputFile;
	std::string mode; 
	double genotypeFactor; 
	double phenotypeFactor; 
	//////////////CHANGE HERE//////////////


	if (argv > 3) {
		mode = argc[1];
		inputFile = argc[2];
		outputFile = argc[3];
		genotypeFactor = std::stod(argc[4]); 
		phenotypeFactor = std::stod(argc[5]);
	}
	else {
		inputFile = "C:\\Source\\CSE881\\hwData.csv";
		outputFile = "C:\\Source\\CSE881\\myClusters.csv";
	}


	std::string outputSeparator = "\n"; 

	DistanceMetric* myMetric = new  MBDistance(genotypeFactor, phenotypeFactor); 

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

	if (mode[0] == 'a' || mode[0] == 'A') {
		std::ofstream ofile(outputFile);
		for (int i = 0; i < myDistances.size(); i++) {
			ofile << myIDs[i] << ", "; 
			for (int j = 0; j < myDistances.size(); j++) {
				ofile << myDistances[i][j] << ", ";
			}
			ofile << std::endl;
		}
		ofile.close();
	}
	else if (mode[0] == 'c' || mode[0] == 'C') {
		std::vector<int> myClusterAssignments = myAlgorithm->getClusters(myPopulation, myDistances);

		std::ofstream ofile(outputFile);
		for (int i = 0; i < myClusterAssignments.size(); i++) {
			ofile << myIDs[i] << ", " << myClusterAssignments[i] << outputSeparator;
		}
		ofile << std::endl;
		ofile.close(); 
	}
	else {
		std::cout << "You did not enter a correct mode. Exiting...\n";
	}

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