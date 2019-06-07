def non_max_supression(detections, iou_threshold=0.5):
    print("Performing non-maximum suppression")
    excluded = [False for i in range(0, len(detections))]
    # get all connected
    for i, di in enumerate(detections):
        for j, dj in enumerate(detections):
            # upper triangle matrix
            if i < j and not excluded[i] and not excluded[j] and di.get_max_intersection(dj) > iou_threshold:
                if di.confidence > dj.confidence:
                    excluded[j] = True
                else:
                    excluded[i] = True
    return [d for idx, d in enumerate(detections) if not excluded[idx]]