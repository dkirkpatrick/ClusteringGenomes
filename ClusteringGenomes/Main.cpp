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


std::vector<std::string> getNextRow(std::istream& str);  

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
		inputFile = "myRows.csv"; 
		outputFile = "myClusters.csv";
	}


	std::string outputSeparator = ", "; 

	DistanceMetric* myMetric = new EuclideanDistance(); 
	ClusteringAlgorithm* myAlgorithm = new DBScan(myMetric, 5, 10.0); 


	//////////////END CHANGE//////////////

	std::ifstream ifile(inputFile);
	std::vector<std::vector<std::string>> myPopulation = std::vector<std::vector<std::string>>();

	while (ifile.peek() != EOF)
	{
		myPopulation.push_back(getNextRow(ifile)); 
	}

	std::vector<int> myClusterAssignments = myAlgorithm->getClusters(myPopulation);
	
	std::ofstream ofile(outputFile);
	for (int i = 0; i < myClusterAssignments.size(); i++) {
		ofile << myClusterAssignments[i] << outputSeparator; 
	}
	ofile << std::endl; 
	ofile.close();

	return 0; 
}

std::vector<std::string> getNextRow(std::istream& str)
{
	std::vector<std::string> result;
	std::string line;
	std::getline(str, line);


	std::stringstream lineStream(line);
	std::string cell;


	while (std::getline(lineStream, cell, ','))
	{
		result.push_back(cell);
	}
	return result;
}