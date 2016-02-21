import operator, random, math, praw

def readFile(filename):
    allWords = []
    f = open(filename, 'r')
    for line in f:
        allWords += line.split()
    return allWords

def generateLists(allWords):
    allNodes = {}
    i = 0
    while i < len(allWords) - 1:
        currentWord = allWords[i]
        nextWord = allWords[i+1]

        if not currentWord in allNodes:
            allNodes[currentWord] = {}
        if not nextWord in allNodes[currentWord]:
            allNodes[currentWord][nextWord] = 1
        allNodes[currentWord][nextWord] += 1
        i+=1
    return allNodes

def wordByProbability(allNodes, word):
    if word not in allNodes:
        print(word + " does not appear in the given text.")
        return
    wordList = allNodes[word]
    totalWords = 0
    for key in wordList:
        totalWords += wordList[key]
    for key in wordList:
        wordList[key] = wordList[key]/totalWords
    randomElement = random.random()
    for key in wordList:
        randomElement -= wordList[key]
        if randomElement <= 0:
            return key

def basicChain(allNodes, startingWord, n):
    if startingWord not in allNodes:
        print(startingWord + " does not appear in the given text.")
        return
    currentWord = startingWord
    i = 0
    while i < n:
        print(currentWord, end=' ')
        currentWord = wordByProbability(allNodes, currentWord)
        i+=1
    print()

jokebot = praw.Reddit(user_agent='joke v0.1 by u/rohacrates')
jokes = jokebot.get_subreddit('jokes').get_top_from_week()
allTitles = []
allText = []
for joke in jokes:
    allTitles += joke.title.split()
    allText += joke.selftext.split()

allTitleNodes = generateLists(allTitles)
allTextNodes = generateLists(allText)
basicChain(allTitleNodes, random.choice(list(allTitleNodes)), 8)
basicChain(allTextNodes, random.choice(list(allTextNodes)), 20)