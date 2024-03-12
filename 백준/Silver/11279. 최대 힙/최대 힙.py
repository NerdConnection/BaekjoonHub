import sys

class hq:
    def __init__(self):
        self.heap = []
        self.heap.append(None)
    
    def check_swap_up(self, idx):
        if idx <= 1:
            return False
        parent_idx = idx//2
        if self.heap[idx] > self.heap[parent_idx]:
            return True
        else:
            return False
    
    def insert(self,data):
        self.heap.append(data)
        idx = len(self.heap) - 1

        while self.check_swap_up(idx):
            parent_idx = idx //2
            self.heap[idx] , self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx
        
        return True

    def check_swap_down(self, idx):
        left_idx = idx * 2
        right_idx = idx * 2 + 1
        
        if left_idx >= len(self.heap):
            return False
        
        elif right_idx >= len(self.heap):
            if self.heap[left_idx] > self.heap[idx]:
                self.flag = 1
                return True
            else:
                return False
            
        else:
            if self.heap[left_idx] > self.heap[right_idx]:
                if self.heap[left_idx] > self.heap[idx]:
                    self.flag = 1
                    return True
                else:
                    return False
            else:
                if self.heap[right_idx] > self.heap[idx]:
                    self.flag = 2
                    return True
                else:
                    return False

    def pop(self):
        if len(self.heap) <= 1:
            return 0
        max_data = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        idx = 1
        self.flag = 0

        while self.check_swap_down(idx):
            left_idx = idx * 2
            right_idx = idx * 2 + 1
            if self.flag == 1:
                self.heap[idx], self.heap[left_idx] = self.heap[left_idx], self.heap[idx]
                idx = left_idx
            elif self.flag == 2:
                self.heap[idx], self.heap[right_idx] = self.heap[right_idx], self.heap[idx]
                idx = right_idx
        return max_data
    
input = sys.stdin.readline
n = int(input())
max_heap = hq()
for _ in range(n):
    commend = int(input())
    if commend == 0:
        print(max_heap.pop())
    else:
        max_heap.insert(commend)