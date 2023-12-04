import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_2Dsim = pd.read_csv("SimData2D.csv")
#  data_3Dsim = pd.read_csv("SimData3D.csv")

data_2Dexp = pd.read_excel("TestData.xlsx", sheet_name="2D_corr_test").drop(0)
data_3Dexp = pd.read_excel("TestData.xlsx", sheet_name="3D_corr_test").drop(0)

data_2Dexp.columns = data_2Dexp.columns.str.strip()
data_3Dexp.columns = data_3Dexp.columns.str.strip()


def plot_curves(x_str: str, y_str: str, dim):
    fig, ax = plt.subplots()
    if dim == 2:
        ax.plot(data_2Dsim[x_str][:index_stall_2D], data_2Dsim[y_str][:index_stall_2D])
        ax.plot(data_2Dexp[x_str][:index_stall_2D], data_2Dexp[y_str][:index_stall_2D], marker="o")
        plt.show()
    if dim == 3:
        ax.plot(data_3Dsim[x_str], data_3Dsim[y_str])
        ax.plot(data_3Dexp[x_str], data_3Dexp[y_str], marker="o")
        plt.show()


alpha_stall_2D = np.max(data_2Dexp["Alpha"])
index_stall_2D = np.where(data_2Dexp["Alpha"] == np.max(data_2Dexp["Alpha"]))[0][0]

alpha_stall_3D = np.max(data_3Dexp["Alpha"])
index_stall_3D = np.where(data_3Dexp["Alpha"] == np.max(data_3Dexp["Alpha"]))[0][0]

plot_curves("Alpha", "Cl", 2)
