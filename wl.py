import networkx as nx
import re
import click

@click.command()
@click.option("-lt","--letters", default=4, show_default=True, help="Number of letters (program might try to infer).")
@click.option("-ln","--language", prompt="Choose en or es language", type=click.Choice(['en', 'es'], case_sensitive=True), default="en", show_default=True, help="Language dictionary en|es.")
@click.option("-s","--start", prompt="Choose initial word", default="love", show_default=True, help="Initial word.")
@click.option("-e","--end", prompt="Choose final word", default="dead", show_default=True, help="Final word.")

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
    click.secho("Number of nodes/words "+str(G.number_of_nodes()),fg='white')

    click.secho("Creating edges between words. This might take a while...", blink=True, bold=True)
    for w in allwords:
        replacelist = []
        for i in range(numletter):
            replacelist.append(w.replace(w[i],".",1))

        r = re.compile("|".join(replacelist))
        listofnearbywords = list(filter(r.match, allwords))

        G.add_edges_from([(w,j) for j in listofnearbywords])

    click.echo("Number of edges "+str(G.number_of_edges()))

#    print("Most connected words", len(list(nx.connected_components(G))), list(nx.connected_components(G)))

    try:
        results = list(nx.all_shortest_paths(G,start,end))
        colours = ['green','red','blue','yellow']
        for i in range(len(results)):
            fgc = colours[i%len(colours)]
            click.secho(str(i+1), bold=True,nl=False,fg=fgc)
            click.secho(".- ", bold=True,nl=False, fg=fgc)
            click.secho(results[i][0]+" > ", bold=True,nl=False, fg=fgc)
            click.secho(" > ".join(results[i][1:-1]), bold=False,nl=False, fg=fgc)
            click.secho(" > "+results[i][-1], bold=True, fg=fgc)

#        click.secho(str(i+1)+". "+" -> ".join(results[i]), fg=colours[i%len(colours)])
    except:
        click.echo("There is no ladder between words {} and {}".format(start,end))


if __name__=="__main__":

    run()
