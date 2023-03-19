import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

class EDA_Outputs:
    def eda_plots_missing_values_heatmap(self, data):
        fig, ax = plt.subplots(figsize=(15,15)) 
        sns.heatmap(data.isnull(),
                    cbar=False,
                    cmap='viridis').set(title='Missing Values by Column and Row',
                                        xlabel='Column',
                                        ylabel='Row')
        fig.savefig("Plots_Storage/EDA_Plots/missing_values_heatmap.png")

        return None