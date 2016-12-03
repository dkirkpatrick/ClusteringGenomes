#include "MBDistance.h"
#include <iostream>
#include <string>

MBDistance::MBDistance(double genomeFactor, double phenotypeFactor)
{
	m_genomeFactor = genomeFactor / (genomeFactor + phenotypeFactor); 
	m_phenotypeFactor = phenotypeFactor / (genomeFactor + phenotypeFactor);
}

double MBDistance::getDistance(std::vector<std::string>& row1, std::vector<std::string>& row2) {
	if (row1.size() != row2.size()) {
		std::cout << "ERROR: Sizes of rows must be equal!!" << std::endl;
		return 0.0;
	}

	//find edit distance of genome
	std::vector<std::vector<int>> table; 
	table.resize(501, std::vector<int>(501, 0)); 

	for (int i = 0; i < 501; i++) {
		table[0][i] = i; 
		table[i][0] = i; 
	}

	for (int i = 1; i < 501; i++) {
		for (int j = 1; j < 501; j++) {
			int a = std::stoi(row1[i - 1]); 
			int b = std::stoi(row2[j - 1]);
			if (a == b) {
				table[i][j] = table[i - 1][j - 1]; 
			}
			else {
				table[i][j] = std::min({ table[i - 1][j - 1] + 1, table[i][j - 1] + 1, table[i - 1][j] + 1 });
			}
		}
	}
	double genomeDistance = table[500][500]/500; 

	double phenotypeDistance = 0.0;
	for (int i = 500; i < row1.size(); i++) {
		double value1 = std::stod(row1[i]); 
		double value2 = std::stod(row2[i]);
		phenotypeDistance += abs(value1 - value2) / (value1 + value2);
	}

	return m_genomeFactor*genomeDistance + m_phenotypeFactor*phenotypeDistance;
}