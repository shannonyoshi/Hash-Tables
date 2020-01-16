# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        #TODO: finish this
        index = self._hash_mod(key)
        if self.storage[index]:
            linked_list=self.storage[index]
            while linked_list:
                if linked_list.key == key:
                    #print(f"original: {linked_list.key}, {linked_list.value}")

                    linked_list.value = value
                    #print(f"new: {key}, {linked_list.value}")
                    return
                else:
                    if linked_list.next is None:
                        linked_list.next = LinkedPair(key, value)
                    else:
                        linked_list = linked_list.next
            

        else:
            self.storage[index] = LinkedPair(key, value)
        pass



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        #print("have index")
        if self.storage[index]:
            linked_list = self.storage[index]
            prev = None
            while linked_list:
                #print("while")
                if linked_list.key == key:
                    #print("linked_list.key == key")
                    if prev:
                        #print("prev true")
                        prev.next = linked_list.next
                        del linked_list
                        return
                    else:
                        #print("prev false")
                        self.storage[index] = linked_list.next
                        del linked_list
                        return
                prev = linked_list
                linked_list = linked_list.next
                
        else:
            print("Key Not Found")
            return



    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        index=self._hash_mod(key)
        if self.storage[index]:
            linked_item = self.storage[index]
            while linked_item is not None:
                if linked_item.key == key:
                    #print(f"key: {key}, value: {linked_item.value}")
                    return linked_item.value
                else:
                    linked_item = linked_item.next
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        data = self.storage
        self.capacity = self.capacity*2
        self.storage = [None] * self.capacity
        for linked_list in data:
            while linked_list is not None:
                self.insert(linked_list.key, linked_list.value)
                linked_list = linked_list.next
        return

        



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
