#Each of a certain set of schoolchildren of a certain school knows a certain number of languages. It is necessary to determine how many languages all students know, and how many languages at least one of the students knows.

#The first line contains the number of students. For each of the students, first the number of languages that he knows is written, and then the names of the languages, one per line.

#In the first line print the number of languages that all students know. Starting from the second line - a list of such languages. Then - the number of languages that at least one student knows, on the next lines - a list of such languages. Languages should be output in lexicographical order, one per line.
students = [{input() for j in range(int(input()))} for i in range(int(input()))]
known_by_everyone, known_by_someone = set.intersection(*students), set.union(*students)
print(len(known_by_everyone), *sorted(known_by_everyone), sep='\n')
print(len(known_by_someone), *sorted(known_by_someone), sep='\n')
