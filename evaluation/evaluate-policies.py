import pandas as pd
import numpy as np
from pathlib import Path

# Inputs
valtargt_file = 'http://kdd.ics.uci.edu/databases/kddcup98/epsilon_mirror/valtargt.txt'
val_pred_file = str(Path.home()) + '/kddcup98/data/val_binary_preds.csv'



#####################
# Load data
#####################

valtargt = pd.read_csv(valtargt_file)

val_preds = pd.read_csv(val_pred_file, header=None)
val_preds.columns = ['pred_vw']

val_preds['pred_model'] = val_preds['pred_vw'] - 1

val_preds['pred_model'].sum()
# 2413


[x.shape for x in [valtargt, val_preds]]
# [(96367, 3), (96367, 1)]

valtargt['TARGET_B'].value_counts()
# 0    91494
# 1     4873

valtargt['TARGET_B'].value_counts(normalize=True)
# 0    0.949433
# 1    0.050567

val_preds['pred_model'].value_counts()
# 0    93954
# 1     2413

val_preds['pred_model'].value_counts(normalize=True)
# 0    0.97496
# 1    0.02504






#####################
# Compare policies
#####################

comparison = pd.DataFrame({'actual' : valtargt['TARGET_B'],
  'model' : val_preds['pred_model']})

comparison['random'] = comparison['model'].sample(frac=1, random_state=666)\
.reset_index(drop=True)

round(len(comparison.loc[comparison.actual == comparison.random]) /
  len(comparison), 5)
# 0.9273

round(len(comparison.loc[comparison.actual == comparison.model]) /
  len(comparison), 5)
# 0.92701

round(len(comparison.loc[comparison.random == comparison.model]) /
  len(comparison), 5)
# 0.95115


p = 0.97496
comparison['prob'] = p
comparison['prob'].loc[comparison.actual == 1] = 1 - p

comparison['loss_a0'] = -1
comparison['loss_a1'] = -1

comparison['loss_a0'].loc[comparison.actual == 1] = 1
comparison['loss_a1'].loc[comparison.actual == 0] = 1

comparison['loss_model'] = np.nan
comparison['loss_model'].loc[comparison.model == 0] = comparison['loss_a0']
comparison['loss_model'].loc[comparison.model == 1] = comparison['loss_a1']

comparison['loss_random'] = np.nan
comparison['loss_random'].loc[comparison.random == 0] = comparison['loss_a0']
comparison['loss_random'].loc[comparison.random == 1] = comparison['loss_a1']



model_set = comparison.loc[comparison.actual == comparison.model]
random_set = comparison.loc[comparison.actual == comparison.random]

model_set['loss_w'] = model_set['loss_model'] / model_set['prob']
random_set['loss_w'] = random_set['loss_random'] / random_set['prob']

model_set.loc[model_set.actual == 1]
random_set.loc[random_set.actual == 1]


###########
# IPS
###########
round(np.mean(model_set['loss_w']), 5)
# -1.08056

round(np.mean(random_set['loss_w']), 5)
# -1.08664
