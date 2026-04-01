import flwr as fl
import torch
import config

def main():
    print("--- SecureEdge-GPT SERVER INITIALIZING ---")

    # Define a simple aggregation strategy
    strategy = fl.server.strategy.FedAvg(
        fraction_fit=config.FRACTION_FIT,
        min_fit_clients=config.MIN_FIT_CLIENTS,
        min_available_clients=config.NUM_CLIENTS,
    )

    # Start the server
    print(f"Server starting on [::]:8080 with {config.NUM_ROUNDS} rounds...")
    fl.server.start_server(
        server_address="0.0.0.0:8080",
        config=fl.server.ServerConfig(num_rounds=config.NUM_ROUNDS),
        strategy=strategy,
    )

if __name__ == "__main__":
    main()
