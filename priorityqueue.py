class PriorityQueue(object):
    def __init__(self):
        self.queue = []
        self.tempqueue = []
  
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
  
    def isEmpty(self):
        return len(self.queue) == 0
  
    def insert(self,data):
        self.queue.append(data)
       
  
    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] < self.queue[max]:
                    max = i
                    # print("max",max)
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()
  
if __name__ == '__main__':
    data  = [1,1,1,2,2,3]
    k = 2
    dict_1 = {}
    for i in data:
        b =data.count(i)
        dict_1[i] = b       
    myQueue = PriorityQueue()
    for dict in dict_1:
        myQueue.insert((-dict_1[dict], dict))
    print("Myqueue",myQueue)

    final_list = []        
    while len(final_list)< k and not myQueue.isEmpty():
       value = myQueue.delete()
       final_list.append(value[1])
    print(final_list)   