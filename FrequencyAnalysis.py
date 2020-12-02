print("Welcome to the sentance analizer")
data = {}
this = []

while True:
    sentance = input("Enter a sentance you want analized: \n").lower()
    sentance = sentance.replace(' ', '')
    ''.join(x for x in sentance if x.isalpha())
    for c in sentance:
        if c not in data:
            data[c] = 1
        else:
            data[c] += 1
    print("Here is the analasis")
    print("\tLetter\tOccurance\tPercentage")
    for k, v in data.items():
        print("\t" + k + "\t" + str(v) + '\t'
              '' + str(format((int(v) / len(data) * 100), '.2f') + "%"))

    print("Sorted")
    data = dict(sorted(data.items(), key=lambda item: item[1]))
    for key in data:
        this.insert(0, key)
    for i in this:
        print(i, end='')
    if input("Want to try another y/n: ") == 'n':
        break
