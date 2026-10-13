while True:
    A, B = map(int, input().split())

    if A == 0 and B == 0:
        break

    alice = set(map(int, input().split()))
    beatriz = set(map(int, input().split()))

    cartas_alice = alice - beatriz
    cartas_beatriz = beatriz - alice

    resposta = min(len(cartas_alice), len(cartas_beatriz))

    print(resposta)