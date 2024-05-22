import random
from words import word_list
from timer import Timer

def programe():
        print("\n\n")
        ticker = Timer()
        x = 25
        while x > 0:
            print(random.choice(word_list),end = " ")
            x-=1
        ticker.start()
        val = input("\n\nStart_typing:---\n\n")
        print("\nTotal time_consumed :--  ",ticker.stop())
        vat = list(val)
        space_count = 0
        for element in vat:
            if " " in element:
                space_count += 1

        print("\n\nTotal words ",space_count+1)


programe()
