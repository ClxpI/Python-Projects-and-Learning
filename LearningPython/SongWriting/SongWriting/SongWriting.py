
Swallowed = "There was an old lady who swallowed a "
Fly = "fly."
Spider = "spider,"+"\n"+"That wriggled and jiggled and tickled inside her."
Bird = "bird." 
def main():
    VerseOne()
    Chorus()
    global VerseSpider
    VerseSpider = 1
    VerseTwo()
    Chorus()
    VerseSpider = 2
    VerseTwo()
    Chorus()
    
def VerseOne():
    print(Swallowed + Fly)

def VerseTwo():
    if VerseSpider == 1:
        print(Swallowed + Spider +"\n"+ "She swallowed the spider to catch the fly")
    else:
        print(Swallowed + Bird +"\n"+ "How absurd to swallow a bird."+"\n"+"She swallowed the bird to chatch the spider,"+"\n"+"That wriggled and jiggled and tickled inside her."+"\n"+"She swallowed the spider to catch the fly")
    
def Chorus():
    Chorus = "I don't know why she swallowed the fly."
    Chorus1 = "Perhaps she'll die."
    print(Chorus+ "\n" +Chorus1)
    print()


    
main()
    
