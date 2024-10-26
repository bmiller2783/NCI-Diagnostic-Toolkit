##### Main Script to Call Handling Modules #####
# Miller; B
# Version: v3.3.2
# Updated: July 2023

import os
SCRIPT_DIR = os.path.join(os.getcwd(), 'src')
import main, correl, plot, hammett

def LoadData(ref, inp, inp_sht, nci_='All', nrg_='Total Interaction Energy'):

    ## gather data ##
    df_ref, df_inp, df_opt = main.READ(ref, inp, inp_sht, nci_, nrg_)

    ## check for no match ##
    df_NOTFND = df_inp[~df_inp['Arene Fragment or Substituent'].isin(df_ref['Arene Fragment or Substituent'])]

    if df_NOTFND.empty == False:
        print('Not Found in Library:\n')
        print(df_NOTFND)
        print('\n check name/spelling with Avaliable Functional Group Names')
        print('\nContinue with Remaining Data?\n')
        print(df_inp)
    else:
        print(df_inp)
        print('\nData Loaded\n')

    return(df_ref, df_inp, df_opt)

def PrintCallNames(df_ref, nrg_):
    import pandas as pd

    df_ref_ = df_ref.drop_duplicates(subset=['Arene Fragment or Substituent'])

    print('Avaliable Input Names for '+nrg_+':\n')
    print('\n'.join(list(df_ref_['Arene Fragment or Substituent'])))

def Run(df_ref, df_inp, nci_='All', nrg_='Total Interaction Energy'):

    ## calculate correls ##
    df_correl, df_plot = correl.CORREL(df_ref, df_inp, nci_, nrg_)

    ## make correl table ##
    plot.TABLE(df_correl)

    ## make SORTED correl table ##
    #plot.SORTEDtable(df_correls)

    ## make plots ##
    plot.PLOT(df_plot, nrg_)

def RunOptional(df_opt, df_inp):

    ## calculate correls ##
    df_correl, df_plot = correl.CORRELOPT(df_opt, df_inp)

    ## make correl table ##
    plot.TABLEOPT(df_correl)

    ## make plots ##
    #plot.PLOT(df_plot)

if __name__ == '__main__':
    print('oops, only jupyter notebook compatible right now!')
