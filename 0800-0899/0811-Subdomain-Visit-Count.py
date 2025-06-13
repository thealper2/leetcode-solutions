from collections import defaultdict
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = defaultdict(int)

        for domain in cpdomains:
            times, domain = domain.split()
            times = int(times)
            subdomains = domain.split('.')
            
            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[i:])
                count[subdomain] += times

        return [f"{v} {k}" for k, v in count.items()]
