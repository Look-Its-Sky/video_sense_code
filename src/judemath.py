def average(landmarks: dict, totalLM: int) -> float:
    try:
        totalX = 0
        totalY = 0

        for i in range(totalLM + 1):
            totalX += landmarks[i].x
            totalY += landmarks[i].y

        return ((totalX / totalLM), (totalY / totalLM))
    except:
        return (0, 0)