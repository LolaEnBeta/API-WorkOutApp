class Activity(object):
    def __init__(self, id, type, reps, totalTime, weight):
        self.id = id
        self.type = type
        self.reps = reps
        self.totalTime = totalTime
        self.weight = weight

    def to_json(self):
        return {
            "id": self.id,
            "type": self.type,
            "reps": self.reps,
            "totalTime": self.totalTime,
            "weight": self.weight
        }
