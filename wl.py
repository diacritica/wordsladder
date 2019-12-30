import networkx as nx
import re


if __name__=="__main__":

    #First extract words with N letters
    
    numletter = int(input("Number of letters: "))
    wordpattern = "^"+"."*numletter+"$"
    wordsregex = re.compile(wordpattern)
    
    with open('words.txt', "r") as wordsfile:
        allwords = list(filter(wordsregex.match, [i.strip() for i in wordsfile.readlines()]))
    
    G=nx.Graph()
    G.add_nodes_from(allwords)
    print("Number of nodes/words",G.number_of_nodes())

    #Then find nearby words per word and inject as edges

    print("Creating edges between words. This might take a while...")
    for w in allwords:
        replacelist = []
        for i in range(numletter):
            replacelist.append(w.replace(w[i],".",1))

        r = re.compile("|".join(replacelist))
        listofnearbywords = list(filter(r.match, allwords))

        G.add_edges_from([(w,j) for j in listofnearbywords])

    print("Number of edges",G.number_of_edges())

#    print("Most connected words", len(list(nx.connected_components(G))), list(nx.connected_components(G)))

    while True:
        word1 = input("Initial word: ")
        word2 = input("Final word: ")
        try:
            print(list(nx.all_shortest_paths(G,word1,word2)))
        except:
            print("There is no ladder between words {} and {}".format(word1,word2))
