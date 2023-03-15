def average(landmarks: dict, totalLM: int) -> float:
    totalX = 0
    totalY = 0

    for i in range(totalLM + 1):
        totalX += landmarks[i].x
        totalY += landmarks[i].y

    return ((totalX / totalLM), (totalY / totalLM))