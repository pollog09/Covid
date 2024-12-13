import torch
print("Starting up...")
print("PyTorch version:", torch.__version__)
print("Checking GPU...")

if torch.cuda.is_available():
    device = torch.device("cuda")
    print("CUDA is available. Using GPU.")
else:
    device = torch.device("cpu")
    print("CUDA is not available. Using CPU.")

