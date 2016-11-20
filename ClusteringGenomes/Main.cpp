/*
*	Part of the ClusteringGenomes Project by Douglas Kirkpatrick
*	Copyright (c) 2016, all rights reserved
*/

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <map>

#include "ClusteringAlgorithm.h"
#include "DistanceMetric.h"
#include "DBScan.h"

constexpr int MINPTS = 5;
constexpr double EPSILON = 0.1;

std::vector<std::string> getNextRow(std::istream& str);

int main(int argv, char* argc[]) {
  std::cout << "Hello World, this is " << argc[0] << std::endl;
  std::string inputFile;
  std::string outputFile;
  // User provided input? If not, use defaults.
  if (argv > 2) {
    inputFile = argc[1];
    outputFile = argc[2];
  }
  else {
    inputFile = "data/snapshot__pop_1000.csv";
    outputFile = "myClusters.csv";
  }

  std::ifstream ifile(inputFile);
  std::vector<std::vector<std::string>> myPopulation = std::vector<std::vector<std::string>>();

  // Capture header information.
  // {"attribute":index}
  std::map<std::string, int> headerLookup;
  if (ifile.peek() != EOF) {
    std::vector<std::string> header = getNextRow(ifile);
    for (size_t i = 0; i < header.size(); i++) headerLookup[header[i]] = i;
  } else {
    std::cout << "This data file is totally empty, wtf?" << std::endl;
    exit(-1);
  }
  // Read in population.
  while (ifile.peek() != EOF)
  {
    myPopulation.push_back(getNextRow(ifile));
  }

  // It's clusterin' time!
  std::string outputSeparator = ",";
  DistanceMetric* distMetric = new AvidaOrganismDistance(headerLookup);
  ClusteringAlgorithm* myAlgorithm = new DBScan(distMetric, MINPTS, EPSILON);
  std::vector<int> myClusterAssignments = myAlgorithm->getClusters(myPopulation);

  // Output results
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
