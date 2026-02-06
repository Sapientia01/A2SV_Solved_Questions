# Question link: https://leetcode.com/problems/subdomain-visit-count/description/

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visits = {}
        for cpdomain in cpdomains:
            count, domains = cpdomain.split()
            count = int(count)
            domains = domains.split(".")

            for i in range(len(domains)):
                curdomain = ".".join(domains[i:])
                if curdomain in visits:
                    visits[curdomain] += count
                else:
                    visits[curdomain] = count


        return [str(count) + " " + domain for domain, count  in visits.items()]