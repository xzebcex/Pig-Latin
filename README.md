# Pig Latin
This is a simple Python application that converts English messages to Pig Latin, a linguistic game in which the original words are altered to sound amusing.

## How it Works
The application takes an English message from the user and converts it into Pig Latin using a set of rules. This is how it works:
1.	The program divides the input message into individual words and stores them in a list.
2.	It isolates any non-letter characters at the start and end of each word.
1.	If the word begins with a vowel, it adds "yay" at the end. If it begins with one or more consonants, it adds "ay" at the end of the word.
2.	The program then merges the translated word with any non-letter characters that were previously eliminated, saving the result in a new list.
3.	The program then prints the translated message.

## How to Use
Simply execute the code and input an English message when requested to utilise this application. The message will subsequently be translated into Pig Latin and displayed by the application.
Please keep in mind that this application only works with English messages and may not create correct translations for messages in other languages.

## Author
This program's author is xzebcex.

## Extra points
1.	Input Validation: The application should check user input to ensure that only letters, spaces, and punctuation marks are present. When provided invalid input, this prevents the application from crashing or giving unexpected outcomes.
2.	Error Handling: The program should gracefully manage problems by presenting informative error messages and asking the user to try again. For example, if the user submits an empty message or a message that has no alphabetic letters, the application may display an error message rather than continue with the translation.
3.	Increase Language Support: The program's present implementation only supports English messages. To improve its use, the software might be expanded to accommodate other languages, such as Spanish or French, by employing language-specific translation rules.
