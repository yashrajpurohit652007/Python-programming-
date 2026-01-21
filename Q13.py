13. Convert Bytes into KB, MB, GB
bytes_val = float(input("Enter number of Bytes: "))
kb = bytes_val / 1024
mb = kb / 1024
gb = mb / 1024
print(f"KB: {kb}, MB: {mb}, GB: {gb}")
