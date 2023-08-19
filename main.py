import chatbot as t
from prompt_enhance import quiz

def learn():
    topic=input("What topic would you like to learn about today? ")
    t.chatbot(topic, task_type, learning_pace)

def test():
    topic=input("What topic would you like give a quiz on today? ")
    t.chatbot(topic, task_type, learning_pace)

def analysis():
    topic="None"
    t.chatbot(topic, task_type, learning_pace)
    
def roadmap():
    topic=input("On what topic would you like to get a roadmap about? ")
    t.chatbot(topic, task_type, learning_pace)

learning_pace = main()

while True:
    task_type=int(input("What would you like to do today?\n1. Learn a new topic from the chatbot\n2. Take a test on a topic of your choice\n3. Perform text analysis \
                        \n4. Create a roadmap for a topic \n5. Quit \n"))
    if task_type==1:
        learn()
    elif task_type==2:
        test()
    elif task_type==3:
        analysis()
    elif task_type==4:
        roadmap()
    else:
        break
