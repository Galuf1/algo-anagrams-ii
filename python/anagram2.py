def anagrams_for(word, list_of_words):
		def filterAnagram(str1):
			list1 = list(word)
			list2 = list(str1)
			for i in list1:
				if i in list2:
					list2.remove(i)
			if len(list2) == 0:
				return True
		
		result_iterator = filter(filterAnagram,list_of_words )
		result = list(result_iterator)

		return result
