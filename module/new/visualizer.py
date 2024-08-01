import plotly.graph_objects as go

class Visualizer:
    def plot_data(self, data: list[float], output_file='output.png'):
        temperatures = [12.66, 11.78, 11.5, 10.93, 10.5]  # 5개의 온도값.
        fig = go.Figure()
        fig.add_trace(go.Scatter(y=data,
                                 mode='lines+markers',
                                 name='Temperature'))
        fig.update_layout(title="Temperature Over Time(24h)",
                          xaxis_title="Time",
                          yaxis_title="Temperature (°C)",
                          template='plotly_dark')
        
        fig.write_image(output_file)
        print(f"Graph saved to {output_file}")