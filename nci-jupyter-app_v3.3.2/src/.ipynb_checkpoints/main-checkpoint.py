import os
import pandas as pd
import numpy as np

def callName(n):

    if '_benzene_' in n or '_benzene' in n:
        n_ = n.split('_')[:n.split('_').index('benzene')]
        return '_'.join(n_)
    elif n.lower() == 'benzene' or n.lower() == 'h':
        return 'benzene'
    elif n.lower() == 'me' or n.lower() == 'ch3':
        return 'me'
    elif '_BA' in n:
            n_ = n.split('_')[:-1]
            return '_'.join(n_)
    else:
        return n

def readOptional(ref, h_sht, esp_sht):

    path = os.path.join(os.getcwd(), ref)

    ## read file ##
    df_h = pd.read_excel(path, h_sht, usecols=['Arene Fragment or Substituent',
                                                    'σp',
                                                    'σm',
                                                    'σ+p',
                                                    'σ-p',
                                                    'σ+m'])
    df_esp = pd.read_excel(path, esp_sht, usecols=['Arene Fragment or Substituent',
                                                    'ESP at 2.4 Å',
                                                    'Quadrupole Moment',
                                                    'Sterimol L',
                                                    'Sterimol B1',
                                                    'Sterimol B5',
                                                    'HOMO',
                                                    'LUMO'])
    df_opt = df_esp.merge(df_h, how='inner', on='Arene Fragment or Substituent')

    ## replace names with callable ##
    for i, row in df_opt.iterrows():
        n = callName(row['Arene Fragment or Substituent'])
        df_opt.loc[i,['Arene Fragment or Substituent']] = n

    return df_opt

def readRef(ref, ref_sht):

    ## check for file in path ##
    path = os.path.join(os.getcwd(), ref)
    try:
        os.path.isfile(path)
    except FileNotFoundError:
        print("Library file not found in directory")
        exit()

    ## read file ##
    df_ref = pd.read_excel(path, ref_sht, usecols=['Arene Fragment or Substituent', 'Probe',
                                                    'Dmin (pm)',
                                                    'Electrostatic E (kcal/mol)',
                                                    'Exchange E (kcal/mol)',
                                                    'Induction E (kcal/mol)',
                                                    'Dispersion E (kcal/mol)',
                                                    'Total E (kcal/mol)'])

    ## replace names with callable ##
    for i, row in df_ref.iterrows():
        n = callName(row['Arene Fragment or Substituent'])
        df_ref.loc[i,['Arene Fragment or Substituent']] = n

    return df_ref

def readInp(inp, inp_sht):

    ## check for file in path ##
    path = os.path.join(os.getcwd(), inp)
    try:
        os.path.isfile(path)
    except FileNotFoundError:
        print("Input file not found in directory")
        exit()

    ## read file ##
    df_inp = pd.read_excel(path, inp_sht, usecols=['Arene Fragment or Substituent', 'Experimental Data'])

    ## replace names with callable ##
    for i, row in df_inp.iterrows():
        n = callName(row['Arene Fragment or Substituent'])
        df_inp.loc[i,['Arene Fragment or Substituent']] = n

    return df_inp

def findMatch(df_inp, df_ref, df_h):

    df_match = pd.merge(df_inp, df_ref, how='inner', on=['Arene Fragment or Substituent'])

    df_h_match=None
    if type(df_h) != bool:
        df_h_match = pd.merge(df_inp, df_h, how='inner', on=['Arene Fragment or Substituent'])

    return (df_match, df_h_match)

def READ(ref, inp, inp_sht, nci_, nrg_):

    ref_sht = "BA'd Library"
    h_sht = "Hammett"
    esp_sht = "ESP"
    if 'anion-pi' == nci_.lower():
        ref_sht = "Fixed Distance Anion-pi"

    ## read files ##
    df_inp = readInp(inp, inp_sht)
    df_ref = readRef(ref, ref_sht)
    df_opt = readOptional(ref, h_sht, esp_sht)

    nci_switcher = {
    'all': df_ref['Probe'].unique(),
    'cation-pi': [i for i in df_ref['Probe'].unique() if '+' in i],
    'anion-pi': [i for i in df_ref['Probe'].unique() if ' –' in i],
    'anion-pi weighted': [i for i in df_ref['Probe'].unique() if ' –' in i],
    'pi-pi':[i for i in df_ref['Probe'].unique() if 'π' in i],
    'ch-pi':[i for i in df_ref['Probe'].unique() if 'C–H axis' in i or 'CH3' in i]
    }

    nrg_switcher = {
    'electrostatic': 'Electrostatic E (kcal/mol)',
    'exchange': 'Exchange E (kcal/mol)',
    'dispersion': 'Dispersion E (kcal/mol)',
    'induction': 'Induction E (kcal/mol)',
    'total interaction energy': 'Total E (kcal/mol)',
    'distance': 'Dmin (pm)'
    }

    df_ref_ = df_ref[df_ref['Probe'].isin(nci_switcher[nci_.lower()])][['Arene Fragment or Substituent','Probe',nrg_switcher[nrg_.lower()]]].dropna()

    return (df_ref_, df_inp, df_opt)

if __name__ == '__main__':
    print('oops, only jupyter notebook compatible right now!')
