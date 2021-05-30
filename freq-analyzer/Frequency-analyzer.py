#!/bin/python3

#a python script for frequency analysis of words characters


#libraries that we used
import matplotlib.pyplot as plt 

#main function
def main():
 
#these paragraphs are from my favorite book "The Art of War" from https://www.gutenberg.org
    file1="Sun Tzu, as a practical soldier, will have none of the bookish theoric. He cautions us here not to pin our faith to abstract principles; for, as Chang Yu puts it, while the main laws of strategy can be stated clearly enough for the benefit of all and sundry, you must be guided by the actions of the enemy in attempting to secure a favorable position in actual warfare. On the eve of the battle of Waterloo, Lord Uxbridge, commanding the cavalry, went to the Duke of Wellington in order to learn what his plans and calculations were for the morrow, because, as he explained, he might suddenly find himself Commander-in-chief and would be unable to frame new plans in a critical moment. The Duke listened quietly and then said: Who will attack the first tomorrow—I or Bonaparte? Bonaparte, replied Lord Uxbridge. Well, continued the Duke, Bonaparte has not given me any idea of his projects; and as my plans will depend upon his, how can you expect me to tell you what mine are? "
    file2="The swift chariots were lightly built and, according to Chang Yu, used for the attack; the heavy chariots were heavier, and designed for purposes of defense. Li Ch’uan, it is true, says that the latter were light, but this seems hardly probable. It is interesting to note the analogies between early Chinese warfare and that of the Homeric Greeks. In each case, the war-chariot was the important factor, forming as it did the nucleus round which was grouped a certain number of foot-soldiers. With regard to the numbers given here, we are informed that each swift chariot was accompanied by 75 footmen, and each heavy chariot by 25 footmen, so that the whole army would be divided up into a thousand battalions, each consisting of two chariots and a hundred men."
    file3="This concise and difficult sentence is not well explained by any of the commentators. Ts’ao Kung, Li Ch’uan, Meng Shih, Tu Yu, Tu Mu and Mei Yao-ch’en have notes to the effect that a general, though naturally stupid, may nevertheless conquer through sheer force of rapidity. Ho Shih says: Haste may be stupid, but at any rate it saves expenditure of energy and treasure; protracted operations may be very clever, but they bring calamity in their train. Wang Hsi evades the difficulty by remarking: Lengthy operations mean an army growing old, wealth being expended, an empty exchequer and distress among the people; true cleverness insures against the occurrence of such calamities. Chang Yu says: So long as victory can be attained, stupid haste is preferable to clever dilatoriness.Now Sun Tzu says nothing whatever, except possibly by implication, about ill-considered haste being better than ingenious but lengthy operations. What he does say is something much more guarded, namely that, while speed may sometimes be injudicious, tardiness can never be anything but foolish—if only because it means impoverishment to the nation. In considering the point raised here by Sun Tzu, the classic example of Fabius Cunctator will inevitably occur to the mind. That general deliberately measured the endurance of Rome against that of Hannibals's isolated army, because it seemed to him that the latter was more likely to suffer from a long campaign in a strange country. But it is quite a moot question whether his tactics would have proved successful in the long run. Their reversal it is true, led to Cannae; but this only establishes a negative presumption in their favour. "

#removing spaces to analyze all of them as a single string    
    found1_raw=file1.replace(" ","")
    found2_raw=file2.replace(" ","")
    found3_raw=file3.replace(" ","")


    #found1
    all_freq1={}
    for i in found1_raw:
        if i in all_freq1:
            all_freq1[i]+=1
        else:
            all_freq1[i]=1
    found1={}
    for i in all_freq1:
        perc=(float(all_freq1[i])/float(len(found1_raw)))*100
        found1[i]=perc
    print("\n")
    print("Frequency of letters found in found1:\n")
    print(found1)
    print("\n")

    #found1
    all_freq2={}
    for i in found2_raw:
        if i in all_freq2:
            all_freq2[i]+=1
        else:
            all_freq2[i]=1
    found2={}
    for i in all_freq2:
        perc=(float(all_freq2[i])/float(len(found2_raw)))*100
        found2[i]=perc
    print("\n")
    print("Frequency of letters found in found2:\n")
    print(found2)
    print("\n")

    #found3
    all_freq3={}
    for i in found3_raw:
        if i in all_freq3:
            all_freq3[i]+=1
        else:
            all_freq3[i]=1
    found3={}
    for i in all_freq3:
        perc=(float(all_freq3[i])/float(len(found3_raw)))*100
        found3[i]=perc
    print("\n")
    print("Frequency of letters found in found3:\n")
    print(found3)
    print("\n")

    #number of letters in the sample
    print("There are about "+str(len(found1.keys()))+" letters in 'found1'")
    print("There are about "+str(len(found2.keys()))+" letters in 'found2'")
    print("There are about "+str(len(found3.keys()))+" letters in 'found3'")

    #number of words in the sample
    print("There are about "+str(len(found1_raw))+" words in 'found1'")
    print("There are about "+str(len(found2_raw))+" words in 'found2'")
    print("There are about "+str(len(found3_raw))+" words in 'found3'")
    
    
    #plotting the dictionaries

    fig1=plt.bar(list(found1.keys()), found1.values(), color='g')
    plt.show()

    plt.bar(list(found2.keys()), found2.values(), color='b')
    plt.show()

    plt.bar(list(found3.keys()), found3.values(), color='r')
    plt.show()
    
if __name__=="__main__":main()
#Finished

