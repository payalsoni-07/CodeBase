class Bucket:
    def __init__(self, bucket_capacity):
        self.local_depth = 1
        self.bucket = []
        self.bucket_capacity = bucket_capacity
        
    def insert(self, key, value):
        if len(self.bucket) < self.bucket_capacity:
            self.bucket.append((key, value))
            return True
        return False

class ExtendibleHash:
    def __init__(self,capacity):
        self.global_depth = 1
        self.directory = []
        self.bucket_capacity  = capacity
        self.split_count = 0
        for i in range(2**self.global_depth):
            self.directory.append(Bucket(self.bucket_capacity))

    def bucket_count(self):
        count = 0
        for i in range(2**self.global_depth):
            if self.directory[i].bucket != []:
                count +=1
        return count
    def calhash(self, key):
        return key % (2**self.global_depth)
    
    def insert(self, key, value):
        directory_index = self.calhash(key)
        bucket = self.directory[directory_index]
        if bucket.insert(key, value) == False:
            self.split(directory_index)
            self.split_count += 1
            self.insert(key, value)
        else:
            return "Inserted"

    def rehash(self, directory_index):
        bucket = self.directory[directory_index]
        dummy = bucket.bucket
        bucket.bucket = []
        for key,value in dummy:
            new_directory_index = self.calhash(key)
            if new_directory_index != directory_index:
                new_bucket = self.directory[new_directory_index]
                new_bucket.bucket.append((key, value))
            else:
                bucket.bucket.append((key, value))


    def split(self, directory_index):
        if self.directory[directory_index].local_depth == self.global_depth:
            self.global_depth += 1
            for i in range(2**(self.global_depth-1)):
                self.directory.append(Bucket(self.bucket_capacity))
        self.directory[directory_index].local_depth += 1
        new_directory_index = directory_index + (2**(self.global_depth-1))
        self.directory[new_directory_index].local_depth = self.directory[directory_index].local_depth
        self.rehash(directory_index)


    def search(self, key):
        directory_index = self.calhash(key)
        bucket = self.directory[directory_index]
        for k,v in bucket.bucket:
            if k == key:
                return v
        return "Not found"
    def update(self, key, value):
        directory_index = self.calhash(key)
        bucket = self.directory[directory_index]
        for k,v in bucket.bucket:
            if k == key:
                bucket.bucket.remove((k,v))
                bucket.bucket.append((k,value))
                return "Updated"
        return "Not found"

    def delete(self, key):
        directory_index = self.calhash(key)
        bucket = self.directory[directory_index]
        for k,v in bucket.bucket:
            if k == key:
                bucket.bucket.remove((k,v))
                self.merge(directory_index)
                return "Deleted"
        return "Not found"
    
    def merge(self, directory_index):
        bucket = 0
        sibling = 0
        if directory_index<2**(self.global_depth-1):
            bucket = self.directory[directory_index]
            sibling = self.directory[directory_index + (2**(self.global_depth-1))]
        else:
            bucket = self.directory[directory_index - (2**(self.global_depth-1))]
            sibling = self.directory[directory_index]
        b = len(bucket.bucket)
        s = len(sibling.bucket)
        if b + s <= bucket.bucket_capacity:
            bucket.bucket.extend(sibling.bucket)
            bucket.local_depth -= 1
            sibling.bucket = []
        for i in range(2**(self.global_depth-1)):
            j = i + (2**(self.global_depth-1))
            if self.directory[j].bucket!=[]:
                return
        for i in range(2**(self.global_depth-1)):
            self.directory.pop()    
        self.global_depth -= 1
