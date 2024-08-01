import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:
    def plot_data(self, date, temp, output_file='output.png'):
        plt.figure(figsize=(12, 4))
        sns.lineplot(x=date, y=temp)
        plt.title('5 Day Weather Forecast', fontsize=12)
        plt.savefig(output_file)
        print(f"Graph saved to {output_file}")
        plt.show()