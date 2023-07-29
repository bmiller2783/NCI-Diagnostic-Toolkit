import pandas as pd
import numpy as np

from scipy.stats import linregress as lr

def main(df_h):

    df_correls_h = {'Probe':[], 'Pearson R':[], 'Determinant R^2':[], "Spearman's Rho":[]}
    df_plots_h = {}
    for s in ['σp','σm','σ+p','σ-p','σ+m']:
      df_correls_h['Probe'].append(s)
      df_plots_h[s] = {}
      df_plots_h[s]['Arene Fragment or Substituent'] = df_h['Arene Fragment or Substituent']

      x = df_h[s].astype(float)
      y = df_h['Experimental Data'].astype(float)
      df_plots_h[s]['X'] = x
      df_plots_h[s]['Y'] = y

      # fit linear
      m, b, r2_, p_, std_err = lr(x, y)

      # Determinant
      r2 = r2_**2
      df_correls_h['Determinant R^2'].append(r2)
      df_plots_h[s]['Determinant R^2'] = r2
      df_plots_h[s]['X_rank'] = x.rank()
      df_plots_h[s]['Y_rank'] = y.rank()
      m_r, b_r, r2_r_, p_R, std_err_r = lr(df_plots_h[s]['X_rank'], df_plots_h[s]['Y_rank'])

      # Spearman
      rho = x.corr(y, method='spearman')
      df_correls_h["Spearman's Rho"].append(rho)
      df_plots_h[s]["Spearman's Rho"] = rho
      y_rank_pred = (m_r * df_plots_h[s]['X_rank']) + b_r
      df_plots_h[s]['Y_rank_pred'] = y_rank_pred

      # Pearson
      r = x.corr(y, method='pearson')
      df_correls_h['Pearson R'].append(r)
      df_plots_h[s]['Pearson R'] = r

      return (pd.DataFrame(df_correls), pd.DataFrame(df_plots))
