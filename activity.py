class Activity(object):
    def __init__(self, type, reps, id_act, totalTime, weight):
        self.type = type
        self.reps = reps
        self.id_act = id_act
        self.totalTime = totalTime
        self.weight = weight

    def to_json(self):
        return {
            "type": self.type,
            "reps": self.reps,
            "id_act": self.id_act,
            "totalTime": self.totalTime,
            "weight": self.weight
        }
