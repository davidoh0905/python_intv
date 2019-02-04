https://leetcode.com/problems/unique-email-addresses/submissions/

class Solution(object):
    def numUniqueEmails(self, emails):
        distinct_emails = list()
        for email in emails:
            local_name = email.split('@')[0].split('+')[0].replace(".", "")
            domain_name = email.split('@')[1]
            distinct_email = local_name+'@'+domain_name

            if distinct_email not in distinct_emails:
                distinct_emails.append(distinct_email)
                
        return len(distinct_emails)


https://leetcode.com/problems/k-closest-points-to-origin/submissions/

class Solution(object):
    def kClosest(self, points, K):
        length_list = list()
        for point in points:
            dist = point[0]**2 + point[1]**2
            length_list.append([dist, point])
        length_list.sort()

        return [x[1] for x in length_list[:K]]
