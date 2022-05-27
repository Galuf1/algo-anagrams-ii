def anagrams_for(word, list_of_words):
		# create a function to filter if the iterator equals word
		def filter_anagram(str1):
			# create lists with string to be able to mutate them
			list1 = list(word)
			list2 = list(str1)
			for i in list1:
				if i in list2:
					#remove the character from list2 if it is in word
					list2.remove(i)
			# should be equal if they match length and characters
			if len(list2) == 0:
				return True
		# filter using the list generates an iterator that has to be converted into a list
		result_iterator = filter(filter_anagram,list_of_words )
		result = list(result_iterator)

		return result
