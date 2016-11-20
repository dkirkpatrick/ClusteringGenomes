/*
*	Part of the ClusteringGenomes Project by Douglas Kirkpatrick
*	Copyright (c) 2016, all rights reserved
*/

#ifndef DistanceMetric_H_
#define DistanceMetric_H_

#include <vector>
#include <algorithm>
#include <iostream>
#include <math.h>
#include <cmath>
#include <map>
#include <string>
#include <bitset>
#include <tuple>


class DistanceMetric {
public:
	virtual double getDistance(std::vector<std::string>& row1, std::vector<std::string>& row2) = 0;
};

class EuclideanDistance : public DistanceMetric {
public:
	double getDistance(std::vector<std::string>& row1, std::vector<std::string>& row2);
};

class TaxicabDistance : public DistanceMetric {
public:
	double getDistance(std::vector<std::string>& row1, std::vector<std::string>& row2);
};

class CorrelationDistance : public DistanceMetric {
public:
	double getDistance(std::vector<std::string>& row1, std::vector<std::string>& row2);
};


class InfNormDistance : public DistanceMetric {
public:
	double getDistance(std::vector<std::string>& row1, std::vector<std::string>& row2);
};

class AvidaOrganismDistance : public DistanceMetric {
public:
  std::map<std::string, int> rowAttributeLookup;

  std::map<std::tuple<std::string, std::string>, double> editDistanceMemo;
  std::map<std::tuple<std::string, std::string>, double> simpleMatchingCoeffMemo;

  AvidaOrganismDistance(std::map<std::string, int>& attributeLookup) :
    rowAttributeLookup(attributeLookup) { }
  double getDistance(std::vector<std::string>& row1, std::vector<std::string>& row2) {
    /*
      Given 2 rows (each represents an organism), return a distance between them.
      Here, distance is calculated as follows:
        (0.5)(EditDistance(row1.genome, row2.genome)) + (0.5)(SMC(row1.phenotype, row2.phenotype))
    */
    std::string r1Genome = row1[rowAttributeLookup["genome_sequence"]];
    std::string r2Genome = row2[rowAttributeLookup["genome_sequence"]];
    // Calculated normalized edit distance between r1's genome and r2's genome.
    double gDist = editDistance(r1Genome, r2Genome) / std::max(r1Genome.size(), r2Genome.size());
    std::string r1Phenotype = row1[rowAttributeLookup["phenotype_signature"]];
    std::string r2Phenotype = row2[rowAttributeLookup["phenotype_signature"]];
    double pDist = 1.0 - simpleMatchingCoeff(r1Phenotype, r2Phenotype);
    return (0.5 * gDist) + (0.5 * pDist);
  };

  double editDistance(std::string& a, std::string& b) {
    /*
      Given 2 strings: a & b, calculate edit distance between them.
    */
    auto search = editDistanceMemo.find(std::make_tuple(a, b));
    if (search != editDistanceMemo.end()) {
      // Found (a, b)
      return search->second;
    } else {
      // Haven't seen these inputs before. Do calculation and add to lookup table.
      // Create DP table:
      //  * 1 Row for null character + each symbol of a
      //  * 1 Column for null character + each symbol of b
      std::vector<std::vector<int>> table;
      table.resize(a.size() + 1, std::vector<int>(b.size() + 1, 0));
      // Fill out the base case.
      for (size_t i = 0; i < table.size(); i++) {
        table[i][0] = i;
      }
      for (size_t i = 0; i < table[0].size(); i++) {
        table[0][i] = i;
      }
      // Fill out table row by row.
      for (size_t r = 1; r < table.size(); r++) {
        for (size_t c = 1; c < table[r].size(); c++) {
          char achar = a[r - 1];
          char bchar = b[c - 1];
          if (achar == bchar) {
            table[r][c] = table[r - 1][c - 1];
          } else {
            table[r][c] = std::min({table[r - 1][c - 1] + 1, table[r][c - 1] + 1, table[r - 1][c] + 1});
          }
        }
      }
      editDistanceMemo[std::make_tuple(a, b)] = table[table.size() - 1][table[0].size() - 1];
      editDistanceMemo[std::make_tuple(b, a)] = table[table.size() - 1][table[0].size() - 1];
      return table[table.size() - 1][table[0].size() - 1];
    }

  }

  double simpleMatchingCoeff(std::string& a, std::string& b) {
    /*
      Given strings a & b, find simple matching coefficient.
      Requirements: len(a) == len(b)
                    a and b should both be bit strings.
                    len(a) <= 8
                    len(b) <= 8
     */
     auto search = simpleMatchingCoeffMemo.find(std::make_tuple(a, b));
     if (search != simpleMatchingCoeffMemo.end()) {
       // Found (a, b)
       return search->second;
     } else {
      int m11 = 0, m01 = 0, m10 = 0, m00 = 0;
      std::bitset<8> aBits(a);
      std::bitset<8> bBits(b);
      for (size_t i = 0; i < a.size(); i++) {
        if      (aBits[i] && bBits[i])   m11++;
        else if (aBits[i] && !bBits[i])  m10++;
        else if (!aBits[i] && bBits[i])  m01++;
        else if (!aBits[i] && !bBits[i]) m00++;
      }
      double result = (double)(m11 + m00) / (double)(m11 + m01 + m10 + m00);
      simpleMatchingCoeffMemo[std::make_tuple(a, b)] = result;
      simpleMatchingCoeffMemo[std::make_tuple(b, a)] = result;
      return result;
    }
  }
};

#endif
