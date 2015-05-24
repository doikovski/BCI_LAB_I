import scipy.io as mat

mat.savemat('PSDE.mat',dict(PSDE_sit=PSDE_sit_transform, PSDE_stand=PSDE_stand_transform))