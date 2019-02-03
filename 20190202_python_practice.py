https://leetcode.com/problems/two-sum/submissions/

class Solution(object):
    def twoSum(self, nums, target):
        res = False
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(i+2, len(nums)):
                    if ( nums[i] + nums[j] ) == target:
                        res = [i,j]

        return res

https://leetcode.com/problems/add-two-numbers/submissions/
        # Definition for singly-linked list.
        class ListNode(object):
            def __init__(self, x):
                self.val = x
                self.next = None

        class Solution(object):
            def addTwoNumbers(self, l1, l2):
                # unpack the linked list
                # l1 and l2 are node of singly linked lists
                list1=[]
                node = l1
                while node.next != None:
                    list1.append(node.val)
                    node = node.next
                list1.append(node.val)

                list2=[]
                node = l2
                while node.next != None:
                    list2.append(node.val)
                    node = node.next
                list2.append(node.val)

                n1 = int("".join([ str(x) for x in list1[::-1] ]))
                n2 = int("".join([ str(x) for x in list2[::-1] ]))
                return [int(x) for x in list(str(n1+n2))[::-1]]



https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
                class Solution(object):
                    def lengthOfLongestSubstring(self, s):
                        substring_dict = dict()
                        substring_list = list()
                        temp_str = ""

                        for i in range(len(s)):
                            # starting from every position of the string.
                            temp_list =[]
                            temp_list.append(s[i])
                            #print("first element is ", temp_list)
                            # keep on adding string until you see an duplicated alphabet
                            for j in range(i+1, len(s)):

                                if s[j] not in temp_list:
                                    temp_list.append(s[j])
                                    #print("current temp_list is ",temp_list)
                                else:
                                    substring_list.append("".join(temp_list))
                                    #print("current substring_list is ", substring_list)
                                    break

                        print(substring_list)
                        print([len(x) for x in substring_list])
                        #print(max([len(x) for x in substring_list]))
                        return max([len(x) for x in substring_list])
