import time

# Record the start time
start_time = time.time()
print(f"Start time: {start_time:.2f}")  # Print the start_time in seconds

# Simulate some itme-consuming operation
for _ in range(10000000):
    _ = _ # Do something simple

# Record the end time
end_time = time.time()
print(f"End time: {end_time}")

# Calculate the elapsed time
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f}")