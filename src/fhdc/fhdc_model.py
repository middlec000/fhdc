from typing import Dict, List
from data_classes import \
    Vocabulary, \
    Corpus, \
    Level, \
    Cluster
from clustering import agglomerative_cluster

num_items_to_print = 10

class FHDC_Model():
    vocabulary: Vocabulary
    corpus: Corpus
    levels: Dict[int, Level] # {level_id: Level}

    def __init__(self, corpus: Corpus, vocabulary: Vocabulary):
        self.corpus = corpus
        self.vocabulary = vocabulary
        self.levels = None
        self.distance_matrix = None
        return

    def __str__(self, verbosity: int=0) -> str:
        fhdc_model_string = f"Levels:\n"
        for i in range(num_items_to_print):
            if i in self.levels:
                fhdc_model_string += self.levels[i].__str__(verbosity=verbosity)
        fhdc_model_string += '...\n'
        return fhdc_model_string
    
    def cluster(self, cluster_type: str='agglomerative', stop_num_clusters: int=None)-> None:
        """Cluster documents in corpus using the specified cluster_type.

        Args:
            cluster_type (str, optional): Chosen clustering method. Defaults to 'agglomerative'.
            stop_num_clusters (int, optional): Controls if and when to stop clustering early. Passed on to the specific clustering method used. Defaults to None.
        """
        if cluster_type == 'agglomerative':
            self.levels, self.distance_matrix = agglomerative_cluster(self.corpus, stop_num_clusters=stop_num_clusters)
        else:
            print('Clustering type not supported.\n')
        return
    
    def get_cluster(self, cluster_id: int) -> Cluster:
        """Returns a cluster with the specified cluster_id in any Level

        Args:
            cluster_id (int): ID of the cluster to be located and returned.

        Returns:
            Cluster: The specified cluster.
        """
        for level in self.levels:
            if cluster_id in self.levels[level].clusters:
                return self.levels[level].clusters[cluster_id]

    def summary(self, levels: List=None, clusters: List=None, verbosity: int=0) -> str:
        """Creates and returns a summary string of the clustering history. The summary can focus on specific levels or clusters by using the optional levels and clusters variables. The detail of the summary is determined by the verbosity variable.

        Args:
            levels (List, optional): Specific levels to summarize. Defaults to None.
            clusters (List, optional): Specific clusters to summarize. Defaults to None.
            verbosity (int, optional): Level of detail to provide. Defaults to 0.
                TODO: add to verbosity description

        Returns:
            str: Summary of clustering history.
        """
        #TODO: add print to file
        cumulative_string = ''
        if (levels is None) and (clusters is None):
            return self.__str__(verbosity=verbosity)
        elif not (levels is None) and not (clusters is None):
            cumulative_string += 'Please choose either levels or clusters.\n'
        else:
            if not (levels is None):
                for level in levels:
                    cumulative_string += self.levels[level].__str__(verbosity=verbosity)
            elif not (clusters is None):
                for cluster_id in clusters:
                    cumulative_string += self.get_cluster(cluster_id=cluster_id).__str__(verbosity=verbosity)
        return cumulative_string
