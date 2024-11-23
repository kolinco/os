def optimal_page_replacement(pages, frame_size):
    frame = []  # Stores pages in memory
    page_faults = 0
    total_pages = len(pages)

    print("Iteration | Frame State           | Result")
    print("------------------------------------------")

    for i, page in enumerate(pages):
        # Check if the page is already in the frame (HIT)
        if page in frame:
            result = "HIT"
        else:
            # Page fault occurs (MISS)
            page_faults += 1
            result = "MISS"

            if len(frame) < frame_size:  # If frame is not full
                frame.append(page)
            else:  # Frame is full, replace a page
                # Find the page that will not be used for the longest time
                future_uses = []
                for f in frame:
                    if f in pages[i + 1:]:  # Check if the page will be used again
                        future_uses.append(pages[i + 1:].index(f))
                    else:  # If the page is not used again
                        future_uses.append(float("inf"))

                # Replace the page with the farthest future use
                index_to_replace = future_uses.index(max(future_uses))
                frame[index_to_replace] = page

        # Display the iteration details
        print(f"{i+1:<9} | {frame} | {result}")

    # Calculate and display the miss ratio
    miss_ratio = page_faults / total_pages
    print("\nTotal Page Faults:", page_faults)
    print("Miss Ratio:", round(miss_ratio, 2))


# Input parameters
pages = [7, 0, 1, 8, 0, 3, 0, 4, 8, 3, 0, 3, 8, 3]
frame_size = 3

# Execute the Optimal page replacement
optimal_page_replacement(pages, frame_size)
