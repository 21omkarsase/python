class MyIterator:
    def __init__(self, data) -> None:
        self.data = data
        self.idx = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.data):
            raise StopIteration
        
        result = self.data[self.idx]
        self.idx += 1
        
        return result 

it = MyIterator([1, 2, 3, 5, 'abc'])

class MyIterator:
    def __init__(self) -> None:
        self.num = 1  # Initialize starting number
    
    def __iter__(self):
        self.num = 1  # Reset the number to 1 when iterating again
        return self
    
    def __next__(self):
        self.num += 1  # Increment the number

        return (self.num - 1) ** 2  # Return square of current number


it = MyIterator()

for i in it:
    if i > 10:
        break
    with open('res.txt', 'a') as f:
        print(i)
        f.write(str(i) + '\n')
        