def find_intersection(set1,set2):
    intersection=set1.intersection(set2)
    return intersection

set1={"a","b","c","d"}
set2={"c","d","e","f"}
intersection=find_intersection(set1,set2)
print(intersection)


