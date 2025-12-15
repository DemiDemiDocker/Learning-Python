# Hangman — Simple Step-by-step Tasks

## 1. Decide what the game does
Write one sentence describing the game: for example, “The program picks a fruit name and you guess letters until you find the word or run out of chances.”

## 2. Prepare the list of possible words
Make a short list of words (fruit names). This is the pool the game will choose from.

## 3. Choose the secret word secretly
Decide that the game will pick one word from the list at random and keep it hidden from the player.

## 4. Show the empty word to the player
Plan to display a series of blanks (one blank per letter) so the player can see how many letters the secret word has.

## 5. Decide how many chances the player gets
Pick a rule for the number of wrong guesses allowed (for example, word length plus two).

## 6. Ask the player for a letter
Decide the exact prompt the player will see when asked to type a letter.

## 7. Check the player’s input (simple)
Plan how to respond if the player types:
- Not a letter
- More than one character
- A letter they already tried  
Decide to show a friendly message and ask again in these cases.

## 8. Record correct guesses
Decide that when the player types a letter that appears in the secret word, the letter will be remembered and revealed in the blanks.

## 9. Reveal letters in the display
Plan to update the blanks so any correctly guessed letters appear in their proper positions each round.

## 10. Handle repeated letters
Decide that letters that appear multiple times in the word will be revealed in all of their positions once guessed.

## 11. Decrease chances after each turn
Decide that each round will reduce the remaining chances by one (or only reduce on incorrect guesses, depending on your rule).

## 12. Decide win and lose conditions
- Win: all letters in the word are revealed before chances run out.  
- Lose: the player runs out of chances before revealing the whole word.  
Plan what message to show for each outcome.

## 13. Allow graceful exit
Decide what happens if the player interrupts or wants to quit early (for example, show a goodbye message).

## 14. Test the game manually
Play several rounds using different words, try invalid inputs, and check win/lose behavior.

## Optional extras
- Let the player guess the entire word at once.  
- Add a hint system that reveals one letter when asked.  
- Add a visible score or leaderboard.  
- Add difficulty levels that change the number of chances.  
- Show letters already guessed.  