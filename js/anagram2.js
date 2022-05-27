exports.anagramsFor = function(word, listOfWords) {
    const filterAnagram = function(str1){
        
       const sortedWord = word.split("").sort().join("")
       const sortedStr = str1.split("").sort().join("")
       return sortedWord === sortedStr

    }
    
    let result = listOfWords.filter(filterAnagram)
    return result
};


// listOfWords = ["threads", "trashed", "hardest", "hatreds", "hounds"];

// anagramsFor("threads",listOfWords)