

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

def reverse_words(sentence):
    words = sentence.split()
    queue = Queue()
    
    for word in words:
        queue.enqueue(word)
    
    reversed_words = []
    while not queue.is_empty():
        reversed_words.append(queue.dequeue())
    
    return ' '.join(reversed_words[::-1])


input_sentence = "Hello World"
output_sentence = reverse_words(input_sentence)
print(output_sentence)  
     
