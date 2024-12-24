#SOLVE THESE QUESTIONS AND SPECIFY RUNNING TIME AND SPACE COMPLEXITY IN COMMENTS.

#Question 1:

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#Example: [2,3,4,2,7] target = 10, output = [1,4]

def twoSum(nums, target):
    #your code goes here
    # Itterate thro array and add values.
    for i in range(len(nums)):
        for k in range(len(nums)):
            mysum = nums[i] + nums[k]

            # Once sum is == target add indexes to the list
            if mysum == target:
                    output =[]
                    output.append(k)
                    output.append(i)  
    print(output)

# Test
nums = [2,3,4,2,7]
target = 10
twoSum(nums, target)

# Time and space complexity: This is my own attempt and this code with nasting loops gives O(n^2) time complexity and O(1) space complexity.
# I am just from CS50 Harward course and kind of understanding the concept of time and space but still Google to double check.
# I asked GPT for optimization and aware now that this better solution to the problem - hash table, 
# but atm I'm not that great with them and couldn't undertand the solution given by GPT. But hey! it's good to know that there are better way :)



#Question 2:
#Given some arrays with strings on them, find the most common longest prefix among them.
#Example: ["flower","flow","flight"] output = "fl"

def findMostCommonPrefix(arr):
    string = arr[0]
    match = ''

    # itterate thro characters of 1 string 
    for i in range(len(string)):

        for k in arr[1:]: # Go to every string in array but start with 1 index
            if string[i] != arr[k][i]: # if no match, return string that we have so far
                return match
        # if match
        match += string[i]      
    return match


arr = ["flower","flow","flight"]
print(findMostCommonPrefix(arr))

#Time and space complexity: O(n) - space complexity, where n is the number of letters in 1 string.
# Time Complexity: 𝑂(n*m) where  n is the length of the first string and m is the number of strings in the array.

#Question 3:
#Given an array of integers, return the indices of three numbers that add up to 0.
#example: [1, 2, -2, -1, 3] output = [0, 2, 3]

def threeSum(nums):
    
    # sort array 
    sorted = nums[:]
    sorted.sort()


    # fix first element
    for i in range(len(sorted)-2):

        #left pointer:
        l = i + 1

        #right last pointer:
        r = len(sorted)-1

        while (l<r):
            if ((sorted[i] + sorted[l] + sorted[r]) == 0):

                # find those elements index in original array
                output_sorted = [i,l,r]
                output_nums = []
                for a in output_sorted:
                    value = sorted[a]
                    index = nums.index(value)
                    output_nums.append(index)

                print(output_nums)
                return True
            
            elif ((sorted[i] + sorted[l] + sorted[r]) < 0):
                l += 1
            elif ((sorted[i] + sorted[l] + sorted[r]) > 0):
                r -= 1

    print("No triples found")          
    return False
            
arr = [1, 2, -2, -1, 3]
threeSum(arr)

# I coudn't solve this task without asking for a hint of the idea how to approach it. Three nested loops seemed
# like a bad idea. So I divided into pointers and recreated this concept from C.
# Time and space complexity: Time complexity - O(n^2), space complexity - O(1)



#Question 4:
#Given a singly linked list, reverse the nodes of the linked list
#Example 1: [1, 2, 3] output = [3, 2, 1]

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def printList(head):
    while head:
        print(head.data)
        head = head.next

head = Node(1)
middle = Node(2)
tail = Node(3)

head.next = middle
middle.next = tail
tail.next = None

printList(head)

def reverseList(head):
    #your code goes here
    if head is None or head.next is None:
        return head
    
    # I wrote this with help of GPT, since understand the theory behind recursion but my brain explodes when I need to write one
    rest = reverseList(head.next) # Once recursion done, rest points to 3

    head.next.next = head
    head.next = None

    return rest

#Time and space complexity: I don't know. Space O(n), time O(n)
# I understand nodes and pointers from C, so for me in theory is clear that we need to follow "next" untill
# there is "None" and than unfold the recursion. I am having really hard time to write it in code, because don't have enough experience in coding




