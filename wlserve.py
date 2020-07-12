import networkx as nx
import re

games = [
    {"name":"Spanish", "lang":"es"},
    {"name":"English", "lang":"en"},
    ]

def run(letters, language, start, end):
    if len(start) == len(end):
        letters = int(len(start))
    numletter = int(letters)
    wordpattern = "^"+"."*numletter+"$"
    wordsregex = re.compile(wordpattern)

    if language in ["es","en"]:
        with open('words_{}.txt'.format(language), "r") as wordsfile:
            allwords = list(filter(wordsregex.match, [i.strip() for i in wordsfile.readlines()]))

    G=nx.Graph()
    G.add_nodes_from(allwords)
#    click.secho("Number of nodes/words "+str(G.number_of_nodes()),fg='white')

#    click.secho("Creating edges between words. This might take a while...", blink=True, bold=True)
    for w in allwords:
        replacelist = []
        for i in range(numletter):
            replacelist.append(w.replace(w[i],".",1))

        r = re.compile("|".join(replacelist))
        listofnearbywords = list(filter(r.match, allwords))

        G.add_edges_from([(w,j) for j in listofnearbywords])

#    click.echo("Number of edges "+str(G.number_of_edges()))

#    print("Most connected words", len(list(nx.connected_components(G))), list(nx.connected_components(G)))

    try:
        results = list(nx.all_shortest_paths(G,start,end))
        rs = []
#        colours = ['green','red','blue','yellow']
        for i in range(len(results)):
            r = str(i+1)+".- "+results[i][0]+" > "+" > ".join(results[i][1:-1])+" > "+results[i][-1]
            rs.append(r)
#            fgc = colours[i%len(colours)]
#            click.secho(str(i+1), bold=True,nl=False,fg=fgc)
#            click.secho(".- ", bold=True,nl=False, fg=fgc)
#            click.secho(results[i][0]+" > ", bold=True,nl=False, fg=fgc)
#            click.secho(" > ".join(results[i][1:-1]), bold=False,nl=False, fg=fgc)
#            click.secho(" > "+results[i][-1], bold=True, fg=fgc)

#        click.secho(str(i+1)+". "+" -> ".join(results[i]), fg=colours[i%len(colours)])
        return rs
    except:
        return "There is no ladder between words {} and {}".format(start,end)
#        click.echo("There is no ladder between words {} and {}".format(start,end))


if __name__=="__main__":

    print(run(4,"en","love","dead"))
