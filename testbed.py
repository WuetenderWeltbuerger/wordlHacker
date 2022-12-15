def comparePlayed(played, firstResult):
    correctPosition = []
    i = 0 #counter
    while i < 5:
        if played[i] == firstResult[i]:
            correctPosition[i] = played[i]
            i += 1
            continue
        else:
            correctPosition[i] = "-"
            i += 1
            continue
        
    print(correctPosition)
    return correctPosition
            
  
  
def main():
    played = input("enter first word")
    parsePlayed = played.split(" ")
    firstResult = input("enter word to compare")
    firstLower = firstResult.lower()
    parseFirstLower = firstLower.split(" ")
    comparePlayed(parsePlayed, parseFirstLower)



    print()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()