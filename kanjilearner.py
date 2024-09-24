import random
import os

radicaldit = {'斤' : 'axe', '青' : 'blue', '耂' : 'coffin', '色' : 'colour', '羽' : 'feathers', '行' : 'go', '金' : 'gold', '冫' : 'ice', '乍' : 'key', '比' : 'kick', '开' : 'lantern', '可' : 'lip ring', '肉' : 'meat', '会' : 'meet', '冋' : 'mustache', '雨' : 'rain', '走' : 'run', '言' : 'say', '辶' : 'scooter', '自' : 'self', '氵' : 'tsunami', '廾' : 'twenty', '龸' : 'viking', '彐' : 'wolverine', '里' : 'village', '西' : 'west'}

kanjidit = {'竹' : [['take', 'たけ'], ['bamboo']], '車' : [['shya', 'しゃ'], ['car']], '央' : [['ou', 'おう'], ['center']], '写' : [['shya', 'しゃ'], ['copy']], '仕' : [['shi', 'し'], ['doing']], '耳' : [['mimi', 'みみ'], ['ear']], '早' : [['sou', 'そう'], ['early']], '気' : [['ki', 'き'], ['energy']], '平' : [['hei', 'へい'], ['flat']], '花' : [['hana', 'はな'], ['flower']], '足' : [['soku', 'そく'], ['foot']], '打' : [['da', 'だ'], ['hit']], '百' : [['hyaku', 'ひゃく'], ['hundred']], '氷' : [['kouri', 'こうり'], ['ice']], '虫' : [['mushi', 'むし'], ['insect']], '字' : [['ji', 'じ'], ['letter']], '男' : [['dan', 'だん'], ['man']], '主' : [['shyu', 'しゅ'], ['master']], '名' : [['mei', 'めい'], ['name']], '不' : [['hu', 'ふ'], ['not']], '号' : [['gou', 'ごう'], ['number']], '他' : [['ta', 'た'], ['other']], '去' : [['kyo', 'きょ'], ['past']], '皿' : [['sara', 'さら'], ['plate']], '先' : [['sen', 'せん'], ['previous']], '赤' : [['aka', 'あか'], ['red']], '休' : [['kyuu', 'きゅう'], ['rest']], '申' : [['mou', 'もう'], ['say humbly']], '見' : [['mi', 'み'], ['see']], '貝' : [['kai', 'かい'], ['shellfish']], '石' : [['seki', 'せき'], ['stone']], '代' : [['dai', 'だい'], ['substitute', 'replace', 'age', 'period']], '礼' : [['rei', 'れい'], ['thanks']], '糸' : [['ito', 'いと'], ['thread']], '町' : [['chyou', 'ちょう'], ['town']], '宝' : [['hou', 'ほう'], ['treasure']], '村' : [['mura', 'むら'], ['village']], '世' : [['se', 'せ'], ['world']], '年' : [['nen', 'ねん'], ['year']]}

vocabdit = {'他人' : [['tanin', 'たにん'], ['other people', 'another person', 'stranger']], '早々' : [['sousou', 'そうそう', 'hayabaya', 'はやばや'], ['as soon as', 'just after', 'promptly', 'quickly', 'immediately after']], '大気' : [['taiki', 'たいき'], ['atmosphere']], '赤ちゃん' : [['akachyan', 'あかちゃん'], ['baby']], '竹' : [['take', 'たけ'], ['bamboo']], '竹の子' : [['takenoko', 'たけのこ'], ['bamboo shoots', 'bamboo sprouts']], '太字' : [['futoji', 'ふとじ'], ['bold', 'bold letter', 'bold character', 'bold text', 'bold face']], '少年' : [['shyounen', 'しょうねん'], ['boy', 'young boy', 'juvenile', 'youth']], '虫' : [['mushi', 'むし'], ['insect', 'bug']], '子牛' : [['koushi', 'こうし'], ['calf', 'baby cow']], '平気' : [['heiki', 'へいき'], ['calm', 'okay', 'all right', 'cool']], '車' : [['kuruma', 'くるま'], ['car']], '中央' : [['chyuuou', 'ちゅうおう'], ['center', 'centered']], '字' : [['ji', 'じ'], ['character', 'kanji character', 'letter', 'symbol']], '耳' : [['mimi', 'みみ'], ['ear', 'ears']], '早い' : [['hayai', 'はやい'], ['early', 'fast', 'quick']], '元気' : [['genki', 'げんき'], ['energy', 'healthy', 'health', 'energetic']], '気分' : [['kibun', 'きぶん'], ['feeling', 'mood']], '花火' : [['hanabi', 'はなび'], ['fireworks']], '先ず' : [['mazu', 'まず'], ['first of all', 'to start with', 'firstly', 'to begin with']], '一年生' : [['ichinensei', 'いちねんせい'], ['first year student']], '五百' : [['gohyaku', 'ごひゃく'], ['500', 'five hundred']], '平ら' : [['taira', 'たいら'], ['flat']], '花' : [['hana', 'はな'], ['flower']], '足' : [['ashi', 'あし'], ['foot', 'leg']], '四十' : [['yonjyuu', 'よんじゅう'], ['forty', '40']], '四百': [['yonhyaku''よんひゃく'], ['400', 'four hundred']], '四日' : [['yokka', 'よっか'], ['four days', 'fourth day', 'day four', '4 days', '4th day', 'day 4']], '四つ' : [['yottsu', 'よっつ'], ['4 things', 'four things']], '四千' : [['yonsen', 'よんせん'], ['4000', 'four thousand', '4 thousand']], '主人' : [['shyujin', 'しゅじん'], ['head of household', 'head of a household', 'master', 'landlord', 'husband']], '休日' : [['kyuujitsu', 'きゅうじつ'], ['holiday']], '百' : [['hyaku', 'ひゃく'], ['hundred', '100']], '氷' : [['koori', 'こおり'], ['ice']], '丸ごと' : [['marugoto', 'まるごと'], ['in its entirety', 'whole', 'wholly', 'entirely']], '不止' : [['husei', 'ふせい', 'fusei', 'ふせい'], ['injustice', 'unfairness', 'dishonesty']], '車内' : [['shyanai', 'しゃない'], ['in the car', 'in a car', 'inside the car', 'inside a car', 'within the car', 'within a car']], '宝石' : [['hoseki', 'ほせき'], ['jewel']], '先月' : [['sengetsu', 'せんげつ'], ['last month']], '去年' : [['kyonen', 'きょねん'], ['last year']], '左手' : [['hidarite', 'ひだいて'], ['left hand']], '文字' : [['moji', 'もじ'], ['letter', 'letter of the alphabet']], '一代' : [['ichidai', 'いちだい'], ['one lifetime', 'one generation', 'lifetime', 'generation']], '主に' : [['omoni', 'おもに'], ['mainly', 'primarily']], '男' : [['otoko', 'おとこ'], ['man']], '名人' : [['meijin', 'めいじん'], ['master', 'expert']], '仕方' : [['shikata', 'しかた'], ['method', 'way of doing', 'way']], '百万' : [['hyakuman', 'ひゃくまん'], ['million', 'one million', '1 000 000', '1000000']], '先々月' : [['sensengetsu', 'せんせんげつ'], ['the month before last', 'month before last', 'last last month']], '月見' : [['tsukimi', 'つきみ'], ['moon viewing']], '名' : [['na', 'な'], ['name', 'reputation']], '号' : [['gou', 'ごう'], ['number', 'model', 'edition']], '一気' : [['ikki', 'いっき'], ['one breath', 'one sitting']], '一打' : [['ichida', 'いちだ'], ['one strike', 'one stroke', 'one blow']], '一本気' : [['shippongi', 'しっぽんぎ'], ['one track mind', 'single mindedness']], '他' : [['hoka', 'ほか'], ['other']], '休止' : [['kyuushi', 'きゅうし'], ['pause', 'rest', 'break']], '皿' : [['sara', 'さら'], ['plate']], '人気' : [['ninki', 'にんき'], ['popular', 'popularity']], '切手' : [['kitte', 'きって'], ['postage stamp', 'stamp']], '先' : [['saki', 'さき'], ['previous', 'ahead', 'past', 'former']], '赤' : [['aka', 'あか'], ['red']], '赤い' : [['akai', 'あかい'], ['red']], '休み' : [['yasumi', 'やすみ'], ['rest', 'break', 'vacation', 'holiday']], '右手' : [['migite', 'みぎて'], ['right hand']], '二世' : [['nisei', 'にせい'], ['second generation', '2nd generation']], '本気' : [['honki', 'ほんき'], ['serious']], 'かき氷' : [['kakigoori', 'かきごおり'], ['shaved ice']], '貝' : [['kai', 'かい'], ['shell', 'shellfish', 'clam']], '不足' : [['fusoku', 'ふそく', 'husoku', 'ふそく'], ['shortage', 'physical shortage', 'insufficient', 'not sufficient', 'not enough']]}

radicals = []
kanji = []
vocabulary = []

def createlist():
  chardict = [radicaldit, kanjidit, vocabdit]
  for i in chardict:
    for j in i.keys():
      if i == radicaldit:
        radicals.append(j)
      elif i == kanjidit:
        kanji.append(j)
      elif i == vocabdit:
        vocabulary.append(j)

createlist()

def intro():
  print("Welcome to your language learning quiz.")
  start = input("Click enter to start. ")
  if start == '':
    os.system("clear")
    allrounds()

def makeclear():
  clear = input('')
  if clear == '':
    os.system('clear')

def askrounds():
  rounds = int(input("How many questions would you like to be asked? "))
  return rounds

def prodef(whichques):
  if whichques == 'pronounce':
    answer = input("pronounciation: ")
  elif whichques == 'definition':
    answer = input("definition: ")
  return answer

def ifdef(answer, definition, correct):
  if answer in definition:
    print("Correct.")
    correct += 1
  elif answer not in definition:
    print("Incorrect. The definition is {}".format(definition[0]))
  return correct

def ifpro(answer, pronounciation, correct):
  if answer in pronounciation:
    print("Correct.")
    correct += 1
  elif answer not in pronounciation:
    print("Incorrect. The definition is {}".format(pronounciation[1]))
  return correct

def allrounds():
  correct = 0
  rounds = askrounds()
  for i in range(rounds):
    correct = quiz(correct)
  print("Your final score is {}/{}".format(correct, rounds))

def numfind(whichques):
  if whichques == 'pronounce':
    num = 0
  elif whichques == 'definition':
    num = 1
  return num

def restartif(onechar, kanjichar, correct, whichques, vocab, radical):
  num = numfind(whichques)
  if onechar == kanjichar:
    kan = kanjidit.get(onechar)
    if whichques in kan[num]:
      quiz(correct)
  elif onechar == vocab:
    voc = vocabdit.get(onechar)
    if whichques in voc[num]:
      quiz(correct)
  elif onechar == radical:
    rad = radicaldit.get(onechar)
    if rad == 'used':
      quiz(correct)

def quiz(correct):
  whichques = random.choice(['pronounce', 'definition'])
  radical = random.choice(radicals)
  kanjichar = random.choice(kanji)
  vocab = random.choice(vocabulary)
  onechar = random.choice([radical, kanjichar, vocab])
  restartif(onechar, kanjichar, correct, whichques, vocab, radical)
  print(onechar)
  if onechar == radical:
    print("radical")
    answer = input("radical name: ")
    r = radicaldit.get(onechar)
    if answer == r:
      correct += 1
      print("Correct.")
    elif answer != r:
      print("Incorrect. The name of this radical was {}".format(r))
    radicaldit[onechar] = 'used'
  elif onechar == kanjichar:
    print("kanji")
    answer = prodef(whichques)
    if whichques == 'pronounce':
      k = kanjidit.get(onechar)
      pronounciation = k[0]
      correct = ifpro(answer, pronounciation, correct)
      kanjidit[onechar][0] = ['pronounce']
    elif whichques == 'definition':
      k = kanjidit.get(onechar)
      definition = k[1]
      correct = ifdef(answer, definition, correct)
      kanjidit[onechar][1] = ['definition']
  elif onechar == vocab:
    print('vocabulary')
    answer = prodef(whichques)
    if whichques == 'pronounce':
      v = vocabdit.get(onechar)
      pronounciation = v[0]
      correct = ifpro(answer, pronounciation, correct)
      vocabdit[onechar][0] = ['pronounce']
    elif whichques == 'definition':
      v = vocabdit.get(onechar)
      definition = v[1]
      correct = ifdef(answer, definition, correct)
      vocabdit[onechar][1] = ['definition']
  makeclear()
  return correct
  return radicaldit

intro()
