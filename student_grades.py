class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        body = self.scores[index]
        if body >= 90:
            return "A"
        elif body >= 80:
            return "B"
        elif body >= 70:
            return "C"
        elif body >= 60:
            return "D"
        elif body >= 50:
            return "E"
        else:
            return "F"

    def find(self, points):
        indexy = []
        for i, n in enumerate(self.scores):
            if n == points:
                indexy.append(i)
        return indexy

    def get_sorted(self):
        scores = self.scores.copy()
        for x in range(len(scores) - 1):
            for i in range(len(scores) - 1 - x):
                if scores[i] > scores[i + 1]:
                    scores[i], scores[i + 1] = scores[i + 1], scores[i]
        return scores

    def average(self):
        return sum(self.scores)/len(self.scores)

    def best(self):
        poradi = sorted(self.scores)
        return poradi[-1]

    def worst(self):
        poradi = sorted(self.scores)
        return poradi[0]

results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

def main():
    print(f"Počet studentů: {results.count()}")
    for n in range(results.count()):
        print(f"Student {n}: {results.get_by_index(n)} points - {results.get_grade(n)}")
    sto_bodu = []
    for n in range(results.count()):
        if results.get_by_index(n) == 100:
            sto_bodu.append(n)
    print(f"Plný počet bodů měli studenti indexů: {sto_bodu}")
    print(f"Seřazené výsledky: {results.get_sorted()}")
    return None

if __name__ == "__main__":
    print(results.worst())