def maior(*num):
    maior = 0

    for i in range(0,len(num)):

        if i == 0:
            maior = num[0]
        else:
            if num[i] > maior:
                maior = num[i]

    print("~" * 60)
    print(f"Os dados informados foram: {num}")
    print(f"O maior valor dentre eles é {maior}.")
    print("~" * 60)


maior(1,2,3,4,5,6)
maior(5, 47, 31, 9)
maior(0)
maior(36, 105, 2, 17)
maior()
