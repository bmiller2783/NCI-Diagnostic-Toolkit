import os
import pandas as pd
import numpy as np

#from plotly.offline import init_notebook_mode, iplot
from plotly.graph_objs import Table, Figure, Scatter, Bar
import plotly.express as px
from plotly.subplots import make_subplots

#init_notebook_mode(connected=True)
def TABLEOPT(df_correls):

    CSS = {'red':'IndianRed', 'green':'SeaGreen', 'yellow':'Gold', 'orange':'SandyBrown'}

    colors = {'Pearson R':[], 'R^2':[], "Spearman's Rho":[]}
    for col in list(colors.keys()):
        for i, row in df_correls.iterrows():
            if col == 'R^2':
                if float(row[col]) <= 0:
                    colors[col].append(CSS['red'])
                elif float(row[col]) <= 0.5:
                    colors[col].append(CSS['orange'])
                elif float(row[col]) <= 0.85:
                    colors[col].append(CSS['yellow'])
                elif float(row[col]) <= 1.0:
                    colors[col].append(CSS['green'])
                else:
                    colors[col].append('white')
            elif col == 'Pearson R' or col == "Spearman's Rho":
                if abs(float(row[col])) <= 0:
                    colors[col].append(CSS['red'])
                elif abs(float(row[col])) <= 0.5:
                    colors[col].append(CSS['orange'])
                elif abs(float(row[col])) <= 0.85:
                    colors[col].append(CSS['yellow'])
                elif abs(float(row[col])) <= 1.0:
                    colors[col].append(CSS['green'])
                else:
                    colors[col].append('white')

    # display table
    table = Figure(data=[Table(header=dict(fill_color=['LightSteelBlue','LightSteelBlue','LightSteelBlue','LightSteelBlue'], values=list(df_correls.columns)),
                        cells=dict(values=[df_correls['Parameter'], df_correls['Pearson R'].round(2), df_correls['R^2'].round(2), df_correls["Spearman's Rho"].round(2)],
                                    fill_color=[['lightgray'for i in range(len(colors['Pearson R']))],colors['Pearson R'],colors['R^2'],colors["Spearman's Rho"]])
                        )])
    table.update_layout(height=300,
                        font=dict(size=14,color='black'),
                        margin=dict(l=20, r=20, t=50, b=20),
                        title=dict(text='Correlation Summary Table',x=0.5,xanchor='center',yanchor='top')
                        )
    table.show()

def TABLE(df_correls):

    df_correls = df_correls.sort_values(by=['NCI Score'],ascending=False)

    CSS = {'red':'IndianRed', 'green':'SeaGreen', 'yellow':'Gold', 'orange':'SandyBrown'}

    colors = {'Pearson R':[], 'R^2':[], "Spearman's Rho":[], 'Residual R^2':[], 'NCI Score':[]}
    for col in list(colors.keys()):
        for i, row in df_correls.iterrows():
            if col == 'R^2' or col == 'NCI Score':
                if float(row[col]) <= 0:
                    colors[col].append(CSS['red'])
                elif float(row[col]) <= 0.5:
                    colors[col].append(CSS['orange'])
                elif float(row[col]) <= 0.85:
                    colors[col].append(CSS['yellow'])
                elif float(row[col]) <= 1.0:
                    colors[col].append(CSS['green'])
                else:
                    colors[col].append('white')
            elif col == 'Residual R^2':
                if float(row[col]) <= 0:
                    colors[col].append(CSS['green'])
                elif float(row[col]) <= 0.5:
                    colors[col].append(CSS['yellow'])
                elif float(row[col]) <= 0.85:
                    colors[col].append(CSS['orange'])
                elif float(row[col]) <= 1.0:
                    colors[col].append(CSS['red'])
                else:
                    colors[col].append('white')
            elif col == 'Pearson R' or col == "Spearman's Rho":
                if abs(float(row[col])) <= 0:
                    colors[col].append(CSS['red'])
                elif abs(float(row[col])) <= 0.5:
                    colors[col].append(CSS['orange'])
                elif abs(float(row[col])) <= 0.85:
                    colors[col].append(CSS['yellow'])
                elif abs(float(row[col])) <= 1.0:
                    colors[col].append(CSS['green'])
                else:
                    colors[col].append('white')

    # display table
    table = Figure(data=[Table(header=dict(fill_color=['LightSteelBlue','LightSteelBlue','LightSteelBlue','LightSteelBlue','LightSteelBlue','CornflowerBlue'], values=list(df_correls.columns)),
                        cells=dict(values=[df_correls['Probe'], df_correls['Pearson R'].round(2), df_correls['R^2'].round(2), df_correls["Spearman's Rho"].round(2), df_correls['Residual R^2'].round(2), df_correls['NCI Score'].round(2)],
                                    fill_color=[['lightgray'for i in range(len(colors['Pearson R']))],colors['Pearson R'],colors['R^2'],colors["Spearman's Rho"],colors['Residual R^2'], colors['NCI Score']])
                        )])
    table.update_layout(height=300,
                        font=dict(size=14,color='black'),
                        margin=dict(l=20, r=20, t=50, b=20),
                        title=dict(text='Correlation Summary Table',x=0.5,xanchor='center',yanchor='top')
                        )
    table.show()

def PLOT(df_plots, nrg_):

    fig = make_subplots(subplot_titles=['Plot'+str(i) for i in range(3*len(list(df_plots.keys())))],horizontal_spacing=0.15,
                    rows=2*len(list(df_plots.keys())), cols=3)

    count = 0
    for p in list(df_plots.keys()):
        #linear
        fig.add_trace(Scatter(x=df_plots[p]['X'], y=df_plots[p]['Y'], mode='markers',
                                text = df_plots[p]['Arene Fragment or Substituent'],
                                name=p,
                                hoverinfo = 'text+y',
                                marker = {'color': 'black',
                                          'size': 8
                                         }
                                ), row=count+1, col=1)
        #linear fit
        fig.add_trace(Scatter(x=df_plots[p]['X'], y=df_plots[p]['Y_pred'], mode='lines',
                                text='R^2='+str(round(df_plots[p]['R^2'], 2)),
                                marker = {'color': 'red'}
                                ), row=count+1, col=1)
        fig.add_annotation(x=1, y=1, xref='x domain',yref='y domain',showarrow=False,
                                text='R^2='+str(round(df_plots[p]['R^2'], 2)),
                                font=dict(size=16,color='white'),bordercolor='black',bgcolor='gray', borderpad=2,
                                row=count+1, col=1)
        #linear residual
        fig.add_trace(Scatter(x=df_plots[p]['X'], y=df_plots[p]['Y_resid'], mode='markers',
                                text = df_plots[p]['Arene Fragment or Substituent'],
                                name=p,
                                hoverinfo = 'text+y',
                                marker = {'color': 'black',
                                          'size': 8
                                         }
                                ), row=count+1, col=2)
        #linear fit (y=0)
        fig.add_trace(Scatter(x=df_plots[p]['X'], y=[0 for i in df_plots[p]['X']], mode='lines',
                                marker = {'color': 'red'}
                                ), row=count+1, col=2)
        #rank
        fig.add_trace(Scatter(x=df_plots[p]['X_rank'], y=df_plots[p]['Y_rank'], mode='markers',
                                text = df_plots[p]['Arene Fragment or Substituent'],
                                name=p,
                                hoverinfo = 'text+x+y',
                                marker = {'color': 'green',
                                          'size': 8
                                         }
                                ), row=count+1, col=3)
        #rank fit
        fig.add_trace(Scatter(x=df_plots[p]['X_rank'], y=df_plots[p]['Y_rank_pred'], mode='lines',
                                text='Rho='+str(round(df_plots[p]["Spearman's Rho"], 2)),
                                marker = {'color': 'blue'}
                                ), row=count+1, col=3)
        fig.add_annotation(x=1, y=1, xref='x domain',yref='y domain',showarrow=False,
                                text='Rho='+str(round(df_plots[p]["Spearman's Rho"], 2)),
                                font=dict(size=16,color='white'),bordercolor='black',bgcolor='gray', borderpad=2,
                                row=count+1, col=3)

        fig.layout.annotations[3*count].text = p+' Linear Plot'
        fig.layout.annotations[3*count].font = {'size':14}
        fig.layout.annotations[(3*count)+1].text = p+' Residual Plot'
        fig.layout.annotations[(3*count)+1].font = {'size':14}
        fig.layout.annotations[(3*count)+2].text = p+' Rank Plot'
        fig.layout.annotations[(3*count)+2].font = {'size':14}

        fig.layout['xaxis'+str((3*count)+1)].update(title_text=nrg_)
        fig.layout['xaxis'+str((3*count)+1)].title.font = {'size':12}
        fig.layout['yaxis'+str((3*count)+1)].update(title_text='Experimental Data (kcal/mol)')
        fig.layout['yaxis'+str((3*count)+1)].title.font = {'size':12}
        fig.layout['xaxis'+str((3*count)+2)].update(title_text=nrg_+' Residual')
        fig.layout['xaxis'+str((3*count)+2)].title.font = {'size':12}
        fig.layout['yaxis'+str((3*count)+2)].update(title_text='Residual')
        fig.layout['yaxis'+str((3*count)+2)].title.font = {'size':12}
        fig.layout['xaxis'+str((3*count)+3)].update(title_text=nrg_+' Rank')
        fig.layout['xaxis'+str((3*count)+3)].title.font = {'size':12}
        fig.layout['yaxis'+str((3*count)+3)].update(title_text='Rank')
        fig.layout['yaxis'+str((3*count)+3)].title.font = {'size':12}
        count+=1
    fig.update_layout(showlegend=False,height=len(list(df_plots.keys()))*1000,
                        title=dict(text=nrg_+' Correlation Plots',x=0.5,xanchor='center',yanchor='top'))
    #fig.update_traces(marker=dict(color='red'),line=dict(color='black'))
    fig.show()

def ranks():
    print('hi')


if __name__ == '__main__':
    print('oops, only jupyter notebook compatible right now!')
