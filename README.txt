# ClusteringGenomes
Clustering algorithms for CSE 881

Clustering Algorithms take a DistanceMetric, return a vector of assignments 
  Should inherit from ClusteringAlgorithm 

DistanceMetric must implement getDistance(vector<string>, vector<string>) and should return a positive double distance 
  Should inherit from DistanceMetric

For DBScan, the 0 cluster is noise points 

