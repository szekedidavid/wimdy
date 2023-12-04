import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_2Dsim = pd.read_excel("SimData2D.xlsx")
data_3Dsim = pd.read_csv("SimData3D.csv")

data_2Dexp = pd.read_excel("TestData.xlsx", sheet_name="2D_corr_test").drop(0)
data_3Dexp = pd.read_excel("TestData.xlsx", sheet_name="3D_corr_test").drop(0)

data_2Dexp.columns = data_2Dexp.columns.str.strip()
data_3Dexp.columns = data_3Dexp.columns.str.strip()


def plot_curves(x_str: str, y_str: str, dim: int):
    alpha_stall_2D = np.max(data_2Dexp["Alpha"])
    index_stall_2D = np.where(data_2Dexp["Alpha"] == np.max(data_2Dexp["Alpha"]))[0][0]

    alpha_stall_3D = np.max(data_3Dexp["Alpha"])
    index_stall_3D = np.where(data_3Dexp["Alpha"] == np.max(data_3Dexp["Alpha"]))[0][0]

    fig, ax = plt.subplots()
    if dim == 2:
        sim_plot, = ax.plot(data_2Dsim[x_str], data_2Dsim[y_str])
        exp_plot, = ax.plot(data_2Dexp[x_str][:index_stall_2D], data_2Dexp[y_str][:index_stall_2D], marker="o")
    else:
        sim_plot, = ax.plot(data_3Dsim[x_str], data_3Dsim[y_str])
        exp_plot, = ax.plot(data_3Dexp[x_str][:index_stall_3D], data_3Dexp[y_str][:index_stall_3D], marker="o")

    sim_plot.set_label("Simulation")
    exp_plot.set_label("Experiment")

    def format_label(st: str):
        if st == "Alpha":
            return r"$\alpha \ [deg]$"
        else:
            return f"${st[0]}_{{{st[1]}}} \ [-]$"

    ax.set_xlabel(format_label(x_str))
    ax.set_ylabel(format_label(y_str))

    plt.legend()
    plt.show()


def plot_comparison():
    fig, ax = plt.subplots()
    ax.plot(data_2Dexp["Alpha"], data_2Dexp["Cl"], label="2D wing")
    ax.plot(data_3Dexp["Alpha"], data_3Dexp["CL"], label="3D wing")
    ax.set_xlabel(r"$\alpha \ [deg]$")
    ax.set_ylabel("$C_l, C_L \ [-]$")

    plt.legend()
    plt.show()


#  def plot_pressure():


plot_curves("Alpha", "Cm", 2)
