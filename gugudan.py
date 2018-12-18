with open("gugudan.txt", "w") as file:
    for i in range(1, 10):
        for j in range(1, 10):
            file.write(f"{i} X {j} = {i*j}\n")


