exports.anagramsFor = function(word, listOfWords) {
    // create a function to filter the listOfWords
    const filterAnagram = function(str1){
       // sort and compare to see if they are anagrams
       const sortedWord = word.split("").sort().join("")
       const sortedStr = str1.split("").sort().join("")
       return sortedWord === sortedStr

    }
    //filter creates a new list
    let result = listOfWords.filter(filterAnagram)
    return result
};

