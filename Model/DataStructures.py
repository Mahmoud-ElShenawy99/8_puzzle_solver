class HashSet:

    def __init__(self):
        self.size = 100000
        self.table = [None] * self.size

    def calculate_hash_value(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        hv = self.calculate_hash_value(key)

        if self.table[hv] == None:
            self.table[hv] = [key]
        else:
            self.table[hv].append(key)

    def get_values(self):
        values=[]
        for i in self.table:
            if i !=None:
                for j in i:
                   values.append(j)
        return values
    def remove(self, key: int) -> None:
        hv = self.calculate_hash_value(key)

        if self.table[hv] != None:
            while key in self.table[hv]:
                self.table[hv].remove(key)
    def clear(self):
        self.table.clear()
        self.table = [None] * self.size

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hv = self.calculate_hash_value(key)

        if self.table[hv] != None:
            return key in self.table[hv]
        return False


class HashMap:

    # Create empty bucket list of given size
    def __init__(self):
        self.size = 1000000
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    # Insert values into hash map
    def set_val(self, key, val):

        # Get the index from the key
        # using hash function
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # check if the bucket has same key as
            # the key to be inserted
            if record_key == key:
                found_key = True
                break

        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))
    def clear(self):
        self.hash_table.clear()
        self.hash_table = self.create_buckets()

    # Return searched value with specific key
    def get_val(self, key):

        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # check if the bucket has same key as
            # the key being searched
            if record_key == key:
                found_key = True
                break

        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        if found_key:
            return record_val
        else:
            return "No record found"

    # Remove a value with specific key
    def delete_val(self, key):

        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # check if the bucket has same key as
            # the key to be deleted
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return

    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)



