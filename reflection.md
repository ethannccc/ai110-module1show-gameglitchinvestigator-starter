# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

The first time I ran it, the game would tell me lower and higher when I guessed a number until I either guessed the number or ran out of guesses. I ran out of guesses because the hints were incorrect. Two concrete bugs I noticed were the higher and lower hints were incorrect. The secret number was 24, but for some reason when I entered 10, it told me to go lower. Another bug I noticed was the range values for each difficulty. As you go higher the range should increase and the guess attempts should decrease, but the values for each difficulty seem out of place. The "Enter to Apply" functionality doesn't work, and the New Game button does not start a new game. Entering a non number also incorrectly reduces the number of attempts I have. Overall lots of bugs.

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Copilot. An AI suggestion that was correct was the logic it gave me to properly reset the history. I verified by checking the code and running it in the app. I could tell it was going to work because it set history to an empty list, and attempts was set back to zero. An AI suggestion that was misleading was the logic that was causing the hint bug. It help fixed the alphabetical comparison of the secret number, but forgot to include the fixes about the print statements in Higher and Lower texts. I was able to run the program and determine the bug and went back to change it and then confirm the change.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided whether a bug was really fixed by running the tests in the test suite and also running the program in Streamlit to actually verify the changes. I made a new test in pytest and to test the alphabetic comparison fixes that Copilot added and it passed, which told me that the original code was faulty and the change I made was accurate. AI help me design the aforementioned test, and I double checked the make sure the tests that it generated was accurate. 

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
