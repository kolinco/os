def mru_page_replacement(pages, frame_size):
    frame = []
    page_faults = 0
    total_pages = len(pages)

    print("Iteration | Frame State          | Result")
    print("----------------------------------------")
    
    for i, page in enumerate(pages):
        if page in frame: 
            result = "HIT"
        else:  
            page_faults += 1
            result = "MISS"
            
            if len(frame) < frame_size: 
                frame.append(page)
            else:  
                frame.pop(-1)
                frame.append(page)
        
        print(f"{i+1:<9} | {frame} | {result}")

    miss_ratio = page_faults / total_pages

    print("\nTotal Page Faults:", page_faults)
    print("Miss Ratio:", round(miss_ratio, 2))


pages = [7, 0, 1, 8, 0, 3, 0, 4, 8, 3, 0, 3, 8, 3]
frame_size = 3

mru_page_replacement(pages, frame_size)

