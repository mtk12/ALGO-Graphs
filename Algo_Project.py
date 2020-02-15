from flask import Flask, render_template,request
import plotly
import plotly.graph_objs as go
import networkx as nx
from plotly.offline import download_plotlyjs, init_notebook_mode,  iplot, plot
import pandas as pd
import numpy as np
import json
import os
from networkx.algorithms import tree
app = Flask(__name__)

globalvar = ""
 
@app.route('/')
def index():
    feature = 'Bar'
    bar = create_plot(feature,"")
    return render_template('index.html', plot=bar)

def adjency_matrix(edges,n):
    Ad = np.zeros(shape=(n,n))
    count=0
    all_edges=edges[0].split("\r\n")
    for x in range(0,len(all_edges)):
        single_edge=all_edges[x].split("\t")
        for i in range(0,len(single_edge)-1):
            ed=(i+1)%2
            if(ed==0):
                if(count==0):
                    e=int(single_edge[i])
                    count=1
                else:
                    Ad[int(single_edge[0])][int(e)]=float(single_edge[i])
                    count=0
    return Ad

def creategraph(algo,data):
    file = data
    a1  = []
    a2 = []
    a3 = []
    a4 = []
    a5 = []
    splat = file.split("\r\n\r\n")
    for number, section in enumerate(splat, 1):
        if number % 5 == 1:
            a1 += [section]
        elif number % 5 == 2:
            a2 += [section]
        elif number % 5 == 3:
            a3 += [section]
        elif number % 5 == 4:
            a4 += [section]
        elif number % 5 == 0:
            a5 += [section]
        
    a2=int(a2[0])
    a5=int(a5[0])
    Ad=adjency_matrix(a4,a2)
    G=nx.from_numpy_matrix(Ad)
    labels=[]
    a3 = a3[0].split("\r\n")
    Xn = []
    Yn = []
    for i in range(0,a2):
        a3[i] = a3[i].split("\t")
        Xn.append(float(a3[i][1]))
        Yn.append(float(a3[i][2]))
        
    for i in range(0,a2):
        labels.append(i)
    
    if algo == "Prims":
         mst = tree.minimum_spanning_edges(G, algorithm='prim', data=False)
         path = list(mst)
         length = 0
         for i in range(0,len(path)):
             length = length + Ad[path[i][0]][path[i][1]]
         title = "Prims Cost : " + str(length)
         Xe=[]
         Ye=[]
         Xe2 = []
         Ye2 = []
         for e in G.edges():
             for i in range(0,len(path)-1):
                 if (e[0]==path[i][0] and e[1]==path[i+1][1]):
                     Xe2.extend([Xn[e[0]], Xn[e[1]], None])
                     Ye2.extend([Yn[e[0]], Yn[e[1]], None])
             Xe.extend([Xn[e[0]], Xn[e[1]], None])
             Ye.extend([Yn[e[0]], Yn[e[1]], None])
    elif algo == "Kruskals":
         mst = tree.minimum_spanning_edges(G, algorithm='prim', data=False)
         path = list(mst)
         length = 0
         for i in range(0,len(path)):
             length = length + Ad[path[i][0]][path[i][1]]
         title = "Kruskal Cost : " + str(length)
         Xe=[]
         Ye=[]
         Xe2 = []
         Ye2 = []
         for e in G.edges():
             for i in range(0,len(path)-1):
                 if (e[0]==path[i][0] and e[1]==path[i+1][1]):
                     Xe2.extend([Xn[e[0]], Xn[e[1]], None])
                     Ye2.extend([Yn[e[0]], Yn[e[1]], None])
             Xe.extend([Xn[e[0]], Xn[e[1]], None])
             Ye.extend([Yn[e[0]], Yn[e[1]], None])
    elif algo == "Dijkstra":
        length,path=nx.bidirectional_dijkstra(G,a5,a2-1)
        title = "Dijkstra Cost : " + str(length)
        Xe=[]
        Ye=[]
        Xe2 = []
        Ye2 = []
        for e in G.edges():
            for i in range(0,len(path)-1):
                if (e[0]==path[i] and e[1]==path[i+1]):
                    Xe2.extend([Xn[e[0]], Xn[e[1]], None])
                    Ye2.extend([Yn[e[0]], Yn[e[1]], None])
            Xe.extend([Xn[e[0]], Xn[e[1]], None])
            Ye.extend([Yn[e[0]], Yn[e[1]], None])
    elif algo=="Bellman Ford":
        length, path = nx.single_source_bellman_ford(G, 6, a2-1)
        title = "Bellman Ford Cost : " + str(length)
        Xe=[]
        Ye=[]
        Xe2 = []
        Ye2 = []
        for e in G.edges():
            for i in range(0,len(path)-1):
                if (e[0]==path[i] and e[1]==path[i+1]):
                    Xe2.extend([Xn[e[0]], Xn[e[1]], None])
                    Ye2.extend([Yn[e[0]], Yn[e[1]], None])
            Xe.extend([Xn[e[0]], Xn[e[1]], None])
            Ye.extend([Yn[e[0]], Yn[e[1]], None])
    elif algo == "Floyd Warshall":
        path = nx.floyd_warshall_numpy(G)
        np.fill_diagonal(path,path.max())
        title = "Floyd Warshall Cost : " + str(path.min())
        Xe=[]
        Ye=[]
        Xe2 = []
        Ye2 = []
        for e in G.edges():
            Xe.extend([Xn[e[0]], Xn[e[1]], None])
            Ye.extend([Yn[e[0]], Yn[e[1]], None])
    elif algo=="Clustering":
        c = nx.average_clustering(G)
        title = "Clustering Cost : " + str(c)
        Xe=[]
        Ye=[]
        Xe2 = []
        Ye2 = []
        for e in G.edges():
            Xe.extend([Xn[e[0]], Xn[e[1]], None])
            Ye.extend([Yn[e[0]], Yn[e[1]], None])
        
    trace_nodes=dict(type='scatter',
                  x=Xn, 
                  y=Yn,
                  mode='markers',
                  marker=dict(size=28, color='peru'),
                  text=labels,
                  hoverinfo='text')
     
    trace_edges=dict(type='scatter',
             mode='lines',
             arrowstyle='->',
             x=Xe,
             y=Ye,
             line=dict(width=1, color='royalblue'),
             hoverinfo='none' 
             )
    
    trace_edges2=dict(type='scatter',
                 mode='lines',
                 x=Xe2,
                 y=Ye2,
                 line=dict(width=4.1,color="firebrick"),
                 hoverinfo='none' 
                )
    axis=dict(showline=True, # hide axis line, grid, ticklabels and  title
              zeroline=False,
              showgrid=True,
              showticklabels=True,
              title='' 
              )
    
    layout=dict(title= title,  
                font= dict(family='Balto'),
                showlegend=True,
                xaxis=axis,
                yaxis=axis,
                )
      
    annotations = []
    for k in range(a2):
        annotations.append(dict(text=labels[k], 
                                x=Xn[k], 
                                y=Yn[k],#this additional value is chosen by trial and error
                                xref='x1', yref='y1',
                                font=dict(color= 'rgb(10,10,10)', size=14),
                                showarrow=False)
                            )
    data = dict(data=[trace_edges, trace_edges2, trace_nodes],layout=layout)
    data['layout'].update(annotations=annotations)
    return data

def create_plot(feature,data):
    if feature == 'Bar':
        G=nx.Graph()
        Xn = []
        Yn = []
        trace_nodes=dict(type='scatter',
                 x=Xn, 
                 y=Yn,
                 mode='markers',
                 marker=dict(size=28, color='rgb(255,0,0)'),
                 hoverinfo='text')
        Xe=[]
        Ye=[]
        trace_edges=dict(type='scatter',
                 mode='lines',
                 x=Xe,
                 y=Ye,
                 line=dict(width=2, color='rgb(25,25,25)'),
                 hoverinfo='none' 
                )

        data = dict(data=[trace_edges, trace_nodes])
    else:
        data=creategraph(feature,data)
        
    
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@app.route('/bar', methods=['GET', 'POST'])
def change_features():

    feature = request.args['selected']
    global globarvar
    data = globalvar
    graphJSON= create_plot(feature,data)
    
    return graphJSON

APP_ROOT = os.path.dirname(os.path.abspath("app.py"))
@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, "testcase/")
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)
    obj=request.files['file'].read()
    obj = str(obj, 'utf-8')
    global globalvar
    globalvar = obj
    
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
