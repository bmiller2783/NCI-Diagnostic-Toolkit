import os
import pandas as pd
import numpy as np

#from sklearn.metrics import r2_score
from scipy.stats import linregress as lr
#import statsmodels.api as sm
#import statsmodels.formula.api as smf
#from sklearn.preprocessing import PolynomialFeatures

def CORRELOPT(df_ref, df_inp):

    df_opt = pd.merge(df_ref, df_inp, how='inner', on=['Arene Fragment or Substituent']).dropna()

    params = df_ref.columns[1:-1]

    df_correls = {'Parameter':[], 'Pearson R':[], 'R^2':[], "Spearman's Rho":[]}
    df_plots = {}
    #print(df_ref)
    for p in params:
        df_correls['Parameter'].append(p)
        df_plots[p] = {}

        df_ = df_opt.dropna()
        df_plots[p]['Arene Fragment or Substituent'] = df_['Arene Fragment or Substituent']

        x = df_[p].astype(float)
        y = df_['Experimental Data'].astype(float)
        df_plots[p]['X'] = x
        df_plots[p]['Y'] = y

        # Spearman
        df_plots[p]['X_rank'] = x.rank()
        df_plots[p]['Y_rank'] = y.rank()
        m_r, b_r, r2_r_, p_R, std_err_r = lr(df_plots[p]['X_rank'], df_plots[p]['Y_rank'])

        rho = x.corr(y, method='spearman')
        df_correls["Spearman's Rho"].append(rho)
        df_plots[p]["Spearman's Rho"] = rho
        y_rank_pred = (m_r * df_plots[p]['X_rank']) + b_r
        df_plots[p]['Y_rank_pred'] = y_rank_pred
        # Pearson
        r = x.corr(y, method='pearson')
        df_correls['Pearson R'].append(r)
        df_plots[p]['Pearson R'] = r

        # fit linear
        m, b, r2_, p_, std_err = lr(x, y)

        # Determinant
        r2 = r2_**2
        df_correls['R^2'].append(r2)
        df_plots[p]['R^2'] = r2

        y_pred = (m * x) + b
        df_plots[p]['Y_pred'] = y_pred

    return (pd.DataFrame(df_correls), pd.DataFrame(df_plots))

def CORREL(df_ref, df_inp, nci_, nrg_):

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

    df_ref = df_ref.merge(df_inp, how='inner', on='Arene Fragment or Substituent')

    df_correls = {'Probe':[], 'Pearson R':[], 'R^2':[], "Spearman's Rho":[], 'Residual R^2':[], 'NCI Score':[]}
    df_plots = {}
    # for each probe
    for p in nci_switcher[nci_.lower()]:
        df_correls['Probe'].append(p)
        df_plots[p] = {}

        df_ = df_ref[df_ref['Probe'] == p].dropna()
        df_plots[p]['Arene Fragment or Substituent'] = df_['Arene Fragment or Substituent']

        x = df_[nrg_switcher[nrg_.lower()]].astype(float)
        y = df_['Experimental Data'].astype(float)
        df_plots[p]['X'] = x
        df_plots[p]['Y'] = y

        # Spearman
        df_plots[p]['X_rank'] = x.rank()
        df_plots[p]['Y_rank'] = y.rank()
        m_r, b_r, r2_r_, p_R, std_err_r = lr(df_plots[p]['X_rank'], df_plots[p]['Y_rank'])

        rho = x.corr(y, method='spearman')
        df_correls["Spearman's Rho"].append(rho)
        df_plots[p]["Spearman's Rho"] = rho
        y_rank_pred = (m_r * df_plots[p]['X_rank']) + b_r
        df_plots[p]['Y_rank_pred'] = y_rank_pred
        # Pearson
        r = x.corr(y, method='pearson')
        df_correls['Pearson R'].append(r)
        df_plots[p]['Pearson R'] = r

        # fit linear
        m, b, r2_, p_, std_err = lr(x, y)

        # Determinant
        r2 = r2_**2
        df_correls['R^2'].append(r2)
        df_plots[p]['R^2'] = r2

        y_pred = (m * x) + b
        df_plots[p]['Y_pred'] = y_pred
        resids = y - y_pred
        df_plots[p]['Y_resid'] = resids
        #df_plots[p]['Xpos'] = [x.iloc(i) for i in range(len(resids)) if float(resids.iloc(i)) >= 0]
        #df_plots[p]['Xneg'] = [x.iloc(i) for i in range(len(resids)) if float(resids.iloc(i)) < 0]

        poly = np.poly1d(np.polyfit(y, resids, 2))
        #eqn = a2 * np.square(resids) + b2 * resids + c2
        #y_resid = a2 * np.square(resids) + b2 * resids + c2

        m_p, b_p, r2_p_, p_p, std_err_p = lr(resids, poly(y))
        r2_p = r2_p_**2
        df_correls['Residual R^2'].append(r2_p)

        y_resid_pred = poly(y)
        df_plots[p]['Y_resid_pred'] = y_resid_pred

        nci_score = (abs(rho) + (r2 - r2_p)) / 2

        df_correls['NCI Score'].append(nci_score)

    return (pd.DataFrame(df_correls), pd.DataFrame(df_plots))

if __name__ == '__main__':
    print('oops, only jupyter notebook compatible right now!')
