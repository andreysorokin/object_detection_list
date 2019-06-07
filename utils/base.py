class QueryImage:
    def __init__(self, image, label):
        """
        :type image: object
        """
        self.image = image
        self.label = label


class Detection:

    def __init__(self, class_id, xmin, ymin, xmax, ymax, confidence, scale=1.0):
        self.confidence = confidence
        self.ymax = ymax
        self.xmax = xmax
        self.ymin = ymin
        self.xmin = xmin
        self.query = class_id
        self.scale = scale

    def area(self):
        return max(1, (self.ymax - self.ymin) * (self.xmax - self.xmin))

    def get_iou(self, other_detection):
        # intersection coords
        interArea = self.get_intersection(other_detection)
        thisArea = self.area()
        otherArea = other_detection.area()

        return interArea / (thisArea + otherArea - interArea)

    def get_max_intersection(self, other_detection):
        # this will also choose how big is intersection compared to each of the areas
        # intersection coords
        interArea = self.get_intersection(other_detection)
        thisArea = self.area()
        otherArea = other_detection.area()

        return max(interArea / thisArea, interArea / otherArea)

    def get_intersection(self, other_detection):
        xA = max(self.xmin, other_detection.xmin)
        yA = max(self.ymin, other_detection.ymin)
        xB = min(self.xmax, other_detection.xmax)
        yB = min(self.ymax, other_detection.ymax)
        interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
        return interArea
