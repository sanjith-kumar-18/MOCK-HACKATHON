def simple_exponential_smoothing(series, alpha):
    # Initialize the forecast
    forecast = [series[0]]

    # Apply simple exponential smoothing
    for i in range(1, len(series)):
        forecast.append(alpha * series[i] + (1 - alpha) * forecast[i - 1])

    return forecast

# Example usage:
if __name__ == "__main__":
    # Example data (replace this with your dataset)
    data = [30, 35, 28, 40, 45, 38, 50, 48, 55, 50]
    
    # Set the smoothing parameter (alpha)
    alpha = 0.2
    
    # Perform simple exponential smoothing
    forecast = simple_exponential_smoothing(data, alpha)
    
    # Output the forecasted values
    print("Original Data:", data)
    print("Forecasted Data:", forecast)
