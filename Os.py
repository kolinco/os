def hvp_page_replacement(pages, frame_size):
    frame = [None] * frame_size
    total_misses = 0
    total_pages = len(pages)
    
    print("Iteration | Frame State        | Status")
    print("--------------------------------------")
    
    for i, page in enumerate(pages):
        if page in frame:
            status = "Hit"
        else:
            # Page fault (miss)
            total_misses += 1
            if None in frame:
                # Empty slot available
                frame[frame.index(None)] = page
            else:
                # Replace page with the highest value
                max_value = max(frame)
                frame[frame.index(max_value)] = page
            status = "Miss"
        
        # Print the current state of the frame
        print(f"    {i + 1:2d}   | {frame} | {status}")
    
    # Calculate miss ratio
    miss_ratio = total_misses / total_pages
    print("--------------------------------------")
    print(f"Total Misses: {total_misses}")
    print(f"Miss Ratio: {miss_ratio:.2f}")

# Input Data
pages = [7, 0, 1, 12, 7, 0, 18, 12, 6, 16, 7, 0, 18]
frame_size = 3

# Execute the algorithm
hvp_page_replacement(pages, frame_size)
