import nltk
from nltk.tokenize import sent_tokenize
from textblob import TextBlob
#input analysis
sent_lambda_parsing_verb=[]
sent_lambda_parsing_subject=[]
sent_lambda_parsing_object=[]
sent_in=[]
sent_txt=[]
end='.'
noun='N'
pronoun='PR'
verb='VB'

#question analysis
question=[]
question_feature=[]
question_feature_verb=[]
question_feature_target=[]
question_feature_determinent=[]
#input analysis function
def input_analysis():
 
 output_file = open('output.txt', 'w') 
 parsesent_file = open('parse_test.txt', 'w')
 f=open('bAb_3.txt','rU')#open the file
 raw=f.read()

#print(raw)

 output_file.write("The sentence of the texts are:"+'\n')

#tokenize the sentence
 token_sent=sent_tokenize(raw)
 a=len(token_sent)
 print('Number of sentences:',a)

#print the sentences
 for i in range(0,a):
  print(token_sent[i])     
 #output_file.write(token_sent[i]+'\n')

 print('\n')



##POS tagging
 
 k=0


 for i in range(0,a):
  word_token=nltk.word_tokenize(token_sent[i])
  sent_in.insert(i,token_sent[i])
  #print('sentence',i, 'is: ', sent_in[i])

  lngth=len(word_token)
  tag=nltk.pos_tag(word_token)

 
  #print('Length of sentence',i,'is: ',lngth)
  #print('\n'+'Parsed types are: ')
 
  for j in range(0,len(tag)):
    #print(tag[j][0],'-------',tag[j][1])
    if verb in tag[j][1]:
          sent_lambda_parsing_verb.append(tag[j][0])
          for k in range(j+2,len(tag)-1):
            #print(tag[k][0],'...',tag[k][1])
            if noun  in tag[k][1]:
             sent_lambda_parsing_object.append(tag[k][0])
            elif pronoun in tag[k][1]:
             sent_lambda_parsing_object.append(tag[k][0])    
                #elif 'PR' in tag[i][1]:
                  #sent_lambda_parsing_object.append(tag[i][0])
          
 #finding noun phrases
 
  for j in range(0,len(tag)):
    if verb not in tag[j][1]:
          sent_lambda_parsing_subject.append(tag[j][0])
    else:
          break
      
 #finding object
    
 print('Verb list:',sent_lambda_parsing_verb)   
 print('Subject list:',sent_lambda_parsing_subject)
 print('Object list:',sent_lambda_parsing_object)

 #for i in range(0,a):
  #parsesent_file.write(sent_lambda_parsing_verb[i]+' '+sent_lambda_parsing_subject[i]+' '+sent_lambda_parsing_object[i]+'.'+'\n')
 #parsesent_file.close()
 
 #for i in range(0,a):
  #print(sent_lambda_parsing_verb[i],'(',sent_lambda_parsing_subject[i],'---',sent_lambda_parsing_object[i],')')
  #output_file.write(sent_lambda_parsing_verb[i]+' '+sent_lambda_parsing_subject[i]+' '+sent_lambda_parsing_object[i]+'.'+'\n')
 #print('\n')
 #output_file.close()
 #parsesent_file.close()
    

print('\n')

#question_analysis fuction
#------------------------------
#--------------------------
def question_analysis():
 
 
#input question
 question=input('Enter your question:')

 wr=TextBlob(question)
 a=wr.noun_phrases
 print(a)

#parse the question
 parse_question=nltk.word_tokenize(question)
 print(parse_question)

 tag=nltk.pos_tag(parse_question)

#print input text
 for i in range(0,len(tag)):
  print(tag[i][0],'....',tag[i][1])

#print tag text
#for i in range(0,len(tag)):
 #print(tag[i][1])

#feature from questions
 q_word='W'
 q_noun='N'
 q_pronoun='PR'
 q_verb='VB'
 for i in range(0,len(tag)):
  if q_word in tag[i][1]:
     print(tag[i][0],'......',tag[i][1])
     question_feature.append(tag[i][0])
     break

#wr=TextBlob(question)
#a=wr.noun_phrases
#question_feature.append(a)
#print(a)

 for i in range(0,len(tag)):
  if q_noun in tag[i][1]:
 
     #print(tag[i][0],'......',tag[i][1])
     question_feature.append(tag[i][0])
     s=int(i)
     break

 for i in range(0,len(tag)):
  if q_pronoun in tag[i][1]:
     #print(tag[i][0],'......',tag[i][1])
     question_feature.append(tag[i][0])
     s=int(i)
     break
 #print('Question Features are: ')
 #print(question_feature)


#answering_function
question_word=[]
question_object=[]
question_word_type=['why','who','Where','which','whom']

def answering_question(question_in,verb_in,subj_in,obj_in):
    object_position=0
    subject_position=0
    len_verb=len(verb_in)
    print(verb_in)
    wh_question_word=question_in[0]
    obj_question_word=question_in[1]
    question_word.append(wh_question_word)
    print(question_word)
    copy_sent_lambda_parsing_object=[]
    copy_sent_lambda_parsing_subject=[]
    print('Length is :',len_verb)

    #match finding
    match=[]
    count=0
    
    #question_feature_extraction
    for i in range(len_verb-1,0,-1):
        if obj_question_word in subj_in[i]:
         print('Subj',i)
         question_object.append('Sbj')
         subject_position=i
         break
        elif obj_question_word in obj_in[i]:
         print('Obj',i)
         question_object.append('Obj')
         object_position=i
         break
        
    #question_answering
    if 'Where' in question_word :
        #print('Yes',object_position)

        #positioning
        sent_in=[]
        f=open('positon_verb.txt','rU')#open the file
        position_verb_raw=f.read()
        pos_verb_sentence=sent_tokenize(position_verb_raw)
        word_token_position_verb=nltk.word_tokenize(pos_verb_sentence[0])
        
        sent_in.append(word_token_position_verb)
        len_word_token=len(word_token_position_verb)
        print(len_word_token)
        print(word_token_position_verb)

        
        
#place checking
     
        for i in range(0,len(sent_lambda_parsing_verb)):
         count=0
         for j in range(0,len_word_token):
           if sent_lambda_parsing_verb[i]==word_token_position_verb[j]:
             #match.append(word_token_position_verb[j])
               match.append('1')
               print(word_token_position_verb[j])
               break
           elif sent_lambda_parsing_verb[i]!=word_token_position_verb[j]:
             #match.append("N")
            count=count+1
         print('position',i,'is:',count) 
         if count==len_word_token:
           match.append('0')
           

        print(match)

        #position of place
        
        for i in range(0,len(sent_lambda_parsing_verb)):
            if '1' in match[i]:
                copy_sent_lambda_parsing_object.append('1')
            elif '1' not in match[i]:
                copy_sent_lambda_parsing_object.append('0')
                
        print(copy_sent_lambda_parsing_object)


   #answer for the object question
        if  'Obj' in question_object:
         subj_for_obj=subj_in[object_position]
         print(subj_for_obj)
         for k in range(object_position-1,0,-1):
            if copy_sent_lambda_parsing_object[k]=='1':
                print('Answer is:',sent_lambda_parsing_object[k])
                break
            


     
        elif 'Sbj' in question_object:
         print('Yes',subject_position)
        #positioning
        
         sent_in=[]
         print(copy_sent_lambda_parsing_object)    
        #answer for the subject question
         for l in range(subject_position,0,-1):
            if copy_sent_lambda_parsing_object[l]=='1':
                print('Answer is:',sent_lambda_parsing_object[l])
                break
    #print(copy_sent_lambda_parsing_object)            
 
def main():
    input_analysis()
    question_analysis()
    answering_question(question_feature,sent_lambda_parsing_verb,sent_lambda_parsing_subject,sent_lambda_parsing_object)
 
    
main()
