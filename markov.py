import operator, random, math

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

def nPopularWords(allNodes, word, n):
	if word not in allNodes:
		print(word + " does not appear in the given text.")
		return
	wordList = allNodes[word]
	sortedWordList = sorted(wordList.items(), key=operator.itemgetter(1), reverse=True)
	i = 0
	print(word + "'s " + str(n) + " most popular words are:")
	while i < n and i < len(sortedWordList):
		print(str((i+1)) + ". " + sortedWordList[i][0] + ", it occurs " + str(sortedWordList[i][1]) + " times.")
		i+=1

def mostPopularWord(allNodes, word):
	if word not in allNodes:
		print(word + " does not appear in the given text.")
		return
	wordList = allNodes[word]
	sortedWordList = sorted(wordList.items(), key=operator.itemgetter(1), reverse=True)
	return sortedWordList[0][0]

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

allWords = readFile('sherlock.txt')
allNodes = generateLists(allWords)
print(allNodes)
